import json

import pendulum
from fastapi import FastAPI
from graphene import Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from src.schema import Query

with open("./src/mock_data.json") as f:
    data = json.load(f)


def datetime_parser(dct):
    for item in dct:
        item["dateLastEdited"] = pendulum.parse(item["dateLastEdited"])
    return dct


data = datetime_parser(data)


app = FastAPI()
app.add_route(
    "/", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor)
)
