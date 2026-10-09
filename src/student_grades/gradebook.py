"""Учёт успеваемости студентов: студенты, оценки, средний балл."""

from dataclasses import dataclass, field

MIN_GRADE = 0
MAX_GRADE = 100
PASS_GRADE = 50


@dataclass
class Student:
    """Студент и его оценки по дисциплинам."""

    student_id: int
    full_name: str
    group: str
    grades: dict = field(default_factory=dict)

    def add_grade(self, subject: str, grade: int) -> None:
        """Добавить (или изменить) оценку по дисциплине."""
        if not subject:
            raise ValueError("Название дисциплины не может быть пустым")
        if not isinstance(grade, int) or not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(f"Оценка должна быть целым числом от {MIN_GRADE} до {MAX_GRADE}")
        self.grades[subject] = grade

    def average(self) -> float:
        """Средний балл студента (0, если оценок нет)."""
        if not self.grades:
            return 0.0
        return round(sum(self.grades.values()) / len(self.grades), 2)

    def debts(self) -> list:
        """Дисциплины, по которым оценка ниже проходного балла."""
        return sorted(s for s, g in self.grades.items() if g < PASS_GRADE)


def letter_grade(score: float) -> str:
    """Перевод балла (0–100) в буквенную оценку."""
    if not MIN_GRADE <= score <= MAX_GRADE:
        raise ValueError("Балл должен быть от 0 до 100")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= PASS_GRADE:
        return "D"
    return "F"


class Gradebook:
    """Журнал успеваемости: хранит студентов и строит простую статистику."""

    def __init__(self):
        self._students = {}

    def add_student(self, student_id: int, full_name: str, group: str) -> Student:
        if student_id in self._students:
            raise ValueError(f"Студент с ID {student_id} уже существует")
        student = Student(student_id, full_name, group)
        self._students[student_id] = student
        return student

    def get_student(self, student_id: int) -> Student:
        if student_id not in self._students:
            raise KeyError(f"Студент с ID {student_id} не найден")
        return self._students[student_id]

    def students_in_group(self, group: str) -> list:
        return [s for s in self._students.values() if s.group == group]

    def group_average(self, group: str) -> float:
        students = self.students_in_group(group)
        if not students:
            return 0.0
        return round(sum(s.average() for s in students) / len(students), 2)

    def top_students(self, n: int = 3) -> list:
        """Лучшие студенты по среднему баллу."""
        ranked = sorted(self._students.values(), key=lambda s: s.average(), reverse=True)
        return ranked[:n]

    def students_with_debts(self) -> list:
        return [s for s in self._students.values() if s.debts()]

    def __len__(self):
        return len(self._students)
