import re

def is_valid_url(url: str) -> bool:
    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'([\da-z.-]+)\.([a-z.]{2,6})'
        r'([\/\w .-]*)*\/?$'
    )
    return bool(pattern.match(url))
