# Usando método de divisao e conquista, merge sort para ordenar o vetor com custo n log2(n)
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
    
def mergeSort(v):
    if(len(v) <= 1):
        return v
    
    h = len(v) // 2
    left_subvector = mergeSort(v[:h])
    right_subvector = mergeSort(v[h:])
        
    return mergeTwo(left_subvector, right_subvector)

class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        # print(nums) DEBUG
        nums = mergeSort(nums)
        # print(nums) DEBUG
        return nums[k-1] # Com o vetor/lista ordenada, retornando o quarto elemento
    
# nums, k = ["2","21","12","1"], 4

# sol = Solution()
# sol.kthLargestNumber(nums, k)