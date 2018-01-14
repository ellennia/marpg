class Species():
    name = ''
    description = ''

    def __init__(self, name, description):
        self.name = name
        self.description = description

def get_species():
    human =  Species('Human','Intelligent primates')
    zeta =   Species('Zeta','Gray aliens')
    hybrid = Species('Hybrid', 'Human and zeta combined')
    reptil = Species('Reptilian', 'Spooky shit + scales')
    all_species = [human, zeta, hybrid, reptilian]
    return all_species

def get_species_names():
    names = []
    species = get_species()
    for specie in species:
        names.append(specie.name)
    return names
