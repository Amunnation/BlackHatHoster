import os
import telebot

API_KEY = os.getenv('API_KEY') 
bot = telebot.Telebot('API_KEY')
                     
@bot.message_handler(commands=['interview'])
def interview(message):          
  bot send_message(message.chat.id,"Okay Let Me Prepare A Set Of Questions")

bot.polling()

