import random
import time


def do_smth_random_for_no_reason() -> None:
    num = random.randint(0, 58)
    if num % 2 == 0:
        time.sleep(3)
        return None
    time.sleep(5)
    return None
