import pytest

from student_grades import Gradebook, Student, letter_grade


# Тест 1: средний балл считается правильно
def test_student_average():
    s = Student(1, "Иванов Иван", "ИС-41")
    s.add_grade("DevOps", 90)
    s.add_grade("Базы данных", 80)
    assert s.average() == 85.0


# Тест 2: у студента без оценок средний балл 0
def test_average_without_grades():
    s = Student(2, "Петрова Анна", "ИС-41")
    assert s.average() == 0.0


# Тест 3: некорректная оценка не принимается
@pytest.mark.parametrize("bad_grade", [-1, 101, "90"])
def test_invalid_grade_rejected(bad_grade):
    s = Student(3, "Сидоров Алексей", "ИС-42")
    with pytest.raises(ValueError):
        s.add_grade("DevOps", bad_grade)


# Тест 4: перевод балла в буквенную оценку
@pytest.mark.parametrize(
    "score, expected",
    [(95, "A"), (80, "B"), (65, "C"), (55, "D"), (30, "F")],
)
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected


# Тест 5: задолженности (оценка ниже 50)
def test_debts():
    s = Student(4, "Ким Дана", "ИС-41")
    s.add_grade("DevOps", 70)
    s.add_grade("Базы данных", 40)
    assert s.debts() == ["Базы данных"]


# Тест 6: журнал — добавление студентов, средний по группе, рейтинг
def test_gradebook_group_and_top():
    book = Gradebook()
    a = book.add_student(1, "Иванов Иван", "ИС-41")
    b = book.add_student(2, "Петрова Анна", "ИС-41")
    a.add_grade("DevOps", 90)
    b.add_grade("DevOps", 70)

    assert len(book) == 2
    assert book.group_average("ИС-41") == 80.0
    assert book.top_students(1)[0].full_name == "Иванов Иван"


# Тест 7: нельзя добавить двух студентов с одинаковым ID
def test_duplicate_student_id():
    book = Gradebook()
    book.add_student(1, "Иванов Иван", "ИС-41")
    with pytest.raises(ValueError):
        book.add_student(1, "Другой Студент", "ИС-42")
