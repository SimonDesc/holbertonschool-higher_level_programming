import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Rectangle.id = 0
        self.rect1 = Rectangle(5, 10, 2, 3)
        self.rect2 = Rectangle(5, 10, 2, 3, 100)
        

    def test_aid(self):
        self.assertEqual(self.rect1.id, 1)  
        self.assertEqual(self.rect2.id, 100)

    def test_dimensions(self):
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect1.height, 10)
        self.assertEqual(self.rect1.x, 2)
        self.assertEqual(self.rect1.y, 3)

    def test_setters(self):
        self.rect1.width = 20
        self.rect1.height = 30
        self.rect1.x = 4
        self.rect1.y = 6

        self.assertEqual(self.rect1.width, 20)
        self.assertEqual(self.rect1.height, 30)
        self.assertEqual(self.rect1.x, 4)
        self.assertEqual(self.rect1.y, 6)
        
    def tearDown(self):
        Rectangle.id = 0

if __name__ == "__main__":
    unittest.main()
