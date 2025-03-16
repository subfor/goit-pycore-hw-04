import re
from pathlib import Path


def get_cats_info(path: str) -> list:
    cats_info = []
    data_file = Path(path)

    if not data_file.exists():
        print("Файл не існує")
        return cats_info

    pattern = re.compile(r"^[0-9a-f]{24},[A-Za-z-]+,\d+$")

    with open(file=path, mode="r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                cat_id, cat_name, cat_age = line.split(",")
                cats_info.append(
                    {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age,
                    }
                )
    return cats_info


if __name__ == "__main__":
    cats_info = get_cats_info("./cats.txt")
    print(cats_info)
