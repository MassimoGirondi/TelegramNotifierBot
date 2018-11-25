import telepot
import config
import sys

# Check if all parameters are present
# ./tg_notify.py ProgramName Text

if len(sys.argv)!=3:
	print('Error in parameters')
program=sys.argv[1]
text=sys.argv[2]
message='`'+program+'`\n'
message+=text



bot = telepot.Bot(config.KEY)
for u in config.IDS:
	bot.sendMessage(u, message, parse_mode='Markdown')
