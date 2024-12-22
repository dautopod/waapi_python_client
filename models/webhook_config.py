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

class WebhookConfig(object):
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
        'url': 'object',
        'events': 'object',
        'hmac': 'object',
        'retries': 'object',
        'custom_headers': 'object'
    }

    attribute_map = {
        'url': 'url',
        'events': 'events',
        'hmac': 'hmac',
        'retries': 'retries',
        'custom_headers': 'customHeaders'
    }

    def __init__(self, url=None, events=None, hmac=None, retries=None, custom_headers=None):  # noqa: E501
        """WebhookConfig - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._events = None
        self._hmac = None
        self._retries = None
        self._custom_headers = None
        self.discriminator = None
        self.url = url
        self.events = events
        if hmac is not None:
            self.hmac = hmac
        if retries is not None:
            self.retries = retries
        if custom_headers is not None:
            self.custom_headers = custom_headers

    @property
    def url(self):
        """Gets the url of this WebhookConfig.  # noqa: E501

        You can use https://docs.webhook.site/ to test webhooks and see the payload  # noqa: E501

        :return: The url of this WebhookConfig.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookConfig.

        You can use https://docs.webhook.site/ to test webhooks and see the payload  # noqa: E501

        :param url: The url of this WebhookConfig.  # noqa: E501
        :type: object
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def events(self):
        """Gets the events of this WebhookConfig.  # noqa: E501


        :return: The events of this WebhookConfig.  # noqa: E501
        :rtype: object
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhookConfig.


        :param events: The events of this WebhookConfig.  # noqa: E501
        :type: object
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def hmac(self):
        """Gets the hmac of this WebhookConfig.  # noqa: E501


        :return: The hmac of this WebhookConfig.  # noqa: E501
        :rtype: object
        """
        return self._hmac

    @hmac.setter
    def hmac(self, hmac):
        """Sets the hmac of this WebhookConfig.


        :param hmac: The hmac of this WebhookConfig.  # noqa: E501
        :type: object
        """

        self._hmac = hmac

    @property
    def retries(self):
        """Gets the retries of this WebhookConfig.  # noqa: E501


        :return: The retries of this WebhookConfig.  # noqa: E501
        :rtype: object
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this WebhookConfig.


        :param retries: The retries of this WebhookConfig.  # noqa: E501
        :type: object
        """

        self._retries = retries

    @property
    def custom_headers(self):
        """Gets the custom_headers of this WebhookConfig.  # noqa: E501


        :return: The custom_headers of this WebhookConfig.  # noqa: E501
        :rtype: object
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        """Sets the custom_headers of this WebhookConfig.


        :param custom_headers: The custom_headers of this WebhookConfig.  # noqa: E501
        :type: object
        """

        self._custom_headers = custom_headers

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
        if issubclass(WebhookConfig, dict):
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
        if not isinstance(other, WebhookConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
