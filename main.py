import telebot,random
from qiwi import *
token = '1347566794:AAE9L1SBoTGT8peiqxjwb4yyUugr1MsLauQ'
bot = telebot.TeleBot(token)

#qiwi_autoreg = open("qiwi_autoreg.txt","r")

back_kb = telebot.types.ReplyKeyboardMarkup(1) # Back key
back_kb.row("Back")

shop_kb = telebot.types.ReplyKeyboardMarkup(1) # Shop keyboard
shop_kb.row("Qiwi","Qiwi/Yandex.Money Verefication","Accounts")

qiwi_kb = telebot.types.ReplyKeyboardMarkup(1) # Qiwi keyboard
qiwi_kb.row("Qiwi : Autoreg","Qiwi : Main Verefication","Qiwi : Api + Card + Veref.","Back")

veref_kb = telebot.types.ReplyKeyboardMarkup(1) # Verefication data keyboard
veref_kb.row("Veref Data : Passport + ИНН or СНИЛС","Back")

acc_kb = telebot.types.ReplyKeyboardMarkup(1)
acc_kb.row("Back") #Empty Category

@bot.message_handler(commands=['check'])
def pay_check(message):
    good = 0
    a1,a2,a3 = get_last_pay()
    if a1 == 'SUCCESS':
        good = 1
    else:
        good = 0
    if a3 == int(message.text[7:13]):
        good = 1
    else:
        good = 0
    if a2 == int(message.text[15:len(message.text)]):
        good = 1
    else:
        good = 0

    if good == 1:
        bot.send_message(message.chat.id,buy,reply_markup=shop_kb)
        bot.send_message(message.chat.id,"Thanks for buy!",buy,reply_markup=shop_kb)
    else:
        bot.send_message(message.chat.id,"Payment not found")        
@bot.message_handler(commands=['start'])
def hello_msg(message):
    bot.send_message(message.chat.id,f"Hello @{message.from_user.username}!",reply_markup=shop_kb)

@bot.message_handler(commands=['qiwi_1','qiwi_2','qiwi_3'])
def qiwi(message):
    if int(message.text[7:len(message.text)]) > 0:
        if message.text[6] == '1':
            cof = 5
            prodt = "Qiwi autoreg"
        elif message.text[6] == '2':
            cof = 30
            prodt = "Qiwi Main verefication"
        elif message.text[6] == '3':
            cof = 50
            prodt = "Qiwi Api + Card + Verefication"
        pay_total = int(message.text[7:len(message.text)])*cof
        pay_cm = ""
        for i in range(6):
            pay_cm += f"{random.randint(0,9)}"
        check_kb =telebot.types.ReplyKeyboardMarkup(1)
        check_kb.row(f"/check {pay_cm} {pay_total}","Back")
        bot.send_message(message.chat.id,f"Products:\n{prodt}\n{message.text[8:len(message.text)]} pieces\n\nPayments:\nEmpty :(\n\nComment for pay: {pay_cm}\n\nTotal: {pay_total} rub\n\nPay only rub!",reply_markup=check_kb)
    else:
        bot.send_message(message.chat.id,"Enter positive number!")
@bot.message_handler(content_types=['text'])
def switcher(message):
    text = message.text
    if text == "Shop" or text == "Back":
        bot.send_message(message.chat.id,"Select category",reply_markup=shop_kb)
    elif text == "Qiwi":
        bot.send_message(message.chat.id,"Selected: Qiwi",reply_markup=qiwi_kb)
    elif text == "Qiwi/Yandex.Money Verefication":
        bot.send_message(message.chat.id,"Selected: Q/YM Verfication",reply_markup=veref_kb)
    elif text == "Accounts":
        bot.send_message(message.chat.id,"Selected: Accounts",reply_markup=acc_kb)
        bot.send_message(message.chat.id,"Sorry, we haven`t accounts(")
    elif text == "Qiwi : Autoreg":
        bot.send_message(message.chat.id,"Price: 5 rub/thing\n\nIndicate the quantity\n\nExample: /qiwi_1 10\nGet 10 Qiwi autoreg",reply_markup=back_kb)
   
bot.polling()
