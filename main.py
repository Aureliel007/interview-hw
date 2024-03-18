class Stack():

    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

def check_brackets(string):
    
    brackets = {
    ')': '(',
    '}': '{',
    ']': '['
}
    stack_1 = Stack()
    for char in string:
        if char in '[({':
            stack_1.push(char)
        if char in ']})':
            prev_char = stack_1.peek()
            if brackets[char] == prev_char:
                stack_1.pop()
            else:
                stack_1.push(char)
    if stack_1.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

print(check_brackets('(((([{}]))))'))
print(check_brackets('[([])((([[[]]])))]{()}'))
print(check_brackets('{{[(])]}}'))
print(check_brackets('[[{())}]'))
print(check_brackets('(((d([{f}])g))d)'))
