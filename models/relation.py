class Relation(object):
    """Class modeling teacher and student relations between KA users"""
    def __init__(self):
        super(Relation, self).__init__()
        self.teachers = set()
        self.students = set()
