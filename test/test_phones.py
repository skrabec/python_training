import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_home_page(0)
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.mobile_number, contact.work_number, contact.secondary_number]))))