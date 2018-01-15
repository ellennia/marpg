class WorldGraph():
    aa = {}
    scenes = []

    def __init__(self, d):
        for scene in d:
            s = d[scene]


    def add(self, scene):
        aa[scene.name] = scene
        scenes.append(scene)

    def get_adjacents(self, scene):
        return [scene.get_adjacent() and adjacent for adjacent in scenes if adjacent.is_adjacent(scene)]
