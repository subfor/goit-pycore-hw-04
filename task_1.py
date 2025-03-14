from pathlib import Path


def total_salary(path: str) -> tuple:
    data_file = Path(path)
    if data_file.exists():
        with open(file=path, mode="r", encoding="utf-8") as file:
            content = file.readlines()
            full_salary_list = [
                int(line.split(",")[1].rstrip())
                for line in content
                if len(line.split(",")) == 2 and line.split(",")[1].rstrip().isdigit()
            ]
            if full_salary_list:
                full_salary = sum(full_salary_list)
                median_salary = int(full_salary / len(full_salary_list))
                return full_salary, median_salary
    else:
        print("Файл не існує")
    return 0, 0


if __name__ == "__main__":
    total, average = total_salary(path="./salaries.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
