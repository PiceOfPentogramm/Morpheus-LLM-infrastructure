# Telegram бот
# Принимает сообщения от пользователя и отправляет их в API

from telebot import types, TeleBot

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot = TeleBot(token)

    @self.bot.message_handler(commands=['start'])
    def handle_start(message):
        self.bot.send_message(message.chat.id, "Соединение подтвержденно.")

    @self.bot.message_handler(func=lambda message: True)
    def handle_message(message):
        # Создание кнопки "Regenerate"
        markup = types.InlineKeyboardMarkup()
        regen_button = types.InlineKeyboardButton("🔁", callback_data="regenerate")
        markup.add(regen_button)

        # обработка сообщения и отправка ответа от LLM core
        self.bot.send_message(message.chat.id, "Сообщение получено.", parse_mode='Markdown', reply_markup=markup) # Отправка ответа пользователю от LLM в формате Markdown

    @self.bot.callback_query_handler(func=lambda call: call.data == "regenerate")
    def handle_regenerate(call):
        # Пересоздание сообщения с другим random
        self.bot.send_message(call.message.chat.id, "Регенерация запущена.")

    def start(self):
        self.bot.infinity_polling()
        # Запустить бота

    

