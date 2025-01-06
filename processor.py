import sys
import redis
from redis import Redis

from time import sleep

from config import RedisConfig
from model import EventType
from argparse import ArgumentError


def process_event(
    key: bytes,
    value: bytes,
    client: Redis,
    input: EventType,
    output: EventType
) -> None:
    print(key, value)
    pipe = client.pipeline()
    pipe.hset(output, key.decode(), value)
    pipe.hdel(input, key.decode())
    pipe.execute()


def parse_args(args: list[str]) -> tuple[EventType, EventType]:
    try:
        return EventType[args[0]], EventType[args[1]]
    except KeyError as exc:
        raise ArgumentError(argument=None, message=f"{str(exc)} is not a valid choice!")


def run() -> None:
    input, output = parse_args(sys.argv[1:])

    config = RedisConfig()
    r = redis.Redis(
        host=config.host,
        port=config.port,
        decode_responses=config.decode_responses
    )

    while True:
        events = r.hgetall(input)
        for key, value in events.items():
            process_event(key, value, r, input, output)

        sleep(1)

if __name__ == "__main__":
    run()
