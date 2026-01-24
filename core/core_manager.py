# Главный менеджер ядра
# Выбирает источник LLM и режим работы

from core.llm_providers.external_llm import ExternalLLM
from core.llm_providers.local_llm import LocalLLM
from core.modes.simple_mode import SimpleMode
from core.modes.memory_mode import MemoryMode


class CoreManager:
    """
    Главный класс ядра.
    Выбирает источник LLM (внешний или локальный) 
    и режим обработки (простой или с памятью).
    """
    
    def __init__(self, llm_source="external", mode="simple", api_key=None, model_path=None):
        """
        Инициализация ядра.
        
        Параметры:
            llm_source: Источник LLM - "external" (внешний API) или "local" (локальная модель)
            mode: Режим работы - "simple" (прямой) или "memory" (с памятью)
            api_key: Ключ API для внешней LLM
            model_path: Путь к локальной модели
        """
        # Выбираем источник LLM
        if llm_source == "external":
            self.llm = ExternalLLM(api_key=api_key)
            print("✅ Используется внешняя LLM")
        else:
            self.llm = LocalLLM(model_path=model_path)
            print("✅ Используется локальная LLM")
        
        # Выбираем режим работы
        if mode == "simple":
            self.processor = SimpleMode(self.llm)
            print("✅ Режим: простой (без памяти)")
        else:
            self.processor = MemoryMode(self.llm)
            print("✅ Режим: с трёхслойной памятью")
    
    def process_message(self, user_message, is_regeneration=False):
        """
        Обработать сообщение пользователя.
        
        Параметры:
            user_message: Текст сообщения от пользователя
            is_regeneration: Это регенерация ответа или новое сообщение
        
        Возвращает:
            Ответ от LLM
        """
        try:
            response = self.processor.process(user_message, is_regeneration)
            return response
        except Exception as e:
            return f"❌ Ошибка ядра: {e}"
