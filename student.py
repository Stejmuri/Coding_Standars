"""
Student Grade Management System.

This module provides a Student class to manage grades, calculate
averages, determine honor roll status, and generate reports.
"""


class Student:
    """Represents a student with a collection of grades."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize a student with an ID and name."""
        self.student_id = student_id
        self.name = name
        self.grades: list[float] = []
        self.is_passed = "NO"
        self.honor = "no"

    def add_grade(self, grade) -> None:
        """Add a grade to the student's record."""
        if not isinstance(grade, (int, float)):
            print(f"Error: '{grade}' is not a valid number.")
            return
        if grade < 0 or grade > 100:
            print(f"Error: grade {grade} is out of range (0-100).")
            return
        self.grades.append(grade)

    def calc_average(self) -> float:
        """Return the average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def check_honor(self) -> None:
        """Update honor roll status based on average."""
        if self.calc_average() > 90:
            self.honor = "yes"
        else:
            self.honor = "no"

    def delete_grade(self, index: int) -> None:
        """Remove a grade by its index."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Error: index {index} is out of range.")

    def report(self) -> None:
        """Print a formatted report of the student's performance."""
        average = self.calc_average()
        if average >= 60:
            self.is_passed = "YES"
        else:
            self.is_passed = "NO"

        print(f"ID: {self.student_id}")
        print(f"Name is: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade = {average:.2f}")
        print(f"Passed: {self.is_passed}")
        print(f"Honor Roll: {self.honor}")


def main() -> None:
    """Run the student grade management demonstration."""
    student = Student("x", "John Doe")
    student.add_grade(100)
    student.add_grade(85.5)
    student.add_grade(90)

    student.add_grade("Fifty")
    student.delete_grade(5)

    student.check_honor()
    student.report()


if __name__ == "__main__":
    main()
