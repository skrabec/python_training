# -*- coding: utf-8 -*-
import unittest

import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="ttl",
                               company="cmp", address="adr1", home="111111", mobile="222222", work="333333",
                               fax="444444",
                               email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com",
                               homepage="www.hopg.com", bday="7", bmonth="July", byear="1977",
                               aday="10", amonth="October", ayear="2010", address2="adr2", phone2="555555",
                               notes="test"))
    app.session.logout()
