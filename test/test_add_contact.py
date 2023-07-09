# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="2", lastname="3", nickname="nn", title="ttl",
                      company="cmp", address="adr1", home_phone="111111", mobile_phone="222222", work_phone="333333",
                      fax="444444",
                      email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com",
                      homepage="www.hopg.com", bday="7", bmonth="July", byear="1977",
                      aday="10", amonth="October", ayear="2010", address2="adr2", secondary_phone="555555",
                      notes="test")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
