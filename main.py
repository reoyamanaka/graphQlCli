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

def customQuery(option, show = length):
    return """
    {
        %s(first: %d) {
            first
            last
            lastLogin
        }
    }
    """%option

def main():
    while True:
        firstAction = input("What would you like to do?\n1) See all users\n2) See some users\n")
        if firstAction == "1":
            print("Showing all users...\n")
            query = customQuery("allUsers")
            break
        elif firstAction == "2":
            print("Showing some users...\n")
    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent = 4))

                    

if __name__ == "__main__":
    main()
