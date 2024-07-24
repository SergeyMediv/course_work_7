from rest_framework.serializers import ValidationError


class FrequencyValidator:

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, habit):
        number_list = [1, 2, 3, 4, 5, 6, 7]
        num = habit.get("periodicity")
        if num not in number_list:
            raise ValidationError('Необходимо выполнять от 1 до 7 раз в неделю')
