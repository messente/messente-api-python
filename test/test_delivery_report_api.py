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
from messente_api.api.delivery_report_api import DeliveryReportApi  # noqa: E501
from messente_api.rest import ApiException


class TestDeliveryReportApi(unittest.TestCase):
    """DeliveryReportApi unit test stubs"""

    def setUp(self):
        self.api = messente_api.api.delivery_report_api.DeliveryReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_delivery_report(self):
        """Test case for retrieve_delivery_report

        Retrieves the delivery report for the Omnimessage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
