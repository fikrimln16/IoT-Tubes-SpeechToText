import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.s2t_post200_response import S2tPost200Response  # noqa: E501
from openapi_server.models.s2t_post_request import S2tPostRequest  # noqa: E501
from openapi_server import util


def s2t_post(s2t_post_request=None):  # noqa: E501
    """Transcribe audio to text

     # noqa: E501

    :param s2t_post_request: Contain data and metadata of the audio
    :type s2t_post_request: dict | bytes

    :rtype: Union[S2tPost200Response, Tuple[S2tPost200Response, int], Tuple[S2tPost200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        s2t_post_request = S2tPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
