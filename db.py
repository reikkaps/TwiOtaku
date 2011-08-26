import apsw

from constant import DB_PATH

_conn_db = None

def init():
  global _conn_db
  if not _conn_db:
    _conn_db = apsw.Connection(DB_PATH)
    cursor = _conn_db.cursor()
    sql = dict(
      id_lists="""CREATE TABLE "id_lists" (
                "uid"  INTEGER NOT NULL,
                "short_id"  INTEGER NOT NULL,
                "long_id"  INTEGER NOT NULL,
                "type"  INTEGER NOT NULL DEFAULT 0
                );
                CREATE INDEX "uid_longid_type"
                ON "id_lists" ("uid", "long_id", "type");
                CREATE INDEX "uid_shortid_type"
                ON "id_lists" ("uid", "short_id", "type");
                """,
      users="""CREATE TABLE "users" (
            "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            "enabled"  INTEGER NOT NULL DEFAULT 1,
            "jid"  TEXT NOT NULL,
            "screen_name"  TEXT,
            "access_key"  TEXT,
            "access_secret"  TEXT,
            "last_cron"  INTEGER NOT NULL DEFAULT 0,
            "last_home_id"  INTEGER NOT NULL DEFAULT 0,
            "last_mention_id"  INTEGER NOT NULL DEFAULT 0,
            "last_dm_id"  INTEGER NOT NULL DEFAULT 0,
            "timeline"  INTEGER NOT NULL DEFAULT 3,
            "id_list_ptr"  INTEGER NOT NULL DEFAULT 0
            );
            CREATE INDEX "enabled"
            ON "users" ("enabled");
            CREATE UNIQUE INDEX "id"
            ON "users" ("id");
            CREATE UNIQUE INDEX "jid"
            ON "users" ("jid");
            CREATE UNIQUE INDEX "enabled_timeline"
            ON "users" ("enabled", "timeline");
            """,
      statuses="""CREATE TABLE "statuses" (
              "id"  INTEGER NOT NULL,
              "json"  BLOB NOT NULL,
              "type"  INTEGER NOT NULL DEFAULT 0,
              PRIMARY KEY ("id") ON CONFLICT REPLACE
              );
              CREATE UNIQUE INDEX "status_id"
              ON "statuses" ("id", "type");
              """,
      )
    for t in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
      t = t[0]
      if t in sql:
        del(sql[t])
    for v in sql.itervalues():
      cursor.execute(v)
  return _conn_db

def get_user_from_jid(jid):
  cursor = _conn_db.cursor()
  user = dict()
  for u in cursor.execute('SELECT * FROM users WHERE jid=?', (jid, )):
    d = cursor.getdescription()
    for i in range(len(d)):
      user[d[i][0]] = u[i]
    break
  return user

def update_user(id=None, jid=None, **kwargs):
  if id is None and jid is None:
    raise TypeError('The method takes at least one argument.')
  if kwargs:
    cursor = _conn_db.cursor()
    cols = list()
    values = list()
    for k, v in kwargs.iteritems():
      cols.append('%s=?' % k)
      values.append(v)
    if id:
      cond = 'id=?'
      values.append(id)
    else:
      cond = 'jid=?'
      values.append(jid)
    sql = 'UPDATE users SET %s WHERE %s' % (','.join(cols), cond)
    cursor.execute(sql, values)

