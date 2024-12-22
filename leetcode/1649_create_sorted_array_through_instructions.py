# Segunda tentativa no exercicio 1649
# Re-Utilizando um algoritmo de D&C de arvore indexada binaria (arvore de fenwick) para armazenar as somas dos 
# subsets do vetor e facilitar o calculo do custo de insercoes
class FenwickTree:
    def __init__(self, n):
        self.n = n # Tamanho máximo
        self.tree = [0] * (n + 1) # inicia a lista de n+1 elementos iguais a zero para armazenar as somas
    
    def update(self, current_index):
        while current_index <= self.n:
            # print(self.tree[current_index])
            self.tree[current_index] += 1
            # print(self.tree[current_index])
            current_index += current_index & -current_index
    
    def query(self, current_index):
        result = 0
        while current_index > 0:
            result += self.tree[current_index]
            current_index -= current_index & -current_index
        return result
    
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ins_max_value = max(instructions)
        fenwick = FenwickTree(ins_max_value)
        cost = 0
        
        for current_index, num in enumerate(instructions):
            # Soma número de elementos menores que a instrucao atual
            smaller = fenwick.query(num - 1)
            
            # Soma o número de elementos maiores que a instrucao atual
            greater = (current_index - fenwick.query(num))
            
            # Calcula o custo
            cost += min(smaller, greater)
            cost %= 10**9 + 7 # Modulo para valores muito grandes
            
            # Adiciona o valor atual na arvore
            fenwick.update(num)
        
        return cost