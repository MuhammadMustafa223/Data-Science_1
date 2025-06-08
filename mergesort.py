import matplotlib.pyplot as plt


def assign_value(target_list, target_index, source_list, source_index):
    """
    Assigns a value from source_list[source_index] to target_list[target_index].
    This function abstracts value assignment for clarity.
    """
    target_list[target_index] = source_list[source_index]


def merge_sort(array):
    """
    Sorts the input array in-place using the Merge Sort algorithm.

    Parameters:
    array (list): A list of comparable elements.
    """
    if len(array) <= 1:
        return  # Base case: already sorted

    # Divide the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge sorted halves back into array
    left_index = right_index = merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            assign_value(array, merged_index, left_half, left_index)
            left_index += 1
        else:
            assign_value(array, merged_index, right_half, right_index)
            right_index += 1
        merged_index += 1

    # Copy remaining elements of left_half
    while left_index < len(left_half):
        array[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    # Copy remaining elements of right_half
    while right_index < len(right_half):
        array[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


# Main Execution with Visualization 

# Unsorted list
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot before sorting
plt.plot(range(len(my_list)), my_list)
plt.title("Before Sorting")
plt.show()

# Sort the list
merge_sort(my_list)

# Plot after sorting
plt.plot(range(len(my_list)), my_list)
plt.title("After Sorting")
plt.show()
