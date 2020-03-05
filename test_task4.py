from unittest import TestCase

import task4


class MyTest(TestCase):

    def setUp(self):
        pass

    def test_func(self):
        self.assertEqual(task4.func(13), -1)
        self.assertEqual(task4.func(10), 25)
        self.assertEqual(task4.func(100), 455)
        self.assertEqual(task4.func(5), 5)

    def tearDown(self):
        pass
