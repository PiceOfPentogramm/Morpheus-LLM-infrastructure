# Короткая память
# Хранит последние 5-10 сообщений диалога


class ShortMemory:
    """
    Короткая память - хранит последние сообщения диалога.
    
    Это контекст текущего разговора, чтобы LLM помнила о чём шла речь.
    Например: если пользователь спрашивает "А что ты об этом думаешь?",
    LLM должна помнить предыдущие сообщения.
    """
    
    def __init__(self, max_messages=10):
        """
        Инициализация короткой памяти.
        
        Параметры:
            max_messages: Максимальное количество сообщений в памяти
        """
        self.history = []  # Список сообщений
        self.max_messages = max_messages
    
    def add(self, user_msg, bot_msg):
        """
        Добавить новое сообщение в память.
        
        Параметры:
            user_msg: Сообщение пользователя
            bot_msg: Ответ бота
        """
        self.history.append({
            "user": user_msg,
            "bot": bot_msg
        })
        
        # Если память переполнена, удаляем самое старое сообщение
        if len(self.history) > self.max_messages:
            self.history.pop(0)
    
    def get_history(self):
        """
        Получить историю диалога в текстовом виде.
        
        Возвращает:
            Текст с историей сообщений
        """
        if not self.history:
            return ""
        
        text_parts = []
        for msg in self.history:
            text_parts.append(f"Пользователь: {msg['user']}")
            text_parts.append(f"Бот: {msg['bot']}")
        
        return "\n".join(text_parts)
    
    def clear(self):
        """Очистить память."""
        self.history = []
