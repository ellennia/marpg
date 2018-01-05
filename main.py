'''
    /main.py
    Mars RPG - Main File

    Uses jinja2 for templating

    Structure:
        - Imports
        - Constants {Species, Attributes, Skills}
        - Classes
        - Global methods
        - Where code execution begins
'''

import xml.etree.ElementTree # XML
from jinja2 import Template

from character import *
from scenes import *

''' Constants '''
# Species information
species_names = ['human', 'zeta', 'hybrid', 'reptilian']

''' Classes '''
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

def get_script(name):
    with open(name) as f:
        template = Template(f.read())
    return template

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
    guard.say("Using the Mars Central Core's species definitions, of course.")
    species_chosen = ask()
    while species_chosen not in species_names:
        guard.say("That... isn't an option. That's buerocracy for ya.")
        guard.say('You have to be either a human, zeta, hybrid, or reptillian.')
        guard.say('Surely you must be one of the above?')
        species_chosen = ask()
    guard.say('Alright, a {}. That was a bit obvious but I just needed to make certain.'.format(species_chosen))
    character = Character(name, species_chosen)
    guard.say('...') 
    guard.say('Now for a medical checkup. Stare directly into the attributizer.')
    guard.say('Let it determine your physical and mental strengths.')
    guard.say('...') 

    # Be 'questioned' by Attributizer
    print('{look into attributizer (press enter)}')
    wait()
    attributizer.capture_interaction(character)
    # Render the Passenger Report in scripts/cc_report.dat
    attribute_report = ''
    for attribute_name in attribute_names: attribute_report += '    = ' + attribute_name + ': ' + str(character.attributes[attribute_name]) + '\n'
    skill_report = ''
    for skill_name in skill_names: skill_report += '    = ' + skill_name + ': ' + str(character.skills[skill_name]) + '\n'
    report = get_script('scripts/cc_report.dat').render(
            character_name = character.name, 
            character_species = character.species, 
            attribute_report = attribute_report, 
            skill_report = skill_report)
    print report

    guard.say("Alright... well, that's that.")
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
does_character_exist = False #detect_save()

if not does_character_exist:
    print (' -- ERROR -- ')
    yn = request_answer('No character found. Create character? y/n/p')
    if yn == 'y':
        clear()
        character = character_creation_sequence()
        clear()
    elif yn == 'p':
        try:
            print('Ah, the old dev cheat.')
            print('Have a pre-made hardcoded character')
            character = Character('Premade', 'human')
            clear()
        except:
            print('wah')
    else:
        filename = request_answer('Type filename of existing save...')
        load_savegame(filename)

first_message = True
continue_loop = True

'''
    This is the game loop.
    It runs as long as 'continue_loop' is set to True.

    The first thing it does is check if a character is already made.
        If not, then it asks if you want to load a save file, or create a character.
            If you want to load a save, it will ask for the file name.
            If you want to create a character, it goes to the character creation wizard.
        Once a character is made, you are dropped into the starting scene.
    If your character is from a save file, it is the last scene you were in.
'''

'''
    Loads scenes from the scenes.xml file
'''
scenes = xml.etree.ElementTree.parse('scripts/scenes.xml').getroot()
scenemap = {}
for scene in scenes:
    scene_type = scene.attrib['type']
    name = scene.find('name').text
    if name == 'GAG': # Is gag 'location', only designed to trigger a joke in command prompt
        game_tag = scene.find('tag').text
        gagtext = scene.find('gagtext').text
        scenemap[game_tag] = Scene(name, gagtext, '', game_tag, [])
        scenemap[game_tag].scene_type = scene_type
    else:
        summary = scene.find('summary').text.split('\n')
        game_tag = scene.find('tag').text
        ambient = scene.find('ambient').text
        adjacent = scene.find('adjacent')
        adjtags = adjacent.findall('tag')
        adjacent_scenes = [tag.text for tag in adjtags]
        the_scene = Scene(name, summary, ambient, game_tag, adjacent_scenes)
        scenemap[game_tag] = the_scene
        scenemap[game_tag].scene_type = scene_type
current_scene = scenemap['terminal_21']
# End scene loading

while continue_loop:
    if first_message:
        print('     Current location: {}'.format(current_scene.get_name()))
        print('                       Money: {}, Health: {}'.format(str(5), str(10)))
        current_scene.print_messages()
    else:
        print('::       \~  ' + current_scene.get_ambient()+ '  \~')
    first_message = False

    action = request_answer('')
    print('')

    '''
        Actions:
        The things you can do every turn.

        Current actions:
            bearings: Tells you about your character's surroundings
            move: Has your character move to a different, adjacent scene.

            quit: Ends the game
            ?: Makes a suggestion.

            {nothing}: Suggests you do something.
            {the final nothing}: Expresses exasperation.
    '''
    if len(action) == 0:
        print('Typing something might be recommended if you wish to play.')
    else:
        fragments = action.split()
        command = fragments[0]

        if command == '?':
            print 'You could try looking around.'
            character.give_item(InventoryStack('goggle', 1))

        elif command == 'bearings':
            print 'You take a deep breath and look around, seeing what opportunities are currently available to you.'
            for adjacents in current_scene.adjacents:
                print('You can see a {}'.format(adjacents))

        elif command == 'move':
            location = fragments[1]
            if location == current_scene.tag:
                    print('The funny thing was, you were already there.')
            elif location in scenemap:
                if scenemap[location].name == 'GAG':
                    print scenemap[location].messages
                else:
                    current_scene = scenemap[location]
                    print('    Current location: {} | Money: {} | Health {}'.format(current_scene.get_name(), str(character.currency), str(character.health)))
                    current_scene.print_messages()
            else:
                print("You can't find anything that resembles that around you.")

        elif command == 'shop':
            if current_scene.scene_type == 'shop':
                print('The machine sputters, uncertain of how to respond.')
            else:
                print('You attempt to conduct a transaction with the air. It is not very effective.')
            
        elif command == 'quit':
            continue_loop = False
        elif command == '':
            print 'You think now might be the time for action.'
        else:
            print 'You\'re not really sure what that means.'
    print ''

print('Quitting...')
''' End runstrip '''



