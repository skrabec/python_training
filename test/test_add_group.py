# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("test", "test", "teeest"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empy_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
