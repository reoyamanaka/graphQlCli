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
    User(first = "Stacy", last = "Smith", last_login = datetime.now()),
    User(first = "Livia", last = "Jackson", last_login = datetime.now())
]

class Query(graphene.ObjectType):
    all_users = graphene.List(User)
    
    def resolve_all_users(self, info):
        return usersList

schema = graphene.Schema(query = Query)

result = schema.execute(
    """
    {
        allUsers {
            first
            last
            lastLogin
        }
    }
    """
)
items = dict(result.data.items())
print(json.dumps(items, indent = 4))
