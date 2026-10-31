import unittest
from datetime import datetime
from python_release_frequency_grapher import parser

class TestParserSorting(unittest.TestCase):
    def setUp(self):
        # Unsorted (version, date) pairs
        self.unsorted_releases = [
            ("1.0.0", datetime(2022, 5, 1)),
            ("1.2.0", datetime(2022, 7, 15)),
            ("1.1.0", datetime(2022, 6, 10)),
            ("2.0.0", datetime(2023, 1, 5)),
            ("0.9.0", datetime(2022, 2, 20)),
        ]
        self.sorted_releases = [
            ("0.9.0", datetime(2022, 2, 20)),
            ("1.0.0", datetime(2022, 5, 1)),
            ("1.1.0", datetime(2022, 6, 10)),
            ("1.2.0", datetime(2022, 7, 15)),
            ("2.0.0", datetime(2023, 1, 5)),
        ]

    def test_sort_releases_chronologically(self):
        result = parser.sort_releases_chronologically(self.unsorted_releases)
        self.assertEqual(result, self.sorted_releases)

    def test_sort_releases_empty(self):
        self.assertEqual(
            parser.sort_releases_chronologically([]),
            []
        )

    def test_sort_releases_single(self):
        single = [("1.0.0", datetime(2022, 5, 1))]
        self.assertEqual(
            parser.sort_releases_chronologically(single),
            single
        )

    def test_sort_releases_with_same_date(self):
        releases = [
            ("1.0.0", datetime(2022, 5, 1)),
            ("1.0.1", datetime(2022, 5, 1)),
            ("0.9.0", datetime(2022, 2, 20)),
        ]
        expected = [
            ("0.9.0", datetime(2022, 2, 20)),
            ("1.0.0", datetime(2022, 5, 1)),
            ("1.0.1", datetime(2022, 5, 1)),
        ]
        result = parser.sort_releases_chronologically(releases)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
