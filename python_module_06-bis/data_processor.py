from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.total: int = 0
        self._data: list[tuple[int, str]] = []

    @property
    def remaining(self) -> int:
        return len(self._data)

    def _store(self, value: str) -> None:
        self._data.append((self.total, value))
        self.total += 1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError(f"No data left on {self.name}")
        return self._data.pop(0)


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_log(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and all(isinstance(k, str) and isinstance(v, str)
                for k, v in value.items())
        and "log_level" in value
        and "log_message" in value
    )


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(is_number(item) for item in data)
        return is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(is_log(item) for item in data)
        return is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(f"{item['log_level']}: {item['log_message']}")


def extract(proc: DataProcessor, count: int, label: str) -> None:
    word = "value" if count == 1 else "values"
    print(f"Extracting {count} {word}...")
    for _ in range(count):
        rank, value = proc.output()
        print(f"{label} {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # mypy warning on purpose (wrong type)
    except ValueError as error:
        print(f"Got exception: {error}")
    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    numeric.ingest(numbers)
    extract(numeric, 3, "Numeric value")

    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input 'Hello': {text.validate('Hello')}")
    print(f"Trying to validate input '42': {text.validate(42)}")
    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)
    extract(text, 1, "Text value")

    print("Testing Log Processor...")
    log = LogProcessor()
    entry = {"log_level": "INFO", "log_message": "Valid entry"}
    print(f"Trying to validate input '{entry}': {log.validate(entry)}")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    extract(log, 2, "Log entry")


if __name__ == "__main__":
    main()
