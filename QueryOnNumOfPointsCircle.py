'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def calc_distance(xi, yi, xj, yj):
            return ((xj - xi) ** 2 + (yj - yi) ** 2) ** 0.5
        
        answer = []
        
        for i in queries:
            c = 0
            for j in points:
                if calc_distance(i[0], i[1], j[0], j[1]) <= i[2]: c += 1
            answer.append(c)
        return answer
