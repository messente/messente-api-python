# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import messente_api
from messente_api.api.contacts_api import ContactsApi  # noqa: E501
from messente_api.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = messente_api.api.contacts_api.ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_contact_to_group(self):
        """Test case for add_contact_to_group

        Adds a contact to a group.  # noqa: E501
        """
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Creates a new contact.  # noqa: E501
        """
        pass

    def test_delete_contact(self):
        """Test case for delete_contact

        Deletes a contact.  # noqa: E501
        """
        pass

    def test_fetch_contact(self):
        """Test case for fetch_contact

        Lists a contact.  # noqa: E501
        """
        pass

    def test_fetch_contact_groups(self):
        """Test case for fetch_contact_groups

        Lists groups of a contact.  # noqa: E501
        """
        pass

    def test_fetch_contacts(self):
        """Test case for fetch_contacts

        Returns all contacts.  # noqa: E501
        """
        pass

    def test_remove_contact_from_group(self):
        """Test case for remove_contact_from_group

        Removes a contact from a group.  # noqa: E501
        """
        pass

    def test_update_contact(self):
        """Test case for update_contact

        Updates a contact.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
