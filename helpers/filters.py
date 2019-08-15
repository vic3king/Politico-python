from graphql import GraphQLError
from api.office.schema import Office
from api.party.schema import Party


def filter_office_id(info, id):

    query_office = Office.get_query(info)

    office = query_office.filter_by(id=id).first()
    if not office:
        raise GraphQLError("Office not found")


def filter_party_id(info, id):
    query_party = Party.get_query(info)
    party = query_party.filter_by(id=id).first()
    if not party:
        raise GraphQLError("Party not found")
