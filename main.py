# Главный файл запуска приложения
# Этот файл будет упакован в .exe

from infrastructure.gui.main_window import SettingsWindow
from infrastructure.telegram.bot import TelegramBot
from infrastructure.api.server import APIServer
from core.stub import CoreStub
from config.settings import Settings

def main():
    print("Запуск Morpheus...")
    
    # 1. Показать окно настройки
    window = SettingsWindow()
    window.show()
    
    # 2. Получить токен бота
    bot_token = window.get_bot_token()
    Settings.BOT_TOKEN = bot_token
    
    # 3. Запустить API сервер
    api_server = APIServer(port=Settings.API_PORT)
    api_server.start()
    
    # 4. Запустить Telegram бота
    bot = TelegramBot(bot_token)
    bot.start()
    
    # 5. Инициализировать ядро (пока заглушка)
    core = CoreStub()
    
    print("Morpheus запущен! Все действия теперь через Telegram бот.")

if __name__ == "__main__":
    main()
