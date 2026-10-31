import unittest
from datetime import datetime
from python_release_frequency_grapher import grouping

class TestGroupingAndCounting(unittest.TestCase):
    def setUp(self):
        # Releases: (version, datetime)
        self.releases = [
            ("0.9.0", datetime(2022, 2, 20)),
            ("1.0.0", datetime(2022, 5, 1)),
            ("1.1.0", datetime(2022, 6, 10)),
            ("1.2.0", datetime(2022, 7, 15)),
            ("2.0.0", datetime(2023, 1, 5)),
            ("2.1.0", datetime(2023, 1, 20)),
        ]

    def test_group_by_month(self):
        grouped = grouping.group_releases(self.releases, by="month")
        expected_keys = [
            "2022-02", "2022-05", "2022-06", "2022-07", "2023-01"
        ]
        self.assertEqual(list(grouped.keys()), expected_keys)
        self.assertEqual(len(grouped["2023-01"]), 2)
        self.assertEqual(len(grouped["2022-05"]), 1)
        self.assertEqual(grouped["2022-02"][0][0], "0.9.0")

    def test_group_by_quarter(self):
        grouped = grouping.group_releases(self.releases, by="quarter")
        expected_keys = [
            "2022-Q1", "2022-Q2", "2023-Q1"
        ]
        self.assertEqual(list(grouped.keys()), expected_keys)
        self.assertEqual(len(grouped["2022-Q2"]), 3)  # May, June, July
        self.assertEqual(len(grouped["2023-Q1"]), 2)
        self.assertEqual(grouped["2022-Q1"][0][0], "0.9.0")

    def test_count_releases_per_group_month(self):
        grouped = grouping.group_releases(self.releases, by="month")
        counts = grouping.count_releases_per_group(grouped)
        expected = {
            "2022-02": 1,
            "2022-05": 1,
            "2022-06": 1,
            "2022-07": 1,
            "2023-01": 2,
        }
        self.assertEqual(counts, expected)

    def test_count_releases_per_group_quarter(self):
        grouped = grouping.group_releases(self.releases, by="quarter")
        counts = grouping.count_releases_per_group(grouped)
        expected = {
            "2022-Q1": 1,
            "2022-Q2": 3,
            "2023-Q1": 2,
        }
        self.assertEqual(counts, expected)

    def test_empty_input(self):
        grouped = grouping.group_releases([], by="month")
        self.assertEqual(grouped, {})
        counts = grouping.count_releases_per_group(grouped)
        self.assertEqual(counts, {})

    def test_single_release(self):
        single = [("1.0.0", datetime(2022, 5, 1))]
        grouped = grouping.group_releases(single, by="month")
        self.assertEqual(list(grouped.keys()), ["2022-05"])
        counts = grouping.count_releases_per_group(grouped)
        self.assertEqual(counts, {"2022-05": 1})

if __name__ == "__main__":
    unittest.main()
