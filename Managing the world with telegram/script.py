import telebot;
from mcrcon import MCRcon
from time import sleep
import os

print("Автор stepan091991")
user_agreement = open("user agreement.txt", "r", encoding="utf-8")
agreement = user_agreement.readline()
user_agreement.close()
if agreement.replace("\n","") != "True":
	while True:
		print("ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ!")
		print("При соглашении вы подтверждаете то, что при любом изменении кода или нахождении бага")
		print("вы напишите об этом на почту mana_the_world_with_tel_help@mail.ru и даждётесь ответа.")
		print("Вы не будите изменять пользовательское соглашение и автора скрипта.")
		print("Скрипт является полностью бесплатным.")
		print("Вы согласны с пользовательским соглашением?")
		user_agreement_result = input("Yes/No:")
		if user_agreement_result == "Yes":
			user_agreement = open("user agreement.txt", "w", encoding="utf-8")
			user_agreement.write("True")
			user_agreement.close()
			break
		elif user_agreement_result == "No":
			exit(0)
		else:
			print("Неизвестная каманда!")
user_agreement.close()
Token = ""
Start_message = """
Привет, вот каманды (:
Каманда!
Каманда!
"""
None_command_message = ""
Debug_messages = "False"
Server_IP = ""
Auto_run_server = "False"
Part_to_server_bat = ""
Server_run_time = 10
Stop_server_message = ""
Rcon_password = ""

bot = telebot.TeleBot(Token.replace("\n",""));
print("Запускаю сервер!")
if Auto_run_server == "True":
	os.startfile(Part_to_server_bat)
	sleep(10)
print("Успешно!")
print("Установка соединения по Rcon!")
mcr = MCRcon(Server_IP, Rcon_password)
mcr.connect()
print("Успешно!")
print("Бот запущен!")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	data = open("data.txt", "r", encoding="utf-8")
	print(Bal_coint)
	while True:
		comment = data.readline()
		if not comment:
			bot.send_message(message.from_user.id, None_command_message)
			data.close()
			break
		message_key = data.readline()
		message_return = data.readline()
		message_console = data.readline()
		minecraft_action = data.readline()
		if message.text == "/start":
			bot.send_message(message.from_user.id, Start_message)
			break
		if message.text == "stop":
			resp = mcr.command("stop")
			exit(0)
		if Debug_messages == "True":
			print(message.text + "<and>" + message_key.replace("\n",""))
		if message.text == message_key.replace("\n",""):
			if Debug_messages == "True":	
				print(message_console)
				resp = mcr.command(minecraft_action)
				print(resp)
				bot.send_message(message.from_user.id, message_return)
				data.close()
				break
			else:
				resp = mcr.command(minecraft_action)
				bot.send_message(message.from_user.id, message_return)
				data.close()
				break
			
bot.polling(none_stop=True, interval=0)
