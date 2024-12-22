# Definindo algoritmo de busca binaria D&C que busca a posicao ideal para adicionar
# o valor de modo que a lista mantenha-se ordenada e sem repeticoes
def binary_search_insertion_position(nums, instruction):
    # Setando inicio e fim da lista nums
    left, right = 0, len(nums) - 1
    
    # Algoritmo de busca (nunca retorna -1 pois o caso de ser o maior ou menor numero ja foram cobertos)
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] < instruction and nums[mid+1] > instruction:
            return mid+1  # Retorna ao encontrar o local de insercao
        elif nums[mid] > instruction:
            right = mid - 1
        else:
            left = mid + 1
    
    # retorno padrao
    return -1


# Algoritmo padrao de busca binaria para quando a instrucao ja esta no array num ou para busca-la
def binary_search_regular(nums, instruction):
    # Setando inicio e fim da lista nums
    left, right = 0, len(nums) - 1
    
    # Algoritmo de busca
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == instruction:
            return mid  # Retorna ao encontrar o local de insercao
        elif nums[mid] > instruction:
            right = mid - 1
        else:
            left = mid + 1
    
    # retorno padrao
    return -1

class Solution:
    def createSortedArray(self, instructions) -> int:
        nums = []
        nums_repeated = []
        largest = 0
        smallest = instructions[0]
        cost = 0
        for aux in instructions:
            # Caso seja o maior insere no final e o custo eh zero por nao haverem numeros maiores no array
            if aux > largest:
                largest = aux
                print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, len(nums), 0, min(len(nums), 0)))
                nums.append(aux)
                nums_repeated.append(aux)
                #print( 'now nums is: ', str(nums))
            # Caso seja o menor insere no final e o custo eh zero por nao haverem numeros menores no array
            elif aux < smallest:
                smallest = aux
                print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, 0, len(nums), min(0, len(nums))))
                nums.insert(0, aux)
                nums_repeated.insert(0, aux)
                #print( 'now nums is: ', str(nums))
            else:
                pos = binary_search_regular(nums, aux)
                insert_pos_repeated = binary_search_insertion_position(nums_repeated, aux)
                if(pos != -1):
                    print('nums is: ', nums_repeated)
                    print('exists: Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, pos, len(nums)-(pos+1), min(pos, len(nums) - (pos+1))))
                    cost += min(pos, len(nums) - (pos+1))
                    nums_repeated.insert(insert_pos_repeated, aux)
                    #print( 'now nums is: ', str(nums))
                else:
                    print('nums is: ', nums_repeated)
                    # Roda busca binaria pela posicao de insercao                    
                    cost += min(insert_pos_repeated, len(nums) - insert_pos_repeated)
                    print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, insert_pos_repeated, len(nums_repeated)-insert_pos_repeated, min(insert_pos_repeated, len(nums)-insert_pos_repeated)))
                    
                    insert_pos = binary_search_insertion_position(nums_repeated, aux)
                    nums.insert(insert_pos, aux)
                    nums_repeated.insert(insert_pos_repeated, aux)

                    #print( 'now nums is: ', str(nums))
        print(nums)
        print(len(nums))
        print(cost)
        return 0

instructions = [1,3,3,3,2,4,2,1,2]
sol = Solution()
sol.createSortedArray(instructions)
