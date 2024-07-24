from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):

    GOOD_CHOICES = (
        (True, 'Приятная'),
        (False, 'Нет'),
    )

    PERIODICITY_CHOICES = (
        (True, 'Ежедневная'),
        (False, 'Еженедельная')
    )

    PUBLIC_CHOICES = (
        (True, 'Публичная'),
        (False, 'Нет'),
    )

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='Место')
    start_time = models.TimeField(max_length=25, verbose_name='Время начала выполнения')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_good = models.BooleanField(default=True, verbose_name='Приятная привычка', choices=GOOD_CHOICES)
    bond_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связана', **NULLABLE)
    periodicity = models.BooleanField(default=True, verbose_name='Ежедневная', choices=PERIODICITY_CHOICES)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.SmallIntegerField(verbose_name='Время выполнения в минутах')
    public = models.BooleanField(default=True, verbose_name='Публичная', choices=PUBLIC_CHOICES)

    def __str__(self):
        return f'Я буду {self.action} в {self.start_time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['id']


