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


class LabelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def labels_controller_create(self, body, session, **kwargs):  # noqa: E501
        """Create a new label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_create(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelBody body: (required)
        :param object session: Session name (required)
        :return: Label
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_create_with_http_info(body, session, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_create_with_http_info(body, session, **kwargs)  # noqa: E501
            return data

    def labels_controller_create_with_http_info(self, body, session, **kwargs):  # noqa: E501
        """Create a new label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_create_with_http_info(body, session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelBody body: (required)
        :param object session: Session name (required)
        :return: Label
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
                    " to method labels_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `labels_controller_create`")  # noqa: E501
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_create`")  # noqa: E501

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
            '/api/{session}/labels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Label',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def labels_controller_delete(self, session, label_id, **kwargs):  # noqa: E501
        """Delete a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_delete(session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_delete_with_http_info(session, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_delete_with_http_info(session, label_id, **kwargs)  # noqa: E501
            return data

    def labels_controller_delete_with_http_info(self, session, label_id, **kwargs):  # noqa: E501
        """Delete a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_delete_with_http_info(session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'label_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method labels_controller_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_delete`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params or
                params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `labels_controller_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']  # noqa: E501

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
            '/api/{session}/labels/{labelId}', 'DELETE',
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

    def labels_controller_get_all(self, session, **kwargs):  # noqa: E501
        """Get all labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_all(session, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_get_all_with_http_info(session, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_get_all_with_http_info(session, **kwargs)  # noqa: E501
            return data

    def labels_controller_get_all_with_http_info(self, session, **kwargs):  # noqa: E501
        """Get all labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_all_with_http_info(session, async_req=True)
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
                    " to method labels_controller_get_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_get_all`")  # noqa: E501

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
            '/api/{session}/labels', 'GET',
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

    def labels_controller_get_chat_labels(self, session, chat_id, **kwargs):  # noqa: E501
        """Get labels for the chat  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_chat_labels(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_get_chat_labels_with_http_info(session, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_get_chat_labels_with_http_info(session, chat_id, **kwargs)  # noqa: E501
            return data

    def labels_controller_get_chat_labels_with_http_info(self, session, chat_id, **kwargs):  # noqa: E501
        """Get labels for the chat  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_chat_labels_with_http_info(session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: object
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
                    " to method labels_controller_get_chat_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_get_chat_labels`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `labels_controller_get_chat_labels`")  # noqa: E501

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
            '/api/{session}/labels/chats/{chatId}', 'GET',
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

    def labels_controller_get_chats_by_label(self, session, label_id, **kwargs):  # noqa: E501
        """Get chats by label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_chats_by_label(session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_get_chats_by_label_with_http_info(session, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_get_chats_by_label_with_http_info(session, label_id, **kwargs)  # noqa: E501
            return data

    def labels_controller_get_chats_by_label_with_http_info(self, session, label_id, **kwargs):  # noqa: E501
        """Get chats by label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_get_chats_by_label_with_http_info(session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session', 'label_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method labels_controller_get_chats_by_label" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_get_chats_by_label`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params or
                params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `labels_controller_get_chats_by_label`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/labels/{labelId}/chats', 'GET',
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

    def labels_controller_put_chat_labels(self, body, session, chat_id, **kwargs):  # noqa: E501
        """Save labels for the chat  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_put_chat_labels(body, session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetLabelsRequest body: (required)
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_put_chat_labels_with_http_info(body, session, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_put_chat_labels_with_http_info(body, session, chat_id, **kwargs)  # noqa: E501
            return data

    def labels_controller_put_chat_labels_with_http_info(self, body, session, chat_id, **kwargs):  # noqa: E501
        """Save labels for the chat  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_put_chat_labels_with_http_info(body, session, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SetLabelsRequest body: (required)
        :param object session: Session name (required)
        :param object chat_id: Chat ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'session', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method labels_controller_put_chat_labels" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `labels_controller_put_chat_labels`")  # noqa: E501
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_put_chat_labels`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `labels_controller_put_chat_labels`")  # noqa: E501

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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/{session}/labels/chats/{chatId}', 'PUT',
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

    def labels_controller_update(self, body, session, label_id, **kwargs):  # noqa: E501
        """Update a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_update(body, session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelBody body: (required)
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: Label
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.labels_controller_update_with_http_info(body, session, label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.labels_controller_update_with_http_info(body, session, label_id, **kwargs)  # noqa: E501
            return data

    def labels_controller_update_with_http_info(self, body, session, label_id, **kwargs):  # noqa: E501
        """Update a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.labels_controller_update_with_http_info(body, session, label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelBody body: (required)
        :param object session: Session name (required)
        :param object label_id: (required)
        :return: Label
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'session', 'label_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method labels_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `labels_controller_update`")  # noqa: E501
        # verify the required parameter 'session' is set
        if ('session' not in params or
                params['session'] is None):
            raise ValueError("Missing the required parameter `session` when calling `labels_controller_update`")  # noqa: E501
        # verify the required parameter 'label_id' is set
        if ('label_id' not in params or
                params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `labels_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'session' in params:
            path_params['session'] = params['session']  # noqa: E501
        if 'label_id' in params:
            path_params['labelId'] = params['label_id']  # noqa: E501

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
            '/api/{session}/labels/{labelId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Label',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
