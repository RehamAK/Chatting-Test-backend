import graphene
from graphene_django import DjangoObjectType


from Chat.models import ChatRoom, ChatMessage


class ChatRoomType(DjangoObjectType)
    class Meta:
        model = ChatRoom

class ChatMessageType(DjangoObjectType)
    class Meta:
        model = ChatMessage

class Query(graphene.ObjectType):
    Messages = graphene.List(ChatMessageType)


    def resolve_Messages(self, info):
        return ChatMessage.objects.all()


class CreateMessage(graphene.Mutation):

    CreateMessage = graphene.Field(ChatMessageType)
    createRoom = graphene.Field(ChatRoom)


    class Arguments:
        Message = graphene.String(required=True)
        fromUser = graphene.String(required=True)
        toUser = graphene.String(required=True)


    def mutate(self, info, Message, fromUser, toUser):
        createRoom = ChatRoom.objects.create(fromUser=fromUser, toUser=toUser)
        
        CreateMessage = ChatMessage.objects.create(RoomID=createRoom,Message=Message)

        createRoom.save()
        CreateMessage.save()
        return CreateMessage(createRoom=createRoom,CreateMessage=CreateMessage)


class Mutation(graphene.ObjectType):
    create_message = CreateMessage.Field()
