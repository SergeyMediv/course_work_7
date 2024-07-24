from rest_framework.serializers import ValidationError


class FrequencyValidator:

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        number_list = [1, 2, 3, 4, 5, 6, 7]
        num = habit.get('periodicity')
        if num not in number_list:
            raise ValidationError('Необходимо выполнять от 1 до 7 раз в неделю')


class CrossValidator:

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, habit):
        if habit.get('is_good'):
            if habit.get('bond_habit') or habit.get('reward'):
                raise ValidationError(
                    'У приятной привычки не может быть связанной привычки или вознаграждения'
                )


class IsGoodValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get('bond_habit'):
            if not habit.get('is_good'):
                raise ValidationError('Связанные привычки могут быть только приятными')


class TimeValidator:
    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        if habit.get('duration') > 120:
            raise ValidationError('Время выполнения не может быть больше 120 секунд')


class IsGoodRewardValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, habit):
        if habit.get('reward') and habit.get('bond_habit'):
            raise ValidationError('Не может быть одновременно приятной привычки и вознаграждения')
