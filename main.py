#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER number_of_socks
#  2. INTEGER_ARRAY socks_color_array
#

def sock_merchant(number_of_socks, socks_color_array):
    # Write your code here
    colour_count_dict = {}
    for colour in socks_color_array:
        if colour not in colour_count_dict:
            colour_count_dict[colour] = 1
        else:
            colour_count_dict[colour] += 1

    total_pairs_count = 0
    for key in colour_count_dict:
        total_pairs_count += colour_count_dict[key] // 2

    print("Of the {} socks, there are only {} valid pairs".format(number_of_socks, total_pairs_count))
    return total_pairs_count


# Test cases
# Case 1: 10 elements, 4 pairs
sock_merchant(number_of_socks=10, socks_color_array=[1, 2, 1, 3, 4, 2, 5, 4, 1, 3])

# Case 2: 30 elements, 10 pairs
sock_merchant(number_of_socks=30,
              socks_color_array=[1, 11, 1, 13, 14, 2, 5, 4, 15, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 7, 8, 9,
                                 10, 12])

# Case 3: 80 elements, 36 pairs
sock_merchant(number_of_socks=80,
              socks_color_array=[1, 2, 1, 3, 4, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1,
                                 31, 12, 23, 14, 35, 46, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 2,
                                 5, 4, 1, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1, 3, 1, 2, 1, 3, 4, 2, 5, 4, 1, 3])
