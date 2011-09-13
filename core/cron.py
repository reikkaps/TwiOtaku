import time
from threading import Thread
from Queue import Queue, Empty

import db
from config import OAUTH_CONSUMER_KEY, OAUTH_CONSUMER_SECRET
from worker import Job
from lib import twitter
from lib.decorators import debug

def cron_start(queues):
  cron_queue = Queue()
  for _ in range(db.get_users_count() // 5 + 1):
    t = Thread(target=cron_job, args=(cron_queue, ))
    t.setDaemon(True)
    t.start()
  for user in db.get_all_users():
    if user['access_key'] and user['access_secret']:
      tl = user['timeline'] & ~db.MODE_EVENT # event only exists in user streaming api.
      if tl:
        user['last_update'] = int(time.time())
        db.update_user(id=user['id'], last_update=user['last_update'])
        if time.time() - user['last_update'] > 180:
          # if it's a long time since last update, we should abandon these old data.
          queue = Queue()
        else:
          queue = queues.get(user['jid'], Queue())
        cron_queue.put((queue, user))
  cron_queue.join()


def cron_job(cron_queue):
  @debug('cron')
  def fetch_home():
    data = api.get_home_timeline(since_id=user['last_home_id'])
    if data and isinstance(data, list) and isinstance(data[0], twitter.Status):
      db.update_user(jid=user_jid, last_home_id=data[0]['id_str'])
      if not user_timeline & db.MODE_HOME:
        if user_timeline & db.MODE_MENTION:
          data = [x for x in data if '@%s' % user['screen_name'] in x['text']]
        else:
          data = list()
      return data

  @debug('cron')
  def fetch_mention():
    if user_timeline & db.MODE_MENTION:
      data = api.get_mentions(since_id=user['last_mention_id'])
      if data and isinstance(data, list) and isinstance(data[0], twitter.Status):
        db.update_user(jid=user_jid, last_mention_id=data[0]['id_str'])
        return data

  @debug('cron')
  def fetch_dm():
    if user_timeline & db.MODE_DM:
      data = api.get_direct_messages(since_id=user['last_dm_id'])
      if data and isinstance(data, list) and isinstance(data[0], twitter.DirectMessage):
        db.update_user(jid=user_jid, last_dm_id=data[0]['id_str'])
        return data

  @debug('cron')
  def fetch_list():
    if user_timeline & db.MODE_LIST:
      if user['list_user'] and user['list_id']:
        try:
          data = api.get_list_statuses(screen_name=user['list_user'], slug=user['list_id'],
            since_id=user['last_list_id'])
        except twitter.TwitterNotFoundError:
          user['timeline'] &= ~db.MODE_LIST
          db.update_user(id=user['id'], timeline=user['timeline'])
          queue.put(Job(user['jid'],
            title='List %s/%s not exists, disable List update.' % (user['list_user'], user['list_name'])))
        else:
          if data and isinstance(data, list) and isinstance(data[0], twitter.Status):
            db.update_user(jid=user_jid, last_list_id=data[0]['id_str'])
            return data

  while True:
    try:
      queue, user = cron_queue.get(True, 3)
    except Empty:
      return
    user_jid = user['jid']
    user_timeline = user['timeline']

    api = twitter.Api(consumer_key=OAUTH_CONSUMER_KEY,
      consumer_secret=OAUTH_CONSUMER_SECRET,
      access_token_key=user['access_key'],
      access_token_secret=user['access_secret'])
    all_data = list()

    data = fetch_dm()
    if data:
      queue.put(Job(user_jid, data=data, title='Direct Message:', allow_duplicate=False, always=False))
    data = fetch_list()
    if data:
      all_data.extend(data)
    data = fetch_mention()
    if data:
      all_data.extend(data)
    data = fetch_home()
    if data:
      all_data.extend(data)

    user_at_screen_name = '@%s' % user['screen_name']
    for x in all_data:
      if user_at_screen_name in x['text'] and 'in_reply_to_status_id_str' in x:
        try:
          x['in_reply_to_status'] = api.get_status(x['in_reply_to_status_id_str'])
        except BaseException:
          pass

    queue.put(Job(user_jid, data=all_data, allow_duplicate=False, always=False))

    cron_queue.task_done()

