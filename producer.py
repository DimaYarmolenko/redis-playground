import array as arr
import random
import redis

from time import time, sleep

from config import RedisConfig
from model import EventType


def generate_input(array_size: int) -> tuple[str, bytes]:
    result_array = arr.array("f", [random.random() for _ in range(array_size)])
    return str(time()), result_array.tobytes()


def run() -> None:
    config = RedisConfig()
    r = redis.Redis(
        host=config.host,
        port=config.port,
        decode_responses=config.decode_responses
    )
    while True:
        key, value = generate_input(10)

        r.hset(EventType.PRODUCER_OUTPUT, key, value)

        print(key, value)

        sleep(1)



if __name__ == "__main__":
    run()
