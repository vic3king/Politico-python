import re
from graphql import GraphQLError


def verify_email(email):
    return bool(re.match('^.+@(\[?)[a-zA-Z0-9-.]+.', email))  # noqa


class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, entity_name, entity):
        # Database integrity error
        raise GraphQLError(
            '{} {} already exists'.format(entity_name, entity))

    def foreign_key_conflict(self, entity_name, entity):
        # Database foreign key error
        raise GraphQLError(
            '{} {} does not exists'.format(entity_name, entity))

    def invalid_data_error(self):
        # Database data error
        raise GraphQLError('Error: Invalid data supplied to parameters')

    def db_connection(self):
        # Database connection error
        raise GraphQLError('Error: Could not connect to Db')


# def validate_question_type(**kwargs):
#     """
#     Function to validate the question types,
#     should allow only check, input and rate
#     :params kwargs
#     """
#     question_types = ['check', 'input', 'rate', 'missing_items']
#     if 'question_type' in kwargs:
#         type = kwargs['question_type']
#         if type.lower() not in question_types:
#             raise AttributeError("Not a valid question type")


def validate_entity_types(list_of_types, field_to_check, **kwargs):
    """
    Function to validate the Enum types,
    should allow only callow client provide a
    type from the list_types for the field_to_check
    """

    if field_to_check in kwargs:
        type = kwargs[field_to_check]
        if type.lower() not in list_of_types:
            raise AttributeError(f"Invalid type provided for field {field_to_check}") # noqa
