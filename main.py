import graphene
from datetime import datetime
import json

class User(graphene.ObjectType, first = graphene.Int()):
    id = graphene.ID()
    first = graphene.String()
    last = graphene.String()
    last_login = graphene.DateTime()

usersList = [
    User(first = "Reo", last = "Yamanaka", last_login = datetime.now()),
    User(first = "Reo", last = "Yamanaka", last_login = datetime.now())
    User(first = "Reo", last = "Yamanaka", last_login = datetime.now())
]


