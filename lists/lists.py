class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_num = 0
        new_list = []
        for num in input_list:
            max_num = max(max_num, num)
        for num in input_list:
            new_list.append(max_num if num > 0 else num)
        return new_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if not input_list:
            return -1
        left, right = 0, len(input_list) - 1
        mid = left + (right - left) // 2
        if input_list[mid] < query:
            ret = ListExercise.search(input_list[mid + 1 :], query)  # noqa: E203
            if ret > -1:
                return mid + 1 + ret
            return -1
        elif input_list[mid] > query:
            ret = ListExercise.search(input_list[: mid - 1], query)
            if ret > -1:
                return ret
            return -1
        else:
            return mid
