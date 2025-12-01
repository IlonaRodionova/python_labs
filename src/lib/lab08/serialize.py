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