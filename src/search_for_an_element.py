# Задача - Поиск элемента в упорядоченном списке
list_num = [1, 2, 3, 45, 356, 569, 600, 705, 923]
sorted_list = sorted(list_num)


def search(number: id) -> bool:
    """
    Если есть число в списке возвращает True. Сложность алгоритма O(log n).
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == number:
            return True
        elif sorted_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(list_num)
print(sorted_list)
print(search(569))
print(search(5))
