#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import requests

def bbva(i):
    b = requests.get('https://hb.bbv.com.ar/fnet/mod/inversiones/NL-dolareuro.jsp')
    aa = b.text.replace('\t', '').replace('\n', '')
    return re.findall('[0-9]*,[0-9]*', aa)[i]

def lala(i):
    b = requests.get('https://banco.santanderrio.com.ar/exec/cotizacion/index.jsp')
    aa = b.text.replace('\t', '').replace('\n', '')
    return re.findall('\$ [0-9]*,[0-9]*', aa)[i]

@respond_to('venta', re.IGNORECASE)
def hello_reply(message):
    message.reply('SANTANDER V:' + lala(0) + '| BBVA V:' + bbva(1))

@respond_to('dolar', re.IGNORECASE)
def hello_reply(message):
    message.reply('SANTANDER C:' + lala(1) + '| BBVA C:' + bbva(2))

@default_reply
def my_default_handler(message):
    message.reply('Es todo un tema.')