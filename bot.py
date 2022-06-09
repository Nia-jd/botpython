# -*- coding: utf-8 -*-
#from distutils.util import copydir_run_2to3
#from multiprocessing import context
import mysql.connector
#from telegram import Update
from telegram.ext import(Updater,CommandHandler, MessageHandler,Filters)

#from multiprocessing import connection
#import mysql.connector
db = mysql.connector.connect(
	user='root', 
	password='',
	host='localhost',
	database='usuarios_bot',
	port=3306
    
)
print(db)

def inicio(update,context):
	context.bot.send_message(update.message.chat_id,'''BIENVENIDO
	\n/new_ingresos
	\n/new_gastos''')

def tec(update,context):
	bot = context.bot
	updateMsg= getattr(update, 'message', None)
	messageId = updateMsg.message_id #obtener el id del mensaje
	chatId = update.message.chat_id
	userName = update.effective_user['first_name']
	text = update.message.text#obtener el texto q envia un usuario

	ingresos = '/new_ingresos'
	gastos = '/new_gastos'

	if ingresos in text:

		bot.sendMessage(
			chat_id = chatId,
			parse_mode="HTML",
			text=f'Digita <b>/nuevos_ingresos</b> + el monto'
		)
	if gastos in text:

		bot.sendMessage(
			chat_id = chatId,
			parse_mode="HTML",
			text=f'Digita <b>/nuevos_gastos</b> + el monto'
		)
	

def new_ingresos(update,context):
	#context.bot.send_message(update.message.chat_id,"Ingrese el monto")
	var=int(context.args[0])
    
	valor=context.args[2]
	fecha=context.args[3]
	des=context.args[1]

	cursor = db.cursor()
	cursor.execute("INSERT INTO ingresos(id,descripcion,valor,fecha) VALUES (%s,%s,%s,%s)",(var,des,valor,fecha))

	db.commit()

def new_gastos(update,context):
	#context.bot.send_message(update.message.chat_id,"Ingrese el monto")
	var=int(context.args[0])
	valor=context.args[2]
	fecha=context.args[3]
	des=context.args[1]

	cursor = db.cursor()
	cursor.execute("INSERT INTO gastos(id,descripcion,valor,fecha) VALUES (%s,%s,%s,%s)",(var,des,valor,fecha))

	db.commit()


def main():
	TOKEN = "5340038938:AAF_xGuwOUVHwtz7B1Ysl7axdouSy0XwgWo"
	updater = Updater(TOKEN, use_context=True)
	dp=updater.dispatcher
    
	dp.add_handler(CommandHandler('Inicio',inicio))
	dp.add_handler(CommandHandler('nuevos_ingresos',new_ingresos))
	dp.add_handler(CommandHandler('nuevos_gastos',new_gastos))
	dp.add_handler(MessageHandler(Filters.text,tec))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()


