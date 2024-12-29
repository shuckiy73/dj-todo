from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User  # Если используется модель User

class TodoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()  # Вычисляемое поле
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Поле для пользователя (если нужно)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'status', 'user')  # Все поля
        read_only_fields = ('id', 'status')  # Поля только для чтения
        extra_kwargs = {
            'description': {'required': False},  # Поле description необязательное
        }

    # Валидация заголовка
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Заголовок не может быть пустым.")
        return value

    # Логика для вычисляемого поля status
    def get_status(self, obj):
        return "Выполнено" if obj.completed else "Не выполнено"

    # Логика создания объекта
    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    # Логика обновления объекта
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance