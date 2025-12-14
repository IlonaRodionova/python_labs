import csv
from pathlib import Path
from src.lib.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])

    def _read_all(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _write_all(self, rows):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)

    def list(self):
        rows = self._read_all()
        students = []
        for row in rows:
            student = Student(
                fio=row['fio'],
                birthdate=row['birthdate'],
                group=row['group'],
                gpa=float(row['gpa'])
            )
            students.append(student)
        return students

    def add(self, student: Student):
        rows = self._read_all()
        new_row = {
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)
        }
        rows.append(new_row)
        self._write_all(rows)

    def find(self, substr: str):
        students = self.list()
        result = []
        for student in students:
            if substr.lower() in student.fio.lower():
                result.append(student)
        return result

    def remove(self, fio: str):
        rows = self._read_all()
        new_rows = []
        for row in rows:
            if row['fio'] != fio:
                new_rows.append(row)
        self._write_all(new_rows)

    def update(self, fio: str, **fields):
        rows = self._read_all()
        for row in rows:
            if row['fio'] == fio:
                for key, value in fields.items():
                    if key in row:
                        row[key] = str(value)
                break
        self._write_all(rows)

    def stats(self) -> dict:
        students = self.list()

        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }

        gpa_values = [s.gpa for s in students]

        groups = {}
        for student in students:
            group_name = student.group
            groups[group_name] = groups.get(group_name, 0) + 1

        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]

        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups,
            "top_5_students": top_5
        }