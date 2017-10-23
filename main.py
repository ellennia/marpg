''' Constants '''
races = ['human', 'zeta', 'hybrid', 'reptilian']
attribute_names = ['strength', 'perception', 'endurance', 'charisma' ,'intelligence' ,'agility' ,'luck']
skill_names = ['speech', 'unarmed', 'melee weapons', 'marksman', 'stealth', 'throwing', 'crafting', 'smithing', 'piloting','engineering','biology','programming','chemistry','psionics']
starting_special_points = 40
starting_skill_points = 5

class Character:
    name = ''
    race = ''
    attributes = {}
    skills = {}

    def __init__(self, name, race):
        self.name = name
        self.race = race

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

class NPC:
    def __init__(self, name):
        self.name = name

    def say(self, string):
        print(self.name + ':: ' + string)

class Species():
    name = ''
    description = ''

    def __init__(self):
        pass

''' Global methods '''
def clear():
    for n in range(0, 100):
        print('')

def request_answer(query):
    print(query)
    return raw_input('> ')

# Savesgame stuff
def detect_save():
    return False

def load_savegame(filename):
    pass
# End savegame stuff

def configure_char_skills(character):
    skill = request_answer('Which skill would you like to increase?')
    points = int(request_answer('By how many points?'))
    character.skills[skill] += points

def configure_char_attributes(character):
    print('ATTRIBUTOR:: ' + str(starting_special_points) + ' points to distribute ====')

    remaining_points = starting_special_points
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
    print('ATTIBUTOR:: Just a review of what you\'ve chosen:')
    for attribute in attribute_names:
        print(' - attribute \'' + attribute + '\': ' + str(character.attributes[attribute]))
    print('-------------------------')

def create_character():
    guard = NPC('Guard')

    guard.say('Hello, welcome to Mars Spaceport I-11.')
    guard.say('We\'re sorry for the inconvienience, but we\'ll have to ask you a')
    guard.say('few questions before you can be allowed through the gate.')

    name = request_answer('Guard:: Firstly, what is your name? No nicknames please.')
    guard.say('' + name + '... ' + name + '...  {typing} ah, here we go, found your record.')
    guard.say('Gotcha. Now I have just a few more questions to verify who you are.')

    guard.say('What species are you a member of? Human, zeta, hybrid, or reptillian?')
    guard.say('Using the Mars Central Core\'s species definitions, of course.')
    
    race_chosen =  raw_input('> ')
    while race_chosen not in races:
        guard.say('That... isn\'t an option. That\'s beurocracy for ya.')
        guard.say('You have to be either a human, zeta, hybrid, or reptillian.')
        guard.say('Surely you must be one of the above?')
        race_chosen = raw_input('> ')

    guard.say('Alright, a ' + race_chosen + '. That was a bit obvious but I just needed to make certain.')

    print('Guard:: ...') 
    print('Guard:: Now for a medical checkup. Stare directly into the attributizer.')
    print('Guard:: Let it determine your physical and mental strengths.')
    print('...')
    print('{look into attributizer (press enter)}')
    raw_input('')

    character = Character(name, race_chosen)

    clear()
    choice = 'n'
    while choice == 'n':
        configure_char_attributes(character)
        choice = request_answer('ATTRIBUTOR:: Is this what you want? y/n. You can\'t change this later!')

    print('ATTRIBUTOR:: ...')
    print('ATTRIBUTOR:: Great! Let\'s take a look at your skills.')
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

    print(' ================ REPORT ===================== ')
    print(' MCC Boarding Report 10/22/2436 MCT            ')
    print('')
    print('= Passenger name: {}'.format(character.name))
    print('= Passenger species: {}'.format(character.race))
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
    print('Guard:: Alright... well, that\'s that.')
    print('Guard:: This all passes by the way. You are free to board your shuttle.')
    print('Guard:: Enjoy!')
    print('...')
    print('{board shuttle}')
    raw_input('')

    print('...')
    print('...')
''' /Global methods '''

''' Start running '''
does_character_exist = detect_save()
character = None

if not does_character_exist:
    print (' -- ERROR -- ')
    yn = request_answer('No character found. Create character? y/n')
    if yn == 'y':
        clear()
        character = create_character()
        clear()
    else:
        filename = request_answer('Type filename of existing save...')
        load_savegame(filename)

while True:
    print(':: You stumble out of your shuttle into the Elyptica spaceport.')
    print(':: Damn, those shuttles could be a bit smoother.')
    print(':: You spent all your cash on that shuttle, barring a tiny bit you could')
    print(':: spend on some various little things. Particularly some food.')

    print('Location: {} - Money {} - Health {}')
    action = request_answer('')

''' End runstrip '''



