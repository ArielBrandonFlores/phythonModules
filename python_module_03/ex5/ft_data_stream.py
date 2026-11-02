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
    """Endlessly generate random events as (player, action) tuples."""
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        # O 'yield' transforma a função em um gerador que pausa a execução
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    """Randomly consume and yield events until the list is empty."""
    while len(events) > 0:
        index: int = random.randrange(len(events))
        # pop() remove e retorna o elemento, modificando a lista original
        event: tuple[str, str] = events.pop(index)
        yield event


def main() -> None:
    """Stream processing workflow demonstrating generators."""
    print("=== Game Data Stream Processor ===")
    
    # Inicializa o gerador infinito
    event_stream: typing.Generator[tuple[str, str], None, None] = gen_event()

    # Consome os primeiros 1000 eventos usando next()
    for index in range(1000):
        player, action = next(event_stream)
        print(f"Event {index}: Player {player} did action {action}")

    # Constrói a lista de 10 elementos usando loop clássico (sem list comprehensions)
    events_list: list[tuple[str, str]] = []
    for _ in range(10):
        events_list.append(next(event_stream))
        
    print(f"Built list of 10 events: {events_list}")

    # O gerador consume_event é usado diretamente na estrutura for...in
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()