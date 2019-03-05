# coding: utf-8

"""
    Messente API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from messente_api.api_client import ApiClient


class ContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_contact_to_group(self, group_id, phone, **kwargs):  # noqa: E501
        """Adds a contact to a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_contact_to_group(group_id, phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: String in uuid format. (required)
        :param str phone: A phone number (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_contact_to_group_with_http_info(group_id, phone, **kwargs)  # noqa: E501
        else:
            (data) = self.add_contact_to_group_with_http_info(group_id, phone, **kwargs)  # noqa: E501
            return data

    def add_contact_to_group_with_http_info(self, group_id, phone, **kwargs):  # noqa: E501
        """Adds a contact to a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_contact_to_group_with_http_info(group_id, phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: String in uuid format. (required)
        :param str phone: A phone number (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['group_id', 'phone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_contact_to_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `add_contact_to_group`")  # noqa: E501
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `add_contact_to_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/contacts/{phone}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_contact(self, contact_fields, **kwargs):  # noqa: E501
        """Creates a new contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact(contact_fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactFields contact_fields: (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_contact_with_http_info(contact_fields, **kwargs)  # noqa: E501
        else:
            (data) = self.create_contact_with_http_info(contact_fields, **kwargs)  # noqa: E501
            return data

    def create_contact_with_http_info(self, contact_fields, **kwargs):  # noqa: E501
        """Creates a new contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact_with_http_info(contact_fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactFields contact_fields: (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['contact_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_contact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'contact_fields' is set
        if ('contact_fields' not in local_var_params or
                local_var_params['contact_fields'] is None):
            raise ValueError("Missing the required parameter `contact_fields` when calling `create_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_fields' in local_var_params:
            body_params = local_var_params['contact_fields']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactEnvelope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_contact(self, phone, **kwargs):  # noqa: E501
        """Deletes a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_contact(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_contact_with_http_info(phone, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_contact_with_http_info(phone, **kwargs)  # noqa: E501
            return data

    def delete_contact_with_http_info(self, phone, **kwargs):  # noqa: E501
        """Deletes a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_contact_with_http_info(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['phone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_contact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `delete_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/{phone}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_contact(self, phone, **kwargs):  # noqa: E501
        """Lists a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contact(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_contact_with_http_info(phone, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_contact_with_http_info(phone, **kwargs)  # noqa: E501
            return data

    def fetch_contact_with_http_info(self, phone, **kwargs):  # noqa: E501
        """Lists a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contact_with_http_info(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['phone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_contact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `fetch_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/{phone}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactEnvelope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_contact_groups(self, phone, **kwargs):  # noqa: E501
        """Lists groups of a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contact_groups(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: GroupListEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_contact_groups_with_http_info(phone, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_contact_groups_with_http_info(phone, **kwargs)  # noqa: E501
            return data

    def fetch_contact_groups_with_http_info(self, phone, **kwargs):  # noqa: E501
        """Lists groups of a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contact_groups_with_http_info(phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :return: GroupListEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['phone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_contact_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `fetch_contact_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/{phone}/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupListEnvelope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_contacts(self, **kwargs):  # noqa: E501
        """Returns all contacts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contacts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_ids: Optional one or many group id strings in uuid format. For example: \"/contacts?groupIds=group_id_one&groupIds=group_id_two\" 
        :return: ContactListEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_contacts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_contacts_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_contacts_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all contacts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_contacts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] group_ids: Optional one or many group id strings in uuid format. For example: \"/contacts?groupIds=group_id_one&groupIds=group_id_two\" 
        :return: ContactListEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['group_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_contacts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_ids' in local_var_params:
            query_params.append(('groupIds', local_var_params['group_ids']))  # noqa: E501
            collection_formats['groupIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactListEnvelope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_contact_from_group(self, group_id, phone, **kwargs):  # noqa: E501
        """Remove a contact from a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_contact_from_group(group_id, phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: String in uuid format. (required)
        :param str phone: A phone number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_contact_from_group_with_http_info(group_id, phone, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_contact_from_group_with_http_info(group_id, phone, **kwargs)  # noqa: E501
            return data

    def remove_contact_from_group_with_http_info(self, group_id, phone, **kwargs):  # noqa: E501
        """Remove a contact from a group.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_contact_from_group_with_http_info(group_id, phone, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: String in uuid format. (required)
        :param str phone: A phone number (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['group_id', 'phone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_contact_from_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in local_var_params or
                local_var_params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `remove_contact_from_group`")  # noqa: E501
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `remove_contact_from_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{groupId}/contacts/{phone}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_contact(self, phone, contact_update_fields, **kwargs):  # noqa: E501
        """Updates a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_contact(phone, contact_update_fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :param ContactUpdateFields contact_update_fields: (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_contact_with_http_info(phone, contact_update_fields, **kwargs)  # noqa: E501
        else:
            (data) = self.update_contact_with_http_info(phone, contact_update_fields, **kwargs)  # noqa: E501
            return data

    def update_contact_with_http_info(self, phone, contact_update_fields, **kwargs):  # noqa: E501
        """Updates a contact.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_contact_with_http_info(phone, contact_update_fields, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone: A phone number (required)
        :param ContactUpdateFields contact_update_fields: (required)
        :return: ContactEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['phone', 'contact_update_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_contact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if ('phone' not in local_var_params or
                local_var_params['phone'] is None):
            raise ValueError("Missing the required parameter `phone` when calling `update_contact`")  # noqa: E501
        # verify the required parameter 'contact_update_fields' is set
        if ('contact_update_fields' not in local_var_params or
                local_var_params['contact_update_fields'] is None):
            raise ValueError("Missing the required parameter `contact_update_fields` when calling `update_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact_update_fields' in local_var_params:
            body_params = local_var_params['contact_update_fields']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/{phone}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactEnvelope',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
