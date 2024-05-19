class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1

def main() :
    print(Sum.get_sum(1,2,34,4,56,6,6))

main()