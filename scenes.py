class Scene:
    messages = []
    name = 'Default Environment'
    ambient = ''
    scene_type = 'default'

    def __init__(self, name, messages, ambient, tag, adjacents):
        self.name = name
        self.messages = messages
        self.ambient = ambient
        self.tag = tag
        self.adjacents = adjacents

    def get_messages(self):
        return self.messages

    def get_name(self):
        return self.name

    def get_ambient(self):
        return self.ambient

    def print_messages(self):
        for message in self.messages:
            print ':: ' + message

    def summarize(self):
        print 'standard scene type 2, name: {}, tag: {}'.format(self.name, self.tag)
        self.print_messages()
        print 'Ambient: ' + self.ambient
        print 'Connected to:'
        for adjacent in self.adjacents:
            print '         ' + adjacent
        print '------------------------------------------------'

