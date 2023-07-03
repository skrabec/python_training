from random import randrange

from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test")))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified_group_name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_modify_first_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create((Group(name="test")))
#     app.group.modify_first_group_header(Group(header="modified_group_header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
