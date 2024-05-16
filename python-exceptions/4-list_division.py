#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    result = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i] if i < len(my_list_1) else 0
                num2 = my_list_2[i] if i < len(my_list_2) else 0

                if isinstance(num1, (int, float)) and \
                        isinstance(num2, (int, float)):
                    try:
                        result.append(num1 / num2)
                    except ZeroDivisionError:
                        result.append(0)
                        print("division by 0")
                else:
                    print("wrong type")
                    result.append(0)
            except IndexError:
                print("out of range")
                break
    finally:
        print("out of range")
        return result
