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


class ChannelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def channels_controller_create(self, body, session, **kwargs):  # noqa: E501
        """Create a new channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_create(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateChannelRequest body: (required)
        :param object session: Session name (required)
        :return: Channel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_create_with_http_info(body, session, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_create_with_http_info(body, session, **kwargs)  # noqa: E501
            return data

    def channels_controller_create_with_http_info(self, body, session, **kwargs):  # noqa: E501
        """Create a new channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_create_with_http_info(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateChannelRequest body: (required)
        :param object session: Session name (required)
        :return: Channel
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
                    " to method channels_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `channels_controller_create`")  # noqa: E501
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_create`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Channel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def channels_controller_delete(self, session, id, **kwargs):  # noqa: E501
        """Delete the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_delete(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_delete_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_delete_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_delete_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Delete the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_delete_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels/{id}', 'DELETE',
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

    def channels_controller_follow(self, session, id, **kwargs):  # noqa: E501
        """Follow the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_follow(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_follow_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_follow_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_follow_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Follow the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_follow_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_follow" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_follow`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_follow`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels/{id}/follow', 'POST',
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

    def channels_controller_get(self, session, id, **kwargs):  # noqa: E501
        """Get the channel info  # noqa: E501

        You can use either id (123@newsletter) OR invite code (https://www.whatsapp.com/channel/123)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_get(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID or invite code from invite link https://www.whatsapp.com/channel/11111 (required)
        :return: Channel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_get_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_get_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_get_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Get the channel info  # noqa: E501

        You can use either id (123@newsletter) OR invite code (https://www.whatsapp.com/channel/123)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_get_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID or invite code from invite link https://www.whatsapp.com/channel/11111 (required)
        :return: Channel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/api/{session}/channels/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Channel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def channels_controller_list(self, session, **kwargs):  # noqa: E501
        """Get list of know channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_list(session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object role:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_list_with_http_info(session, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_list_with_http_info(session, **kwargs)  # noqa: E501
            return data

    def channels_controller_list_with_http_info(self, session, **kwargs):  # noqa: E501
        """Get list of know channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_list_with_http_info(session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object role:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'role']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501

        query_params = []
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501

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
            '/api/{session}/channels', 'GET',
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

    def channels_controller_mute(self, session, id, **kwargs):  # noqa: E501
        """Mute the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_mute(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_mute_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_mute_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_mute_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Mute the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_mute_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_mute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_mute`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_mute`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels/{id}/mute', 'POST',
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

    def channels_controller_unfollow(self, session, id, **kwargs):  # noqa: E501
        """Unfollow the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_unfollow(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_unfollow_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_unfollow_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_unfollow_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Unfollow the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_unfollow_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_unfollow" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_unfollow`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_unfollow`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels/{id}/unfollow', 'POST',
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

    def channels_controller_unmute(self, session, id, **kwargs):  # noqa: E501
        """Unmute the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_unmute(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.channels_controller_unmute_with_http_info(session, id, **kwargs)  # noqa: E501
        else:
            (data) = self.channels_controller_unmute_with_http_info(session, id, **kwargs)  # noqa: E501
            return data

    def channels_controller_unmute_with_http_info(self, session, id, **kwargs):  # noqa: E501
        """Unmute the channel.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.channels_controller_unmute_with_http_info(session, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object id: WhatsApp Channel ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channels_controller_unmute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `channels_controller_unmute`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `channels_controller_unmute`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/channels/{id}/unmute', 'POST',
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