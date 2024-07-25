from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN
from habits.models import Habits
import requests


def get_user_name(email):
    name = ""
    for letter in email:
        if letter != "@":
            name += letter
        else:
            break
    return name


def create_message(habit_id):

    habit = Habits.objects.get(id=habit_id)
    user = habit.owner
    name = get_user_name(user.email)
    time = habit.start_time
    action = habit.action

    if habit.place is None:
        place = "Любое место"
    else:
        place = habit.place

    if habit.bond_habit_id:
        message = (f"Привет {name}! Настало время({time}) выполнить({action}),"
                   f"Место:({place}),"
                   f" если сделаешь, можешь: {Habits.objects.get(id=habit.bond_habit_id).action}!")
    elif habit.reward:
        message = (f"Привет {name}! Настало время({time}) выполнить({action}),"
                   f"Место:({place}), если сделаешь, можешь: {habit.reward}!")
    else:
        message = (f"Привет {name}! Настало время({time}) выполнить({action}),"
                   f"Место:({place}).")

    return message


def send_message(tg_chat_id, message):
    params = {
        "text": message,
        "chat_id": tg_chat_id,
    }
    requests.post(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
