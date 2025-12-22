from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'target_date', 'is_completed']
        # The 'user' is handled by the view, so we don't need to send it in the JSON
