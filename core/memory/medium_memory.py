# Средняя память
# Хранит важные факты текущей сессии


class MediumMemory:
    """
    Средняя память - хранит важную информацию о текущей сессии.
    
    Например: если пользователь работает над проектом, здесь можно хранить:
    - Название проекта
    - Текущую задачу
    - Важные детали, которые не должны забываться
    
    Эта память живёт дольше, чем короткая, но меньше, чем долгая.
    """
    
    def __init__(self):
        """Инициализация средней памяти."""
        self.session_info = {
            "topic": None,  # Тема сессии
            "context": [],  # Важные факты
        }
    
    def set_topic(self, topic):
        """
        Установить тему текущей сессии.
        
        Параметры:
            topic: Тема сессии (например, "программирование", "бизнес")
        """
        self.session_info["topic"] = topic
    
    def add_context(self, fact):
        """
        Добавить важный факт в контекст сессии.
        
        Параметры:
            fact: Важная информация для запоминания
        """
        if fact not in self.session_info["context"]:
            self.session_info["context"].append(fact)
    
    def get_session(self):
        """
        Получить информацию о текущей сессии.
        
        Возвращает:
            Текст с информацией о сессии
        """
        parts = []
        
        if self.session_info["topic"]:
            parts.append(f"Тема: {self.session_info['topic']}")
        
        if self.session_info["context"]:
            parts.append("Важные факты:")
            for fact in self.session_info["context"]:
                parts.append(f"- {fact}")
        
        return "\n".join(parts) if parts else ""
    
    def clear(self):
        """Очистить память сессии."""
        self.session_info = {
            "topic": None,
            "context": [],
        }
