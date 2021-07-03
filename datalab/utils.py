from django.forms.models import model_to_dict
import json


def get_json_ready(model_instance):
    '''
    :param model_instance:
    :return: serialized model instance
    '''

    to_dict = model_to_dict(model_instance)
    # serialized_instance = json.dumps(to_dict)

    return to_dict
