# coding: utf-8

"""
    WAHA - WhatsApp HTTP API

    <b>WhatsApp HTTP API</b> that you can run in a click!<br/><a href=\"/dashboard\"><b>📊 Dashboard</b></a><br/><br/>Learn more:<ul><li><a href=\"https://waha.devlike.pro/\" target=\"_blank\">Documentation</a></li><li><a href=\"https://waha.devlike.pro/docs/how-to/engines/#features\" target=\"_blank\">Supported features in engines</a></li><li><a href=\"https://github.com/devlikeapro/waha\" target=\"_blank\">GitHub - WAHA Core</a></li><li><a href=\"https://github.com/devlikeapro/waha-plus\" target=\"_blank\">GitHub - WAHA Plus</a></li></ul><p>Support the project and get WAHA Plus version!</p><ul><li><a href=\"https://waha.devlike.pro/docs/how-to/plus-version/\" target=\"_blank\">WAHA Plus</a></li><li><a href=\"https://patreon.com/wa_http_api/\" target=\"_blank\">Patreon</a></li><li><a href=\"https://boosty.to/wa-http-api/\" target=\"_blank\">Boosty</a></li><li><a href=\"https://portal.devlike.pro/\" target=\"_blank\">Patron Portal</a></li></ul>  # noqa: E501

    OpenAPI spec version: 2024.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SessionConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'object',
        'proxy': 'object',
        'debug': 'object',
        'noweb': 'object',
        'webhooks': 'object'
    }

    attribute_map = {
        'metadata': 'metadata',
        'proxy': 'proxy',
        'debug': 'debug',
        'noweb': 'noweb',
        'webhooks': 'webhooks'
    }

    def __init__(self, metadata=None, proxy=None, debug=None, noweb=None, webhooks=None):  # noqa: E501
        """SessionConfig - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._proxy = None
        self._debug = None
        self._noweb = None
        self._webhooks = None
        self.discriminator = None
        if metadata is not None:
            self.metadata = metadata
        if proxy is not None:
            self.proxy = proxy
        if debug is not None:
            self.debug = debug
        if noweb is not None:
            self.noweb = noweb
        if webhooks is not None:
            self.webhooks = webhooks

    @property
    def metadata(self):
        """Gets the metadata of this SessionConfig.  # noqa: E501

        Metadata for the session. You'll get 'metadata' in all webhooks.  # noqa: E501

        :return: The metadata of this SessionConfig.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SessionConfig.

        Metadata for the session. You'll get 'metadata' in all webhooks.  # noqa: E501

        :param metadata: The metadata of this SessionConfig.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def proxy(self):
        """Gets the proxy of this SessionConfig.  # noqa: E501


        :return: The proxy of this SessionConfig.  # noqa: E501
        :rtype: object
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this SessionConfig.


        :param proxy: The proxy of this SessionConfig.  # noqa: E501
        :type: object
        """

        self._proxy = proxy

    @property
    def debug(self):
        """Gets the debug of this SessionConfig.  # noqa: E501


        :return: The debug of this SessionConfig.  # noqa: E501
        :rtype: object
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this SessionConfig.


        :param debug: The debug of this SessionConfig.  # noqa: E501
        :type: object
        """

        self._debug = debug

    @property
    def noweb(self):
        """Gets the noweb of this SessionConfig.  # noqa: E501


        :return: The noweb of this SessionConfig.  # noqa: E501
        :rtype: object
        """
        return self._noweb

    @noweb.setter
    def noweb(self, noweb):
        """Sets the noweb of this SessionConfig.


        :param noweb: The noweb of this SessionConfig.  # noqa: E501
        :type: object
        """

        self._noweb = noweb

    @property
    def webhooks(self):
        """Gets the webhooks of this SessionConfig.  # noqa: E501


        :return: The webhooks of this SessionConfig.  # noqa: E501
        :rtype: object
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this SessionConfig.


        :param webhooks: The webhooks of this SessionConfig.  # noqa: E501
        :type: object
        """

        self._webhooks = webhooks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SessionConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SessionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other