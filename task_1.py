from pathlib import Path


def total_salary(path: str) -> tuple:
    data_file = Path(path)
    if not data_file.exists():
        print("Файл не існує")
        return 0, 0

    full_salary_list = []

    with data_file.open(mode="r", encoding="utf-8") as file:
        for line in file:
            person = line.strip().split(",")
            if len(person) == 2 and person[1].isdigit():
                full_salary_list.append(int(person[1]))

    if full_salary_list:
        full_salary = sum(full_salary_list)
        median_salary = int(full_salary / len(full_salary_list))
        return full_salary, median_salary

    return 0, 0


if __name__ == "__main__":
    total, average = total_salary(path="./salaries.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
