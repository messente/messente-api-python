# coding: utf-8

"""
    Messente Combined API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ContactUpdateFields(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'title': 'str',
        'custom': 'str',
        'custom2': 'str',
        'custom3': 'str',
        'custom4': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company': 'company',
        'title': 'title',
        'custom': 'custom',
        'custom2': 'custom2',
        'custom3': 'custom3',
        'custom4': 'custom4'
    }

    def __init__(self, email=None, first_name=None, last_name=None, company=None, title=None, custom=None, custom2=None, custom3=None, custom4=None):  # noqa: E501
        """ContactUpdateFields - a model defined in OpenAPI"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._company = None
        self._title = None
        self._custom = None
        self._custom2 = None
        self._custom3 = None
        self._custom4 = None
        self.discriminator = None

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.title = title
        self.custom = custom
        self.custom2 = custom2
        self.custom3 = custom3
        self.custom4 = custom4

    @property
    def email(self):
        """Gets the email of this ContactUpdateFields.  # noqa: E501


        :return: The email of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactUpdateFields.


        :param email: The email of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this ContactUpdateFields.  # noqa: E501


        :return: The first_name of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactUpdateFields.


        :param first_name: The first_name of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactUpdateFields.  # noqa: E501


        :return: The last_name of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactUpdateFields.


        :param last_name: The last_name of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this ContactUpdateFields.  # noqa: E501


        :return: The company of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ContactUpdateFields.


        :param company: The company of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def title(self):
        """Gets the title of this ContactUpdateFields.  # noqa: E501


        :return: The title of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ContactUpdateFields.


        :param title: The title of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def custom(self):
        """Gets the custom of this ContactUpdateFields.  # noqa: E501


        :return: The custom of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ContactUpdateFields.


        :param custom: The custom of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._custom = custom

    @property
    def custom2(self):
        """Gets the custom2 of this ContactUpdateFields.  # noqa: E501


        :return: The custom2 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom2

    @custom2.setter
    def custom2(self, custom2):
        """Sets the custom2 of this ContactUpdateFields.


        :param custom2: The custom2 of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._custom2 = custom2

    @property
    def custom3(self):
        """Gets the custom3 of this ContactUpdateFields.  # noqa: E501


        :return: The custom3 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom3

    @custom3.setter
    def custom3(self, custom3):
        """Sets the custom3 of this ContactUpdateFields.


        :param custom3: The custom3 of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._custom3 = custom3

    @property
    def custom4(self):
        """Gets the custom4 of this ContactUpdateFields.  # noqa: E501


        :return: The custom4 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom4

    @custom4.setter
    def custom4(self, custom4):
        """Sets the custom4 of this ContactUpdateFields.


        :param custom4: The custom4 of this ContactUpdateFields.  # noqa: E501
        :type: str
        """

        self._custom4 = custom4

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContactUpdateFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
