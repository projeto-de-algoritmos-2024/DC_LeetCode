# Re-utilizando um algoritmo de D&C para recursivamente encontrar todas as somas de todos os subsets no vetor.
# Codigo alterado para incluir uma funcao de merge, e retornar as somas em um vetor ao inves de apenas printa-las
# Em seguida, a implementacao da solucao no contexto do problema

# Código de autoria de Shreyanshi Arun, re-utilizado e alterado por Eric Chagas abaixo 
# (https://www.geeksforgeeks.org/print-sums-subsets-given-set/) ***********************************************

# Python3 program to print sums of
# all possible subsets.
 
# Prints sums of all subsets of arr[l..r]
 
 
def subsetSums(arr, l, r, sum=0):
 
    # Print current subset
    if l > r:
        # print('current vector: ', arr[l:r])
        # print('returning sum: ', [sum])
        return [sum]
 
    # Subset including arr[l]
    left_subvector = subsetSums(arr, l + 1, r, sum + arr[l])
 
    # Subset excluding arr[l]
    right_subvector = subsetSums(arr, l + 1, r, sum)
    
    # print('sum: ', sum)
    # print('left: ', left_subvector)
    # print('right: ', right_subvector)
    
    return mergeTwo(left_subvector, right_subvector)
 
 
# This code is contributed by Shreyanshi Arun.

# Algoritmo original editado por Eric Chagas.

# Fim do código re-utilizado e alterado ***********************************************

def mergeTwo(v1_str, v2_str):
    v1, v2 = list(map(int, v1_str)), list(map(int, v2_str)) # Convertendo lista de strings pra int
    sorted = []
    l, r = 0, 0
    
    while(l < len(v1) and r < len(v2)):
        if v1[l] < v2[r]:
            sorted.append(v1[l])
            l += 1
        else:
            sorted.append(v2[r])
            r += 1
            
    sorted.extend(v1[l:])
    sorted.extend(v2[r:])
    return sorted

# Definindo algoritmo de busca binaria D&C que busca a posicao ideal para adicionar
# o valor de modo que a lista mantenha-se ordenada e sem repeticoes
def binary_search(nums, key):
    # Setando inicio e fim da lista nums
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2
        
        if nums[mid] == key:
            return mid  # Return the index if found
        elif nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    
    # If the instruction is not found, return -1
    return -1

class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        nums_len = len(nums)
        ranges_count = 0
        sums = subsetSums(nums, 0, nums_len-1)
        print(sums)
        zero = binary_search(sums, 0)
        print(zero)
        if(zero != -1):
            sums.remove(0)
        for i in sums:
            if(i >= lower and i <= upper):
                ranges_count += 1
        return ranges_count
        
sol = Solution()
nums = [2147483647,-2147483648,-1,0]
nums_len = len(nums)
lower, upper = -1, 0
count = sol.countRangeSum(nums, lower, upper)
print(count)