for fizzbuzz in range(1, 100):
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)


class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result


ob1 = Solution()
print(ob1.fizzBuzz(15))


class Solution1(object):
    def fizzBuzz(self, n):

        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(str(n))


ob2 = Solution1()
ob2.fizzBuzz(7)
