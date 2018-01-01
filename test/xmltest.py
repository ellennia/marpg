import xml.etree.ElementTree

scenes = xml.etree.ElementTree.parse('../scripts/scenes.xml').getroot()
for scene in scenes:
    name = scene.find('name').text
    summary = scene.find('summary').text

    adjacent = scene.find('adjacent')
    adjacent_tags = adjacent.findall('tag')

    print('Scene: {}'.format(name))
    print('     Summary: {}'.format(summary))
    print('     Adjacent to:')
    for tag in adjacent_tags:
        print('         ' + tag.text)
