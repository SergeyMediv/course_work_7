import datetime

from celery import shared_task

from habits.models import Habits
from habits.services import create_message, send_message


@shared_task
def send_message_tg():
    current_time = datetime.datetime.now().strftime("%X")
    habits = Habits.objects.all()

    for habit in habits:
        if habit.start_time == current_time:
            tg_chat_id = habit.owner.tg_chat_id
            if tg_chat_id:
                count = habit.periodicity
                if count != 0:
                    text_message = create_message(habit.pk)
                    send_message(tg_chat_id=tg_chat_id, message=text_message)
                    count -= 1
                    habit.save()
