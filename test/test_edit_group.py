from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("test", "test", "teeest"))
    app.session.logout()
