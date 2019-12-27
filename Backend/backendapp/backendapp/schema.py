import graphene
import Chat.schema
from Chat.subscriptions import SubscriptionChatting


class Query(graphene.ObjectType, Chat.schema.Query):
    pass

class Mutation(graphene.ObjectType, Chat.schema.Mutation):


class Subscription(SubscriptionChatting):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)

