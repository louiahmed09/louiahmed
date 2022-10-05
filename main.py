import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SUDO = int(os.environ.get("SUDO","5359109940"))
Heroku = os.environ.get("HEROKU", "APP-NAME")
APP_URL = "https://"+ Heroku +".herokuapp.com/" + BOT_TOKEN
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

ban = []

@bot.message_handler(commands=["start"])
def start(message):
	f = message.from_user.id
	if f == SUDO:
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.send_message(message.chat.id, text=f"- أهلاً {message.from_user.first_name}  !\n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	else:
		rr = types.InlineKeyboardMarkup(row_width=2)
		me = types.InlineKeyboardButton(text="يوزري",url="https://t.me/Y_U_8")
		ch = types.InlineKeyboardButton(text="▶ قناة البوت ◀",url="https://t.me/W_B_Y")
		rr.add(me,he,de)
		rr.add(ch)
		bot.send_message(message.chat.id,text="هذا البوت مدفوع وليس لك\n للتفعيل راسل",reply_markup=rr)
               
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="Y_U_8":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="(KKKK4)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="(FF8FF)", callback_data="F2")
		
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		
		F = types.InlineKeyboardButton(text ="(UUU4UU)", callback_data="F7")
		
		M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	elif call.data == "SS":
		v = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		S = types.InlineKeyboardButton(text ="(G_K_K)", callback_data="F10")
		B = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		v.add(K,J,O,I,S)
		v.add(B)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=v)
	elif call.data =="F1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "1234567890"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			us1 = str(us)+str(us)+str(us)+str(us)+str(ua)
			us2 = str(us)+str(us)+str(us)+str(ua)+str(us)
			us3 = str(us)+str(us)+str(ua)+str(us)+str(us)
			us4 = str(us)+str(ua)+str(us)+str(us)+str(us)
			d = [us1,us2,us3,us4]
			h = random.choice(d)
			url = "https://t.me/"+h
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and d not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{h}\n────── • ✧✧ • ──────\n•مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{h}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
			
	elif call.data =="F8":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(c8bot)",callback_data="b1")
		c = types.InlineKeyboardButton(text="(vd2bot)",callback_data="b2")
		z = types.InlineKeyboardButton(text="(wdv4bot)",callback_data="b4")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="F100":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(vv_vv)",callback_data="ew1")
		c = types.InlineKeyboardButton(text="(UUU4UU)",callback_data="F7")
		d = types.InlineKeyboardButton(text="(FFAAA)",callback_data="ew")
		z = types.InlineKeyboardButton(text="(KKKK4)",callback_data="F1")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z,d)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="bckkk":
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
		
	
	elif call.data =="b4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(u2s)+str(un)+"bot"
			u2 = str(us)+str(un)+str(u2s)+str(u1s)+"bot"
			u3 = str(us)+str(u1s)+str(un)+str(u2s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	
	elif call.data =="ew1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+"_"+str(us)+str(us)
			u2= str(us)+"_"+str(us)+str(us)+str(us)
			u3= str(us)+str(us)+str(us)+"_"+str(us)
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="ew":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+str(us)+str(u1s)+str(u1s)
			u2= str(u1s)+str(u1s)+str(us)+str(us)+str(us)
			g = [u1,u2]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="b2":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(un)+"bot"
			u2 = str(us)+str(u1s)+str(u2s)+"bot"
			u3 = str(us)+str(un)+str(u1s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	
		
	elif call.data =="b1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(un)+"bot"
			u2 = str(us)+str(u1s)+"bot"
			f = [u1,u2]
			v = random.choice(f)
			url = "https://t.me/"+v
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and f not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{v}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{v}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F6":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(u2s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F5":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1n)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(un)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F3":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F7":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			h1 = str(us)+str(un)+str(us)+str(us)+str(us)+str(us)
			h2 = str(us)+str(us)+str(un)+str(us)+str(us)+str(us)
			h3 = str(us)+str(us)+str(us)+str(un)+str(us)+str(us)
			h4 = str(us)+str(us)+str(us)+str(us)+str(un)+str(us)
			h5 = str(us)+str(us)+str(us)+str(us)+str(us)+str(un)
			Y_U_8 = [h1,h2,h3,h4,h5]
			j = random.choice(Y_U_8)
			url = "https://t.me/"+j
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and j not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{j}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{j}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				Y_U_8 = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,Y_U_8)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
	elif call.data =="F10":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(us)+"_"+str(u2s)
			d = str(u1s)+"_"+str(us)+"_"+str(us)
			v = str(us)+"_"+str(u1s)+"_"+str(us)
			p = str(us)+"_"+str(un)+"_"+str(us)
			m = str(us)+"_"+str(us)+"_"+str(un)
			i = str(us)+"_"+str(un)+"_"+str(un)
			cs = [c,d,v,p,m,i]
			cc = random.choice(cs)
			url = "https://t.me/"+cc
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and cs not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{cc}\n────── • ✧✧ • ──────\n• مطور البوت @Y_U_8")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{cc}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/Y_U_8')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
  
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://"+ Heroku +".herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
