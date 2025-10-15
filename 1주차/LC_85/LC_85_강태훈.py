from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        rows_wise_cum_matrix = [[0]*n_cols for _ in range(n_rows)]
        cols_wise_cum_matrix = [[0]*n_cols for _ in range(n_rows)]

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j]=="0":
                    rows_wise_cum_matrix[i][j] = 0
                else:
                    rows_wise_cum_matrix[i][j] = 1 if j == 0 else rows_wise_cum_matrix[i][j-1] + 1

        for j in range(n_cols):
            for i in range(n_rows):
                if matrix[i][j]=="0":
                    cols_wise_cum_matrix[i][j] = 0
                else:
                    cols_wise_cum_matrix[i][j] = 1 if i == 0 else cols_wise_cum_matrix[i-1][j] + 1

        ans = 0

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == "0":
                    continue
                min_w = rows_wise_cum_matrix[i][j]
                max_h = cols_wise_cum_matrix[i][j]

                for k in range(max_h):
                    r = i - k
                    w = rows_wise_cum_matrix[r][j]
                    if w < min_w:
                        min_w = w
                        if min_w == 0:
                            break
                    area = min_w * (k + 1)
                    if area > ans:
                        ans = area

        return ans


# class Solution: # by GPT
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         n_rows, n_cols = len(matrix), len(matrix[0])
#         heights = [0] * n_cols
#         max_area = 0

#         for i in range(n_rows):
#             for j in range(n_cols):
#                 heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

#             stack = []
#             for k in range(n_cols + 1):
#                 h = heights[k] if k < n_cols else 0
#                 while stack and heights[stack[-1]] > h:
#                     H = heights[stack.pop()]
#                     W = k if not stack else k - stack[-1] - 1
#                     max_area = max(max_area, H * W)
#                 stack.append(k)

#         return max_area
    
