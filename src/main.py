import json
from typing import List

import pendulum
from fastapi import FastAPI
from graphene import Int, List, ObjectType, Schema, String
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from src.schema import Data
from src.utils import filter_by

with open("./src/mock_data.json") as f:
    data = json.load(f)


def datetime_parser(dct):
    for item in dct:
        item["dateLastEdited"] = pendulum.parse(item["dateLastEdited"])
    return dct


data = datetime_parser(data)


class Query(ObjectType):
    get_data = List(
        Data,
        name=String(),
        desc=String(),
        sort=String(),
        first=Int(),
        skip=Int(),
    )

    async def resolve_get_data(self, info, **args):
        q_name = args.get("name")
        q_desc = args.get("desc")
        q_sort = args.get("sort")
        q_first = args.get("first")
        q_skip = args.get("skip")
        data_filtered = data
        if q_name:
            data_filtered = filter_by(data=data_filtered, key=q_name, val="name")
        if q_desc:
            data_filtered = filter_by(data=data_filtered, key=q_desc, val="description")
        if q_sort:
            data_filtered = sorted(
                data_filtered,
                key=lambda k: k[q_sort]
                if q_sort != "dateLastEdited"
                else pendulum.parse(k[q_sort]),
            )
        if q_skip:
            data_filtered = data_filtered[q_skip:]
        if q_first:
            data_filtered = data_filtered[:q_first]
        return data_filtered


app = FastAPI()
app.add_route(
    "/", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor)
)
