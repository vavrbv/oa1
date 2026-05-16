from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(ABC, Generic[T]):
    ENQUEUE_NIL = 0  # В очередь ещё не добавлялись элементы
    ENQUEUE_OK = 1   # Последнее добавление элемента в очередь было успешно
    ENQUEUE_ERR = 2  # Элемент не был добавлен в очередь

    DEQUEUE_NIL = 0  # В очередь ещё не добавлялись элементы
    DEQUEUE_OK = 1   # Последнее удаление элемента из начала очереди успешно выполнено
    DEQUEUE_ERR = 2  # Очередь пуста

    PEEK_NIL = 0     # В очередь ещё не добавлялись элементы
    PEEK_OK = 1      # Элемент из начала очереди успешно получен
    PEEK_ERR = 2     # Очередь пуста

    # Конструктор
    @abstractmethod
    def __init__(self) -> None:
        """Постусловие: создана пустая очередь."""

    # Команды
    @abstractmethod
    def enqueue(self, value: T) -> None:
        """Постусловие: заданный элемент добавлен в конец очереди."""

    @abstractmethod
    def dequeue(self) -> None:
        """Предусловие: очередь не пуста.
        Постусловие: удалён первый элемент в очереди."""

    @abstractmethod
    def clear(self) -> None:
        """Постусловие: очередь пуста."""

    # Запросы
    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def peek(self) -> T | None:
        """Предусловие: очередь не пуста."""

    # Дополнительные запросы
    @abstractmethod
    def get_enqueue_status(self) -> int: ...

    @abstractmethod
    def get_dequeue_status(self) -> int: ...

    @abstractmethod
    def get_peek_status(self) -> int: ...


class ListQueue(Queue, Generic[T]):
    _values: list[T]
    _size: int

    _enqueue_status: int
    _dequeue_status: int
    _peek_status: int

    # Конструктор
    def __init__(self) -> None:
        self.clear()

    # Команды
    def enqueue(self, value: T) -> None:
        self._values.append(value)
        self._size += 1
        self._enqueue_status = self.ENQUEUE_OK

    def dequeue(self) -> None:
        if self._size > 0:
            self._values.pop(0)
            self._size -= 1
            self._dequeue_status = self.DEQUEUE_OK
        else:
            self._dequeue_status = self.DEQUEUE_ERR

    def clear(self) -> None:
        self._values = []
        self._size = 0
        self._enqueue_status = self.ENQUEUE_NIL
        self._dequeue_status = self.DEQUEUE_NIL
        self._peek_status = self.PEEK_NIL

    # Запросы
    def size(self) -> int:
        return self._size

    def peek(self) -> T | None:
        if self._size > 0:
            self._peek_status = self.PEEK_OK
            return self._values[0]
        else:
            self._peek_status = self.PEEK_ERR
            return None

    # Дополнительные запросы
    def get_enqueue_status(self) -> int:
        return self._enqueue_status

    def get_dequeue_status(self) -> int:
        return self._dequeue_status

    def get_peek_status(self) -> int:
        return self._peek_status
