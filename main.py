import telebot, functions, random, time
bot = telebot.TeleBot('5891684002:AAF9GzovRLlRapruKpGQLvFxoVGVeuwgB4I')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в CANDYS', reply_markup=functions.buttons('Курсы валют'))
    bot.register_next_step_handler(message, mainmenu)
    
@bot.message_handler(content_types=['text'])
def mainmenu(message):
    if message.text == 'Курсы валют':
        bot.send_message(message.chat.id, f'Выберите валюту.', reply_markup=functions.valbuttons())
        bot.register_next_step_handler(message, value)

def value(message):
    finded = functions.findobject(functions.valsdict(), message.text)
    if finded != 0:
        bot.send_message(message.chat.id, functions.change(finded), reply_markup=functions.buttons('Курсы валют'))
    bot.register_next_step_handler(message, mainmenu)
bot.polling(none_stop=True, interval=0)