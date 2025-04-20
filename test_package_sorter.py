import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard(self):
        # STANDARD: Not bulky, not heavy
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_special_bulky(self):
        # SPECIAL: Bulky but not heavy
        self.assertEqual(sort(200, 10, 10, 5), "SPECIAL")

    def test_special_heavy(self):
        # SPECIAL: Heavy but not bulky
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_rejected(self):
        # REJECTED: Both bulky and heavy
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_edge_case_bulky_volume(self):
        # Edge case: Exactly at the bulky threshold (volume)
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")

    def test_edge_case_bulky_dimension(self):
        # Edge case: Exactly at the bulky threshold (dimension)
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_edge_case_heavy(self):
        # Edge case: Exactly at the heavy threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_invalid_negative_dimensions(self):
        # Invalid input: Negative dimensions
        with self.assertRaises(ValueError):
            sort(-10, 10, 10, 5)

    def test_invalid_zero_mass(self):
        # Invalid input: Zero mass
        with self.assertRaises(ValueError):
            sort(10, 10, 10, 0)

    def test_invalid_non_numeric(self):
        # Invalid input: Non-numeric values
        with self.assertRaises(TypeError):
            sort("10", 10, 10, 5)

if __name__ == "__main__":
    unittest.main()
