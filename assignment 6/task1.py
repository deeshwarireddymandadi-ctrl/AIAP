# ...existing code...

from typing import List, Dict

class Student:
    """
    Simple Student class holding basic attributes and grade-related methods.
    Attributes:
      - name: student's full name (str)
      - student_id: unique identifier (str)
      - grades: list of numeric grades (floats 0-100)
    Methods:
      - add_grade(grade): add a grade (validated 0-100)
      - average(): return average grade (0.0 if no grades)
      - is_passing(threshold=60.0): return True if average >= threshold
      - summary(): return a short summary string
      - to_dict()/from_dict(): simple (de)serialization helpers
    """
    def __init__(self, name: str, student_id: str, grades: List[float] | None = None):
        self.name = name.strip()
        self.student_id = str(student_id).strip()
        self.grades: List[float] = list(grades) if grades else []

    def add_grade(self, grade: float) -> None:
        """Add a grade after validating it's within 0..100."""
        try:
            g = float(grade)
        except (TypeError, ValueError):
            raise ValueError("Grade must be a number.")
        if g < 0 or g > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(g)

    def average(self) -> float:
        """Return average of grades (0.0 if no grades)."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_passing(self, threshold: float = 60.0) -> bool:
        """Return True if average grade >= threshold."""
        return self.average() >= threshold

    def summary(self) -> str:
        """Return a human-friendly summary of the student's record."""
        avg = self.average()
        return (
            f"Student: {self.name} (ID: {self.student_id})\n"
            f"Grades: {', '.join(f'{g:.1f}' for g in self.grades) if self.grades else 'No grades'}\n"
            f"Average: {avg:.2f}\n"
            f"Status: {'Passing' if self.is_passing() else 'Not passing'}"
        )

    def to_dict(self) -> Dict:
        """Serialize to a dictionary."""
        return {"name": self.name, "student_id": self.student_id, "grades": list(self.grades)}

    @classmethod
    def from_dict(cls, data: Dict) -> "Student":
        """Create a Student from a dictionary."""
        return cls(name=data.get("name", ""), student_id=data.get("student_id", ""), grades=data.get("grades", []))

if __name__ == "__main__":
    try:
        name = input("Enter student name: ").strip() or "Unnamed Student"
        sid = input("Enter student ID: ").strip() or "N/A"
        student = Student(name=name, student_id=sid)

        print("\nEnter grades one by one (press Enter on blank line to finish).")
        while True:
            s = input("Grade (0-100): ").strip()
            if s == "":
                break
            try:
                student.add_grade(float(s))
            except ValueError as e:
                print(f"Invalid grade: {e}")

        print("\n" + student.summary())

        # optional: ask for custom passing threshold
        thr_in = input("\nCheck passing with custom threshold (press Enter to skip): ").strip()
        if thr_in:
            try:
                thr = float(thr_in)
                print(f"Passing at {thr}: {'Yes' if student.is_passing(thr) else 'No'}")
            except ValueError:
                print("Invalid threshold value; skipping.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
# ...existing code...