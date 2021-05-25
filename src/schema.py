import graphene


class Data(graphene.ObjectType):
    name = graphene.String()
    image = graphene.String()
    description = graphene.String()
    dateLastEdited = graphene.DateTime()
