import xml.etree.ElementTree # XML

scenes = xml.etree.ElementTree.parse('scenes.xml').getroot()
for scene in scenes:
    name = scene.find('name').text
    summary = scene.find('summary').text
    adjacent = scene.find('adjacent')
    adjtags = adjacent.findall('tag')

    print('Scene: {}'.format(name))
    print('     Summary: {}'.format(summary))
    print('     Adjacent to:')
    for tag in adjtags:
        print('         ' + tag.text)
