from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Task
        fields = ['id', 'name', 'title', 'task_description', 'completed', 'created_at', 'updated_at', 'owner_name']
