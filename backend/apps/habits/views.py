from rest_framework import viewsets, permissions
from .models import Task, Journal
from .serializers import TaskSerializer, JournalSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This ensures a user ONLY sees their own tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This is the only "manual" part needed: 
        # It links the new task to the user who is currently logged in.
        serializer.save(user=self.request.user)


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
