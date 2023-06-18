from model.group import Group


def test_add_group(app):
    app.group.edit_first_group(Group("test", "test", "teeest"))


def test_modify_first_group_name(app):
    app.group.modify_first_group_name(Group("modified_group_name"))


def test_modify_first_group_header(app):
    app.group.modify_first_group_header(Group(header="modified_group_header"))
