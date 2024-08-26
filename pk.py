import random

print('=' * 60)
print(' ' * 20, '剪刀石头布游戏')
print('1代表剪刀 2代表石头 3代表布')

'''用户出拳'''


def user_choice():
    user_num = input("请出拳")
    if user_num not in '123':
        print("出拳错误，请重新出拳")
    else:
        user_num = int(user_num)
    return user_num


'''电脑出拳'''


def cpu_choice():
    cpu_num = random.randint(1, 3)
    return cpu_num


'''分数计算'''


def eval_core(user_num, cpu_num, user_core):
    if user_num == cpu_num:
        print("您打成平手，不加分")
    elif user_num == 1 and cpu_num == 2 or user_num == 2 and cpu_num == 3 or user_num == 3 and cpu_num == 1:
        user_core -= 10
        print(f'"您输了,当前得分为：{user_core}"')
    elif user_num == 1 and cpu_num == 3 or user_num == 2 and cpu_num == 1 or user_num == 3 and cpu_num == 2:
        user_core += 10
        print(f'"您赢了,当前得分为：{user_core}"')
    if user_core >= 200:
        print("游戏结束,您赢了！")
    elif user_core <= 0:
        print("游戏结束，您输了！")
    return user_core


'''游戏'''


def game():
    user_core = cpu_core = 100
    try:
        while True:
            user_num = user_choice()
            cpu_num = cpu_choice()
            user_core = eval_core(user_num, cpu_num, user_core)
            if user_core >= 200 and user_core <= 0:
                break
    except:
        print("出拳错误，游戏结束！")


def main():
    game()


if __name__ == '__main__':
    main()
