from scenes import *

def get_intro():
    fragments = ['','','','']
    fragments[0] = "You stumble out of your shuttle into the Elyptica spaceport."
    fragments[1] = "Damn, those shuttles could be a bit smoother."
    fragments[2] = "You spent all your cash on that shuttle, you only have a small"
    fragments[3] = "amount left to spend on some things."
    ambient = 'You shuffle restlessly under the somewhat dim electric lights.'
    elyptica_intro = Scene('Elyptica Terminal 21', fragments, ambient)
    return elyptica_intro
