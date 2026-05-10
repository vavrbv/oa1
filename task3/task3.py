from typing import TypeVar, Generic

T = TypeVar("T")


class ParentList(Generic[T]):
    HEAD_NIL = 0
    HEAD_OK = 1
    HEAD_ERR = 2

    TAIL_NIL = 0
    TAIL_OK = 1
    TAIL_ERR = 2

    RIGHT_NIL = 0
    RIGHT_OK = 1
    RIGHT_ERR = 2

    PUT_RIGHT_NIL = 0
    PUT_RIGHT_OK = 1
    PUT_RIGHT_ERR = 2

    PUT_LEFT_NIL = 0
    PUT_LEFT_OK = 1
    PUT_LEFT_ERR = 2

    ADD_TO_EMPTY_NIL = 0
    ADD_TO_EMPTY_OK = 1
    ADD_TO_EMPTY_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    REPLACE_NIL = 0
    REPLACE_OK = 1
    REPLACE_ERR = 2

    FIND_NIL = 0
    FIND_OK = 1
    FIND_NOT_FOUND = 2
    FIND_EMPTY = 3

    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2

    _values: list[T]
    _cursor: int
    _size: int

    # Конструктор
    def __init__(self) -> None:
        """Постусловие: создан новый пустой список."""
        self.clear()

    # Команды
    def head(self) -> None:
        """Предусловие: список не пуст.
        Постусловие: курсор установлен на первый узел в списке."""

        if self._size > 0:
            self._cursor = 0
            self._head_status = self.HEAD_OK
        else:
            self._head_status = self.HEAD_ERR

    def tail(self) -> None:
        """Предусловие: список не пуст.
        Постусловие: курсор установлен на последний узел в списке."""
        if self._size > 0:
            self._cursor = self._size - 1
            self._tail_status = self.TAIL_OK
        else:
            self._tail_status = self.TAIL_ERR

    def right(self) -> None:
        """Предусловие: справа от курсора есть узел.
        Постусловие: курсор сдвинут на один узел вправо."""
        if not self.is_tail():
            self._cursor += 1
            self._right_status = self.RIGHT_OK
        else:
            self._right_status = self.RIGHT_ERR

    def put_right(self, value: T) -> None:
        """Предусловие: список не пуст.
        Постусловие: справа от текущего узла добавлен новый узел с заданным значением."""
        if self._size > 0:
            self._values.insert(self._cursor + 1, value)
            self._size += 1
            self._put_right_status = self.PUT_RIGHT_OK
        else:
            self._put_right_status = self.PUT_RIGHT_ERR

    def put_left(self, value: T) -> None:
        """Предусловие: список не пуст; 
        Постусловие: слева от текущего узла добавлен новый узел с заданным значением."""
        if self._size > 0:
            self._values.insert(self._cursor - 1, value)
            self._size += 1
            self._put_left_status = self.PUT_LEFT_OK
        else:
            self._put_left_status = self.PUT_LEFT_ERR

    def add_to_empty(self, value: T) -> None:
        """Предусловие: список пуст.
        Постусловие: в список добавлен единственный узел."""
        if self._size == 0:
            self._values.append(value)
            self._cursor = 0
            self._size += 1
            self._add_to_empty_status = self.ADD_TO_EMPTY_OK
        else:
            self._add_to_empty_status = self.ADD_TO_EMPTY_ERR

    def remove(self) -> None:
        """Предусловие: список не пуст.
        Постусловие: текущий узел удалён, курсор смещён к правому соседу, если он есть, 
                     в противном случае курсор смещён к левому соседу, если он есть."""
        if self._size > 0:
            self._values.pop(self._cursor)
            if self.is_tail():
                self._cursor -= 1
            self._size -= 1
            self._remove_status = self.REMOVE_OK
        else:
            self._remove_status = self.REMOVE_ERR

    def clear(self) -> None:
        """Постусловие: список пуст."""
        self._values = []
        self._cursor = 0
        self._size = 0

        self._head_status = self.HEAD_NIL
        self._tail_status = self.TAIL_NIL
        self._right_status = self.RIGHT_NIL
        self._put_right_status = self.PUT_RIGHT_NIL
        self._put_left_status = self.PUT_LEFT_NIL
        self._add_to_empty_status = self.ADD_TO_EMPTY_NIL
        self._remove_status = self.REMOVE_NIL
        self._replace_status = self.REPLACE_NIL
        self._find_status = self.FIND_NIL
        self._get_status = self.GET_NIL

    def add_tail(self, value: T) -> None:
        """Постусловие: узел с заданным значением добавлен в хвост списка."""
        self._values.append(value)

    def remove_all(self, value: T) -> None:
        """Постусловие: в списке удалены все узлы с заданным значением."""
        last_cursor = self._cursor
        remove_flag = False

        self._cursor = 0
        while self._cursor < self._size:
            if self._values[self._cursor] == value:
                self.remove()
                remove_flag = True
                continue
            break

        if not remove_flag:
            self._cursor = last_cursor

    def replace(self, value: T) -> None:
        """Предусловие: список не пуст.
        Постусловие: значение текущего узла заменено на заданное."""
        if self._size > 0:
            self._values[self._cursor] = value
            self._replace_status = self.REPLACE_OK
        else:
            self._replace_status = self.REPLACE_ERR

    def find(self, value: T) -> None:
        """Предусловие: список не пуст.
        Постусловие: курсор установлен на следующий узел с заданным значением, если такой узел есть."""
        if self._size > 0:
            for i in range(self._cursor + 1, self._size):
                if self._values[i] == value:
                    self._cursor = i
                    break
            else:
                self._find_status = self.FIND_NOT_FOUND

            self._find_status = self.FIND_OK
        else:
            self._find_status = self.FIND_EMPTY

    # Запросы
    def get(self) -> T | None:
        """Предусловие: список не пуст."""
        if self._size > 0:
            self._get_status = self.GET_OK
            return self._values[self._cursor]
        else:
            self._get_status = self.GET_ERR
            return None

    def is_head(self) -> bool:
        return self._size > 0 and self._cursor == 0

    def is_tail(self) -> bool:
        return self._size > 0 and self._cursor == self._size - 1

    def is_value(self) -> bool:
        return self._size > 0

    def size(self) -> int:
        return self._size

    # Дополнительные запросы
    def get_head_status(self) -> int:
        return self._head_status

    def get_tail_status(self) -> int:
        return self._tail_status

    def get_right_status(self) -> int:
        return self._right_status

    def get_put_right_status(self) -> int:
        return self._put_right_status

    def get_put_left_status(self) -> int:
        return self._put_left_status

    def get_add_to_empty_status(self) -> int:
        return self._add_to_empty_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def get_replace_status(self) -> int:
        return self._replace_status

    def get_find_status(self) -> int:
        return self._find_status

    def get_get_status(self) -> int:
        return self._get_status


class LinkedList(ParentList): ...


class TwoWayList(ParentList):
    LEFT_NIL = 0
    LEFT_OK = 1
    LEFT_ERR = 2

    # Команды
    def left(self) -> None:
        """Предусловие: справа от курсора есть узел.
        Постусловие: курсор сдвинут на один узел влево."""
        if not self.is_head():
            self._cursor -= 1
            self._right_status = self.LEFT_OK
        else:
            self._right_status = self.LEFT_ERR

    def clear(self) -> None:
        super().clear()
        self._left_status = self.LEFT_NIL

    # Дополнительные запросы
    def get_left_status(self) -> int:
        return self._left_status
