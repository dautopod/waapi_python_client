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

class LabelChatAssociation(object):
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
        'label_id': 'object',
        'chat_id': 'object',
        'label': 'object'
    }

    attribute_map = {
        'label_id': 'labelId',
        'chat_id': 'chatId',
        'label': 'label'
    }

    def __init__(self, label_id=None, chat_id=None, label=None):  # noqa: E501
        """LabelChatAssociation - a model defined in Swagger"""  # noqa: E501
        self._label_id = None
        self._chat_id = None
        self._label = None
        self.discriminator = None
        self.label_id = label_id
        self.chat_id = chat_id
        self.label = label

    @property
    def label_id(self):
        """Gets the label_id of this LabelChatAssociation.  # noqa: E501

        Label ID  # noqa: E501

        :return: The label_id of this LabelChatAssociation.  # noqa: E501
        :rtype: object
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this LabelChatAssociation.

        Label ID  # noqa: E501

        :param label_id: The label_id of this LabelChatAssociation.  # noqa: E501
        :type: object
        """
        if label_id is None:
            raise ValueError("Invalid value for `label_id`, must not be `None`")  # noqa: E501

        self._label_id = label_id

    @property
    def chat_id(self):
        """Gets the chat_id of this LabelChatAssociation.  # noqa: E501

        Chat ID  # noqa: E501

        :return: The chat_id of this LabelChatAssociation.  # noqa: E501
        :rtype: object
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this LabelChatAssociation.

        Chat ID  # noqa: E501

        :param chat_id: The chat_id of this LabelChatAssociation.  # noqa: E501
        :type: object
        """
        if chat_id is None:
            raise ValueError("Invalid value for `chat_id`, must not be `None`")  # noqa: E501

        self._chat_id = chat_id

    @property
    def label(self):
        """Gets the label of this LabelChatAssociation.  # noqa: E501


        :return: The label of this LabelChatAssociation.  # noqa: E501
        :rtype: object
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelChatAssociation.


        :param label: The label of this LabelChatAssociation.  # noqa: E501
        :type: object
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

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
        if issubclass(LabelChatAssociation, dict):
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
        if not isinstance(other, LabelChatAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other