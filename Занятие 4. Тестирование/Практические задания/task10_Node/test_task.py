import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        print("test_init_node_without_next")
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        self.assertIsNone(self.next, self.Node)  # TODO с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        print("test_init_node_with_next(")
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        self.assertEqual(self.Node.next)  # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        print("test_repr_node_without_next")
        self.__repr__(Node)
        self.assertEqual(self.__repr__())  # TODO проверить метод __repr__ без следующего узла

    ...  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        # TODO проверить строковое представление

    def test_is_valid(self):
        ...  # TODO проверить метод is_valid при корректных узлах

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
