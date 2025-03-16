import sys
from pathlib import Path

from colorama import Fore, Style


def list_directory(path: Path, prefix: str = "    ") -> None:
    for child in sorted(path.iterdir()):
        if child.is_dir():
            print(prefix + Fore.GREEN + "📂 " + child.name + Style.RESET_ALL)
            list_directory(path=child, prefix=prefix + "    ")
        else:
            print(prefix + Fore.YELLOW + "📄 " + child.name + Style.RESET_ALL)


def main() -> None:
    if len(sys.argv) < 2:
        print("❌ Error: No path provided")
        sys.exit(1)

    path = sys.argv[1]
    folder = Path(path.strip())

    if not (folder.exists() and folder.is_dir()):
        print("❌ Directory not found")
        sys.exit(1)

    print(Fore.GREEN + "📂 " + folder.name + Style.RESET_ALL)
    list_directory(path=folder)


if __name__ == "__main__":
    main()
