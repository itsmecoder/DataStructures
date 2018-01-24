
input_array = [1,2,3,4,5,6,7,8,9]
key = 2


def rotate_array(input_array, key):
	if not input_array or key < 0:
		raise ValueError("Invalid inputs. Please provide valid inputs to rotate array")

	if key == len(input_array):
		return input_array

	if key > len(input_array):
		key = key % len(input_array)

	result = []

	for num in input_array[key:]:
		result.append(num)

	for num in input_array[0:key]:
		result.append(num)

	return result

def _rotate_array_element_by_one(input_array):
	temp = input_array[0]
	for i in range(len(input_array)-1):
		input_array[i] = input_array[i+1]

	input_array[len(input_array)-1] = temp
	#return input_array


def rotate_array_efficient(input_array, key):
    if not input_array or key < 0:
        raise ValueError("Invalid inputs. Please provide valid inputs to rotate array")

    if key == len(input_array):
        return input_array

    if key > len(input_array):
        key = key % len(input_array)

    for index in range(key):
        _rotate_array_element_by_one(input_array)

    return input_array


if __name__ == '__main__':
	print rotate_array(input_array, key)
	print rotate_array_efficient(input_array, key)