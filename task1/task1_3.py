import unittest

from .task1 import BoundedStack, Nothing


class TestClearStack(unittest.TestCase):
    def test_new(self) -> None:
        stack = BoundedStack[object]()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_NIL)
        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_NIL)
        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_NIL)

    def test_clear(self) -> None:
        stack = BoundedStack[object]()
        stack.push(123)
        stack.push("abc")
        stack.peek()
        stack.pop()
        stack.push(None)

        stack.clear()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_NIL)
        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_NIL)
        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_NIL)

    def test_min_size(self) -> None:
        stack = BoundedStack[object](-100)
        stack.push(123)

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_OK)

        stack.push("abc")
        value = stack.peek()

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_ERR)
        self.assertEqual(value, 123)


class TestPeek(unittest.TestCase):
    def test_ok(self) -> None:
        stack = BoundedStack[object]()
        stack.push(123)
        stack.push("abc")
        value = stack.peek()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_OK)
        self.assertEqual(value, "abc")

    def test_error(self) -> None:
        stack = BoundedStack[object]()
        value = stack.peek()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_ERR)
        self.assertTrue(isinstance(value, Nothing))


class TestPop(unittest.TestCase):
    def test_ok(self) -> None:
        stack = BoundedStack[object]()
        stack.push(123)
        stack.push("abc")

        stack.pop()
        value = stack.peek()

        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_OK)
        self.assertEqual(value, 123)

    def test_error(self) -> None:
        stack = BoundedStack[object]()
        stack.pop()

        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_ERR)


class TestPush(unittest.TestCase):
    def test_ok(self) -> None:
        stack = BoundedStack[object]()
        stack.push(123)
        value = stack.peek()

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_OK)
        self.assertEqual(value, 123)

    def test_error(self) -> None:
        stack = BoundedStack[object](2)
        stack.push(123)
        stack.push("abc")

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_OK)

        stack.push(456.0)
        value = stack.peek()

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_ERR)
        self.assertEqual(value, "abc")


if __name__ == "__main__":
    unittest.main()
