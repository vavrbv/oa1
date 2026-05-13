from __future__ import annotations 
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class DynArray(ABC, Generic[T]):
    DEFAULT_SIZE = 16

    APPEND_NIL = 0  # Операции над массивом ещё не выполнялись
    APPEND_OK = 1   # Последнее добавление в конец массива было успешно выполнено
    APPEND_ERR = 2  # Массив заполнен до максимального значения, невозможно выделить дополнительную память

    INSERT_NIL = 0  # Операции над массивом ещё не выполнялись
    INSERT_OK = 1   # Последнее добавление по индексу было успешно выполнено
    INSERT_ERR = 2  # Массив заполнен до максимального значения, невозможно выделить дополнительную память

    REMOVE_NIL = 0  # Операции над массивом ещё не выполнялись
    REMOVE_OK = 1   # Последнее удаление элемента по индексу было успешно выполнено
    REMOVE_ERR = 2  # Индекс отсутствует в массиве

    GET_NIL = 0     # Операции над массивом ещё не выполнялись
    GET_OK = 1      # Последний запрос на получение элемента по индексу был выполнен успешно
    GET_ERR = 2     # Индекс отсутствует в массиве

    # Конструктор
    @abstractmethod
    def __init__(self, size: int = 16) -> None:
        """Постусловие: создан динамический массив размера 0."""
        ...

    # Команды
    @abstractmethod
    def append(self, value: T) -> None:
        """Постусловие: элемент с заданным значением добавлен в конец массива."""
        ...

    @abstractmethod
    def insert(self, value: T, index: int) -> None:
        """Постусловие: элемент с заданным значением добавлен по указанному индексу,
        если индекса нет в массиве, то элемент добавлен в конец массива."""
        ...

    @abstractmethod
    def remove(self, index: int) -> None:
        """Предусловие: элемент с указанным индексом есть в массиве.
        Постусловие: элемент с заданным индексом удалён из массива."""
        ...

    @abstractmethod
    def clear(self) -> None:
        """Постусловие: массив пуст."""
        ...

    # Запросы
    @abstractmethod
    def get(self, index: int) -> T | None:
        """Предусловие: элемент с указанным индексом есть в массиве."""
        ...

    @abstractmethod
    def size(self) -> int:
        ...

    # Дополнительные запросы
    @abstractmethod
    def get_append_status(self) -> int:
        ...

    @abstractmethod
    def get_insert_status(self) -> int:
        ...

    @abstractmethod
    def get_remove_status(self) -> int:
        ...

    @abstractmethod
    def get_get_status(self) -> int:
        ...


class TupleDynArray(DynArray, Generic[T]):
    _data: tuple[T, ...]
    _max_size: int
    _size: int

    # Конструктор
    def __init__(self, size: int = 16) -> None:
        self.clear()

    # Команды
    def append(self, value: T) -> None:
        if self._size == self._max_size:
            # Реаллокация массива по мультипликативной схеме
            self._max_size = (self._max_size * 3) // 2 + 1

        self._data = (*self._data, value)
        self._size += 1
        self._append_status = self.APPEND_OK

    def insert(self, value: T, index: int) -> None:
        if self._size == self._max_size:
            # Реаллокация массива по мультипликативной схеме
            self._max_size = (self._max_size * 3) // 2 + 1

        self._data = (*self._data[:index], value, *self._data[index:])
        self._size += 1
        self._insert_status = self.INSERT_OK

    def remove(self, index: int) -> None:
        if index < self._size:
            self._data = (*self._data[:index], *self._data[index + 1:])
            self._size -= 1
            if self._size < self._max_size // 2:
                self._max_size = max(int(self._max_size / 1.5), self.DEFAULT_SIZE)
            self._remove_status = self.REMOVE_OK
        else:
            self._remove_status = self.REMOVE_ERR

    def clear(self) -> None:
        self._data = tuple()
        self._max_size = self.DEFAULT_SIZE
        self._size = 0

        self._append_status = self.APPEND_NIL
        self._insert_status = self.INSERT_NIL
        self._remove_status = self.REMOVE_NIL
        self._get_status = self.GET_NIL

    # Запросы
    def get(self, index: int) -> T | None:
        if index < self._size:
            self._get_status = self.GET_OK
            return self._data[index]
        else:
            self._get_status = self.GET_ERR
            return None

    def size(self) -> int:
        return self._size

    # Дополнительный запросы
    def get_append_status(self) -> int:
        return self._append_status

    def get_insert_status(self) -> int:
        return self._insert_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def get_get_status(self) -> int:
        return self._get_status
