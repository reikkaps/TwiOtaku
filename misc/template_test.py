# -*- encoding: utf-8 -*-
# Copyright 2011 ayanamist
# the program is distributed under the terms of the GNU General Public License
# This file is part of TwiOtaku.
#
#    Foobar is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TwiOtaku is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TwiOtaku.  If not, see <http://www.gnu.org/licenses/>.

from lib import myjson
from lib import twitter

_text = r'{"favorited":false,"contributors":null,"truncated":false,"text":"RT @TwiOtaku: @gh05tw01f Welcome! Wish you enjoy!","in_reply_to_status_id":null,"user":{"utc_offset":28800,"statuses_count":25890,"follow_request_sent":false,"friends_count":393,"profile_use_background_image":true,"profile_sidebar_fill_color":"95E8EC","profile_link_color":"0099B9","profile_image_url":"http://a2.twimg.com/profile_images/1470742579/avatar_normal.PNG","default_profile_image":false,"notifications":false,"is_translator":false,"show_all_inline_media":true,"profile_background_image_url_https":"https://si0.twimg.com/images/themes/theme4/bg.gif","protected":false,"id":8104012,"profile_background_image_url":"http://a1.twimg.com/images/themes/theme4/bg.gif","description":"\u5916\u8868\u5927\u53d4\u7684\u706b\u661f\u8179\u9ed1\u6b63\u592a\u3002\u80bf\u7624\u79d1\u533b\u5b66\u751f\u3002\u8bfa\u57fa\u4e9aE71\u4f7f\u7528\u8005\u3002\u7231\u751f\u6d3b\u7231\u5410\u69fd\u3002\u4eb2\u65e5\u6d3e\uff0c\u4eb2\u817e\u8baf\uff0c\u4e2d\u533b\u9ed1\uff0c\u4e0d\u559c\u52ff\u6270\u3002\u57fa\u7763\u5f92\u3002\u76ee\u524d\u4ee5\u751f\u6d3b\u63a8\u3001\u719f\u4eba\u63a8\u4e3a\u4e3b\uff0c\u6280\u672f\u63a8\u548c\u533b\u5b66\u63a8\u6781\u5c11\u6570\u3002","lang":"en","default_profile":false,"profile_background_tile":false,"verified":false,"screen_name":"gh05tw01f","url":"http://www.cnblogs.com/ayanamist/","profile_image_url_https":"https://si0.twimg.com/profile_images/1470742579/avatar_normal.PNG","contributors_enabled":false,"time_zone":"Beijing","name":"ayanamist","geo_enabled":true,"profile_text_color":"3C3940","followers_count":876,"profile_sidebar_border_color":"5ED4DC","id_str":"8104012","profile_background_color":"0099B9","following":true,"favourites_count":47,"listed_count":53,"created_at":"Fri Aug 10 13:52:07 +0000 2007","location":"Wuhan, China"},"geo":null,"in_reply_to_user_id_str":null,"source":"<a href=\"http://code.google.com/p/twiotaku/\" rel=\"nofollow\">TwiOtaku</a>","created_at":"Sat Sep 17 13:56:45 +0000 2011","retweeted":false,"coordinates":null,"id":115061633151279104,"entities":{"user_mentions":[{"indices":[3,12],"id_str":"250488521","screen_name":"TwiOtaku","name":"TwiOtaku","id":250488521},{"indices":[14,24],"id_str":"8104012","screen_name":"gh05tw01f","name":"ayanamist","id":8104012}],"hashtags":[],"urls":[]},"in_reply_to_status_id_str":null,"in_reply_to_screen_name":null,"id_str":"115061633151279104","place":null,"retweet_count":0,"in_reply_to_user_id":null}'
_text_retweeted_status = r'{"favorited":false,"contributors":null,"truncated":false,"text":"@gh05tw01f Welcome! Wish you enjoy!","in_reply_to_status_id":115061186621476864,"user":{"utc_offset":28800,"statuses_count":3,"follow_request_sent":false,"friends_count":1,"profile_use_background_image":true,"profile_sidebar_fill_color":"DDEEF6","profile_link_color":"0084B4","profile_image_url":"http://a3.twimg.com/profile_images/1240928412/otaku_normal.png","default_profile_image":false,"notifications":false,"is_translator":false,"show_all_inline_media":true,"profile_background_image_url_https":"https://si0.twimg.com/images/themes/theme1/bg.png","protected":false,"id":250488521,"profile_background_image_url":"http://a0.twimg.com/images/themes/theme1/bg.png","description":"TwiOtaku is a GTalk based Twitter client using Twitter Streaming API written by @gh05tw01f .","lang":"en","default_profile":true,"profile_background_tile":false,"verified":false,"screen_name":"TwiOtaku","url":"http://code.google.com/p/twiotaku/","profile_image_url_https":"https://si0.twimg.com/profile_images/1240928412/otaku_normal.png","contributors_enabled":false,"time_zone":"Chongqing","name":"TwiOtaku","geo_enabled":false,"profile_text_color":"333333","followers_count":13,"profile_sidebar_border_color":"C0DEED","id_str":"250488521","profile_background_color":"C0DEED","following":false,"favourites_count":0,"listed_count":0,"created_at":"Fri Feb 11 05:30:20 +0000 2011","location":"China"},"geo":null,"id":115061412182761472,"source":"<a href=\"http://code.google.com/p/twiotaku/\" rel=\"nofollow\">TwiOtaku</a>","created_at":"Sat Sep 17 13:55:53 +0000 2011","retweeted":false,"coordinates":null,"in_reply_to_user_id_str":"8104012","entities":{"user_mentions":[{"indices":[0,10],"id_str":"8104012","screen_name":"gh05tw01f","name":"ayanamist","id":8104012}],"hashtags":[],"urls":[]},"in_reply_to_status_id_str":"115061186621476864","in_reply_to_screen_name":"gh05tw01f","in_reply_to_user_id":8104012,"place":null,"retweet_count":0,"id_str":"115061412182761472"}'
_text_in_reply_to_status = r'{"favorited":false,"contributors":null,"truncated":false,"text":"Hello from TwiOtaku!","in_reply_to_status_id":null,"user":{"utc_offset":28800,"statuses_count":25890,"follow_request_sent":false,"friends_count":393,"profile_use_background_image":true,"profile_sidebar_fill_color":"95E8EC","profile_link_color":"0099B9","profile_image_url":"http://a2.twimg.com/profile_images/1470742579/avatar_normal.PNG","default_profile_image":false,"notifications":false,"is_translator":false,"show_all_inline_media":true,"profile_background_image_url_https":"https://si0.twimg.com/images/themes/theme4/bg.gif","protected":false,"id":8104012,"profile_background_image_url":"http://a1.twimg.com/images/themes/theme4/bg.gif","description":"\u5916\u8868\u5927\u53d4\u7684\u706b\u661f\u8179\u9ed1\u6b63\u592a\u3002\u80bf\u7624\u79d1\u533b\u5b66\u751f\u3002\u8bfa\u57fa\u4e9aE71\u4f7f\u7528\u8005\u3002\u7231\u751f\u6d3b\u7231\u5410\u69fd\u3002\u4eb2\u65e5\u6d3e\uff0c\u4eb2\u817e\u8baf\uff0c\u4e2d\u533b\u9ed1\uff0c\u4e0d\u559c\u52ff\u6270\u3002\u57fa\u7763\u5f92\u3002\u76ee\u524d\u4ee5\u751f\u6d3b\u63a8\u3001\u719f\u4eba\u63a8\u4e3a\u4e3b\uff0c\u6280\u672f\u63a8\u548c\u533b\u5b66\u63a8\u6781\u5c11\u6570\u3002","lang":"en","default_profile":false,"profile_background_tile":false,"verified":false,"screen_name":"gh05tw01f","url":"http://www.cnblogs.com/ayanamist/","profile_image_url_https":"https://si0.twimg.com/profile_images/1470742579/avatar_normal.PNG","contributors_enabled":false,"time_zone":"Beijing","name":"ayanamist","geo_enabled":true,"profile_text_color":"3C3940","followers_count":876,"profile_sidebar_border_color":"5ED4DC","id_str":"8104012","profile_background_color":"0099B9","following":true,"favourites_count":47,"listed_count":53,"created_at":"Fri Aug 10 13:52:07 +0000 2007","location":"Wuhan, China"},"geo":null,"id":115061186621476864,"source":"<a href=\"http://code.google.com/p/twiotaku/\" rel=\"nofollow\">TwiOtaku</a>","created_at":"Sat Sep 17 13:54:59 +0000 2011","retweeted":false,"coordinates":null,"in_reply_to_user_id_str":null,"entities":{"user_mentions":[],"hashtags":[],"urls":[]},"in_reply_to_status_id_str":null,"in_reply_to_screen_name":null,"in_reply_to_user_id":null,"place":null,"retweet_count":0,"id_str":"115061186621476864"}'

status = twitter.Status(myjson.loads(_text))
status['retweeted_status'] = twitter.Status(myjson.loads(_text_retweeted_status))
status['retweeted_status']['in_reply_to_status'] = twitter.Status(myjson.loads(_text_in_reply_to_status))