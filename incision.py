'''
    /incision.py
    Mars RPG - Main File

    Structure:
        - Imports
        - Constants {Species, Attributes, Skills}
        - Classes
        - Global methods
        - Where code execution begins
'''

import books/scenes
from books/inventories import *        # Provides code for inventories
from books/species_loader import *   # Manages species XML files.
import books/default_scenes          # Manages scene XML files.

''' Constants '''
# Species information
species_names = ['human', 'zeta', 'hybrid', 'reptilian']

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
''' End constants '''

''' Classes '''
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

class NPC:
    def __init__(self, name):
        self.name = name

    def say(self, string):
        print(self.name + ':: ' + string)

    def request_answer(self, string):
        self.say(string)
        return ask()

    def capture_interaction(character):
        pass

    def ellipse(self):
        print('...')

class Attributizer(NPC):
    def __init__(self):
        self.name = "ATTRIBUTION MACHINE"
    
    def attributes(self, character):
        self.say(str(starting_attribute_points) + ' points to distribute ====')
        remaining_points = starting_attribute_points
        for attribute in attribute_names:
            correct_value = False
            while correct_value == False:
                try:
                    points = int(raw_input(' - How many points in attribute \'' + attribute + '\': '))
                    remaining_points -= points
                    character.attributes[attribute] = points
                    print('    ' + str(remaining_points) + ' remaining')
                    correct_value = True
                except:
                    print('Not a number!')
        print('-------------------------')
        self.say('Just a review of what you\'ve chosen:')
        for attribute in attribute_names:
            print(' - attribute \'' + attribute + '\': ' + str(character.attributes[attribute]))
        print('-------------------------')
        return self.request_answer('Is this what you want? y/n. You can\'t change this later!')
    
    def capture_interaction(self, character):
        clear()
        choice = 'n'
        while choice == 'n':
                choice = self.attributes(character)
        self.say('...')
        self.say('Great! Let\'s take a look at your skills.')
        remaining_points = starting_skill_points
        for skill_name in skill_names:
            print('skill: ' + skill_name + ': ' + str(character.skills[skill_name]))
        choice = request_answer('Is this correct? Skill detector is in alpha and it\'s assessments can be modified by selecting no. y/n')
        while choice == 'n':
            configure_char_skills(character)
            for skill_name in skill_names:
                print('skill: ' + skill_name + ': ' + str(character.skills[skill_name]))
            choice = request_answer('Is this what you want? y/n')
        clear()

''' End classes'''

''' Global methods '''
# Clears the screen (by printing 100 blank lines)
def clear():
    for n in range(0, 100):
        print('')

# Asks a question, by printing the query, and then returns the player's answer.
def request_answer(query):
    print(query)
    return ask()

def ask():
    return raw_input('> ')

# Wait for the player to press enter to continue.
def wait():
    return raw_input('')
# Detect whether or not there is a save file already existing.
# End savegame stuff

def configure_char_skills(character):
    skill = request_answer('Which skill would you like to increase?')
    points = int(request_answer('By how many points?'))
    character.skills[skill] += points

def character_creation_sequence():
    guard = NPC('Guard')
    attributizer = Attributizer() # (NPC)
    guard.say('Hello, welcome to Mars Spaceport I-11.')
    guard.say('We\'re sorry for the inconvienience, but we\'ll have to ask you a')
    guard.say('few questions before you can be allowed through the gate.')
    name = guard.request_answer('Firstly, what is your name? No nicknames please.')
    guard.say('' + name + '... ' + name + '...  {typing} ah, here we go, found your record.')
    guard.say('Gotcha. Now I have just a few more questions to verify who you are.')
    guard.say('What species are you a member of? Human, zeta, hybrid, or reptilian?')
    guard.say('Using the Mars Central Core\'s species definitions, of course.')
    species_chosen = ask()
    while species_chosen not in species_names:
        guard.say('That... isn\'t an option. That\'s beurocracy for ya.')
        guard.say('You have to be either a human, zeta, hybrid, or reptillian.')
        guard.say('Surely you must be one of the above?')
        species_chosen = ask()
    guard.say('Alright, a {}. That was a bit obvious but I just needed to make certain.'.format(species_chosen))
    character = Character(name, species_chosen)
    guard.say('...') 
    guard.say('Now for a medical checkup. Stare directly into the attributizer.')
    guard.say('Let it determine your physical and mental strengths.')
    guard.say('...') 
    print('{look into attributizer (press enter)}')
    wait()
    attributizer.capture_interaction(character)
    print(' ================ REPORT ===================== ')
    print(' MCC Boarding Report 10/22/2436 MCT            ')
    print('')
    print('= Passenger name: {}'.format(character.name))
    print('= Passenger species: {}'.format(character.species)) 
    print('= Origin port: Central Elonia')
    print('= Destination port: Elyptica')
    print('')
    print('= Passenger attribute report:')
    for attribute_name in attribute_names:
        print('    = ' + attribute_name + ': ' + str(character.attributes[attribute_name]))
    print('= Passenger skill report:')
    for skill_name in skill_names:
        print('    = ' + skill_name + ': ' + str(character.skills[skill_name]))
    print('')
    print('Approved by ATRS (Automatic Terrorism Reduction System): yes')
    print('Flight boarding to commense at 14:36.')
    print(' ==============================================')
    print('')
    guard.say('Alright... well, that\'s that.')
    guard.say('This all passes by the way. You are free to board your shuttle.')
    guard.say('Enjoy!')
    print('...')
    print('{board shuttle}')
    wait()
    print('...')
    print('...')
    return character
''' /Global methods '''

''' Start running '''
character = None
does_character_exist = False#detect_save()

if not does_character_exist:
    print (' -- ERROR -- ')
    yn = request_answer('No character found. Create character? y/n')
    if yn == 'y':
        clear()
        character = character_creation_sequence()
        clear()
    else:
        filename = request_answer('Type filename of existing save...')
        load_savegame(filename)

current_scene = default_scenes.get_intro()
first_message = True
continue_loop = True
# Game loop
while continue_loop:
    if first_message:
        current_scene.print_messages()
    else:
        print(current_scene.get_ambient())
    first_message = False

    print('Location: {} | Money {} | Health {}'.format(current_scene.get_name(), str(5), str(10)))
    action = request_answer('')

    if action == '?':
        print 'You could try looking around.'

        character.give_item(Stack('goggle', 2))
    elif action == '':
        print 'You think now might be the time for action.'
    elif action == 'quit':
        continue_loop = False
    else:
        print 'You\'re not really sure what that means.'
print('Quitting...')
''' End runstrip '''


