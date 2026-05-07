from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class LinkedList(ABC, Generic[T]):
    PUT_NIL = 0         # В список ещё не добавлялись узлы
    PUT_OK =  1         # Последняя команда put_right(), put_left(), add_to_empty() или add_tail() была успешна
    PUT_ERR = 2         # Список пустой

    GET_NIL = 0         # В список ещё не добавлялись узлы
    GET_OK =  1         # Последний запрос get() был успешен
    GET_ERR = 2         # Список пустой

    FIND_NIL = 0        # В список ещё не добавлялись узлы
    FIND_OK =  1        # Последний запрос find() был успешен
    FIND_ERR = 2        # Список пустой

    REMOVE_NIL = 0      # В список ещё не добавлялись узлы
    REMOVE_OK =  1      # Последняя команда remove() была успешна
    REMOVE_ERR = 2      # Список пустой

    REPLACE_NIL = 0     # В список ещё не добавлялись узлы
    REPLACE_OK =  1     # Последняя команда replace() была успешна
    REPLACE_ERR = 2     # Список пустой

    CURSOR_SET_NIL = 0  # В список ещё не добавлялись узлы
    CURSOR_SET_OK =  1  # Последняя команда head(), tail(), right() была успешна
    CURSOR_SET_ERR = 2  # Список пустой

    # Команды
    @abstractmethod
    def head(self) -> None:
        """Предусловие: список не пустой.
        Постусловие: курсор установлен на первый узел списка."""

    @abstractmethod
    def tail(self) -> None:
        """Предусловие: список не пустой.
        Постусловие: курсор установлен на последний узел списка."""

    @abstractmethod
    def right(self) -> None:
        """Предусловие: список не пустой и текущий узел не последний.
        Постусловие: курсор установлен на следующий за текущим узел,
                     если он не последний, иначе курсор не меняет своего положения."""

    @abstractmethod
    def put_right(self, value: T) -> None:
        """Предусловие: список не пустой.
        Постусловие: новый узел добавлен в список справа от текущего."""

    @abstractmethod
    def put_left(self, value: T) -> None:
        """Предусловие: список не пустой.
        Постусловие: новый узел добавлен в список слева от текущего."""

    @abstractmethod
    def remove(self) -> None:
        """Предусловие: список не пустой.
        Постусловие: текущий узел удалён, курсор смещается к правому соседу, если он есть,
                     в противном случае курсор смещается к левому соседу, если он есть."""

    @abstractmethod
    def clear(self) -> None:
        """Постусловие: из списка удалены все элементы."""

    @abstractmethod
    def add_to_empty(self, value: T) -> None:
        """Предусловие: список пустой.
        Постусловие: в список добавлен единственный узел."""

    @abstractmethod
    def add_tail(self, value: T) -> None:
        """Предусловие: список не пустой.
        Постусловие: узел добавлен в хвост списка."""

    @abstractmethod
    def replace(self, value: T) -> None:
        """Предусловие: список не пустой.
        Постусловие: значение текущего узла заменено на заданное."""

    @abstractmethod
    def find(self, value: T) -> None:
        """Предусловие: список не пустой.
        Постусловие: курсор установлен на следующий от текущего узел с заданным значением,
                     если узла с заданным значением справа от текущего узла нет, то курсор
                     не меняет свою позицию."""

    @abstractmethod
    def remove_all(self, value: T) -> None:
        """Постусловие: из списка удалены все узлы с заданным значением."""

    # Запросы
    @abstractmethod
    def get(self) -> T:
        """Предусловие: список не пуст."""

    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def is_head(self) -> bool: ...

    @abstractmethod
    def is_tail(self) -> bool: ...

    @abstractmethod
    def is_value(self) -> bool: ...

    # Дополнительные запросы
    @abstractmethod
    def get_put_status(self) -> int:
        """Возвращает значения PUT_*"""

    @abstractmethod
    def get_get_status(self) -> int:
        """Возвращает значения GET_*"""

    @abstractmethod
    def get_find_status(self) -> int:
        """Возвращает значения FIND_*"""

    @abstractmethod
    def get_remove_status(self) -> int:
        """Возвращает значения REMOVE_*"""

    @abstractmethod
    def get_replace_status(self) -> int:
        """Возвращает значения REPLACE_*"""

    @abstractmethod
    def get_cursor_set_status(self) -> int:
        """Возвращает значения CURSOR_SET_*"""


# 2.2 Операция tail() не сводима к другим операциями, так как её асимптотическая сложность была бы O(N):
# необходимо последовательно выполнять операции get(), is_tail(), right() пока is_tail() не вернёт логическую единицу.

# 2.3 Операция поиска всех узлов с заданным значением не нужна, так как она сводится к выполнению операции head()
# и последовательности операций find() пока get_find_status() возвращает значение FIND_OK.
