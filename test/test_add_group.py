# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_new_group(Group("test", "test", "teeest"))
    app.logout()


def test_add_empy_group(app):
    app.login("admin", "secret")
    app.create_new_group(Group("", "", ""))
    app.logout()

