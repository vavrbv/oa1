import unittest

from .task6 import Deque


class TestEmpty(unittest.TestCase):
    def test_new(self) -> None:
        deque = Deque[object]()

        self.assertEqual(deque.get_remove_front_status(), Deque.REMOVE_FRONT_NIL)
        self.assertEqual(deque.get_remove_tail_status(), Deque.REMOVE_TAIL_NIL)
        self.assertEqual(deque.get_peek_front_status(), Deque.PEEK_FRONT_NIL)
        self.assertEqual(deque.get_peek_tail_status(), Deque.PEEK_TAIL_NIL)

        self.assertEqual(deque.size(), 0)

    def test_clear(self) -> None:
        deque = Deque[object]()
        deque.add_front(123)
        deque.add_tail("abc")
        deque.clear()

        self.assertEqual(deque.get_remove_front_status(), Deque.REMOVE_FRONT_NIL)
        self.assertEqual(deque.get_remove_tail_status(), Deque.REMOVE_TAIL_NIL)
        self.assertEqual(deque.get_peek_front_status(), Deque.PEEK_FRONT_NIL)
        self.assertEqual(deque.get_peek_tail_status(), Deque.PEEK_TAIL_NIL)

        self.assertEqual(deque.size(), 0)


class TestAddFront(unittest.TestCase):
    def test_add_front(self) -> None:
        deque = Deque[object]()

        deque.add_front(123)
        deque.add_front("abc")

        self.assertEqual(deque.size(), 2)

        front = deque.peek_front()
        self.assertEqual(front, "abc")

        tail = deque.peek_tail()
        self.assertEqual(tail, 123)


class TestRemoveTail(unittest.TestCase):
    def test_remove_tail_ok(self) -> None:
        deque = Deque[object]()
        deque.add_front(123)
        deque.add_front("abc")

        deque.remove_tail()
        self.assertEqual(deque.get_remove_tail_status(), Deque.REMOVE_TAIL_OK)
        self.assertEqual(deque.size(), 1)

        value = deque.peek_tail()
        self.assertEqual(value, "abc")

        deque.remove_tail()
        self.assertEqual(deque.get_remove_tail_status(), Deque.REMOVE_TAIL_OK)
        self.assertEqual(deque.size(), 0)

    def test_remove_tail_error(self) -> None:
        deque = Deque[object]()
        deque.remove_tail()

        self.assertEqual(deque.get_remove_tail_status(), Deque.REMOVE_TAIL_ERR)


if __name__ == "__main__":
    unittest.main()
