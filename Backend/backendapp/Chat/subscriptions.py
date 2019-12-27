import graphene
from graphene_django.types import DjangoObjectType
from graphene_subscriptions.events import CREATED

from Chat.models import ChatRoom, ChatMessage


class ChatRoomType(DjangoObjectType)
    class Meta:
        model = ChatRoom

class ChatMessageType(DjangoObjectType)
    class Meta:
        model = ChatMessage



class SubscriptionChatting(graphene.ObjectType):
    ChatMessage = graphene.Field(ChatMessageType)

    def resolve_ChatMessage(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, ChatMessage)
        ).map(lambda event: event.instance)

