#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    result = []
    division_by_zero = False
    wrong_type = False
    out_of_range = False

    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i] if i < len(my_list_1) else None
                num2 = my_list_2[i] if i < len(my_list_2) else None

                if isinstance(num1, (int, float)) and \
                        isinstance(num2, (int, float)):
                    try:
                        result.append(num1 / num2)
                    except ZeroDivisionError:
                        result.append(0)
                        if not division_by_zero:
                            print("division by 0")
                            division_by_zero = True
                else:
                    if not wrong_type:
                        print("wrong type")
                        wrong_type = True
                    result.append(0)
            except IndexError:
                if not out_of_range:
                    print("out of range")
                    out_of_range = True
                break
    finally:
        if not out_of_range:
            print("out of range")
        return result
