# Настройки приложения

class Settings:
    # API настройки
    API_PORT = 5000
    API_HOST = "127.0.0.1"
    
    # Telegram настройки
    BOT_TOKEN = None  # Будет установлен через GUI
    
    # Общие настройки
    DEBUG_MODE = False
    
    @classmethod
    def load_from_file(cls, filepath):
        # Загрузить настройки из файла
        pass
    
    @classmethod
    def save_to_file(cls, filepath):
        # Сохранить настройки в файл
        pass
