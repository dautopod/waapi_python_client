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

class WANumberExistResult(object):
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
        'chat_id': 'object',
        'number_exists': 'object'
    }

    attribute_map = {
        'chat_id': 'chatId',
        'number_exists': 'numberExists'
    }

    def __init__(self, chat_id=None, number_exists=None):  # noqa: E501
        """WANumberExistResult - a model defined in Swagger"""  # noqa: E501
        self._chat_id = None
        self._number_exists = None
        self.discriminator = None
        if chat_id is not None:
            self.chat_id = chat_id
        self.number_exists = number_exists

    @property
    def chat_id(self):
        """Gets the chat_id of this WANumberExistResult.  # noqa: E501


        :return: The chat_id of this WANumberExistResult.  # noqa: E501
        :rtype: object
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this WANumberExistResult.


        :param chat_id: The chat_id of this WANumberExistResult.  # noqa: E501
        :type: object
        """

        self._chat_id = chat_id

    @property
    def number_exists(self):
        """Gets the number_exists of this WANumberExistResult.  # noqa: E501


        :return: The number_exists of this WANumberExistResult.  # noqa: E501
        :rtype: object
        """
        return self._number_exists

    @number_exists.setter
    def number_exists(self, number_exists):
        """Sets the number_exists of this WANumberExistResult.


        :param number_exists: The number_exists of this WANumberExistResult.  # noqa: E501
        :type: object
        """
        if number_exists is None:
            raise ValueError("Invalid value for `number_exists`, must not be `None`")  # noqa: E501

        self._number_exists = number_exists

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
        if issubclass(WANumberExistResult, dict):
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
        if not isinstance(other, WANumberExistResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
