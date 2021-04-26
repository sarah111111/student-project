class Day4:
    def day4_1(self):
        """
        for - in 循环
        range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
        range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
        range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
        range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
        :return:
        """
        # 用for循环实现1~100求和
        sum = 0
        for x in range(101):
            sum += x
        print(sum)

    def day4_2(self):
        # 用for循环实现1~100之间的偶数求和
        sum = 0
        for x in range(1,101):
            if x % 2 ==0:
                sum += x
        print(sum)

    def day4_3(self):
        import random
        answer = random.randint(1, 100)
        counter = 0
        while True:
            counter += 1
            number = int(input("请输入："))
            if number < answer:
                print('大一点')
            elif number > answer:
                print('小一点')
            else:
                print('恭喜猜对了！')
                break
        print('你总共猜了%d次' % counter)
        if counter > 7:
            print('你的智商余额明显不足')
        else:
            print('你真聪明')

    def day4_4(self):
        # 输出乘法口诀表(九九表)
        for i in range(1, 10):
            for j in range(1, i+1):
                print('%d * %d = %d' % (i, j, i*j), end='\t')
            print()

    def day4_5(self):
        """
        练习1：输入一个正整数判断是不是素数。
        提示：素数指的是只能被1和自身整除的大于1的整数。
        :return:
        """
        from math import sqrt
        num = int(input("请输入一个正整数："))
        end = int(sqrt(num))
        is_prime = True
        for x in range(2, end + 1):
            if num % x == 0:
                is_prime = False
                break
        if is_prime and num != 1:
            print('%d是素数' % num)
        else:
            print('%d不是素数' % num)

    def day4_6(self):
        """
        输入两个正整数，计算它们的最大公约数和最小公倍数。
        提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
        :return:
        """
        x = int(input('x = '))
        y = int(input('y = '))
        if x > y:
            x, y = y, x
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                print('%d和%d的最大公约数是%d' % (x, y, factor))
                print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
                break

    def day4_7(self):
        """
        打印三角形图案
        :return:
        """
        row = int(input("请输入行数："))
        for i in range(row):
            for _ in range(i + 1):
                print('*', end='')
            print()

        for i in range(row):
            for j in range(row):
                if j < row - i - i:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()

        for i in range(row):
            for _ in range(row - i - 1):
                print(' ', end='')
            for _ in range(2 * i + 1):
                print('*', end='')
            print()


if __name__ == '__main__':
    day = Day4()
    # day.day4_1()
    # day.day4_2()
    # day.day4_3()
    # day.day4_4()
    # day.day4_5()
    # day.day4_6()
    day.day4_7()
