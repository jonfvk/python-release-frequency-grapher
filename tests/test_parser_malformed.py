import unittest
from datetime import datetime
from python_release_frequency_grapher import parser

class TestParserMalformedDates(unittest.TestCase):
    def test_malformed_and_missing_dates(self):
        # Lines with various malformed or missing date entries
        lines = [
            '## [1.0.0] - 2022-05-01',  # valid
            '## [1.1.0] - 2022-06-31',  # invalid date (June 31 does not exist)
            '## [1.2.0] - 2022-07-15',  # valid
            '## [1.3.0] - not-a-date',  # malformed date
            '## [1.4.0]',               # missing date
            'v1.5.0 (2022-08-01)',      # valid
            'v1.6.0 (08/15/2022)',      # valid (US-style, but parser expects dd/mm/yyyy)
            'v1.7.0 (15/08/2022)',      # valid
            'v1.8.0 (2022/08/15)',      # malformed date format
            '## [1.9.0] - ',            # missing date
            '## [2.0.0] - 2022-13-01',  # invalid month
        ]
        # Only valid dates should be parsed
        result = parser.parse_changelog_lines(lines)
        # Only lines 1, 3, 6, and 8 should be valid (by default parser)
        expected = [
            ('1.0.0', datetime(2022, 5, 1)),
            ('1.2.0', datetime(2022, 7, 15)),
            ('1.5.0', datetime(2022, 8, 1)),
            ('1.7.0', datetime(2022, 8, 15)),
        ]
        self.assertEqual(result, expected)

    def test_empty_lines(self):
        lines = [
            '',
            '   ',
            '# Changelog',
            'Some random text',
        ]
        result = parser.parse_changelog_lines(lines)
        self.assertEqual(result, [])

    def test_partial_match(self):
        # Line matches version but not date
        lines = [
            '## [1.0.0] - ',
            'v1.1.0 ()',
            'v1.2.0 (2022-05-01)',
        ]
        result = parser.parse_changelog_lines(lines)
        expected = [
            ('1.2.0', datetime(2022, 5, 1)),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
