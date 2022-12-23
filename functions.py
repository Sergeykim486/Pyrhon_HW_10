import telebot
from telebot import types
import random, requests

def buttons(buttons):
    mark = types.ReplyKeyboardRemove()
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mark.row(buttons)
    return mark

def change(val):
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    return f"Курс {data['Valute'][val]['Name']} - {data['Valute'][val]['Value']}"

def valbuttons():
    mark = types.ReplyKeyboardRemove()
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    for item in data['Valute']:
        mark.row(data['Valute'][item]['Name'])
    return mark

def valsdict():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    res = dict()
    for item in data['Valute']:
        res[data['Valute'][item]['Name']] = data['Valute'][item]['CharCode']
    return res

def findobject(data, obj):
    res = 0
    for item in data:
        if item == obj:
            res = data[item]
    return res