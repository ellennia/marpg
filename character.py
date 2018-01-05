# Attributes
starting_attribute_points = 40
attribute_names = [
        'strength', 
        'perception', 
        'endurance', 
        'charisma' ,
        'intelligence' ,
        'agility' ,
        'luck'
        ]

# Skills
starting_skill_points = 5
skill_names = [
        'speech', 
        'unarmed', 
        'melee weapons', 
        'marksman', 
        'stealth', 
        'throwing', 
        'crafting', 
        'smithing', 
        'piloting',
        'engineering',
        'biology',
        'programming',
        'chemistry',
        'psionics'
        ]

class Inventory():
    stacks = []

    def add_stack(self, stack):
        found = False
        for fs in self.stacks:
            if stack.name == fs.name:
                fs.amount += stack.amount
                found = True
                
        if found == False:
            self.stacks.append(stack)

    def remove_stack(self, stack):
        if(self.contains_stack(stack)):
            for fs in self.stacks:
                if stack.name == fs.name:
                    fs.amount -= stack.amount

    def contains_stack(self, stack):
        found = False
        for fs in self.stacks:
            if stack.name == fs.name:
                if stack.amount <= fs.amount:
                    found = True
        return found

    def print_inv(self):
        for item in self.stacks:
            item.out()

class InventoryStack:
        def __init__(self, name, amount):
            self.name = name
            self.amount = amount

        def out(self):
            print '{} of {}'.format(str(self.amount), self.name)

class Character:
    name = ''
    species = ''
    attributes = {}
    skills = {}
    inventory = Inventory()
    currency = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species

        for name in attribute_names:
            self.attributes[name] = 0

        for name in skill_names:
            self.skills[name] = 1
 
    ''' health points '''
    def get_hp():
        default_health = 50
        return default_health + 10 * get_attribute('endurance')

    ''' mental health points '''
    def get_mp(self):
        default_health = 50
        return default_health + 10 * get_attribute('intelligence')

    ''' action points '''
    def get_ap(self):
        return get_attribute('agility')

    ''' value of attributes (SPECIAL) '''
    def get_attribute(self, att_name):
        return int(attributes[att_name])

    def give_item(self, stack):
        print('You have received a stack of {} {}s.'.format(str(stack.amount),stack.name))
        self.inventory.add_stack(stack)

    def get_currency(self):
        return self.currency
