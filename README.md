# Учёт успеваемости студентов

## Описание

Учебное приложение для учёта успеваемости студентов (СРОП по дисциплине
«Прикладные аспекты DevOps», вариант 11).

Возможности:
- добавление студентов и их оценок по дисциплинам (0–100 баллов);
- расчёт среднего балла студента и группы;
- перевод балла в буквенную оценку (A, B, C, D, F);
- рейтинг лучших студентов;
- список студентов с задолженностями (оценка ниже 50).

## Используемые технологии

- Python 3.12
- pytest — автоматическое тестирование
- build / setuptools — сборка пакета
- Git, GitHub, GitHub Actions — контроль версий и CI/CD

## Структура проекта

```
student-grades/
├── src/student_grades/      # исходный код
│   ├── __init__.py
│   ├── gradebook.py         # основная логика
│   └── main.py              # демонстрация работы
├── tests/
│   └── test_gradebook.py    # тесты pytest
├── .github/workflows/ci.yml # конфигурация CI/CD
├── pyproject.toml           # конфигурация проекта
├── requirements.txt         # зависимости
└── README.md
```

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
# Windows (PowerShell)
$env:PYTHONPATH="src"; python -m student_grades.main

# Linux / macOS
PYTHONPATH=src python -m student_grades.main
```

## Тестирование

```bash
pytest -v
```

## CI/CD

Pipeline настроен в GitHub Actions (`.github/workflows/ci.yml`) и запускается
автоматически при каждом `push` и `pull request`:

```
Push → Build (установка зависимостей + сборка пакета) → Test (pytest) → Result
```

Этап **Test** запускается только после успешного этапа **Build**.
Если сборка или тесты завершаются с ошибкой, pipeline останавливается со статусом Failed.

## Автор: limon4ik212
