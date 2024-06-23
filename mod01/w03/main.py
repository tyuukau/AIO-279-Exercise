import torch

from softmax import Softmax, SoftmaxStable
from queue import Queue
from stack import Stack
from ward import Ward, Student, Teacher, Doctor


def main():
    print("Demo softmax")

    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)

    print("Demo stack")

    stack1 = Stack(capacity=5)
    stack1.push(1)
    stack1.push(2)

    print(stack1.is_full())  # Output: False
    print(stack1.top())  # Output: 2
    print(stack1.pop())  # Output: 2
    print(stack1.top())  # Output: 1
    print(stack1.pop())  # Output: 1
    print(stack1.is_empty())  # Output: True

    print("Demo queue")

    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)

    print(queue1.is_full())  # Output: False
    print(queue1.front())  # Output: 1
    print(queue1.dequeue())  # Output: 1
    print(queue1.front())  # Output: 2
    print(queue1.dequeue())  # Output: 2
    print(queue1.is_empty())  # Output: True

    print("Demo ward")

    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    print()

    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

    ward1 = Ward(name="Ward1")
    for person in [student1, teacher1, doctor1, teacher2, doctor2]:
        ward1.add_person(person)
    ward1.describe()

    print(f"\nNumber of doctors: {ward1.count_doctor()}")

    print("\nAfter sorting Age of Ward1 people ")
    ward1.sort_by_age()
    ward1.describe()

    print(f"\nAverage year of birth (teachers): {ward1.compute_average_teacher_yob()}")


if __name__ == "__main__":
    main()
