import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze a Python project's release history and generate an ASCII graph showing release frequency over time."
    )
    parser.add_argument(
        'changelog_path',
        metavar='CHANGELOG_PATH',
        type=str,
        help='Path to the changelog or version history file.'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    changelog_path = args.changelog_path
    if not os.path.isfile(changelog_path):
        print(f"Error: File '{changelog_path}' does not exist.")
        exit(1)
    print(f"Changelog file accepted: {changelog_path}")


if __name__ == "__main__":
    main()
