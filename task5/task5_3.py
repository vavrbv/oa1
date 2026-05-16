import unittest

from .task5 import ListQueue


class TestEmpty(unittest.TestCase):
    def test_new(self) -> None:
        queue = ListQueue[object]()

        self.assertEqual(queue.get_dequeue_status(), ListQueue.DEQUEUE_NIL)
        self.assertEqual(queue.get_enqueue_status(), ListQueue.ENQUEUE_NIL)
        self.assertEqual(queue.get_peek_status(), ListQueue.PEEK_NIL)

        self.assertEqual(queue.size(), 0)

    def test_clear(self) -> None:
        queue = ListQueue[object]()
        queue.enqueue(123)
        queue.enqueue("abc")
        queue.clear()

        self.assertEqual(queue.get_dequeue_status(), ListQueue.DEQUEUE_NIL)
        self.assertEqual(queue.get_enqueue_status(), ListQueue.ENQUEUE_NIL)
        self.assertEqual(queue.get_peek_status(), ListQueue.PEEK_NIL)

        self.assertEqual(queue.size(), 0)


class TestEnqueue(unittest.TestCase):
    def test_enqueue_ok(self) -> None:
        queue = ListQueue[object]()

        queue.enqueue(123)
        self.assertEqual(queue.get_enqueue_status(), ListQueue.ENQUEUE_OK)
        queue.enqueue("abc")
        self.assertEqual(queue.get_enqueue_status(), ListQueue.ENQUEUE_OK)

        self.assertEqual(queue.size(), 2)

        value = queue.peek()
        self.assertEqual(value, 123)


class TestDequeue(unittest.TestCase):
    def test_dequeue_ok(self) -> None:
        queue = ListQueue[object]()
        queue.enqueue(123)
        queue.enqueue("abc")

        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), ListQueue.DEQUEUE_OK)
        self.assertEqual(queue.size(), 1)

        value = queue.peek()
        self.assertEqual(value, "abc")

        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), ListQueue.DEQUEUE_OK)
        self.assertEqual(queue.size(), 0)

    def test_dequeue_error(self) -> None:
        queue = ListQueue[object]()
        queue.dequeue()

        self.assertEqual(queue.get_dequeue_status(), ListQueue.DEQUEUE_ERR)


class TestPeek(unittest.TestCase):
    def test_peek_ok(self) -> None:
        queue = ListQueue[object]()
        queue.enqueue(123)
        queue.enqueue("abc")

        value = queue.peek()
        self.assertEqual(value, 123)
        self.assertEqual(queue.get_peek_status(), ListQueue.PEEK_OK)

    def test_peek_error(self) -> None:
        queue = ListQueue[object]()
        value = queue.peek()

        self.assertEqual(queue.get_peek_status(), ListQueue.PEEK_ERR)
        self.assertEqual(value, None)


if __name__ == "__main__":
    unittest.main()
