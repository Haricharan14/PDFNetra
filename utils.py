import logging
from itertools import islice

def create_chunks(iterable, chunk_size):
    """Create chunks of specified size from iterable"""
    iterator = iter(iterable)
    return iter(lambda: list(islice(iterator, chunk_size)), [])

def save_to_markdown(filepath, content, append=False):
    """Save content to markdown file"""
    mode = 'a' if append else 'w'
    with open(filepath, mode, encoding='utf-8') as f:
        f.write(content + '\n\n')

def setup_logger():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)
