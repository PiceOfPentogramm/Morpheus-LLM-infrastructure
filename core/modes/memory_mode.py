# Режим с трёхслойной памятью
# Использует короткую, среднюю и долгую память

from core.memory.short_memory import ShortMemory
from core.memory.medium_memory import MediumMemory
from core.memory.long_memory import LongMemory


class MemoryMode:
    """
    Режим 2: С трёхслойной памятью.
    
    Перед отправкой в LLM добавляет контекст из трёх слоёв памяти:
    - Короткая: последние 5-10 сообщений диалога
    - Средняя: важные факты текущей сессии
    - Долгая: профиль пользователя
    """
    
    def __init__(self, llm):
        """
        Инициализация режима с памятью.
        
        Параметры:
            llm: Объект LLM (внешний или локальный)
        """
        self.llm = llm
        self.short = ShortMemory()
        self.medium = MediumMemory()
        self.long = LongMemory()
    
    def process(self, user_message, is_regeneration=False):
        """
        Обработать сообщение с использованием памяти.
        
        Параметры:
            user_message: Текст сообщения от пользователя
            is_regeneration: Регенерация или новое сообщение
        
        Возвращает:
            Ответ от LLM с учётом контекста
        """
        # 1. Собираем контекст из всех слоёв памяти
        context = self._build_context()
        
        # 2. Формируем полный промт с контекстом
        full_prompt = f"{context}\n\nПользователь: {user_message}"
        
        # 3. Отправляем в LLM
        response = self.llm.generate(full_prompt)
        
        # 4. Сохраняем в короткую память (только если не регенерация)
        if not is_regeneration:
            self.short.add(user_message, response)
        
        return response
    
    def _build_context(self):
        """
        Собрать контекст из всех слоёв памяти.
        
        Возвращает:
            Текст с контекстом для LLM
        """
        context_parts = []
        
        # Долгая память: профиль пользователя
        profile = self.long.get_profile()
        if profile:
            context_parts.append(f"=== ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ===\n{profile}")
        
        # Средняя память: тема сессии
        session = self.medium.get_session()
        if session:
            context_parts.append(f"=== ТЕКУЩАЯ СЕССИЯ ===\n{session}")
        
        # Короткая память: история диалога
        history = self.short.get_history()
        if history:
            context_parts.append(f"=== ИСТОРИЯ ДИАЛОГА ===\n{history}")
        
        return "\n\n".join(context_parts) if context_parts else ""
