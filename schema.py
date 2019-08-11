import api.user.schema
import api.party.schema
import api.office.schema

from graphene import Schema


class Mutation(
    api.user.schema.Mutation,
    api.party.schema.Mutation,
    api.office.schema.Mutation,
):
    """Root for politico Graphql queries"""
    pass


class Query(
        api.user.schema.Query,
        api.office.schema.Query,
        api.party.schema.Query
):
    """Root for converge Graphql queries"""
    pass


schema = Schema(mutation=Mutation, query=Query)
