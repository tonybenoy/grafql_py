import graphene
import pytest
from graphene.test import Client

from src.schema import Query


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query))
    return client
