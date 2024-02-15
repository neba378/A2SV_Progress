class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return image


        return []
        