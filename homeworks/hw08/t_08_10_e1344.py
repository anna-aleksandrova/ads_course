def less_cl(c1: str, c2: str):
    c11 = ""
    for i in range(len(c1)):
        if c1[i].isnumeric():
            c11 += c1[i]
    c12 = c1[i:]
    c21 = ""
    for i in range(len(c2)):
        if c2[i].isnumeric():
            c21 += c2[i]
    c22 = c2[i:]
    if int(c11) < int(c21):
        return True
    elif int(c11) == int(c21) and c12 < c22:
        return True
    else:
        return False

def less(student1, student2):
    """Returns True if student1 << student2.
    """
    if less_cl(student1[2], student2[2]):
        return True
    if student1[2] == student2[2] and student1[0] < student2[0]:
        return True
    else:
        return False

def solve(lst):
    n = len(lst)
    for j in range(n, 1, -1):
        pos = 0
        for i in range(j):
            if not less(lst[i], lst[pos]):
                pos = i
        lst[pos], lst[j - 1] = lst[j - 1], lst[pos]


if __name__ == "__main__":
    lst = []
    am = int(input())
    for i in range(am):
        student = []
        for j in range(4):
            temp = str(input())
            student.append(temp)
        lst.append(student)
    solve(lst)
    for student in lst:
        print(" ".join([student[2], student[0], student[1], student[3]]))