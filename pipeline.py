import asyncio
from data_fetcher import fetch_all_data
from data_processor import process_items, filter_by_source, transform_data

async def run_pipeline(source_filter=None):
    first_data = await fetch_all_data()
    second_data = process_items(first_data)
    if source_filter is not None:
        second_data = filter_by_source(second_data , source_filter)
        
    fourth_data =  transform_data(second_data)
    return list(fourth_data)


if __name__ == "__main__":
    print("=== ALL SOURCES ===")
    result = asyncio.run(run_pipeline())
    for item in result:
        print(item)
    
    print("\n=== GITHUB ONLY ===")
    result = asyncio.run(run_pipeline(source_filter='github'))
    for item in result:
        print(item)