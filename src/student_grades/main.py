"""Демонстрация работы приложения «Учёт успеваемости студентов»."""

from student_grades import Gradebook, letter_grade


def main():
    book = Gradebook()

    s1 = book.add_student(1, "Иванов Иван", "ИС-41")
    s1.add_grade("DevOps", 95)
    s1.add_grade("Базы данных", 88)

    s2 = book.add_student(2, "Петрова Анна", "ИС-41")
    s2.add_grade("DevOps", 72)
    s2.add_grade("Базы данных", 45)

    s3 = book.add_student(3, "Сидоров Алексей", "ИС-42")
    s3.add_grade("DevOps", 64)
    s3.add_grade("Базы данных", 70)

    print("=== Учёт успеваемости студентов ===")
    for s in book.top_students(len(book)):
        print(f"{s.full_name:<18} {s.group:<6} средний балл: {s.average():>6}  ({letter_grade(s.average())})")

    print(f"\nСредний балл группы ИС-41: {book.group_average('ИС-41')}")
    print("Задолженности:")
    for s in book.students_with_debts():
        print(f"  {s.full_name}: {', '.join(s.debts())}")


if __name__ == "__main__":
    main()
