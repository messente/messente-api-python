# coding: utf-8

"""
    Messente Combined API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.0.1
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
