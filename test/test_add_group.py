# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group("test", "test", "teeest"))


def test_add_empy_group(app):
    app.group.create(Group("", "", ""))
