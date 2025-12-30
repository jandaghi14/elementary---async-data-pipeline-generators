'''test_fetch_github_repos_success - Mock GitHub API
test_fetch_posts_success - Mock Posts API
test_fetch_users_success - Mock Users API
test_process_items - Test generator yields all items with 'source'
test_filter_by_source - Test filtering works
test_transform_data - Test transformation to common format'''

import pytest
from unittest.mock import patch , Mock
from pipeline import run_pipeline
from aioresponses import aioresponses
import asyncio
import aiohttp
from data_fetcher import fetch_github_repos,fetch_posts,fetch_users
from data_processor import process_items,transform_data,filter_by_source

@pytest.mark.asyncio
async def test_fetch_github_repos_success():
    with aioresponses() as mock:
        fake_response = {'items' : [{ 
                                        'name' : 'alijandaghi',
                                        'stargazers_count' : 5000
            }]}
        mock.get("https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=5" , payload = fake_response)
        async with aiohttp.ClientSession() as session:
            response = await fetch_github_repos(session)
            assert response == fake_response
#=======================================================
@pytest.mark.asyncio
async def test_fetch_posts_success():
    with aioresponses() as mock:
        fake_response = {'items' : [{ 
                                        'name' : 'alijandaghi',
                                        'stargazers_count' : 5000
            }]}
        mock.get("https://jsonplaceholder.typicode.com/posts?_limit=5" , payload = fake_response)
        async with aiohttp.ClientSession() as session:
            response = await fetch_posts(session)
            assert response == fake_response
#=======================================================
@pytest.mark.asyncio
async def test_fetch_users_success():
    with aioresponses() as mock:
        fake_response = {'items' : [{ 
                                        'name' : 'alijandaghi',
                                        'stargazers_count' : 5000
            }]}
        mock.get("https://randomuser.me/api/?results=5" , payload = fake_response)
        async with aiohttp.ClientSession() as session:
            response = await fetch_users(session)
            assert response == fake_response
#=======================================================
def test_process_items():
    fake =data_dict = {
        'github' : {
                    'items' :  [{
                                "id": 54346799,
                                "node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
                                "name": "public-apis"
                    }] 
        },
        'posts' :  [{
                    "userId": 1,
                    "id": 1,
                    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }],
        'users' : {
            "results": 
                [
                    {
                    "gender": "female",
                    "name": {
                        "title": "Ms",
                        "first": "Melodie",
                        "last": "Roy"}
                    } 
                ]
        }
        }
    result = list(process_items(data_dict))
    assert result[0]['source'] == 'github'
    assert result[1]['source'] == 'posts'
    assert result[2]['source'] == 'users'
    
    