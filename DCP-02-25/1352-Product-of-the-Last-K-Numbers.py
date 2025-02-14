class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]  
        self.last_zero_index = -1 

    def add(self, num):
        if num == 0:
            self.prefix_products = [1]
            self.last_zero_index = len(self.prefix_products) - 1
        else:
            if self.last_zero_index == len(self.prefix_products) - 1:
                self.prefix_products.append(num)
            else:
                self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k):
        if len(self.prefix_products) - 1 < k:
            return 0
        if self.last_zero_index >= len(self.prefix_products) - k:
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k-1]

