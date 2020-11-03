import random
import time
from copy import deepcopy


def merge_lists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(left_sublist) and j<len(right_sublist):
		#if left value is lower than right then append it to the result
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(right_sublist[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += left_sublist[i:]
	result += right_sublist[j:]
	#return the result
	return result

def merge_sort(input_list):
	#if list contains only 1 element return it
	if len(input_list) <= 1:
		return input_list
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(input_list)/2)
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		#return the merged list using the merge_list function above
		return merge_lists(left_sublist,right_sublist)

def insertionsort(A):
    #we start loop at second element (index 1) since the first item is already sorted
    for j in range(1,len(A)):
        key = A[j] #The next item we are going to insert into the sorted section of the array

        i = j-1 #the last item we are going to compare to
        #now we keep moving the key back as long as it is smaller than the last item in the array
        while (i > -1) and key < A[i]: #if i == -1 means that this key belongs at the start
            A[i+1]=A[i] #move the last object compared one step ahead to make room for key
            i=i-1 #observe the next item for next time.
        #okay i is not greater than key means key belongs at i+1
        A[i+1] = key
    return A

def tim_sort(input_list, k):
    if len(input_list) == 1:
        return input_list
    elif len(input_list) <= k:
        return insertionsort(input_list)
    else:
        #split the lists into two sublists and recursively split sublists
        midpoint = int(len(input_list)/2)
        left_sublist = tim_sort(input_list[:midpoint], k)
        right_sublist = tim_sort(input_list[midpoint:], k)
        #return the merged list using the merge_list function above
        return merge_lists(left_sublist,right_sublist)

if __name__ == "__main__":
	# number_list = [3,1,5,3,2,5,8,2,9,6,12,53,75,22,83,123,12123]
	# print(tim_sort(number_list, 5))

	cases = [2, 5, 10, 25, 50, 75, 100, 200, 500, 1000]
	ns = [10, 50, 100, 500, 1000, 5000]

	# dictionary with a key of N and a value of a dictionary with key: k and value: 10 execution times
	all_times = {}

	for n in ns:

		times = {}

		sample = []
		for _ in range(n):
			sample.append(random.randint(0, 1000000))

		for k in cases:

			times[k] = []
			
			for i in range(10):

				if n <= 100:
					start = time.time()
					for _ in range(1000):
						tim_sort(deepcopy(sample), k)
					duration = (time.time() - start) / 1000.0
				else:
					start = time.time()
					for _ in range(10):
						tim_sort(deepcopy(sample), k)
					duration = (time.time() - start) / 10.0

				times[k].append(duration)

		all_times[n] = times

	for n, times in all_times.items():
		print("N = " + str(n))
		for k, durations in times.items():
			print("K: " + str(k))
			print(sum(durations) / len(durations))
		print()
		
		

		
