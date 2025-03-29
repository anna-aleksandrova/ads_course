def convert(expr: str):
    stack = []
    op = {"+", "-", "*", "/"}
    for el in expr[::-1]:
        if el not in op:
            stack.append((el, ""))
        else:
            a, op1 = stack.pop()
            b, op2 = stack.pop()
            if (op1, op2) == ("", ""):
                stack.append((a+el+b, el))

            elif el == "+":
                stack.append((a+el+b, el))

            elif el == "-":
                if op2 == "-" or op2 == "+":
                    b = "(" + b + ")"
                stack.append((a+el+b, el))

            elif el == "*":
                if op1 == "+" or op1 == "-":
                    a = "(" + a + ")"
                if op2 == "+" or op2 == "-":
                    b = "(" + b + ")"
                stack.append((a+el+b, el))

            elif el == "/":
                if op1 == "+" or op1 == "-":
                    a = "(" + a + ")"
                if op2 != "":
                    b = "(" + b + ")"
                stack.append((a+el+b, el))
            else:
                pass
    res = stack.pop()[0]
    return res


if __name__ == "__main__":
    expr = input()
    print(convert(expr))
    
