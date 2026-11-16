class Solution:
    def calPoints(self, operations: list[str]) -> int:
        list_ = []
        for i in range(len(operations)):
            total = 0
            product = 1
            if operations[i] == '+':
                total += list_[-1] + list_[-2]
                list_.append(total)
            elif operations[i] == 'D':
                product = 2 * list_[-1]
                list_.append(product)
            elif operations[i] == 'C':
                list_.pop()
            else:
                list_.append(int(operations[i]))
        return sum(list_)
            
