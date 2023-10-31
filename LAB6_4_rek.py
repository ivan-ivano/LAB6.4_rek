import random


def generate_list(b, i=0):
    if i >= 22:
        return b
    else:
        b.append(random.randint(-40, 50))
        generate_list(b, i + 1)
    return b


def search_min_element_index(lst, min_index=-1, i=0):
    if i >= len(lst):
        return min_index
    else:
        if min_index < 0:
            min_index = i
        else:
            if lst[i] < lst[min_index]:
                min_index = i
    return search_min_element_index(lst, min_index, i + 1)


def first_positive_index(lst, i=0):
    if i > len(lst):
        return i
    else:
        if lst[i] > 0:
            return i
        return first_positive_index(a, i+1)


def last_positive_index(lst, i=21):
    if i <= 0:
        return i
    else:
        if lst[i] > 0:
            return i
        return last_positive_index(lst, i - 1)


def sum_between(lst, i, j):
    if i is None or j is None:
        return 0
    elif i >= j - 1:
        return 0
    else:
        return lst[i + 1] + sum_between(lst, i + 1, j)


def replace_nulls(lst, i=0):
    if i < len(lst):
        if lst[i] == 0:
            lst.pop(i)
            lst.insert(0, 0)
        return replace_nulls(lst, i + 1)
    return lst


if __name__ == '__main__':
    a = generate_list([])
    print(a)
    print('Мінімальний елемент: ', a[search_min_element_index(a)])
    print("Сума: ", sum_between(a, first_positive_index(a), last_positive_index(a)))
    print(replace_nulls(a))
