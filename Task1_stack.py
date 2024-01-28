class Stack:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.container[-1] 

    def size(self):
        return len(self.container)


def check_brackets(string):
    bracket_stack = Stack()
    ch1, ch2, ch3 = 0, 0, 0
    for i in string:
        if i in '(':
            bracket_stack.push(i)
            ch1 += 1
        elif i in ')':
            if bracket_stack.isEmpty() or ch1 == 0:
                return "Несбалансированно"
            bracket_stack.pop()
            ch1 -= 1

        if i in '{':
            bracket_stack.push(i)
            ch2 += 1
        elif i in '}':
            if bracket_stack.isEmpty() or ch2 == 0:
                return "Несбалансированно"
            bracket_stack.pop()
            ch2 -= 1

        if i in '[':
            bracket_stack.push(i)
            ch3 += 1
        elif i in ']':
            if bracket_stack.isEmpty() or ch3 == 0:
                return "Несбалансированно"
            bracket_stack.pop()
            ch3 -= 1

    return "Сбалансированно"
            

print(check_brackets('(((([{}]))))'))
print(check_brackets('[([])((([[[]]])))]{()}'))
print(check_brackets('{{[()]}}'))
print(check_brackets('}{}'))
print(check_brackets('{{[(])]}}'))
print(check_brackets('[[{())}]'))