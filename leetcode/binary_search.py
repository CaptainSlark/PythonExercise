def binary_search(array, key):
    #sorted array
    low = 0
    high = len(array) - 1

    while(low <= high):
	mid = (low + high)//2
	midval = array[mid]
	if midval > key:
	    high = mid - 1
	elif midval < key:
	    low = mid + 1
	else:
	    return mid
