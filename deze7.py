class NumberIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):

        for i in range(1 , self.n + 1):
            yield i

nums = NumberIterable(10)

for number in nums:
    print(number)