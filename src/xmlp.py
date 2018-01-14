'''
    Manages the loading of XML files in scripts/
'''

import os
from scenes import *
from shop import *
from species import *
import xml.etree.ElementTree # XML

def get_scripts():
    map_map = {}

    script_map = {}
    npc_map = {}
    scene_map = {}
    species_map = {}

    map_map['script'] = script_map
    map_map['npc'] = npc_map
    map_map['scene'] = scene_map
    map_map['species'] = species_map

    # Get list of scripts in scripts/
    scripts = [f for f in os.listdir('../scripts/') if f.endswith('.xml')]

    for script in scripts:
        root = xml.etree.ElementTree.parse('../scripts/' + script).getroot()

        if root.attrib['class'] == 'script':
            script_map[root.attrib['name']] = root.text
        elif root.attrib['class'] == 'scene':
            print 'SCENES'
            scenes = load_scenes(root)
            for scene in scenes:
                print scene
        elif root.attrib['class'] == 'npc':
            npcs = load_npcs(root)
        elif root.attrib['class'] == 'species':
            print 'SPECIES'
            species = load_species(root)
            for specie in species:
                print specie

    return map_map

def load_species(root):
    species_map = {}

    for species in root:
        basestat_map = {}

        description = species.find('description').text
        basestats = species.find('basestats')

        for stat in basestats.findall('stat'):
            basestat_map[stat.attrib['name']] = stat.text

        new_species = Species(species.attrib['name'], description)
        species_map[new_species.name] = new_species

    return species_map

def load_npcs(root):
    return None

def load_scenes(root):
    scenemap = {}
    for scene in root:
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

            market = scene.find('market')
            if not market == None:
                items = []
                style = market.attrib['style']
                item_tags = market.findall('item')
                for item in item_tags:
                    #print 'loaded item : ' + item.attrib['name'] + ' ' + item.attrib['description']
                    se = ShopEntry(item.attrib['name'], item.attrib['description'], .50)
                    items.append(se)
                shop = Shop(items)
                the_scene.shop = shop

            scenemap[game_tag] = the_scene
            scenemap[game_tag].scene_type = scene_type
    return scenemap

get_scripts()
