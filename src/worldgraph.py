class WorldGraph():
    aa = {}
    scenes = []

    def __init__(self, d):
        print 'Generating World Graph..'

        print len(d), 'scenes {nodes} (7 counting DEFNODE)'
        
        po = 'DEFNODE, '
        for scene in d:
            s = d[scene]
            po += scene + ', '

        print '{', po[:-2], '}'

        xml_adjacents = [adj for scene in d for adj in d[scene].adjacents]
        print len(xml_adjacents), 'adjacencies {edges} denoted in tags'

    def add(self, scene):
        aa[scene.name] = scene
        scenes.append(scene)

    def get_adjacents(self, scene):
        return [scene.get_adjacent() and adjacent for adjacent in scenes if adjacent.is_adjacent(scene)]
