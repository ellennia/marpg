class Inventory:
    stacks = []

    def add_stack(self, stack):
        found = False
        for fs in self.stacks:
            if stack.name == fs.name:
                fs.amount += stack.amount
                found = True
                
        if found == False:
            self.stacks.append(stack)

    def contains_stack(self, stack):
        found = False
        for fs in self.stacks:
            if stack.name == fs.name:
                if stack.amount <= fs.amount:
                    found = True
        return found
    
    def remove_stack(self, stack):
        if(self.contains_stack(stack)):
            for fs in self.stacks:
                if stack.name == fs.name:
                    fs.amount -= stack.amount

    def print_inv(self):
        for item in self.stacks:
            item.out()

class Stack:
        def __init__(self, name, amount):
            self.name = name
            self.amount = amount

        def out(self):
            print '{} of {}'.format(str(self.amount), self.name)


