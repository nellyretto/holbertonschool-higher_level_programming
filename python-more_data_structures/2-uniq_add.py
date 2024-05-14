#!/usr/bin/python3


def uniq_add(my_list=[]):

    unique_nums = set()
    total_sum = 0

    for num in my_list:
        if num not in unique_nums:
            unique_nums.add(num)
            total_sum += num

    return total_sum
