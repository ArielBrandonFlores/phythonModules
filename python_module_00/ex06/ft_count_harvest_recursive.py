def	ft_count_harvest_recursive():
	day = int(input("Days until harvest: "))

	def helper(current_days, total_days):
		if current_days > total_days:
			print("Harvest time!")
			return
		print(f"Day {current_days}")

		helper(current_days + 1, total_days)
	helper(1, day)
ft_count_harvest_recursive()
