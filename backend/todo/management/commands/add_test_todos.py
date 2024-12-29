from django.core.management.base import BaseCommand
from todo.models import Todo

class Command(BaseCommand):
    help = 'Добавляет тестовые задачи на тему программирования в базу данных'

    def handle(self, *args, **kwargs):
        # Список тестовых задач на тему программирования
        test_todos = [
            {
                "title": "Изучить Django",
                "description": "Пройти официальный туториал по Django и создать первый проект.",
                "completed": False
            },
            {
                "title": "Написать тесты для приложения",
                "description": "Добавить unit-тесты для всех моделей и представлений.",
                "completed": False
            },
            {
                "title": "Оптимизировать SQL-запросы",
                "description": "Проанализировать и оптимизировать медленные SQL-запросы в проекте.",
                "completed": False
            },
            {
                "title": "Изучить React",
                "description": "Пройти курс по React и создать простое SPA.",
                "completed": True
            },
            {
                "title": "Добавить CI/CD",
                "description": "Настроить непрерывную интеграцию и доставку для проекта.",
                "completed": False
            },
            {
                "title": "Рефакторинг кода",
                "description": "Улучшить читаемость и поддерживаемость кода.",
                "completed": False
            },
            {
                "title": "Изучить Docker",
                "description": "Разобраться с контейнеризацией и создать Docker-образ для проекта.",
                "completed": False
            },
            {
                "title": "Написать документацию",
                "description": "Документировать API и ключевые функции проекта.",
                "completed": False
            },
            {
                "title": "Изучить алгоритмы",
                "description": "Решить 10 задач на LeetCode или HackerRank.",
                "completed": False
            },
            {
                "title": "Создать портфолио",
                "description": "Разработать и выложить портфолио на GitHub Pages.",
                "completed": False
            },
        ]

        # Создание задач
        for todo_data in test_todos:
            Todo.objects.create(**todo_data)

        self.stdout.write(self.style.SUCCESS('Тестовые задачи на тему программирования успешно добавлены!'))