import telepot
import config
import time
from telepot.loop import MessageLoop
bot = telepot.Bot(config.KEY)
print(bot.getMe())

# Function run every time a message is received 
def handle(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    print(content_type, chat_type, chat_id)
 
bot.message_loop(handle)
print ('Waiting for new messages...')
while 1:
	time.sleep(10)
