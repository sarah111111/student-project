class Day3:
    # 分支结构
    def day3_1(self):
        # if语句的使用
        # 用户身份验证
        username = input('请输入用户名：')
        password = input("请输入密码：")
        if username == 'admin' and password == '123456':
            print("身份验证成功！")
        else:
            print("身份验证失败！")

    def day3_2(self):
        """分段函数求值
                    3x - 5  (x > 1)
            f(x) =  x + 2   (-1 <= x <= 1)
                    5x + 3  (x < -1)
        :return:
        """
        x = float(input('x = '))
        if x > 1:
            y = 3 * x - 5
        elif x >= -1:
            y = x + 1
        else:
            y = 5 * x + 3
        print('f(%.2f) = %.2f' % (x, y))

    def day3_3(self):
        """
        嵌套分支
        分段函数求值
                3x - 5	(x > 1)
        f(x) =	x + 2	(-1 <= x <= 1)
                5x + 3	(x < -1)
                :return:
                """
        x = float(input("x = "))
        if x > 1:
            y = 3 * x - 5
        else:
            if x >= -1:
                y = x + 2
            else:
                y = 5 * x + 3
        print('f(%.2f) = %.2f' % (x, y))

    def day3_4(self):
        """
        英制单位英寸和公制单位厘米互换
        :return:
        """
        value = float(input("请输入长度："))
        unit = input("请输入单位:")
        if unit == 'in' or unit == '英寸':
            print('%.2f英寸 = %.2f厘米' % (value, value*2.54))
        elif unit == 'cm' or unit == '厘米':
            print('%.2f厘米 = %.2f英寸' % (value, value/2.54))
        else:
            print("请输入有效的单位")

    def day3_5(self):
        """
        百分制成绩转换为等级制成绩
        如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
        :return:
        """
        score = float(input("请输入成绩："))
        if score >= 90:
            grade = 'A'
        elif score >=80:
            grade = 'B'
        elif score >=70:
            grade = 'C'
        elif score >=60:
            grade = 'D'
        else:
            grade = 'E'
        print("对应的等级是：", grade)

    def day3_6(self):
        """
        计算三角形面积的公式叫做海伦公式。
        判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
        :return:
        """
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        if a + b > c and a + c > b and b + c >a:
            print('周长：%.2f' % (a+b+c))
            p = (a+b+c)/2
            area = (p*(p-a)*(p-b)*(p-c))**0.5
            print('面积：%.2f' % (area))
        else:
            print('不能构成三角形')
if __name__ == '__main__':
    day = Day3()
    # day.day3_1()
    # day.day3_2()
    # day.day3_3()
    # day.day3_4()
    # day.day3_5()
    day.day3_6()