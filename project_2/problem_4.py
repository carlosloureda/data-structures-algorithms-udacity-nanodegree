"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such.

Where User is represented by str representing their ids.

"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

"""
Write a function that provides an efficient look up of whether the user is in a group.
"""


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()

    if len(users) > 0:
        if user in users:
            return True

    groups = group.get_groups()
    for group in groups:
        return is_user_in_group(user, group)

    return False


def test():

    assert is_user_in_group(user='sub_child_user', group=parent) == True
    assert is_user_in_group(user='sub_child_user', group=child) == True
    assert is_user_in_group(user='sub_child_user', group=sub_child) == True

    assert is_user_in_group(user='parent_user', group=parent) == False
    assert is_user_in_group(user='child_user', group=parent) == False

    print(is_user_in_group(user='sub_child_user', group=parent))
    # True

    # EDGE CASES

    assert is_user_in_group(user='', group=parent) == False
    print(is_user_in_group(user='', group=parent))
    # False

    assert is_user_in_group(user='', group=child) == False
    print(is_user_in_group(user='', group=child))
    #  False

    print("> First tests passed")


test()
