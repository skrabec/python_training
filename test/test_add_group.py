# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("test", "test", "teeest"))
    app.session.logout()


def test_add_empy_group(app):
    app.session.logout()
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
