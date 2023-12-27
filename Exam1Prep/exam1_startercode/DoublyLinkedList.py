class DLLNode:
	def __init__(self, item, link, prev):
		"""LL Nodes have an item and a link to the next node"""
		self.item = item
		self.link = link
		self.prev = prev

	def __repr__(self):
		"""String representation of an LLNode"""
		return f"DLLNode({self.item})"

class DoublyLinkedList:
	def __init__(self):
		"""Linked Lists have a head, a tail, and a length"""
		self._head = None
		self._tail = None
		self._len = 0

	def __len__(self):
		"""Returns the number of nodes in the Doubly Linked List"""
		return self._len

	def __repr__(self):
		"""String representation of a DoublyLinkedList"""
		return f"DoublyLinkedList: head-->{self._head}, tail-->{self._tail}"

	def add_first(self, item):
		"""Adds node to front of DLL"""
		node = DLLNode(item, link=self._head, prev=None)	# create node
		self._head = node									# update head
		if len(self) == 0: self._tail = self._head			# update tail (edge case)
		else: self._head.link.prev = node					# update old head.prev
		self._len += 1										# increment length

	def remove_first(self):
		"""Removes and returns first item from LL"""
		item = self._head.item					# retrive item
		self._head = self._head.link			# update new head node
		if self._head is not None: self._head.prev = None
		else: self._tail = None
		self._len -= 1							# decrement length
		return item								# return