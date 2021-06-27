# Time:  O(m * n)
# Space: O(1)

import fractions


# inplace rotation
class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_index(m, n, l):
            if l-(m-1) < 0:
                return l, 0
            l -= (m-1)
            if l-(n-1) < 0:
                return m-1, l
            l -= (n-1)
            if l-(m-1) < 0:
                return m-1-l, n-1
            l -= (m-1)
            return 0, n-1-l

        m, n = len(grid), len(grid[0])
        for i in xrange(min(m, n)//2):
            total = 2*((m-1)+(n-1))
            nk = k%total
            num_cycles = fractions.gcd(total, nk)
            cycle_len = total//num_cycles
            for offset in xrange(num_cycles):
                r, c = get_index(m, n, offset)
                for j in xrange(1, cycle_len):
                    nr, nc = get_index(m, n, (offset+j*nk)%total)
                    grid[i+nr][i+nc], grid[i+r][i+c] = grid[i+r][i+c], grid[i+nr][i+nc]
            m, n = m-2, n-2
        return grid


# Time:  O(m * n)
# Space: O(1)
# inplace rotation
class Solution2(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_index(m, n, l):
            if l-(m-1) < 0:
                return l, 0
            l -= (m-1)
            if l-(n-1) < 0:
                return m-1, l
            l -= (n-1)
            if l-(m-1) < 0:
                return m-1-l, n-1
            l -= (m-1)
            return 0, n-1-l

        def reverse(grid, m, n, i, start, end):
            while start < end:
                lr, lc = get_index(m, n, start)
                rr, rc = get_index(m, n, end)
                grid[i+lr][i+lc], grid[i+rr][i+rc] = grid[i+rr][i+rc], grid[i+lr][i+lc]
                start += 1
                end -= 1

        m, n = len(grid), len(grid[0])
        for i in xrange(min(m, n)//2):
            total = 2*((m-1)+(n-1))
            nk = k%total
            reverse(grid, m, n, i, 0, total-1)
            reverse(grid, m, n, i, 0, nk-1)
            reverse(grid, m, n, i, nk, total-1)
            m, n = m-2, n-2
        return grid
