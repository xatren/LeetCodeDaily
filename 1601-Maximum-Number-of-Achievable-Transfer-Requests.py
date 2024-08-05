class Solution:
    def maximumRequests(self, n, requests):
        def is_valid_subset(mask):
            net_transfer = [0] * n
            count = 0
            for i in range(len(requests)):
                if mask & (1 << i):
                    from_bldg, to_bldg = requests[i]
                    net_transfer[from_bldg] -= 1
                    net_transfer[to_bldg] += 1
                    count += 1
            if all(x == 0 for x in net_transfer):
                return count
            return 0

        max_requests = 0
        total_requests = len(requests)
        for mask in range(1 << total_requests):
            max_requests = max(max_requests, is_valid_subset(mask))

        return max_requests
