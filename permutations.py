class Solution(object):
    def permute(self, nums):
        
        def backtrack(nums):
            if len(nums) == 1: #si esta vacia
                return [nums]

            resultado = []    
            for i in range (len(nums)):
                fijo = nums[i]
                resto = nums[:i] + nums[i+1:]
                for p in backtrack(resto):
                    resultado.append([fijo]+p)
            return resultado
        return backtrack(nums)