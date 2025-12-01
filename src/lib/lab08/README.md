# Лабораторная 8
## Задание 1
``` python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Требуется: YYYY-MM-DD")

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть от 0 до 5, получено: {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data.get("fio"),
            birthdate=data.get("birthdate"),
            group=data.get("group"),
            gpa=data.get("gpa")
        )

    def __str__(self) -> str:
        return f"{self.fio}, {self.group}, {self.age()} лет, GPA: {self.gpa:.2f}"
```


## Задание 2

``` python
import json
from pathlib import Path
from typing import List
from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив объектов")

    students = []
    for item in data:
        student = Student.from_dict(item)
        students.append(student)

    return students
```
![students_output.png](..%2F..%2F..%2Fimages%2Flab08%2Fstudents_output.png)

