import json

from fastapi import FastAPI
from graphene import Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from src.schema import Query
from src.utils import datetime_parser

with open("./src/mock_data.json") as f:
    data = json.load(f)


data = datetime_parser(dct=data)


app = FastAPI()
app.add_route(
    "/", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor)
)
