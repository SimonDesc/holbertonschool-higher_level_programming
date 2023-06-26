import unittest
from models.base import Base

class testBase(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        Base._Base__nb_objects = 0
    
    def test_id_is_assigned_when_provided(self):
        """Test if an id is correctly assigned when it is provided"""
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)

    def test_id_is_generated_when_not_provided(self):
        """Test if an id is generated when it is not provided"""
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_id_incrementation(self):
        """Test if id is correctly incremented when multiple instances are created without providing an id"""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

if __name__ == '__main__':
    unittest.main()
