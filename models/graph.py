from user import User
from relation import Relation

"""Class modeling Khan Academy learner-teacher graph"""
class Graph(object):
    def __init__(self):
        super(Graph, self).__init__()
        self.v = {}
        self.e = {}

    """Adds a user to the learner-teacher graph"""
    def add_user(self, username, userid, version):
        user = User(username, userid, version)
        self.v[username] = user
        self.e[username] = {'students': {}, 'teachers': {}}

    """Connect a student and teacher in the KA graph"""
    def connect(self, teacher, student):
        teacher = self.v[teacher]
        student = self.v[student]
        edge = Relation(teacher.name, student.name)
        self.e[teacher.name]['students'][student.name] = edge
        self.e[student.name]['teachers'][teacher.name] = edge

    """Deletes a user from the KA graph and eliminates
    all existing relationships involving the user"""
    def delete_user(self, username):
        ue = self.e[username]
        for sid in ue['students']:
            se = self.e[sid]['teachers']
            del se[username]
        for tid in ue['teachers']:
            te = self.e[tid]['students']
            del te[username]
        del self.e[username]
        del self.v[username]
