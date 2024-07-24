from django.urls import path


from habits.apps import HabitsConfig
from habits.views import HabitsListAPIView, HabitsCreateAPIView, HabitsUpdateAPIView, HabitsRetrieveAPIView, \
    HabitsDestroyAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitsListAPIView.as_view(), name='habits_list'),
    path('<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits_retrieve'),
    path('create/', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('<int:pk>/update/', HabitsUpdateAPIView.as_view(), name='habits_update'),
    path('<int:pk>/delete/', HabitsDestroyAPIView.as_view(), name='habits_delete'),
]
