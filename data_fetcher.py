import aiohttp
import asyncio

#=======================================
async def fetch_github_repos(session):
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=5"
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Bad status : {response.status} ")
                return None
            data =await response.json()
            return data
    except asyncio.TimeoutError:
        print("Timeout error!")
        return None
    except aiohttp.ClientError as e:
        print(f"Error : {e}")
        return None
#=======================================
async def fetch_posts(session):
    url = "https://jsonplaceholder.typicode.com/posts?_limit=5"
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Bad status : {response.status} ")
                return None
            data =await response.json()
            return data
    except asyncio.TimeoutError:
        print("Timeout error!")
        return None
    except aiohttp.ClientError as e:
        print(f"Error : {e}")
        return None
#=======================================
async def fetch_users(session):
    url = "https://randomuser.me/api/?results=5"
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Bad status : {response.status} ")
                return None
            data =await response.json()
            return data
    except asyncio.TimeoutError:
        print("Timeout error!")
        return None
    except aiohttp.ClientError as e:
        print(f"Error : {e}")
        return None
#=======================================
async def fetch_all_data():
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        
        github , posts , users = await asyncio.gather(
            fetch_github_repos(session),
            fetch_posts(session),
            fetch_users(session)
        )
        return {
            'github': github,
            'posts': posts,
            'users': users
        }
#=======================================

if __name__ == '__main__':
    result = asyncio.run(fetch_all_data())
    print(result)
