Section 33: Code Example
::::::::::::::::::::::::

Using what we've learned, we can create a script which incrementally learns a concept in a simple domain. As you explore the code below, think about the following questions:

- How might this model incorporate the drop-link heuristic to ignore attributes?

- How might this model be generalized to recognize abstract attributes, e.g. the set of numbers or set of characters? (climb-tree heuristic)

.. activecode:: Chapter10_example
   :nocanvas:
   :language: python

   class Concept(object):
	def __init__(self):
		self.positive_attributes = {}
		self.required_attributes = {}
		self.forbid_attributes   = {}
		self.examples = []

		# background knowledge
		self.characters = 'abcdefghijklmnopqrstuvwxyz'
		self.numbers    = '1234567890'


	def _check_example(self, example):
		# Check if the example has the required attributes
		for idx, attr in self.required_attributes.items():
			if example[idx] not in attr:
				return False, (idx, attr, 0)

		# Check if the example has any forbidden attributes
		for idx, attr in self.forbid_attributes.items():
			if example[idx] in attr:
				return False, (idx, attr, 1)

		# Check if the example's attributes are positive attributes
		for idx, attr in self.positive_attributes.items():
			if example[idx] not in attr:
				return None, (idx, example[idx], 2)

		return bool(self.positive_attributes), (None, None, None)


	def learn_positive_example(self, example):
		is_positive, (idx, attr, flag) = self._check_example(example)

		# If the example isn't already labeled as positive, add the attributes
		if not is_positive:

			# If it's not positive but has been seen, it must have been a negative
			if example in self.examples:
				print 'Conflicting example: "%s"' % example 
				return
			else: self.examples.append(example)

			for idx, attr in enumerate(example):
				if idx not in self.positive_attributes:
					self.positive_attributes[idx] = ''
				if attr not in self.positive_attributes[idx]:
					self.positive_attributes[idx] += attr


	def learn_negative_example(self, example):
		is_positive, (idx, attr, flag) = self._check_example(example)
		
		# Positive class - need to specialize (forbid)
		if is_positive: 
			if example in self.examples:
				print 'Conflicting example: "%s"' % example
				return 
			else: self.examples.append(example)

			# Forbid all attributes which are not positive / required 
			for idx, attr in enumerate(example):
				if idx not in self.positive_attributes or attr not in self.positive_attributes[idx]:
					if idx not in self.required_attributes or attr not in self.required_attributes[idx]:
						if idx not in self.forbid_attributes:
							self.forbid_attributes[idx] = ''
						self.forbid_attributes[idx] += attr

		# Unknown class - need to specialize (require)
		elif is_positive is None:
			print example
			for idx, attr in enumerate(example):
				# if the attribute has been seen in a positive example, switch the 
				# other attributes at that index to be required
				if idx not in self.positive_attributes or attr not in self.positive_attributes[idx]:
					if idx not in self.required_attributes:
						self.required_attributes[idx] = ''
					self.required_attributes[idx] += ''.join([a for a in self.positive_attributes[idx] 
																if a not in self.required_attributes[idx]+attr])


	def is_positive(self, example):
		is_positive, (idx, attr, flag) = self._check_example(example)
		if is_positive: return 'Yes'
		if flag == 0:
			return 'No: "%s" is required attributes at location %i' % (attr, idx)
		if flag == 1:
			return 'No: "%s" is forbidden at location %i' % (attr, idx)
		if flag == 2:
			return 'Unknown: "%s" has not been seen at location %i' % (attr, idx)
		return 'Unknown: no positive examples seen so far'


   if __name__ == '__main__':
	positive_examples = ['abc', 'bbc', 'abb']
	negative_examples = ['cbc']
	check_examples    = ['abc', 'aac', 'cbc','dbc']

	c = Concept()
	for example in positive_examples:
		print 'Learning positive example "%s"' % example
		c.learn_positive_example(example)
	print 

	for example in check_examples:
		print 'Checking example "%s" - %s' % (example, c.is_positive(example))
	print 

	for example in negative_examples:
		print 'Learning negative example "%s"' % example 
		c.learn_negative_example(example)
	print 

	for example in check_examples:
		print 'Checking example "%s" - %s' % (example, c.is_positive(example))
