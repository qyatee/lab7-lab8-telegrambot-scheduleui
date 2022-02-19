import telebot
import psycopg2
from telebot import types
from week import weeker

conn = psycopg2.connect(database="schedulev3",
                        user="postgres",
                        password="privet",
                        host="localhost",
                        port="5432",)
cursor = conn.cursor()

c = int(weeker())  # глобальная переменная, принимающая 1(нечетная) или 0(четная)

token = "2075108574:AAHqeuLvaUv3t3zkd2O9CBqdqdeLCfKkNSo"
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("Понедельник", "Вторник")
keyboard1.row("Среда", "Четверг")
keyboard1.row("Пятница")
keyboard1.row("Расписание на текущую неделю")
keyboard1.row("Расписание на следующую неделю")
keyboard1.row("/help")


@bot.message_handler(commands=['start'])
def start_message(message):
    global c, keyboard1
    bot.send_message(message.chat.id, 'Вас приветствует GoryachevBot. Выберите день недели на который хотите узнать раписание', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я служу для того, чтобы вы могли узнать актуальное учебное расписание на любой '
                                      'день недели. Для корректной работы используйте кнопки.\nДоступные команды:\n/mtuci - вывод ссылки на сайт МТУСИ\n/week - вывод типа недели (четная/нечетная)')

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ссылка на сайт МТУСИ: https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def start_message(message):
	global c
	if c==0:
		bot.send_message(message.chat.id, 'Сейчас четная неделя')
	else:
		bot.send_message(message.chat.id, 'Сейчас нечетная неделя')

@bot.message_handler(content_types=['text'], )
def manipulator(message):
	global c, keyboard0, keyboard1
	if message.text == 'Расписание на текущую неделю' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Понедельник, дистанционный режим\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Вторник, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Среда, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Четверг, метро Авиамоторная\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Пятница, метро Октябрьское поле\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Расписание на следующую неделю' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Понедельник, дистанционный режим\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Вторник, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Среда, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Четверг, метро Авиамоторная\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Пятница, метро Октябрьское поле\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Расписание на текущую неделю' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Понедельник, дистанционный режим\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Вторник, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Среда, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Четверг, метро Авиамоторная\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Пятница, метро Октябрьское поле\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Расписание на следующую неделю' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Понедельник, дистанционный режим\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Вторник, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Среда, дистанционный режим\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Четверг, метро Авиамоторная\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 += 'Пятница, метро Октябрьское поле\n\n'
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Понедельник' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, четная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Понедельник' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Понедельник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, нечетная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Вторник' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, четная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Вторник' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Вторник' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, нечетная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Среда' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, четная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Среда' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Среда' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('Дистанционный режим, нечетная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Четверг' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('метро Авиамоторная, четная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Четверг' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Четверг' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('метро Авиамоторная, нечетная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Пятница' and c == 0:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 0 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('метро Октябрьское поле, четная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	elif message.text == 'Пятница' and c == 1:
		cursor.execute("SELECT timetable.subject, teacher.full_name, "
					   "timetable.room_numb, timetable.start_time FROM timetable JOIN teacher ON timetable.teacher = "
					   "teacher.id WHERE timetable.day = 'Пятница' AND timetable.weektype = 1 ORDER BY timetable.start_time;")
		out = cursor.fetchall()
		out1 = str('метро Октрябрьское поле, нечетная неделя\n\n')
		for row in out:
			for i in range(4):
				out1 += str(row[i]) + '\n'
			out1 += '\n'
		bot.send_message(message.chat.id, out1)
	else:
		bot.send_message(message.chat.id, 'Извините, я Вас не понял. Для справки введите /help')

bot.infinity_polling()