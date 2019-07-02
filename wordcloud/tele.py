import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import WC

token = "620472562:AAENVcmTsxZZSCA_5boE2QBTeLWaTKt6nI4"
bot = telegram.Bot(token = token)
#def get_message(bot, update):
#    update.message.reply_text(update.message.text)
def get_wordcloud(bot, update):
    WC.wcClass(update.message.text).main()
    print(update.message.chat_id, update.message, "./wcimg/"+update.message.text+".png")
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open("./wcimg/"+update.message.text+".png",'rb'))
def get_whatyourname(bot, update):
    update.message.reply_text("HeonJin Jeong")
updater = Updater(token)
#messagehandler = MessageHandler(Filters.text, get_message)
#updater.dispatcher.add_handler(messagehandler)
messagehandler = MessageHandler(Filters.text, get_wordcloud)
updater.dispatcher.add_handler(messagehandler)
commanderhandler = CommandHandler("name", get_whatyourname)
updater.dispatcher.add_handler(commanderhandler)
updater.start_polling(timeout=10, clean=True)
updater.idle()
