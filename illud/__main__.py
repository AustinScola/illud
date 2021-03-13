"""Package main."""
import sys

from illud.main import main


def package_main() -> None:
    """Run the Illud package main method with the system arguments."""
    if __name__ == '__main__':
        sys.exit(main(sys.argv[1:]))


package_main()
