import graphene
import pendulum
from graphene import Int, List, ObjectType, String


from src.utils import filter_by


class Data(graphene.ObjectType):
    name = graphene.String()
    image = graphene.String()
    description = graphene.String()
    dateLastEdited = graphene.DateTime()


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
        from src.main import data

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
