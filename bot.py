import telebot
from ai import ai

api_key=""
bot=telebot.TeleBot(api_key)
@bot.message_handler(commands=['start','info','help'])
def send_welcome(message):
    bot.reply_to(message,"Приветствую вас в English Adventure, здесь вы можете попрактиковаться в использовании английского языка в жизненных ситуациях, \nдля того чтобы начать игру /start_game")
@bot.message_handler(commands=['start_game'])
def handle_message(message):
    """Обработка любого текстового сообщения."""
    user_id = message.chat.id
    user_input = message.text

    bot.send_chat_action(user_id, 'typing')

    response_text = ai(user_id,"/start_game")

    # Отправляем полученный ответ пользователю просто как сырой текст
    bot.reply_to(message, response_text)
@bot.message_handler(content_types=['text'])
def send_message(message):
    user_input=message.text
    user_id=message.chat.id
    response_text=ai(user_id,user_input)
    if not response_text:
        response_text="Ошибка бота"
    bot.reply_to(message, f"{response_text}")
print("Бот запущен...")
bot.infinity_polling()
