def search_range(nums, target):
	"""Return the first and last positions of target in sorted nums."""

	def bound(find_first):
		left, right = 0, len(nums) - 1
		result = -1

		while left <= right:
			middle = (left + right) // 2
			if nums[middle] == target:
				result = middle
				if find_first:
					right = middle - 1
				else:
					left = middle + 1
			elif nums[middle] < target:
				left = middle + 1
			else:
				right = middle - 1

		return result

	return [bound(True), bound(False)]