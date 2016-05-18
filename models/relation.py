class Relation(object):
    """Class modeling teaching relations between KA users"""
    def __init__(self, teacher, student):
        super(Relation, self).__init__()
        self.t = teacher
        self.s = student
