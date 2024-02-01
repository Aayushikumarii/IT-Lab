class Question3:
    x,n = 0,0
    result = 1
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def solve(self):
        i = 1
        while(i<=n):
            self.result = self.result * self.x
            i+=1
        return self.result
x = int(input('Enter number x: '))
n = int(input('Enter number n: '))
question3 = Question3(x, n)
print(question3.solve())