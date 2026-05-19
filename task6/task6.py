from typing import Generic, TypeVar

T = TypeVar("T")


class ParentQueue(Generic[T]):
    REMOVE_FRONT_NIL = 0  # В очередь ещё не добавлялись элементы
    REMOVE_FRONT_OK = 1   # Последнее удаление элемента из начала очереди успешно выполнено
    REMOVE_FRONT_ERR = 2  # Очередь пуста

    PEEK_FRONT_NIL = 0     # В очередь ещё не добавлялись элементы
    PEEK_FRONT_OK = 1      # Элемент из начала очереди успешно получен
    PEEK_FRONT_ERR = 2     # Очередь пуста

    _values: list[T]
    _size: int

    _enqueue_status: int
    _dequeue_status: int
    _peek_status: int

    # Конструктор
    def __init__(self) -> None:
        """Постусловие: создана пустая очередь."""
        self.clear()

    # Команды
    def add_tail(self, value: T) -> None:
        """Постусловие: заданный элемент добавлен в конец очереди."""
        self._values.append(value)
        self._size += 1

    def remove_front(self) -> None:
        """Предусловие: очередь не пуста.
        Постусловие: удалён первый элемент в очереди."""
        if self._size > 0:
            self._values.pop(0)
            self._size -= 1
            self._remove_front_status = self.REMOVE_FRONT_OK
        else:
            self._remove_front_status = self.REMOVE_FRONT_ERR

    def clear(self) -> None:
        """Постусловие: очередь пуста."""
        self._values = []
        self._size = 0
        self._remove_front_status = self.REMOVE_FRONT_NIL
        self._peek_front_status = self.PEEK_FRONT_NIL

    # Запросы
    def size(self) -> int:
        return self._size

    def peek_front(self) -> T | None:
        """Предусловие: очередь не пуста."""
        if self._size > 0:
            self._peek_status = self.PEEK_FRONT_OK
            return self._values[0]

        self._peek_status = self.PEEK_FRONT_ERR
        return None

    # Дополнительные запросы
    def get_remove_front_status(self) -> int:
        return self._remove_front_status

    def get_peek_front_status(self) -> int:
        return self._peek_front_status


class Queue(ParentQueue, Generic[T]): ...


class Deque(ParentQueue, Generic[T]):
    REMOVE_TAIL_NIL = 0
    REMOVE_TAIL_OK = 1
    REMOVE_TAIL_ERR = 2

    PEEK_TAIL_NIL = 0
    PEEK_TAIL_OK = 1
    PEEK_TAIL_ERR = 2

    # Команды
    def remove_tail(self) -> None:
        """Предусловие: дек не пуст.
        Постусловие: удалён элемент из хвоста."""
        if self._size > 0:
            self._values.pop(-1)
            self._size -= 1
            self._remove_tail_status = self.REMOVE_TAIL_OK
        else:
            self._remove_tail_status = self.REMOVE_TAIL_ERR

    def add_front(self, value: T) -> None:
        """Постусловие: заданный элемент добавлен в начало дека."""
        self._values.insert(0, value)
        self._size += 1

    def clear(self) -> None:
        """Постусловие: дек пуст."""
        super().clear()
        self._remove_tail_status = self.REMOVE_TAIL_NIL
        self._peek_tail_status = self.PEEK_TAIL_NIL

    # Запросы
    def peek_tail(self) -> T | None:
        """Предусловие: дек не пуст."""
        if self._size > 0:
            self._peek_tail_status = self.PEEK_TAIL_OK
            return self._values[-1]

        self._remove_front_status = self.PEEK_TAIL_ERR
        return None

    # Дополнительный запросы
    def get_remove_tail_status(self) -> int:
        return self._remove_tail_status

    def get_peek_tail_status(self) -> int:
        return self._peek_tail_status
