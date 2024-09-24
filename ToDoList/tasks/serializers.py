from rest_framework import serializers
from tasks.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tasks
        fields = '__all__'
