from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                           nickname="nickname", title="ttl",
                               company="cmp", address="adr1", home="111111", mobile="222222", work="333333",
                               fax="444444",
                               email="mail@mail.com", email2="mail2@mail.com", email3="mail3@mail.com",
                               homepage="www.hopg.com", bday="7", bmonth="July", byear="1977",
                               aday="10", amonth="October", ayear="2010", address2="adr2", phone2="555555",
                               notes="test"))
    app.session.logout()
