from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class Nothing:
    ...

class AbstractBoundedStack(ABC, Generic[T]):
    """Абстрактный класс, соответствующий АТД BoundedStack."""

    @abstractmethod
    def __init__(self, max_size: int) -> None:
        """Постусловие: создан новый пустой стек."""
        ...

    # Команды
    @abstractmethod
    def push(self, value: T) -> None:
        """Постусловие: в стек добавлено новое значение."""
        ...

    @abstractmethod
    def pop(self) -> None:
        """Предусловие: стек не пустой.
        Постусловие: из стека удалён верхний элемент.
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """Постусловие: из стека удаляются все значения."""
        ...

    # Запросы
    @abstractmethod
    def peek(self) -> T | Nothing:
        """Предусловие: стек не пустой."""
        ...

    @abstractmethod
    def size(self) -> int:
        ...

    # Дополнительные запросы
    @abstractmethod
    def get_pop_status(self) -> int:
        ...

    @abstractmethod
    def get_peek_status(self) -> int:
        ...

    @abstractmethod
    def get_push_status(self) -> int:
        ...


class BoundedStack(AbstractBoundedStack, Generic[T]):
    """Класс, реализующий АТД BoundedStack."""

    # Статусы команд
    POP_NIL: int = 0   # Команда push() ещё не вызывалась
    POP_OK: int = 1    # Последняя команда pop() отработала нормально
    POP_ERR: int = 2   # Стек пуст

    PUSH_NIL: int = 0  # Команда push() ещё не вызывалась
    PUSH_OK: int = 1   # Последняя команда push() отработала нормально
    PUSH_ERR: int = 2  # Стек переполнен

    # Статусы запросов
    PEEK_NIL: int = 0  # Команда push() ещё не вызывалась
    PEEK_OK: int = 1   # Последняя команда peek() вернула корректное значение
    PEEK_ERR: int = 2  # Стек пуст

    # Скрытые поля
    _stack: list[T]    # Основное хранилище стека
    _pop_status: int   # Статус последней команды pop()
    _peek_status: int  # Статус последней команды peek()
    _push_status: int  # Статус последней команды push()

    def __init__(self, max_size: int = 32) -> None:
        """Постусловие: создан новый пустой стек."""
        self._max_size = max(1, max_size)
        self.clear()

    # Команды
    def push(self, value: T) -> None:
        """Постусловие: в стек добавлено новое значение."""
        if self.size() < self._max_size:
            self._stack.append(value)
            self._push_status = BoundedStack.PUSH_OK
        else:
            self._push_status = BoundedStack.PUSH_ERR

    def pop(self) -> None:
        """Предусловие: стек не пустой.
        Постусловие: из стека удалён верхний элемент.
        """
        if self.size() > 0:
            self._stack.pop()
            self._pop_status = BoundedStack.POP_OK
        else:
            self._pop_status = BoundedStack.POP_ERR

    def clear(self) -> None:
        """Постусловие: из стека удаляются все значения."""
        self._stack = []  # Пустой стек
        # Начальные статусы команд pop(), peek(), push()
        self._pop_status = BoundedStack.POP_NIL
        self._peek_status = BoundedStack.PEEK_NIL
        self._push_status = BoundedStack.PUSH_NIL

    # Запросы
    def peek(self) -> T | Nothing:
        """Предусловие: стек не пустой."""
        if self.size() > 0:
            result: T | Nothing = self._stack[-1]
            self._peek_status = BoundedStack.PEEK_OK
        else:
            result = Nothing()
            self._peek_status = BoundedStack.PEEK_ERR

        return result

    def size(self) -> int:
        return len(self._stack)

    # Дополнительные запросы
    def get_peek_status(self) -> int:
        return self._peek_status

    def get_pop_status(self) -> int:
        return self._pop_status

    def get_push_status(self) -> int:
        return self._push_status
