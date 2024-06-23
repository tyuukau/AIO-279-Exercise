from dataclasses import dataclass


@dataclass
class Person:
    name: str
    yob: int

    def describe(self) -> str:
        return self.__str__()


@dataclass
class Student(Person):
    grade: str


@dataclass
class Doctor(Person):
    specialist: str


@dataclass
class Teacher(Person):
    subject: str


class Ward:
    """
    Represents a ward containing various people such as students, teachers, and doctors.

    Attributes:
        name (str): The name of the ward.
        people (list[Person]): A list containing all people (instances of Person) in the ward.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a Ward object with a given name.

        Args:
            name (str): The name of the ward.
        """
        self.name = name
        self.people: list[Person] = []

    def add_person(self, person: Person) -> None:
        """
        Adds a person to the ward.

        Args:
            person (Person): The person object to be added to the ward.
        """
        self.people.append(person)

    def describe(self) -> None:
        """
        Prints information about the ward and its residents.
        """
        print(f"Ward: {self.name}")
        for person in self.people:
            print(person.describe())

    def count_doctor(self) -> int:
        """
        Counts the number of doctors in the ward.

        Returns:
            int: The number of doctors in the ward.
        """
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_by_age(self) -> None:
        """
        Sorts the people in the ward by their year of birth (ascending).
        """
        self.people.sort(key=lambda person: person.yob)

    def compute_average_teacher_yob(self) -> float:
        """
        Computes the average year of birth of teachers in the ward.

        Returns:
            float: The average year of birth of teachers. Returns 0.0 if no teachers are present.
        """
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0.0
        total_yob = sum(teacher.yob for teacher in teachers)
        return total_yob / len(teachers)
