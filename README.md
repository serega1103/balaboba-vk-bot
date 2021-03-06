<h1 align="center">Balaboba VK Bot</h1>

## О боте
Бот позволяет генерировать нейротексты Балабобы от Яндекса в беседах ВКонтакте.

## Технические требования
На вашем компьютере должен быть установлен Python 3+. Если вы этого не сделали - вот [ссылка](https://www.python.org/downloads/)

Должны быть установлены следующие пакеты Python
* [vk_api](https://github.com/python273/vk_api)

## Руководство по использованию
**1. Создайте токен сообщества с правами доступа к управлению и сообщениям сообщества.**

Управление -> Настройки -> Работа с API -> Ключи доступа.
Выберите следующие права для нового ключа доступа:
+ Разрешить приложению доступ к управлению сообществом
+ Разрешить приложению доступ к сообщениям сообщества

В конфиге config.py введите созданный токен вашего сообщества.

**2. Включите Long Poll API и выберите последнюю версию.**

Управление -> Настройки -> Работа с API -> Long Poll API -> Настройки:
+ Long Poll API: Включено
+ Версия API: 5.131

**3. Выберите все типы событий, связанных с сообщениями, для Long Poll API.**

Управление -> Настройки -> Работа с API -> Long Poll API -> Типы событий -> Сообщения:
+ Входящее сообщение
+ Исходящее сообщение
+ Редактирование сообщения
+ Действие с сообщением
+ Разрешение на получение
+ Запрет на получение
+ Статус набора текста

**4. Запустите main.py (расширение должно быть асоциированно с Python), открыв терминал, переместившись через cd в каталог этого репозитория и введя:**
```
python main.py
```

# Команды бота
+ Балабоба, команды — узнать список команд
+ Балабоба, как дела — узнать работоспособность
+ Балабоба, (любой текст) — набалабобить нейротекст без стиля
+ Балабоба (стиль), (любой текст) — набалабобить нейротекст в указанном стиле

**Стили:**
+ 0 — Без стиля
+ 1 — Теории заговора
+ 2 — ТВ-репортажи
+ 3 — Тосты
+ 4 — Пацанские цитаты
+ 5 — Рекламные слоганы
+ 6 — Короткие истории
+ 7 — Подписи в Instagram
+ 8 — Википедия
+ 9 — Синопсисы фильмов
+ 10 — Гороскоп
+ 11 — Народные мудрости
+ 12 — Произведения современного искусства

## Разработчик
+ [**Сергей Калдыркаев**](https://github.com/serega1103)
