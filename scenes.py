class Scene:
    messages = []
    name = 'Default Environment'
    ambient = ''

    def __init__(self, name, messages, ambient):
        self.name = name
        self.messages = messages
        self.ambient = ambient

    def __init__(self, name, messages, ambient, adjacents):
        self.name = name
        self.messages = messages
        self.ambient = ambient
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

