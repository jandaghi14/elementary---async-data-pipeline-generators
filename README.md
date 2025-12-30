# Async Data Pipeline

A Python application demonstrating the combination of asynchronous programming and generators for efficient data fetching and processing from multiple APIs.

## Features

- **Async API Fetching**: Concurrent data retrieval from 3 different APIs using asyncio
- **Generator Processing**: Memory-efficient data processing with generator chaining
- **Data Transformation**: Standardizes different data formats into common structure
- **Flexible Filtering**: Filter results by data source
- **Production Patterns**: Combines async/await with generator pipelines

## Technologies Used

- **Python 3.7+**
- **aiohttp** - Async HTTP client for API calls
- **asyncio** - Asynchronous programming
- **Generators** - Memory-efficient data processing
- **pytest** - Testing framework
- **aioresponses** - Mocking async HTTP responses

## Architecture

### Data Sources

The pipeline fetches data from three public APIs:

1. **GitHub API** - Python repositories sorted by stars
2. **JSONPlaceholder** - Sample blog posts
3. **Random User API** - Random user profiles

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    ASYNC FETCH LAYER                        │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│  │ GitHub   │    │  Posts   │    │  Users   │             │
│  │   API    │    │   API    │    │   API    │             │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘             │
│       └──────────┬─────┴──────────┘                        │
│                  │ asyncio.gather()                         │
└──────────────────┼──────────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                 GENERATOR PROCESSING LAYER                  │
│                                                              │
│  1. process_items()     → Flatten all sources               │
│  2. filter_by_source()  → Optional filtering                │
│  3. transform_data()    → Standardize format                │
│                                                              │
└──────────────────┬──────────────────────────────────────────┘
                   ▼
            Unified Data Output
```

## Components

### 1. data_fetcher.py

Async functions for fetching data:

- `fetch_github_repos(session)` - Fetch top Python repos
- `fetch_posts(session)` - Fetch sample posts
- `fetch_users(session)` - Fetch random users
- `fetch_all_data()` - Fetch all sources concurrently

### 2. data_processor.py

Generator functions for processing:

- `process_items(data_dict)` - Flatten nested data, add source tags
- `filter_by_source(items, source)` - Filter by data source
- `transform_data(items)` - Transform to common format

### 3. pipeline.py

Main pipeline orchestration:

- `run_pipeline(source_filter=None)` - Complete async + generator pipeline

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/async-data-pipeline.git
cd async-data-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage - All Sources

```python
import asyncio
from pipeline import run_pipeline

# Fetch and process all data sources
result = asyncio.run(run_pipeline())

for item in result:
    print(item)
```

### Filtered Usage - Single Source

```python
# Get only GitHub repos
github_only = asyncio.run(run_pipeline(source_filter='github'))

# Get only posts
posts_only = asyncio.run(run_pipeline(source_filter='posts'))

# Get only users
users_only = asyncio.run(run_pipeline(source_filter='users'))
```

### Run Demo

```bash
python pipeline.py
```

## Output Format

All data is transformed to a common format:

```python
{
    'source': 'github' | 'posts' | 'users',
    'name': str,
    'data': str
}
```

### Examples

**GitHub:**
```python
{'source': 'github', 'name': 'django', 'data': '75000 stars'}
```

**Posts:**
```python
{'source': 'posts', 'name': 'Post Title', 'data': 1}
```

**Users:**
```python
{'source': 'users', 'name': 'John Doe', 'data': 'john@example.com'}
```

## Error Handling

The fetcher includes comprehensive error handling:

- **Timeout errors**: 10-second timeout per request
- **HTTP errors**: Non-200 status codes
- **Network errors**: Connection failures
- **Graceful degradation**: Failed sources return None without crashing

## Project Structure

```
async-data-pipeline/
├── data_fetcher.py          # Async API fetching
├── data_processor.py        # Generator processing
├── pipeline.py              # Main pipeline
├── test_pipeline.py         # Test suite
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

## Why This Pattern?

### Async Benefits
- **Speed**: Fetch from 3 APIs concurrently (not sequentially)
- **Efficiency**: Non-blocking I/O operations
- **Scalability**: Easily add more data sources

### Generator Benefits
- **Memory**: Process items one at a time
- **Lazy Evaluation**: Only compute what's needed
- **Composability**: Chain generators together

### Combined Power
- Fetch fast (async)
- Process efficiently (generators)
- Real-world pattern used in data engineering, ETL pipelines, web scraping

## Real-World Applications

- **Data Aggregation**: Combine multiple API sources
- **ETL Pipelines**: Extract, Transform, Load workflows
- **Web Scraping**: Concurrent scraping with efficient processing
- **Monitoring Dashboards**: Fetch from multiple services
- **API Gateways**: Aggregate and normalize data

## Performance

**Sequential (without async):**
```
GitHub: 2s
Posts: 2s
Users: 2s
Total: 6 seconds
```

**Concurrent (with async):**
```
All 3 APIs: 2s (parallel)
Processing: <1s
Total: ~3 seconds
```

**50% faster!**

## Future Enhancements

- Add caching layer (Redis)
- Implement retry logic with exponential backoff
- Add more data sources
- Stream processing for real-time updates
- Data validation with Pydantic
- Metrics and monitoring
- Rate limiting
- Database persistence

## Learning Goals

This project demonstrates:
- ✅ Async/await patterns
- ✅ asyncio.gather() for concurrency
- ✅ Generator functions
- ✅ Generator chaining
- ✅ Error handling in async code
- ✅ API integration
- ✅ Data transformation
- ✅ Production-ready patterns

## License

MIT License