# coding: utf-8

"""
    WAHA - WhatsApp HTTP API

    <b>WhatsApp HTTP API</b> that you can run in a click!<br/><a href=\"/dashboard\"><b>📊 Dashboard</b></a><br/><br/>Learn more:<ul><li><a href=\"https://waha.devlike.pro/\" target=\"_blank\">Documentation</a></li><li><a href=\"https://waha.devlike.pro/docs/how-to/engines/#features\" target=\"_blank\">Supported features in engines</a></li><li><a href=\"https://github.com/devlikeapro/waha\" target=\"_blank\">GitHub - WAHA Core</a></li><li><a href=\"https://github.com/devlikeapro/waha-plus\" target=\"_blank\">GitHub - WAHA Plus</a></li></ul><p>Support the project and get WAHA Plus version!</p><ul><li><a href=\"https://waha.devlike.pro/docs/how-to/plus-version/\" target=\"_blank\">WAHA Plus</a></li><li><a href=\"https://patreon.com/wa_http_api/\" target=\"_blank\">Patreon</a></li><li><a href=\"https://boosty.to/wa-http-api/\" target=\"_blank\">Boosty</a></li><li><a href=\"https://portal.devlike.pro/\" target=\"_blank\">Patron Portal</a></li></ul>  # noqa: E501

    OpenAPI spec version: 2024.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wa_agent.api_client import ApiClient


class PresenceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def presence_controller_get_presence(self, session, chat_id, **kwargs):  # noqa: E501
        """Get the presence for the chat id. If it hasn't been subscribed - it also subscribes to it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_get_presence(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: WAHAChatPresences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.presence_controller_get_presence_with_http_info(session, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.presence_controller_get_presence_with_http_info(session, chat_id, **kwargs)  # noqa: E501
            return data

    def presence_controller_get_presence_with_http_info(self, session, chat_id, **kwargs):  # noqa: E501
        """Get the presence for the chat id. If it hasn't been subscribed - it also subscribes to it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_get_presence_with_http_info(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: WAHAChatPresences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method presence_controller_get_presence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `presence_controller_get_presence`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `presence_controller_get_presence`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'chat_id' in params:
            path_params['chatId'] = params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/presence/{chatId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WAHAChatPresences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def presence_controller_get_presence_all(self, session, **kwargs):  # noqa: E501
        """Get all subscribed presence information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_get_presence_all(session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.presence_controller_get_presence_all_with_http_info(session, **kwargs)  # noqa: E501
        else:
            (data) = self.presence_controller_get_presence_all_with_http_info(session, **kwargs)  # noqa: E501
            return data

    def presence_controller_get_presence_all_with_http_info(self, session, **kwargs):  # noqa: E501
        """Get all subscribed presence information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_get_presence_all_with_http_info(session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method presence_controller_get_presence_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `presence_controller_get_presence_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/presence', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def presence_controller_set_presence(self, body, session, **kwargs):  # noqa: E501
        """Set session presence  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_set_presence(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WAHASessionPresence body: (required)
        :param object session: Session name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.presence_controller_set_presence_with_http_info(body, session, **kwargs)  # noqa: E501
        else:
            (data) = self.presence_controller_set_presence_with_http_info(body, session, **kwargs)  # noqa: E501
            return data

    def presence_controller_set_presence_with_http_info(self, body, session, **kwargs):  # noqa: E501
        """Set session presence  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_set_presence_with_http_info(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WAHASessionPresence body: (required)
        :param object session: Session name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'session']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method presence_controller_set_presence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `presence_controller_set_presence`")  # noqa: E501
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `presence_controller_set_presence`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/presence', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def presence_controller_subscribe(self, session, chat_id, **kwargs):  # noqa: E501
        """Subscribe to presence events for the chat.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_subscribe(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.presence_controller_subscribe_with_http_info(session, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.presence_controller_subscribe_with_http_info(session, chat_id, **kwargs)  # noqa: E501
            return data

    def presence_controller_subscribe_with_http_info(self, session, chat_id, **kwargs):  # noqa: E501
        """Subscribe to presence events for the chat.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.presence_controller_subscribe_with_http_info(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method presence_controller_subscribe" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `presence_controller_subscribe`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `presence_controller_subscribe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'chat_id' in params:
            path_params['chatId'] = params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/presence/{chatId}/subscribe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
