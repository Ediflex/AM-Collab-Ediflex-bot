 
 ​class​ ​script​(​object​): 
 ​    ​START_TXT​ ​=​ ​"""𝙷𝙴𝙻𝙾 {}, 
 ​𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/movie_bus6{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍""" 
 ​    ​HELP_TXT​ ​=​ ​"""𝙷𝙴𝚈 {} 
 ​𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.""" 
 ​    ​ABOUT_TXT​ ​=​ ​"""✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {} 
 ​✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Mallu_mass>ℤ𝕚𝕟𝕒𝕟 𝕋𝕖𝕔𝕙2.0</a> 
 ​✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 
 ​✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹 
 ​✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱 
 ​✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄 
 ​✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v6.8.1 [ 𝙴𝙳𝙸𝙵𝙻𝙴𝚇 ]""" 
 ​    ​SOURCE_TXT​ ​=​ ​"""<b>NOTE:</b> 
 ​- 𝚁𝚎𝚡𝚎𝚛 is a open source project.  
 ​- Source - https://github.com/Ediflex/AM-Collab-Ediflex-bot
  
 ​<b>DEVS:</b> 
 ​- <a href=https://t.me/movie_bus6> 𝗥𝗲𝘅𝗲𝗿📽™ </a>""" 
 ​    ​MANUELFILTER_TXT​ ​=​ ​"""Help: <b>Filters</b> 
  
 ​- Filter is the feature were users can set automated replies for a particular keyword and Movieworld will respond whenever a keyword is found the message 
  
 ​<b>NOTE:</b> 
 ​1. Rexer should have admin privillage. 
 ​2. only admins can add filters in a chat. 
 ​3. alert buttons have a limit of 64 characters. 
  
 ​<b>Commands and Usage:</b> 
 ​• /filter - <code>add a filter in chat</code> 
 ​• /filters - <code>list all the filters of a chat</code> 
 ​• /del - <code>delete a specific filter in chat</code> 
 ​• /delall - <code>delete the whole filters in a chat (chat owner only)</code>""" 
 ​    ​BUTTON_TXT​ ​=​ ​"""Help: <b>Buttons</b> 
  
 ​- Rexer Supports both url and alert inline buttons. 
  
 ​<b>NOTE:</b> 
 ​1. Telegram will not allows you to send buttons without any content, so content is mandatory. 
 ​2. Rexer supports buttons with any telegram media type. 
 ​3. Buttons should be properly parsed as markdown format 
  
 ​<b>URL buttons:</b> 
 ​<code>[Button Text](buttonurl:https://t.me/movie_bus6)</code> 
  
 ​<b>Alert buttons:</b> 
 ​<code>[Button Text](buttonalert:This is an alert message)</code>""" 
 ​    ​AUTOFILTER_TXT​ ​=​ ​"""Help: <b>Auto Filter</b> 
  
 ​<b>NOTE:</b> 
 ​1. Make me the admin of your channel if it's private. 
 ​2. make sure that your channel does not contains camrips, porn and fake files. 
 ​3. Forward the last message to me with quotes. 
 ​ I'll add all the files in that channel to my db.""" 
 ​    ​CONNECTION_TXT​ ​=​ ​"""Help: <b>Connections</b> 
  
 ​- Used to connect bot to PM for managing filters  
 ​- it helps to avoid spamming in groups. 
  
 ​<b>NOTE:</b> 
 ​1. Only admins can add a connection. 
 ​2. Send <code>/connect</code> for connecting me to ur PM 
  
 ​<b>Commands and Usage:</b> 
 ​• /connect  - <code>connect a particular chat to your PM</code> 
 ​• /disconnect  - <code>disconnect from a chat</code> 
 ​• /connections - <code>list all your connections</code>""" 
 ​    ​EXTRAMOD_TXT​ ​=​ ​"""Help: <b>Extra Modules</b> 
  
 ​<b>NOTE:</b> 
 ​these are the extra features of Movie World 
  
 ​<b>Commands and Usage:</b> 
 ​• /id - <code>get id of a specifed user.</code> 
 ​• /info  - <code>get information about a user.</code> 
 ​• /imdb  - <code>get the film information from IMDb source.</code> 
 ​• /search  - <code>get the film information from various sources.</code>""" 
 ​    ​ADMIN_TXT​ ​=​ ​"""Help: <b>Admin mods</b> 
  
 ​<b>NOTE:</b> 
 ​This module only works for my admins 
  
 ​<b>Commands and Usage:</b> 
 ​• /logs - <code>to get the rescent errors</code> 
 ​• /stats - <code>to get status of files in db.</code> 
 ​• /delete - <code>to delete a specific file from db.</code> 
 ​• /users - <code>to get list of my users and ids.</code> 
 ​• /chats - <code>to get list of the my chats and ids </code> 
 ​• /leave  - <code>to leave from a chat.</code> 
 ​• /disable  -  <code>do disable a chat.</code> 
 ​• /ban  - <code>to ban a user.</code> 
 ​• /unban  - <code>to unban a user.</code> 
 ​• /channel - <code>to get list of total connected channels</code> 
 ​• /broadcast - <code>to broadcast a message to all users</code>""" 
 ​    ​STATUS_TXT​ ​=​ ​"""★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code> 
 ​★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code> 
 ​★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code> 
 ​★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱 
 ​★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱""" 
 ​    ​LOG_TEXT_G​ ​=​ ​"""#NewGroup 
 ​Group = {}(<code>{}</code>) 
 ​Total Members = <code>{}</code> 
 ​Added By - {} 
 ​""" 
 ​    ​LOG_TEXT_P​ ​=​ ​"""#NewUser 
 ​ID - <code>{}</code> 
 ​Name - {} 
 ​"""
