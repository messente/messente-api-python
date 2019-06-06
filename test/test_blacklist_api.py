# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import messente_api
from messente_api.api.blacklist_api import BlacklistApi  # noqa: E501
from messente_api.rest import ApiException


class TestBlacklistApi(unittest.TestCase):
    """BlacklistApi unit test stubs"""

    def setUp(self):
        self.api = messente_api.api.blacklist_api.BlacklistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_to_blacklist(self):
        """Test case for add_to_blacklist

        Adds a phone number to the blacklist  # noqa: E501
        """
        pass

    def test_delete_from_blacklist(self):
        """Test case for delete_from_blacklist

        Deletes a phone number from the blacklist  # noqa: E501
        """
        pass

    def test_fetch_blacklist(self):
        """Test case for fetch_blacklist

        Returns all blacklisted phone numbers  # noqa: E501
        """
        pass

    def test_is_blacklisted(self):
        """Test case for is_blacklisted

        Checks if a phone number is blacklisted  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
