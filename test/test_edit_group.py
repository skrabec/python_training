from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test")))
    app.group.edit_first_group(Group("test", "test", "teeest"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test")))
    app.group.modify_first_group_name(Group("modified_group_name"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create((Group(name="test")))
    app.group.modify_first_group_header(Group(header="modified_group_header"))
