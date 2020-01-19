import datetime

class DataNode():
	'''
	Hold a key, value, and the time of most recent use. 
	'''
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None
		self.last_used_time = datetime.datetime.now()

	def get(self):
		'''
		Return the current value and update the time
		'''
		self.last_used_time = datetime.datetime.now()
		return self.value
 
	def time_since_use(self):
		'''
		In seconds
		'''
		return (datetime.datetime.now() - self.last_used_time).seconds 


class DLL():
	'''
	Doubly-Linked List
	  * ordered from most recently used (head) to least recently used (tail)
	  * when the list reaches MAX_SIZE, the least-recently used is evicted
	  * nodes can expire; if a node is not called within TIMEOUT, it and all 
	    following nodes are deleted on the next get request
	  * iterable for debugging, testing
	'''
	def __init__(self, MAX_SIZE, TIMEOUT):
		self.head = None
		self.tail = None
		self.size = 0
		self.MAX_SIZE = MAX_SIZE
		self.TIMEOUT = TIMEOUT

	def __iter__(self):
		self.current = self.head
		return self

	def __next__(self):
		if self.current is None:
			raise StopIteration
		else:
			result = self.current
			self.current = self.current.next
			return result

	def add(self, key, value):
		'''
		Add a node to the head of the list.
		'''
		if self.size >= self.MAX_SIZE:
			self.removeLRU()
		new = DataNode(key, value)
		self.size += 1
		self.insert_at_head(new)

	def insert_at_head(self, node):
		'''
		Place a node at the head of the list.
		'''
		if self.head is None:
			self.head = node
			self.head.next = None
			self.head.prev = None
			self.tail = self.head
		else:
			node.prev = None
			node.next = self.head
			node.next.prev = node
			self.head = node

	def removeLRU(self):
		'''
		Remove the least-recently used node (the tail).
		'''
		self.size -= 1;
		self.tail = self.tail.prev
		self.tail.next = None

	def get(self, key):
		'''
		Returns: value of DataNode if found, otherwise None

		If it hits a node that has timed out, it and all nodes after it are 
		deleted. 
		'''
		# Empty list
		if self.head is None:
			return None
		# Non-empty list
		index = 0
		for node in self:
			if node.key == key:
				# Move node to the front and return value
				if node != self.head:
					if node == self.tail:
						node.prev.next = None
						self.tail = node.prev
					else:
						node.next.prev = node.prev
						node.prev.next = node.next
					self.insert_at_head(node)
				return node.get()
			elif node.time_since_use() > self.TIMEOUT:
				# All further entries are timed out
				if node == self.head:
					self.head = None
					self.tail = None
				else:
					node.prev.next = None
					self.tail = node.prev
				self.size = index
				return None
			index += 1
