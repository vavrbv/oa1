import unittest

from .task3 import ParentList


class TestParentList(unittest.TestCase):
    def test_new(self) -> None:
        parent_list = ParentList[object]()

        self.assertEqual(parent_list.get_head_status(), ParentList.HEAD_NIL)
        self.assertEqual(parent_list.get_tail_status(), ParentList.TAIL_NIL)
        self.assertEqual(parent_list.get_right_status(), ParentList.RIGHT_NIL)
        self.assertEqual(parent_list.get_put_right_status(), ParentList.PUT_RIGHT_NIL)
        self.assertEqual(parent_list.get_put_left_status(), ParentList.PUT_LEFT_NIL)
        self.assertEqual(parent_list.get_add_to_empty_status(), ParentList.ADD_TO_EMPTY_NIL)
        self.assertEqual(parent_list.get_remove_status(), ParentList.REMOVE_NIL)
        self.assertEqual(parent_list.get_replace_status(), ParentList.REPLACE_NIL)
        self.assertEqual(parent_list.get_find_status(), ParentList.FIND_NIL)
        self.assertEqual(parent_list.get_get_status(), ParentList.GET_NIL)

        self.assertFalse(parent_list.is_head())
        self.assertFalse(parent_list.is_tail())
        self.assertFalse(parent_list.is_value())

        self.assertEqual(parent_list.size(), 0)

    def test_add_to_empty_ok(self) -> None:
        parent_list = ParentList[object]()
        parent_list.add_to_empty(123)

        self.assertEqual(parent_list.get_add_to_empty_status(), ParentList.ADD_TO_EMPTY_OK)

        self.assertTrue(parent_list.is_head())
        self.assertTrue(parent_list.is_tail())
        self.assertTrue(parent_list.is_value())

        self.assertEqual(parent_list.size(), 1)

    def test_add_to_empty_error(self) -> None:
        parent_list = ParentList[object]()
        parent_list.add_to_empty(123)

        self.assertEqual(parent_list.get_add_to_empty_status(), ParentList.ADD_TO_EMPTY_OK)

        parent_list.add_to_empty("abc")

        self.assertEqual(parent_list.get_add_to_empty_status(), ParentList.ADD_TO_EMPTY_ERR)

    def test_head_ok(self) -> None:
        parent_list = ParentList[object]()
        parent_list.add_to_empty(123)
        parent_list.put_right("abc")
        parent_list.tail()

        parent_list.head()

        self.assertEqual(parent_list.get_head_status(), ParentList.HEAD_OK)
        self.assertTrue(parent_list.is_head())


if __name__ == "__main__":
    unittest.main()
