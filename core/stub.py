# Заглушка ядра для MVP
# Просто возвращает простой ответ, чтобы проверить работу инфраструктуры

class CoreStub:
    def process(self, message):
        # Простая заглушка - возвращает эхо сообщения
        return f"Получил ваше сообщение: {message}"
    
    def health_check(self):
        # Проверка работы ядра
        return {"status": "ok", "message": "Заглушка работает!"}
