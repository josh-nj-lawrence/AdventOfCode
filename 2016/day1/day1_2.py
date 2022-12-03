from collections import deque

class HashTable:

	# Create empty bucket list of given size
	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]

	# Insert values into hash map
	def set_val(self, key, val):
		
		# Get the index from the key
		# using hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be inserted
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key to be inserted,
		# Update the key value
		# Otherwise append the new key-value pair to the bucket
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	# Return searched value with specific key
	def get_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key being searched
			if record_key == key:
				found_key = True
				break

		# If the bucket has same key as the key being searched,
		# Return the value found
		# Otherwise indicate there was no record found
		if found_key:
			return record_val
		else:
			return "No record found"

	# Remove a value with specific key
	def delete_val(self, key):
		
		# Get the index from the key using
		# hash function
		hashed_key = hash(key) % self.size
		
		# Get the bucket corresponding to index
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# check if the bucket has same key as
			# the key to be deleted
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	# To print the items of hash map
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)

class Solution:
    def solution(filename):
        with open(filename) as file:
            line = file.readline().split(sep=", ")
        
        # Solve Problem
        visted = HashTable(1000)
        x,y = 0,0
        directions = deque(["N","W","S","E"])
        dir = "N"
        for i in line:
            #Change direction
            [directions.rotate(1) if i[0] =="R" else directions.rotate(-1)]
            dir = directions[1] 

            # Move
            if dir == "E":
                for x in range(x,x+int(i[1:])):
                    visted.set_val([x,y], visted.get_val([x,y])+1)
                    if visted.get_val([x,y]) > 1:
                        return x+y
                x += int(i[1:])
            elif dir == "W":
                for x in range(x-int(i[1:]),x):
                    visted.set_val([x,y], visted.get_val([x,y])+1)
                    if visted.get_val([x,y]) > 1:
                        return x+y
                x -= int(i[1:])
            elif dir == "N":
                for y in range(y,int(i[1:])):
                    if visted.get_val([x,y]) > 1:
                        return x+y
                    visted.set_val((str(x)+":"+str(y)), visted.get_val([x,y])+1)
                y += int(i[1:])
            else:
                for y in range(y-int(i[1:]),y):
                    visted.set_val([x,y], visted.get_val([x,y])+1)
                    if visted.get_val([x,y]) > 1:
                        return x+y
                y -= int(i[1:])
solution = Solution
print(solution.solution("day1_input.txt"))