from core.llm_providers.external_llm import ExternalLLM
from core.llm_providers.local_llm import LocalLLM
from core.modes.simple_mode import SimpleMode
from core.modes.memory_mode import MemoryMode


class CoreManager:
    """
    Главный класс ядра.
    Выбирает источник LLM и режим работы.
    """
    def __init__(self, llm_source="external", mode="simple", api_key=None):
        # Выбираем источник LLM
        if llm_source == "external":
            self.llm = ExternalLLM(api_key=api_key)
        else:
            self.llm = LocalLLM()
        
        # Выбираем режим работы
        if mode == "simple":
            self.processor = SimpleMode(self.llm)
        else:
            self.processor = MemoryMode(self.llm)
    
    def process_message(self, user_message, is_regeneration=False):
        """
        Обработать сообщение пользователя.
        
        Args:
            user_message: текст от пользователя
            is_regeneration: это регенерация или новое сообщение
        
        Returns:
            Ответ от LLM
        """
        response = self.processor.process(user_message, is_regeneration)
        return response
