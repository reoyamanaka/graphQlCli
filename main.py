import graphene
from datetime import datetime
import json

class User(graphene.ObjectType):
    first = graphene.String()
    last = graphene.String()
    last_login = graphene.DateTime()

usersList = [
    User(first = "Reo", last = "Yamanaka", last_login = datetime.now()),
    User(first = "Stacy", last = "Smith", last_login = datetime.now()),
    User(first = "Livia", last = "Jackson", last_login = datetime.now())
]

class Query(graphene.ObjectType):
    all_users = graphene.List(User, showCount = graphene.Int())
    
    def resolve_all_users(self, info, showCount):
        return usersList[:showCount]

def customQuery(option, show = len(usersList)):
    return """
    {
        %s(showCount: %d) {
            first
            last
            lastLogin
        }
    }
    """%(option, show)

def main():
    schema = graphene.Schema(query = Query)
    while True:
        firstAction = input("What would you like to do?\n1) See all users\n2) See some users\n")
        if firstAction == "1":
            query = customQuery("allUsers")
            print(query)
            break

    result = schema.execute(query)
    items = dict(result.data.items())
    print(json.dumps(items, indent = 4))
    #break
                    

if __name__ == "__main__":
    main()
