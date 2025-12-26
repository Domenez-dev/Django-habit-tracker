from rest_framework import viewsets, permissions
from .models import Goal
from .serializers import GoalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.habits.models import Task, Journal


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnalyticsView(APIView):
    def get(self, request):
        user = request.user
        
        # Calculate simple stats
        total_tasks = Task.objects.filter(user=user).count()
        done_tasks = Task.objects.filter(user=user, is_done=True).count()
        
        active_goals = Goal.objects.filter(user=user, is_completed=False).count()
        journal_count = Journal.objects.filter(user=user).count()

        # Calculate completion rate
        rate = (done_tasks / total_tasks * 100) if total_tasks > 0 else 0

        return Response({
            "username": user.username,
            "stats": {
                "task_completion_rate": f"{round(rate, 2)}%",
                "total_tasks_created": total_tasks,
                "pending_goals": active_goals,
                "total_journal_entries": journal_count
            }
        })
