# Summary
This is a distributed LRU cache with time expiration. It is implemented using a hash ring with consistent hashing and a doubly-linked list in Python.
<br><br>
The cache maps server nodes (servers) to roughly equidistant points in a circle. When the cache receives a get request, the key is hashed and placed onto the same circle. The closest server node (clockwise) is chosen. If the cache contains an entry corresponding to that key, it will be on that server, so the cache routes the get request to this server node. The server node iterates through a doubly-linked list containing all of its data nodes for a matching key. If one is found (cache hit), the corresponding value is returned and the data node is moved to the head. If there's no match (cache miss), the server node uses a predefined load function to load the corresponding data into the cache.
<br><br>
Note: expired cache entries (data nodes whose time since last access has exceeded the value specified in its configuration) are only removed when a get request is made to a server with expired entries and the key is not found before reaching an expired entry.

## The Challenge
Write a geo distributed LRU (least recently used) cache with time expiration. It should meet the following criteria:

* Simplicity. Integration needs to be dead-simple.
* Resilient to network failures or crashes.
* Near real time replication of data across locations. Writes need to be in real time.
* Data consistency across regions.
* Locality of reference, data should almost always be available from the closest region.
* Flexibile schema.
* Cache can expire.

## Adressing the design criteria
* Simple. The interface is very simple:
	* get(key)
	* add\_server(id, configurations)
	* remove\_server(id)

* Resilient to network failures and crashes. Using consistent hashing allows for dynamic addition and removal of nodes, so if a server fails or if we were to add new servers, there wouldn't be any major problems.

* Flexible schema. There's no real limit to what the key maps to.

* The cache can expire, and this time to expiration can be customized for each server.

# Example
```python
from lru_cache import LRUCache

def load_function(key):
	'''
	placeholder
	'''
	return key

TIMEOUT = 3  # 3 seconds
MAX_SIZE = 10  # 10 items

cache = LRUCache(load_function)
cache.add_server('a', MAX_SIZE, TIMEOUT)
cache.add_server('b', MAX_SIZE, TIMEOUT)

for i in range(30)
	print(cache.get(i))

cache.remove_server('a')
```

For more sample usages, see client.py.

# Still to do
* I didn't really address the geolocation element. My idea would be to attach location data attached to server nodes and get requests to the cache. The cache would route the request to the nearest local cluster of server nodes.
* I tested manually, but with more time, I would add unit tests.
* Better documentation.
* Currently, expired entries are only removed when the server node containing the expired entries receives a get request. It might be better to have a function that checks regularly if there are expired entries.
