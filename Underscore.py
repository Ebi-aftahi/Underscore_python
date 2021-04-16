class Underscore:
	def map(self, iterable, callback):
		# changes and maps the elements to a new one
		for i in range(len(iterable)):
			iterable[i] = callback(iterable[i])			
		return iterable
		
	def find(self, iterable, callback):
		# returns the first value that is true for the condition in lambda
		for i in range(len(iterable)):
			if callback(iterable[i]):
				return iterable[i]
		return None
	
	def filter(self, iterable, callback):
		# Filters over iterable, returns new iterable that meets condition(Even/Odd)
		new_iterable = []
		for i in range(len(iterable)):
			if callback(iterable[i]):
				new_iterable.append(iterable[i])
		return new_iterable
		
	def reject(self, iterable, callback):
		# Filters over iterable, returns new iterable that do NOT meet condition(Even/Odd)
		new_iterable = []
		for i in range(len(iterable)):
			if  not callback(iterable[i]):
				new_iterable.append(iterable[i])
		return new_iterable
		
			
_ = Underscore()	
print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]
		

