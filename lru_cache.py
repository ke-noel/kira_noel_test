from uhashring import HashRing
from server_node import ServerNode

class LRUCache():
	'''
	A least-recently used cache
	    * distributed, composed of server nodes (each server is a node)
	    * resize cluster dynamically
	    * each server node can have a custom MAX_SIZE and TIMEOUT
	    * data entries can expire if they are not called within TIMEOUT
	    * the LRU data entries are evicted first if MAX_SIZE is exceeded
	    * roughly even distribution of keys between server nodes

	This implementation combines a hash ring with consistent hashing and a 
	doubly-linked list.
	'''
	def __init__(self, load_function):
		'''
		params:
		    load_function: on a cache miss, this function will be used to 
		    		   load a value into the cache, given a key
		'''
		self.load_function = load_function
		self.hr = HashRing(nodes=[])
		self.servers = {}

	def add_server(self, id, MAX_SIZE, TIMEOUT):
		'''
		Add a server to the ring. 

		params:
		    id: to identify the server
		    MAX_SIZE: int, max number of entries in the server
		    TIMEOUT: int or float, seconds after use before an entry times 
		    	     out and is removed from the cache
		'''
		self.servers[id] = ServerNode(id, self.load_function, MAX_SIZE, TIMEOUT)
		self.hr.add_node(id)

	def remove_server(self, id):
		'''
		Remove a server from the ring.
		'''
		del self.servers[id]
		self.hr.remove_node(id)
	
	def get(self, key):
		'''
		Return the value corresponding with a given key.
		'''
		target_server_id = self.hr.get_node(key)
		return self.servers[target_server_id].get(key)	

	def get_state(self):
		'''
		Return dictionary in form {server_id: list of server nodes}
		'''
		server_contents = {}
		if len(self.servers) > 0:
			for server in self.servers:
				server_contents[server] = self.servers[server].get_state()
		return server_contents
