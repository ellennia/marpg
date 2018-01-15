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
            self.aa[s.tag] = s

        print '{', po[:-2], '}'

        xml_adjacents = [adj for scene in d for adj in d[scene].adjacents]
        print len(xml_adjacents), 'adjacencies {edges} denoted in tags'

    def add(self, scene):
        aa[scene.name] = scene
        scenes.append(scene)

    def get_adjacents(self, scene):
        return [scene.get_adjacent() and adjacent for adjacent in scenes if adjacent.is_adjacent(scene)]

    def route(self, frm, to):
        start = self.aa[frm]
        finish = self.aa[to]
        current = start
        visited = [start]
        chain = [start]

        print start.name, finish.name

        while current != finish:
            print 'current: ', current.name
            if len(current.adjacents) == 1: # You must only be able to turn around
                visited.append(current)
                chain.pop()
                current = chain[len(chain) - 1]
            else:
                adj = None

                for adjs in current.adjacents:
                    if not adjs == 'DEFNODE':
                        target = self.aa[adjs]
                        if not target in visited:
                            adj = target
                            break

                if adj == None:
                    current = start
                else:
                    chain.append(adj)
                    visited.append(current)
                    current = adj

        return chain




