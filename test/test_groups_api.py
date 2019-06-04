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
from messente_api.api.groups_api import GroupsApi  # noqa: E501
from messente_api.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = messente_api.api.groups_api.GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Creates a new group with the provided name  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Deletes a group  # noqa: E501
        """
        pass

    def test_fetch_group(self):
        """Test case for fetch_group

        Lists a group  # noqa: E501
        """
        pass

    def test_fetch_groups(self):
        """Test case for fetch_groups

        Returns all groups  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Updates a group with the provided name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
