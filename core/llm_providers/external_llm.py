# Внешний провайдер LLM (через API)
# Работает с OpenAI, Anthropic и другими сервисами

import openai


class ExternalLLM:
    """
    Класс для работы с внешними LLM через API.
    Поддерживает OpenAI (GPT-3.5, GPT-4) и совместимые API.
    """
    
    def __init__(self, api_key, model="gpt-3.5-turbo", base_url=None):
        """
        Инициализация внешней LLM.
        
        Параметры:
            api_key: Ключ API от OpenAI или другого сервиса
            model: Название модели (по умолчанию gpt-3.5-turbo)
            base_url: Базовый URL API (для совместимых сервисов)
        """
        self.api_key = api_key
        self.model = model
        
        if not api_key:
            raise ValueError("❌ API ключ не указан!")
        
        openai.api_key = api_key
        if base_url:
            openai.api_base = base_url
        
        print(f"✅ Внешняя LLM инициализирована: {model}")
    
    def generate(self, prompt, max_tokens=500, temperature=0.7):
        """
        Генерация ответа через внешний API.
        
        Параметры:
            prompt: Текст запроса к LLM
            max_tokens: Максимальная длина ответа
            temperature: Креативность ответа (0.0 - 1.0)
        
        Возвращает:
            Текст ответа от LLM
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except openai.error.AuthenticationError:
            return "❌ Ошибка: неверный API ключ"
        except openai.error.RateLimitError:
            return "❌ Превышен лимит запросов к API"
        except Exception as e:
            return f"❌ Ошибка при обращении к LLM: {e}"
