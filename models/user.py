class User(object):
    """Generic KA User Class"""
    def __init__(self, name, userid, version):
        super(User, self).__init__()
        self.id = userid
        self.name = name
        self.version = version

    def __str__(self):
        return str({"id": self.id, "name": self.name})
