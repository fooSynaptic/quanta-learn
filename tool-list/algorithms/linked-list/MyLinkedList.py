# py3


class MyLinkedList:
	class Node:
		def __init__(self, val):
			self.val = val
			self.next = None

	def __init__(self):
		#pre_head is a virtual node before head to simple the ops
		self.pre_head = self.Node(None)
		self.sz = 0


	#main workhorse: given index i, return (pre, h)
	# h is the i-th node or None
	#pre is the node before h

	def _get(self, i):
		j = 0
		h = self.pre_head.next
		pre = self.pre_head

		while j < i and h:
			j += 1
			pre = h
			h = h.next

		return (pre, h)


	def get(self, i):
		(_, h) = self._get(i)
		return h.val if h else -1


	def addAtHead(self, val):
		self.addAtIndex(0, val)


	def addAtTail(self, val):
		self.addAtIndex(self.sz, val)


	def addAtIndex(self, i, val):
		if i > self.sz:
			return
		(pre, _) = self._get(i)
		node = self.Node(val)
		node.next = pre.next
		pre.next = node
		self.sz += 1


	def deleteAtIndex(self, i):
		if i < 0 or i >= self.sz:
			return
		(pre, h) = self._get(i)
		pre.next = h.next
		self.sz -= 1


