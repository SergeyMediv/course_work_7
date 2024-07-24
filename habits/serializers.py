from rest_framework import serializers

from habits.models import Habits
from habits.validators import FrequencyValidator, CrossValidator, IsGoodValidator, TimeValidator, IsGoodRewardValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

        validators = [
            FrequencyValidator('periodicity'),
            CrossValidator('is_good', "reward", 'bond_habit'),
            IsGoodValidator('bond_habit', 'is_good'),
            TimeValidator('duration'),
            IsGoodRewardValidator('is_good', 'reward')
        ]
