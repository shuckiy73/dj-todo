from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title