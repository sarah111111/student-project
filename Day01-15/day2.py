
class Day2:

    def day2_1(self):
        # 变量的使用
        a = 321
        b = 12
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)

    def day2_2(self):
        #使用type()检查变量的类型
        a = 100
        b = 12.345
        c = 1 + 5j
        d = 'hello,world'
        e = True
        print(type(a))
        print(type(b))
        print(type(c))
        print(type(d))
        print(type(e))

    def day2_3(self):
        """
            使用input()函数获取键盘输入(字符串)
            使用int()函数将输入的字符串转换成整数
            使用print()函数输出带占位符的字符串
        :return:
        """
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d + %d = %d' % (a, b, a + b))
        print('%d - %d = %d' % (a, b, a - b))
        print('%d * %d = %d' % (a, b, a * b))
        print('%d / %d = %d' % (a, b, a / b))
        print('%d // %d = %d' % (a, b, a // b))
        print('%d %% %d = %d' % (a, b, a % b))
        print('%d ** %d = %d' % (a, b, a ** b))

    def day2_4(self):
        # 赋值运算符和复合赋值运算符
        a = 10
        b = 3
        a += b
        a *= a + 2
        print(a)

    def day2_5(self):
        # 比较运算符和逻辑运算符的使用
        flag0 = 1 == 1
        flag1 = 3 > 2
        flag2 = 2 < 1
        flag3 = flag1 and flag2
        flag4 = flag1 or flag2
        flag5 = not (1 != 2)
        print('flag0 =', flag0) # flag0  = true
        print('flag1 = ', flag1) # flag1 = true
        print('flag2 = ', flag2) # flag2 = false
        print('flag3 = ', flag3) # flag3 = false
        print('flag4 = ',flag4) # flag4 = true
        print('flag5 =',flag5) # flag5 = false

    def day2_6(self):
        # 将华氏温度转换为摄氏温度  $C=(F - 32) \div 1.8$。
        f = float(input('请输入华氏温度：'))
        c = (f-32)/1.8
        print('%.1f华氏温度 = %.1f摄氏温度' % (f, c))

    def day2_7(self):
        # 输入半径计算圆的周长和面积
        redius = float(input('请输入圆的半径：'))
        perimeter = 2 * 3.1416 * redius
        area = 3.1416 * redius * redius
        print('周长：%.2f' % perimeter)
        print('面积：%.2f' % area)

    def day2_8(self):
        # 输入年份 如果是闰年输出True 否则输出False
        year = int(input('请输入年份：'))
        is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        print(is_leap)
if __name__ == '__main__':
    day = Day2()
    # day.day2_1()
    # day.day2_2()
    # day.day2_3()
    # day.day2_4()
    # day.day2_5()
    # day.day2_6()
    # day.day2_7()
    day.day2_8()

