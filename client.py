from lru_cache import LRUCache
import time

def load(key):
	'''
	Placeholder
	'''
	return key

def print_state(cache):
	'''
	Print the contents of each server node.
	'''
	state = cache.get_state()
	print('current state:')
	for id in state:
		print(id,end=' ')
		print([n.key for n in state[id]])

TIMEOUT = 0.5
MAX_SIZE = 5

cache = LRUCache(load)
cache.add_server("a", MAX_SIZE, TIMEOUT)
cache.add_server("b", MAX_SIZE, TIMEOUT)
cache.add_server("c", MAX_SIZE, 2)

for i in range(20):
	print('%d: %d' %(i, cache.get(i)))

print_state(cache)
cache.get(6)
print_state(cache)
