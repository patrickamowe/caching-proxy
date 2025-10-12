import time
import requests

cache = {}  # dictionary to hold cached data

def get_from_cache(url):
    """
    Get the response data from cache.
    :param url: Address or the location.
    :return: The response data and the state of the data.
    """

    entry = cache.get(url)
    if not entry:
        return None, "MISS"

    age = time.time() - entry["timestamp"]
    if age < entry["ttl"]:
        return entry["data"], "FRESH"
    else:
        return entry["data"], "STALE"

def fetch_response(url, ttl=60):
    """
    Fetch the response of the get request.
    :param url: Address or the location.
    :param ttl: Time to live in cache for the response data.
    :return: The response data.
    """

    cached_data, status = get_from_cache(url)

    if status == "FRESH":
        print("✅ Serving from cache (fresh)")
        return cached_data

    headers = {}
    if cached_data and "etag" in cache[url]:
        headers["If-None-Match"] = cache[url]["etag"]

    response = requests.get(url, headers=headers)

    if response.status_code == 304:
        # Cache is still valid
        print("♻️ Validated cache (still fresh)")
        cache[url]["timestamp"] = time.time() # Update the timestamp to the current time
        return cache[url]["data"]
    else:
        # New data or no cache
        print("🌐 Fetching new content")
        cache[url] = {
            "data": response.text,
            "timestamp": time.time(),
            "ttl": ttl,
            "etag": response.headers.get("ETag")
        }
        return response.text

def invalidate_cache():
    """Clear all the response store in cache"""

    cache.clear()
    print("🧹 All cache cleared")