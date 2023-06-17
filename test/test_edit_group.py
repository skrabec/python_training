from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("test", "test", "teeest"))
    app.session.logout()


def test_modify_first_group_name(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group_name(Group("modified_group_name"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group_header(Group(header="modified_group_header"))
    app.session.logout()
