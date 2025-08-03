import telebot

bot=telebot.TeleBot('SEU_TOKEN_AQUI')

@bot.message_handler(['start','help'])
def start(msg:telebot.types.Message):
    bot.reply_to(msg,'Olá, Mundo!')
    
@bot.message_handler(func=lambda msg: True)
def pegar_chat_id(msg):
    print(f"🧾 Seu chat_id é: {msg.chat.id}")
    bot.reply_to(msg, "Chat ID capturado! Pode voltar pro scraper 😄")
    
bot.infinity_polling()