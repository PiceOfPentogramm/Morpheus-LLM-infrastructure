# Долгая память
# Хранит профиль пользователя и долгосрочные знания

import json
import os


class LongMemory:
    """
    Долгая память - хранит профиль пользователя.
    
    Это информация, которая не должна забываться:
    - Имя пользователя
    - Интересы и хобби
    - Предпочтения в общении
    - Другие важные детали
    
    Данные сохраняются в JSON файл, чтобы не теряться при перезапуске.
    """
    
    def __init__(self, storage_path="data/profile.json"):
        """
        Инициализация долгой памяти.
        
        Параметры:
            storage_path: Путь к файлу для хранения профиля
        """
        self.storage_path = storage_path
        self.profile = self._load_profile()
    
    def _load_profile(self):
        """Загрузить профиль из файла."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        # Профиль по умолчанию
        return {
            "name": "Неизвестно",
            "interests": [],
            "preferences": {},
            "facts": []
        }
    
    def _save_profile(self):
        """Сохранить профиль в файл."""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.profile, f, ensure_ascii=False, indent=2)
    
    def set_name(self, name):
        """
        Установить имя пользователя.
        
        Параметры:
            name: Имя пользователя
        """
        self.profile["name"] = name
        self._save_profile()
    
    def add_interest(self, interest):
        """
        Добавить интерес пользователя.
        
        Параметры:
            interest: Интерес или хобби
        """
        if interest not in self.profile["interests"]:
            self.profile["interests"].append(interest)
            self._save_profile()
    
    def add_fact(self, fact):
        """
        Добавить факт о пользователе.
        
        Параметры:
            fact: Важный факт для запоминания
        """
        if fact not in self.profile["facts"]:
            self.profile["facts"].append(fact)
            self._save_profile()
    
    def get_profile(self):
        """
        Получить профиль пользователя в текстовом виде.
        
        Возвращает:
            Текст с профилем
        """
        parts = []
        
        parts.append(f"Имя: {self.profile['name']}")
        
        if self.profile["interests"]:
            parts.append(f"Интересы: {', '.join(self.profile['interests'])}")
        
        if self.profile["facts"]:
            parts.append("Важные факты:")
            for fact in self.profile["facts"]:
                parts.append(f"- {fact}")
        
        return "\n".join(parts)
