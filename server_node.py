from dll import DLL

class ServerNode():
	def __init__(self, id, load_function, MAX_SIZE, TIMEOUT):
		'''
		params:
		    id: unique identifier
		    load_function: if there's a cache miss, use this function to load
		    		   the value associated with a given key
		    MAX_SIZE: int, maximum number of items the ServerNode can hold
		    TIMEOUT: int/float, seconds until a node times out from unuse
		'''
		self.id = id
		self.load_function = load_function
		self.nodes = DLL(MAX_SIZE, TIMEOUT) 

	def get_state(self):
		'''
		returns: list of current nodes
		'''
		nodes = []
		for node in self.nodes:
			nodes.append(node)
		return nodes

	def get(self, key):
		'''
		returns: value associated with given key

		If a key is not found, load the data into the cache and return.
		'''
		result = self.nodes.get(key)
		if result is None:
			value = self.load_function(key)
			self.nodes.add(key, value)
			return value
		else:
			return result
