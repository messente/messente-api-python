# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from messente_api.configuration import Configuration


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

    def __init__(self, email=None, first_name=None, last_name=None, company=None, title=None, custom=None, custom2=None, custom3=None, custom4=None, local_vars_configuration=None):  # noqa: E501
        """ContactUpdateFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

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

        The email of the contact  # noqa: E501

        :return: The email of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactUpdateFields.

        The email of the contact  # noqa: E501

        :param email: The email of this ContactUpdateFields.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this ContactUpdateFields.  # noqa: E501

        The first name of the contact  # noqa: E501

        :return: The first_name of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactUpdateFields.

        The first name of the contact  # noqa: E501

        :param first_name: The first_name of this ContactUpdateFields.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactUpdateFields.  # noqa: E501

        The last name of the contact  # noqa: E501

        :return: The last_name of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactUpdateFields.

        The last name of the contact  # noqa: E501

        :param last_name: The last_name of this ContactUpdateFields.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this ContactUpdateFields.  # noqa: E501

        The company of the contact  # noqa: E501

        :return: The company of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ContactUpdateFields.

        The company of the contact  # noqa: E501

        :param company: The company of this ContactUpdateFields.  # noqa: E501
        :type company: str
        """

        self._company = company

    @property
    def title(self):
        """Gets the title of this ContactUpdateFields.  # noqa: E501

        The title of the contact  # noqa: E501

        :return: The title of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ContactUpdateFields.

        The title of the contact  # noqa: E501

        :param title: The title of this ContactUpdateFields.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def custom(self):
        """Gets the custom of this ContactUpdateFields.  # noqa: E501

        The first custom field  # noqa: E501

        :return: The custom of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ContactUpdateFields.

        The first custom field  # noqa: E501

        :param custom: The custom of this ContactUpdateFields.  # noqa: E501
        :type custom: str
        """

        self._custom = custom

    @property
    def custom2(self):
        """Gets the custom2 of this ContactUpdateFields.  # noqa: E501

        The second custom field  # noqa: E501

        :return: The custom2 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom2

    @custom2.setter
    def custom2(self, custom2):
        """Sets the custom2 of this ContactUpdateFields.

        The second custom field  # noqa: E501

        :param custom2: The custom2 of this ContactUpdateFields.  # noqa: E501
        :type custom2: str
        """

        self._custom2 = custom2

    @property
    def custom3(self):
        """Gets the custom3 of this ContactUpdateFields.  # noqa: E501

        The third custom field  # noqa: E501

        :return: The custom3 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom3

    @custom3.setter
    def custom3(self, custom3):
        """Sets the custom3 of this ContactUpdateFields.

        The third custom field  # noqa: E501

        :param custom3: The custom3 of this ContactUpdateFields.  # noqa: E501
        :type custom3: str
        """

        self._custom3 = custom3

    @property
    def custom4(self):
        """Gets the custom4 of this ContactUpdateFields.  # noqa: E501

        The fourth custom field  # noqa: E501

        :return: The custom4 of this ContactUpdateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom4

    @custom4.setter
    def custom4(self, custom4):
        """Sets the custom4 of this ContactUpdateFields.

        The fourth custom field  # noqa: E501

        :param custom4: The custom4 of this ContactUpdateFields.  # noqa: E501
        :type custom4: str
        """

        self._custom4 = custom4

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactUpdateFields):
            return True

        return self.to_dict() != other.to_dict()
