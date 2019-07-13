import api.user.schema
import api.party.schema

from graphene import Schema


class Mutation(
    api.user.schema.Mutation,
    api.party.schema.Mutation
):
    """Root for politico Graphql queries"""
    pass


class Query(
        api.user.schema.Query
):
    """Root for converge Graphql queries"""
    pass


schema = Schema(mutation=Mutation, query=Query)
