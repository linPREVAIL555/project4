import collections
lst = []
num = int(input('How many numbers: '))
for n in range(num):
	numbers = int(input('Enter number '))
	lst.append(numbers)
print("Mean: ", sum(lst)/num)
print("Maximum: ", max(lst))
print("Minimum: ", min(lst))




 
if len(lst) % 2 == 0: 
    median1 = lst[n//2] 
    median2 = lst[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = lst[n//2] 
print("Median: " + str(median)) 



data = collections.Counter(lst)
data_list = dict(data)
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(lst):
   print("No mode in the list")
else:
   print("Mode: " + ', '.join(map(str, mode_val)))


print("Range: ",max(lst)-min(lst))
