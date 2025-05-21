# Project1: Bank Operations

## Описание
Этот проект представляет собой систему для управления банковскими операциями. Он включает в себя функции для фильтрации и сортировки операций по статусу и дате. Проект написан на Python и использует список словарей для хранения данных о банковских транзакциях.

## Структура проекта
Проект состоит из следующих частей:
- Основной код, реализующий функции обработки банковских операций.
- Тесты для проверки функциональности.
- Конфигурационные файлы проекта.

### Основные файлы и папки:
- src/ — Исходный код проекта.
- tests/ — Тесты для проверки корректности работы функций.
- README.md — Документация по проекту.
- .gitignore — Файл для исключения ненужных файлов из Git.

## Установка

Для того чтобы начать работать с проектом, следуйте этим шагам:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/skrimeks1/project1.git
2. Перейдите в папку проекта:

cd project1

3. Установите все необходимые зависимости :

pip install -r requirements.txt


Функции

1. filter_by_state()

Функция фильтрует банковские операции по их статусу (например, ‘EXECUTED’, ‘IN_PROGRESS’).

Аргументы:
 • operations (List[Dict]) — Список операций.
 • state (str) — Статус операций для фильтрации. По умолчанию ‘EXECUTED’.

Возвращаемое значение:
 • Список операций, фильтрованных по статусу.

Пример использования:
from src.processing import filter_by_state

# Пример данных
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2025-01-01"},
    {"id": 2, "state": "IN_PROGRESS", "date": "2025-01-02"},
    {"id": 3, "state": "EXECUTED", "date": "2025-01-03"},
]

# Фильтрация операций по статусу 'EXECUTED'
executed_operations = filter_by_state(operations, 'EXECUTED')
print(executed_operations)


2.sort_by_date()

Функция сортирует операции по дате. По умолчанию сортируются новые операции сначала.

Аргументы:
 • operations (List[Dict]) — Список операций.
 • reverse (bool) — Если True, сортирует от новых к старым. По умолчанию True.

Возвращаемое значение:
 • Список операций, отсортированных по дате.

Пример использования:
from src.processing import sort_by_date

# Пример данных
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2025-01-01"},
    {"id": 2, "state": "IN_PROGRESS", "date": "2025-01-02"},
    {"id": 3, "state": "EXECUTED", "date": "2025-01-03"},
]

# Сортировка операций по дате (новые сначала)
sorted_operations = sort_by_date(operations)
print(sorted_operations)

Пример:

from src.processing import filter_by_state, sort_by_date

# Список операций
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2025-01-01"},
    {"id": 2, "state": "IN_PROGRESS", "date": "2025-01-02"},
    {"id": 3, "state": "EXECUTED", "date": "2025-01-03"},
]

# Фильтрация по состоянию
executed_operations = filter_by_state(operations, "EXECUTED")

# Сортировка по дате
sorted_operations = sort_by_date(operations)

# Печать результатов
print("Executed operations:", executed_operations)
print("Sorted operations:", sorted_operations)

Тестирование

Для тестирования проекта можно использовать библиотеку pytest.
 1. Убедитесь, что установлены все зависимости.
 2. Запустите тесты:

pytest

Для проверки покрытия:
pytest –cov=src –cov-report=html

Результаты покрытие можно посмотреть в папке htmlcov/index.html.

Лицензия

Этот проект лицензирован под лицензией MIT. Для подробностей смотрите файл LICENSE.