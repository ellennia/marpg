import xml.etree.ElementTree

from scenes import *

scenes = xml.etree.ElementTree.parse('../scripts/scenes.xml').getroot()
for scene in scenes:
    scene_type = scene.attrib['type']

    if scene_type == 'standard':
        name = scene.find('name').text
        summary = scene.find('summary').text
        tag = scene.find('tag').text
        ambient = scene.find('ambient').text
        adjacents = scene.find('adjacent')
        scene = Scene(name, summary.split('\n'), ambient, tag, [adjtag.text for adjtag in adjacents]) 
        scene.summarize()
    if scene_type == 'standard2':
        name = scene.attrib['name']
        tag = scene.attrib['tag']
        ambient = scene.find('ambient').text
        adjacents = scene.find('adjacent')
        scene = Scene(name, scene.text.split('\n'), ambient, tag, [adjtag.text for adjtag in adjacents]) 
        scene.summarize()

