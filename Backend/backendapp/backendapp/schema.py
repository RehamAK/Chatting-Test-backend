import graphene
import Chat.schema
from Chat.subscriptions import SubscriptionChatting


class Query(Chat.schema.Query,graphene.ObjectType):
    pass

class Mutation(Chat.schema.Mutation,graphene.ObjectType):
    pass

class Subscription(SubscriptionChatting):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)

