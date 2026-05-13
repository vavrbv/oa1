import unittest

from .task4 import TupleDynArray


class TestTupleDynArray(unittest.TestCase):
    def test_new(self) -> None:
        array = TupleDynArray[int]()

        self.assertEqual(array.size(), 0)

        self.assertEqual(array.get_append_status(), TupleDynArray.APPEND_NIL)
        self.assertEqual(array.get_get_status(), TupleDynArray.GET_NIL)
        self.assertEqual(array.get_insert_status(), TupleDynArray.INSERT_NIL)
        self.assertEqual(array.get_remove_status(), TupleDynArray.REMOVE_NIL)

    def test_get(self) -> None:
        array = TupleDynArray[int]()
        array.append(3)
        array.append(2)
        array.append(1)

        x1 = array.get(0)
        self.assertEqual(array.get_get_status(), TupleDynArray.GET_OK)
        self.assertEqual(x1, 3)

        x2 = array.get(1)
        self.assertEqual(array.get_get_status(), TupleDynArray.GET_OK)
        self.assertEqual(x2, 2)

        x3 = array.get(2)
        self.assertEqual(array.get_get_status(), TupleDynArray.GET_OK)
        self.assertEqual(x3, 1)

        x4 = array.get(3)
        self.assertEqual(array.get_get_status(), TupleDynArray.GET_ERR)
        self.assertEqual(x4, None)

    def test_append(self) -> None:
        array = TupleDynArray[int]()

        array.append(3)
        self.assertEqual(array.get_append_status(), TupleDynArray.APPEND_OK)

        array.append(2)
        self.assertEqual(array.get_append_status(), TupleDynArray.APPEND_OK)

        array.append(1)
        self.assertEqual(array.get_append_status(), TupleDynArray.APPEND_OK)

        self.assertEqual(array.size(), 3)

        self.assertEqual(array.get(0), 3)
        self.assertEqual(array.get(1), 2)
        self.assertEqual(array.get(2), 1)

    def test_insert(self) -> None:
        array = TupleDynArray[int]()
        array.append(3)
        array.append(2)
        array.append(1)

        array.insert(4, 0)
        self.assertEqual(array.get_append_status(), TupleDynArray.INSERT_OK)

        array.insert(5, 2)
        self.assertEqual(array.get_append_status(), TupleDynArray.INSERT_OK)

        array.insert(10, 100)
        self.assertEqual(array.get_append_status(), TupleDynArray.INSERT_OK)

        self.assertEqual(array.size(), 6)

        self.assertEqual(array.get(0), 4)
        self.assertEqual(array.get(2), 5)
        self.assertEqual(array.get(5), 10)

    def test_remove(self) -> None:
        array = TupleDynArray[int]()
        array.append(3)
        array.append(2)
        array.append(1)

        array.remove(0)
        self.assertEqual(array.get_remove_status(), TupleDynArray.REMOVE_OK)
        self.assertEqual(array.size(), 2)

        array.remove(3)
        self.assertEqual(array.get_remove_status(), TupleDynArray.REMOVE_ERR)
        self.assertEqual(array.size(), 2)


if __name__ == "__main__":
    unittest.main()
