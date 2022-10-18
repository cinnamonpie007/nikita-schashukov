# ## task 1
#
# from random import sample
#
#
# ##############################################################################
# def check_1(lst_obj):
#     """Функция должна создать множество из списка.
#     Алгоритм 1:
#     Создать множество из списка
#     Сложность: O(n).
#     """
#     lst_to_set = set(lst_obj)  # O(n)
#     return lst_to_set  # O(1)
#
#
# ##############################################################################
# def check_2(lst_obj):
#     """Функция должная вернуть True, если все элементы списка различаются.
#     Алгоритм 2:
#     Проходимся по списку и для каждого элемента проверяем,
#     что такой элемент отстутствует
#     в оставшихся справа элементах
#     Сложность: O(n).
#     """
#     for j in range(len(lst_obj)):          # O(n)
#         if lst_obj[j] in lst_obj[j+1:]:    # O(n)
#             return False                   # O(1)
#     return True                            # o(1)
#
#
# ##############################################################################
# def check_3(lst_obj):
#     """Функция должная вернуть True, если все элементы списка различаются.
#     Алгоритм 3:
#     Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
#     Если присутствуют дубли, они будут находиться рядом.
#     Сложность: O(n)
#     """
#     lst_copy = list(lst_obj)                 # O(n)
#     lst_copy.sort()                          # O(n log n)
#     for i in range(len(lst_obj) - 1):        # O(N)
#         if lst_copy[i] == lst_copy[i+1]:     # O(1)
#             return False                     # O(1)
#     return True                              # O(1)
#
#
# for j in (50, 500, 1000, 5000, 10000):
#     # Из 100000 чисел возьмем 'j' случайно выбранных
#     # Всего 10 тыс. чисел
#     lst = sample(range(-100000, 100000), j)
#
# print(check_1(lst))
# print(check_2(lst))
# print(check_3(lst))

#task #2
# O(n^2)

# list_num = [2, 5, 23, 2434, -18]
# def n_2(lst):
#     for i in lst:
#         if i < lst[0]:
#             lst.insert(0, lst[lst.index(i)])
#     return lst[0]
# # O(n)
# def line(lst):
#     res = lst[0]
#     for i in lst:
#         if i < res:
#             res = i
#     return res
#
# print(n_2(list_num))
# print(line(list_num))

# task 3


# storage = {
#     'company_1': 2343.54,
#     'company_2': 74859574,
#     'company_3': 3645658.84,
#     'company_4': 4575893.33,
#     'company_5': 4865638,
#     'company_6': 43786,
#     'company_7': 348756385549,
#     'company_8': 348626.28
# }
#
# #Сложность: O(n log n)
#
# def version_1(dct):
#     sort_items = sorted(dct.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
#     res = dict(sort_items[:3])  # O(1) ?
#     return res  # O(1)
#
# #Сложность: O(n)
# def version_2(dct):
#     res = []  # O(1)
#     copy_dct = dct.copy()  # O(n)
#     for i in range(3):  # O(1)
#         top = max(copy_dct.items(), key=lambda x: x[1])  # O(n)
#         res.append(top)  # O(1)
#         del copy_dct[top[0]]  # O(1)
#     return dict(res)  # O(1)
#
#
# print(version_1(storage))
# print(version_2(storage))
# task 4
# storage = [
#     {'login': 'user_1', 'password': '1234', 'activation': False},
#     {'login': 'user_2', 'password': '5678', 'activation': True},
#     {'login': 'user_3', 'password': '0987', 'activation': False}
# ]
#
# # Сложность: O(n)
# def authentication_1(login, password):
#     for idx, account in enumerate(storage):
#         if account['login'] == login and account['password'] == password:
#             if not account['activation']:
#                 if input(f'{login}, your account is not activated, activate now? (y/n) ') == 'y':
#                     storage[idx]['activation'] = True
#                 else:
#                     return False
#             return True
#     return False
#
# # Сложность: O(n^2)
# def authentication_2(login, password):
#     for account in storage:
#         if account['login'] == login and account['password'] == password:
#             if not account['activation']:
#                 if input(f'{login}, your account is not activated, activate now? (y/n) ') == 'y':
#                     idx = 0
#                     for acc in storage:
#                         if acc['login'] == login:
#                             storage[idx]['activation'] = True
#                         else:
#                             idx += 1
#                 else:
#                     return False
#             return True
#     return False
#
#
# print(authentication_1('user_1', '1234'))
# print(authentication_1('user_2', '5678'))
# print(authentication_1('user_3', '0987'))
#
# print()
#
# print(authentication_2('user_1', '1234'))
# print(authentication_2('user_2', '5678'))
# print(authentication_2('user_3', '0987'))

# task 5
#
# class StackOfPlates:
#     def __init__(self):
#         self.limit = 10
#         self.lst = []
#
#     def is_empty(self):
#         return self.lst == []
#
#     def push_in(self, el):
#         """Предполагаем, что верхний элемент стека находится в конце списка"""
#         if self.is_empty() or len(self.lst[-1]) == self.limit:
#             self.lst.append([])
#         self.lst[-1].append(el)
#
#     def pop_out(self):
#         el = self.lst[-1].pop()
#         if len(self.lst[-1]) == 0:
#             del self.lst[-1]
#         return el
#
#     def get_val(self):
#         return self.lst[-1][-1]
#
#     def stack_size(self):
#         size_list = []
#         for st in self.lst:
#             size_list.append(len(st))
#         return size_list
#
#
# if __name__ == '__main__':
#
#     stack = StackOfPlates()
#
#     print(stack.is_empty())
#     for i in range(32):
#         stack.push_in(i)
#
#     print(stack.is_empty())
#     print(stack.stack_size())
#
#     print(stack.get_val())
#     print(stack.pop_out())
#     print(stack.pop_out())
#     print(stack.get_val())
#
#     print(stack.stack_size())

# task 6

