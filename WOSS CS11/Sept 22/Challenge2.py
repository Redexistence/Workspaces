def majorityElement(nums):
	"""Return the element that appears more than half the time."""
	candidate = None
	count = 0

	for number in nums:
		if count == 0:
			candidate = number
		count += 1 if number == candidate else -1

	return candidate