from telebot import types, TeleBot


class TelegramBot:
    def __init__(self, token: str):
        self.bot = TeleBot(token)

        self.bot.message_handler(func=lambda message: True)(self.handle_message)
        self.bot.callback_query_handler(func=lambda call: call.data == "regenerate")(self.handle_regenerate)

    def _llm_stub(self, regen: bool, text_message: str) -> str:
        if not regen:
            # Если это первоначальная генерация
            return "заменённое сообщение"
        else:
            # Если это регенерация
            return "заменённое сообщение"

    def handle_message(self, message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔁", callback_data="regenerate"))
        generation_result = self._llm_stub(regen=False, text_message=message.text)

        # Отправляем сообщение
        self.bot.send_message(
            message.chat.id,
            generation_result,
            reply_markup=markup
        )

    def handle_regenerate(self, call):
        # 1) Закрыть "крутилку" у кнопки (Telegram ждёт ответ на callback) [web:24]
        try:
            self.bot.answer_callback_query(call.id)
        except Exception:
            pass

        chat_id = call.message.chat.id
        message_id = call.message.message_id
        message_txt = call.message.text

        # 2) Меняем текст того же сообщения на "Печатает...." [web:24][web:21]
        self.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Печатает...."
        )

        # 3) Заглушка вместо LLM
        regeneration_result = self._llm_stub(regen=True, text_message=message_txt)

        # 4) Меняем текст на результат, и возвращаем кнопку [web:24][web:21]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔁", callback_data="regenerate"))

        self.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=regeneration_result,
            reply_markup=markup
        )

    def start(self):
        self.bot.infinity_polling()
