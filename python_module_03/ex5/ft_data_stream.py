#!/usr/bin/env python3
import random
import typing


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index: int = random.randrange(len(events))
        event: tuple[str, str] = events.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_stream: typing.Generator[tuple[str, str], None, None] = gen_event()

    for index in range(1000):
        player, action = next(event_stream)
        print(f"Event {index}: Player {player} did action {action}")

    events_list: list[tuple[str, str]] = []
    for _ in range(10):
        events_list.append(next(event_stream))

    print(f"Built list of 10 events: {events_list}")
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
