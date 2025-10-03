from loguru import logger
import time
import os

def create_log():

    t = time.localtime()
    current_time = time.strftime("%H-%M-%S", t)
    current_day = time.strftime("%d-%m-%Y", t)

    log_path= "logs"
    if not os.path.exists(log_path): os.makedirs(log_path)
    day_path = f'logs/{current_day}'
    if not os.path.exists(day_path): os.mkdir(day_path)
    
    logger.add(f'{day_path}/{current_day} {current_time}.log')