


def process_items(data_dict):
    for item in data_dict['github']['items']:
        item['source'] = 'github'
        yield item
    for item in data_dict['posts']:
        item['source'] = 'posts'
        yield item
    for item in data_dict['users']['results']:
        item['source'] = 'users'
        yield item
        
def filter_by_source(items, source):
    for item in items:
        if item['source'] == source:
            yield item

def transform_data(items):
    for item in items:
        if item['source'] == 'github': 
            yield {
                'name': item['name'], 
                'data': f"{item['stargazers_count']} stars", 
                'source': 'github'
                }
        elif item['source'] == 'posts': 
            yield {
                'data': item['id'], 
                'name':item['title'], 
                'source': 'posts'}
        elif item['source'] == 'users': 
            yield {
                'source': 'users', 
                'name': item['name']['first'] + ' ' + item['name']['last'], 
                'data': item['email']}
    