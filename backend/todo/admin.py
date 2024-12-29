from django.contrib import admin
from .models import Todo

# Пользовательское действие для отметки задач как выполненных
def mark_completed(modeladmin, request, queryset):
    queryset.update(completed=True)
mark_completed.short_description = "Отметить выбранные задачи как выполненные"

# Класс для настройки административной панели
class TodoAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('title', 'description', 'completed', 'created_at')
    
    # Фильтры
    list_filter = ('completed', 'created_at')
    
    # Поля для поиска
    search_fields = ('title', 'description')
    
    # Поля, которые можно редактировать прямо в списке
    list_editable = ('completed',)
    
    # Сортировка по умолчанию
    ordering = ('-created_at',)
    
    # Иерархия по дате
    date_hierarchy = 'created_at'
    
    # Пользовательские действия
    actions = [mark_completed]
    
    # Настройка формы редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Статус', {
            'fields': ('completed',)
        }),
    )

# Регистрация модели Todo с использованием TodoAdmin
admin.site.register(Todo, TodoAdmin)