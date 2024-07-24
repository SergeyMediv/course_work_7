from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginators import CustomPagination
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

