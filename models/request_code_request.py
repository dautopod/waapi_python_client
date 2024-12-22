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

class RequestCodeRequest(object):
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
        'phone_number': 'object',
        'method': 'object'
    }

    attribute_map = {
        'phone_number': 'phoneNumber',
        'method': 'method'
    }

    def __init__(self, phone_number=None, method=None):  # noqa: E501
        """RequestCodeRequest - a model defined in Swagger"""  # noqa: E501
        self._phone_number = None
        self._method = None
        self.discriminator = None
        self.phone_number = phone_number
        if method is not None:
            self.method = method

    @property
    def phone_number(self):
        """Gets the phone_number of this RequestCodeRequest.  # noqa: E501

        Mobile phone number in international format  # noqa: E501

        :return: The phone_number of this RequestCodeRequest.  # noqa: E501
        :rtype: object
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this RequestCodeRequest.

        Mobile phone number in international format  # noqa: E501

        :param phone_number: The phone_number of this RequestCodeRequest.  # noqa: E501
        :type: object
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def method(self):
        """Gets the method of this RequestCodeRequest.  # noqa: E501

        How would you like to receive the one time code for registration? |sms|voice. Leave empty for Web pairing.  # noqa: E501

        :return: The method of this RequestCodeRequest.  # noqa: E501
        :rtype: object
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this RequestCodeRequest.

        How would you like to receive the one time code for registration? |sms|voice. Leave empty for Web pairing.  # noqa: E501

        :param method: The method of this RequestCodeRequest.  # noqa: E501
        :type: object
        """

        self._method = method

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
        if issubclass(RequestCodeRequest, dict):
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
        if not isinstance(other, RequestCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
