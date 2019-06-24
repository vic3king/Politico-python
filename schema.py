
import graphene
import api.user.schema

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType,
                                 SQLAlchemyConnectionField)


# class Query(
#     api.user.schema.Query,
# ):
#     """Root for politico Graphql queries"""
#     pass


class Mutation(
    api.user.schema.Mutation,
):
    """Root for politico Graphql queries"""
    pass


class Query(
        api.user.schema.Query
):
    """Root for converge Graphql queries"""
    pass

schema = Schema(mutation=Mutation, query=Query)
