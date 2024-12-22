# Definindo algoritmo de busca binaria D&C que busca a posicao ideal para adicionar
# o valor de modo que a lista mantenha-se ordenada e sem repeticoes
def binary_search_insertion_position(nums, instruction):
    # Setando inicio e fim da lista nums
    left, right = 0, len(nums) - 1
    
    # Algoritmo de busca (nunca retorna -1 pois o caso de ser o maior ou menor numero ja foram cobertos)
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == instruction or (nums[mid] <= instruction and nums[mid+1] > instruction):
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
        largest = 0
        smallest = instructions[0]
        cost = 0
        for aux in instructions:
            # Caso seja o maior insere no final e o custo eh zero por nao haverem numeros maiores no array
            if aux >= largest:
                largest = aux
                print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, len(nums), 0, min(len(nums), 0)))
                nums.append(aux)
            # Caso seja o menor insere no final e o custo eh zero por nao haverem numeros menores no array
            elif aux <= smallest:
                smallest = aux
                print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, 0, len(nums), min(0, len(nums))))
                nums.insert(0, aux)
            else:
                pos = binary_search_regular(nums, aux)
                insert_pos = binary_search_insertion_position(nums, aux)
                if(pos != -1):
                    print('nums is: ', nums)
                    # Com a posicao de insercao ideal, busca pelo final da repeticao do numero caso haja
                    repeat_end = pos
                    while(nums[repeat_end] == aux and repeat_end < len(nums)-1):
                        repeat_end += 1
                    # Com a posicao de insercao ideal, busca pelo inicio da repeticao do numero caso haja    
                    repeat_begin = pos
                    while(nums[repeat_begin] == aux):
                        repeat_begin -= 1
                        
                    print('exists: Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, repeat_begin+1, len(nums)-(repeat_end), min(repeat_begin+1, len(nums) - (repeat_end+1))))

                    cost += min(repeat_begin+1, len(nums) - (repeat_end+1))
                    nums.insert(insert_pos, aux)
                else:
                    print('nums is: ', nums)
                    # Roda busca binaria pela posicao de insercao                    
                    cost += min(insert_pos, len(nums) - insert_pos)
                    print('Insert %2d with cost min(%2d, %2d) = %2d.' % (aux, insert_pos, len(nums)-insert_pos, min(insert_pos, len(nums)-insert_pos)))
                    insert_pos = binary_search_insertion_position(nums, aux)
                    nums.insert(insert_pos, aux)
                    #print( 'now nums is: ', str(nums))
        # print(nums)
        # print(len(nums))
        # print(cost)
        return cost
