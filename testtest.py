import requests
import json

# url = "https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=5"
# a = requests.get(url).json()
# with open("testtest.json" , "w") as file:
#     json.dump(a,file,indent=4)

# url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
# a = requests.get(url).json()
# with open("testtest_post.json" , "w") as file:
#     json.dump(a,file,indent=4)
url = "https://randomuser.me/api/?results=5"
a = requests.get(url).json()
with open("testtest_user.json" , "w") as file:
    json.dump(a,file,indent=4)