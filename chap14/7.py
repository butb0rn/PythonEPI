class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def groupByAge(people):
    ppl = {}
    res = []
    for p in people:
        if p.age in ppl.keys():
            ppl[p.age] += 1
        else:
            ppl[p.age] = 1

    for key, value in ppl.items():
        res.append(str(value)+str(key))

    return "".join(res)


students = [Student("Greg", 14),Student("John", 12),Student("Andy", 11),Student("Jim", 13), Student("Phil", 12), \
                    Student("Bob", 13), Student("Chip", 13), Student("Tim", 14)]
print groupByAge(students)
