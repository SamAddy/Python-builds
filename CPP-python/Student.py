"""
Define the class Student with the following fields: a name (being a string), a unique positive sequential 
index number computed for each student and an array/list of his marks (empty by default). The given index number
cannot be changed since the Student object creation time.

output:
Name: Scott Tiger
Index: 1
Marks: 4.0, 5.0 
Average grade: 4.5
"""


class Student:
    index_num = 0

    def __init__(self, name:str, marks=[]) -> None:
        self.name = name
        self.marks = []
        #Student.index_num += 1

    def getName(self):
        return f"Name: {self.name }"

    @classmethod
    def getIndex(cls):
        cls.index_num += 1
        return f"Index: {cls.index_num}"

    def addMark(self, m):
        try:
            if m >= 2.0 and m <= 5.0:
                self.marks.append(m)
        except:
            print("Marks should be between 2.0 and 5.0")

    def getMarkCount(self):
        return len(self.marks)

    def showMarks(self):
        return f"Marks: {self.marks}"

    def avgGrade(self):
        average = sum(self.marks) / len(self.marks)
        return f"Average grade: {average}"

    def removeMark(self, m):
        return self.marks.remove(m)


stud1 = Student("Scott Tiger")
stud1.addMark(3.5)
stud1.addMark(5.0)
stud1.addMark(1.5)
stud1.marks[0] = 4.0
stud1.removeMark(5.0)
print(stud1.getName())
print(stud1.getIndex())
print(stud1.showMarks())
print(stud1.avgGrade())


stud2 = Student("John Smiths")
stud2.addMark(5.0)
stud2.addMark(3.0)
stud2.addMark(4.0)
stud2.addMark(3.0)

print(stud2.marks[1])
stud2.removeMark(3.0)
print(stud2.marks[1])
print(stud2.getIndex())

# print(stud2)
print(stud2.getName())