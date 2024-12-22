# Terceira tentativa no exercicio 327. Mudando a abordagem, um vetor com todas as soma 
# eh criado, dividido em dois e ordenado a medida que a somagem
# dos ranges ocorre

class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        def mergeCount(sums, start, mid, end, lower, upper):
            count = 0
            j, k = mid + 1, mid + 1
            for i in range(start, mid + 1):
                # Conta os ranges que estao entre o intervalo lower e upper
                while j <= end and sums[j] - sums[i] < lower:
                    j += 1
                while k <= end and sums[k] - sums[i] <= upper:
                    k += 1
                count += k - j

            # Faz o merge dos dois arrays
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if sums[i] <= sums[j]:
                    temp.append(sums[i])
                    i += 1
                else:
                    temp.append(sums[j])
                    j += 1
            while i <= mid:
                temp.append(sums[i])
                i += 1
            while j <= end:
                temp.append(sums[j])
                j += 1
            for i in range(len(temp)):
                sums[start + i] = temp[i]

            return count
        
        # Definicao da funcao que divide o vetor no meio para contar os ranges
        def mergeSum(sums, start, end, lower, upper):
            if start >= end:
                return 0
            mid = (start + end) // 2
            # conta os ranges nas duas metades
            count = mergeSum(sums, start, mid, lower, upper) + \
                    mergeSum(sums, mid + 1, end, lower, upper)
            # Count the ranges that span both parts
            count += mergeCount(sums, start, mid, end, lower, upper)
            return count
        
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        
        return mergeSum(sums, 0, n, lower, upper)
