from loguru import logger
import time
import os

def create_log():

    t = time.localtime()
    current_day = time.strftime("%d-%m-%Y", t)
    current_month = time.strftime("%m-%Y", t)

    day_path = f'logs/{current_month}'
    if not os.path.exists(day_path): os.mkdir(day_path)

    logger.add(f'{day_path}/{current_month} {current_day}.txt')