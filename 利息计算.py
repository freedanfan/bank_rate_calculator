
def deng_e_ben_jin(total_num, nian_li_lv, month_num):
    """
    等额本金
    :param total_num:借款总数
    :param li_lv: 利率
    :param month_num: 月数量
    :return:
    """
    yue_li_lv = nian_li_lv / 12
    meiyue_benjin = total_num / month_num
    shengyu_total_num =total_num

    meiyue_huankuan = []
    total_li_xi = 0

    print("等额本金 还款方式：")

    for index in range(month_num):
        shengyu_yue = month_num - index
        shengyu_total_num = shengyu_yue * meiyue_benjin
        meiyue_lixi = shengyu_total_num * yue_li_lv
        total_li_xi += meiyue_lixi
        print("还款期数：{}，还款金额：{}，还款本金：{}，还款利息：{}，剩余本金：{}".format(index+1,
                                                               round(meiyue_lixi+meiyue_benjin,2),
                                                               round(meiyue_benjin,2),
                                                               round(meiyue_lixi, 2),
                                                               round(shengyu_total_num-meiyue_benjin, 2)))
    print("利息合计：{}".format(round(total_li_xi, 2)))


def deng_e_ben_xi(P, r, N, jiezhi_start=0, jiezhi_end=-1):
    """
    等额本息
    :param P: 贷款金额
    :param r: 年利率
    :param n: 贷款期限n年
    :param N: 月份数
    :param jiezhi_start: 统计区间内的利息情况
    :param jiezhi_end: 统计区间内的利息情况
    :return:
    """
    R = r / 12 / 100  # 月利率
    meiyue_huankuan = P * R * (1 + R) ** N / ((1 + R) ** N - 1)
    print("借款：{}， 年利率：{}，借款月数：{}，每月还款：{}".format(P, r , N, round(meiyue_huankuan, 2)))

    dic1 = {"本月偿还金额": [0] + [meiyue_huankuan] * N,
            "本月偿还本金": [0],
            "本月偿还利息": [0],
            "本月剩余本金": [P]}

    print("等额本息 还款方式：")


    total_lixi = 0
    total_huankuan_num = 0
    total_benjin_num = 0

    if jiezhi_start == 0:
        jiezhi_start = 1
    if jiezhi_end == -1:
        jiezhi_end = N+1

    shengyu_benjin = 0
    for n in range(1, N+1):
        benyue_huankuan_benjin = P * R * (1 + R) ** (n - 1) / ((1 + R) ** N - 1)
        # 四舍五入，保留2位小数
        benyue_huankuan_benjin = round(benyue_huankuan_benjin, 2)
        # print("本月偿还本金n=", benyue_huankuan_benjin)
        dic1["本月偿还本金"].append(benyue_huankuan_benjin)
        benyue_shengyu_benjin = dic1["本月剩余本金"][n - 1] - benyue_huankuan_benjin
        benyue_shengyu_benjin = round(benyue_shengyu_benjin, 2)
        # print("本月剩余本金n=", benyue_shengyu_benjin)
        dic1["本月剩余本金"].append(benyue_shengyu_benjin)
        benyue_changhuan_lixi = dic1["本月偿还金额"][n] - benyue_huankuan_benjin
        benyue_changhuan_lixi = round(benyue_changhuan_lixi, 2)
        # print("本月偿还利息n=", benyue_changhuan_lixi)
        dic1["本月偿还利息"].append(benyue_changhuan_lixi)


        if jiezhi_start <= n and jiezhi_end >= n:
            print("还款期数：{}，还款金额：{}，还款本金：{}，还款利息：{}，剩余本金：{}".format(n,
                                                                   round(benyue_changhuan_lixi+benyue_huankuan_benjin, 2),
                                                                   benyue_huankuan_benjin,
                                                                   benyue_changhuan_lixi,
                                                                   benyue_shengyu_benjin))
            total_lixi += benyue_changhuan_lixi
            total_huankuan_num += round(benyue_changhuan_lixi+benyue_huankuan_benjin, 2)
            total_benjin_num += benyue_huankuan_benjin
            shengyu_benjin = benyue_shengyu_benjin

    print("总还款金额={}, 总还款本金={}, 总利息={} \n\n".format(round(total_huankuan_num, 2),round(total_benjin_num, 2), round(total_lixi, 2)))

    # import pandas as pd
    # data1 = pd.DataFrame(dic1)
    # data1.head()

    return shengyu_benjin


def xianxi_houben(principal, rate, periods, interest_only_periods):
    """
    计算先息后本贷款的每期还款额和总共支付的利息

    :param principal: 贷款本金
    :param rate: 年利率
    :param periods: 贷款期数
    :param interest_only_periods: 先息期数，即仅还利息的期数
    :return: 每期还款额和总支付利息
    """
    # 计算每期利息
    monthly_rate = rate / 12 / 100
    interest_only_payment = round(principal * monthly_rate, 2)
    principal_payment = principal / (periods - interest_only_periods)

    # 计算总共支付的利息
    total_interest = interest_only_payment * interest_only_periods + principal_payment * (
                periods - interest_only_periods) * (periods - interest_only_periods + 1) / 2

    # 计算每期还款额
    payment = interest_only_payment + principal_payment

    total_huankuan_num = 0
    total_benjin_num = 0
    total_lixi = 0

    for index in range(1, periods + 1):
        if index <= interest_only_periods:
            huankuan_benjin = 0
            interest_only_payment = interest_only_payment
        else:
            huankuan_benjin = principal_payment
            interest_only_payment = round(principal * monthly_rate, 2)
            principal = principal - huankuan_benjin
        total_huankuan = interest_only_payment + huankuan_benjin

        total_benjin_num += huankuan_benjin
        total_huankuan_num += total_huankuan
        total_lixi += interest_only_payment
        print("还款期数：{}，还款金额：{}，还款本金：{}，还款利息：{}，剩余本金：{}".format(index, total_huankuan, huankuan_benjin, interest_only_payment, principal))

    print("总还款金额={}, 总还款本金={}, 总利息={} \n\n".format(round(total_huankuan_num, 2), round(total_benjin_num, 2),
                                                   round(total_lixi, 2)))
    return payment, total_interest

if __name__ == '__main__':
    total_money = 1000000   # 贷款总额


    # 截止还款期数，用于查看阶段性利息
    jiezhi_start = 0
    jiezhi_end = 12

    # deng_e_ben_jin(total_money, lilv, meinian_huankuan_cishu)

    # 一期调整利率 5.45%
    lilv = 5.45  # 利率
    daikuan_zhouqi = 360  # 贷款周期
    shengyu_benjin = deng_e_ben_xi(total_money, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)

    # 二期调整利率 5.4%
    lilv = 5.4  # 5.1
    daikuan_zhouqi = 360 - 12
    # 截止还款期数，用于查看阶段性利息
    shengyu_benjin2 = deng_e_ben_xi(shengyu_benjin, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)

    print("2023年1-6月份已还，计入已支付，提前还贷需要等待3个月，也累计进入5.1利率中")
    # 目前已还7个月
    # 三期调整利率  5.1%
    lilv = 5.1  # 5.1
    daikuan_zhouqi = 360 - 12 * 2
    # 截止还款期数，用于查看阶段性利息
    # 截止还款期数，用于查看阶段性利息
    jiezhi_start = 0
    jiezhi_end = 9
    shengyu_benjin3 = deng_e_ben_xi(shengyu_benjin2, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)

    print("开始计算对比 降低利率之后， 求1年之间的利息差额")

    print("保持5.1利率不变，不提前还款")
    # 三期调整利率  5.1%
    lilv = 5.1  # 5.1
    daikuan_zhouqi = 360 - 12 * 2 - 9
    # 截止还款期数，用于查看阶段性利息
    jiezhi_start = 0
    jiezhi_end = 12
    shengyu_benjin4 = deng_e_ben_xi(shengyu_benjin3, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)


    # print("3.91的利率")
    # # 三期调整利率  5.1%
    # lilv = 3.91  # 5.1
    # daikuan_zhouqi = 360 - 12 * 2 - 9
    # # 截止还款期数，用于查看阶段性利息
    # jiezhi_start = 0
    # jiezhi_end = 12
    # shengyu_benjin4 = deng_e_ben_xi(shengyu_benjin3, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)


    # 开始计算对比 提前还款和不提前还款的利差
    print("开始计算对比 提前还款和不提前还款的利差， 求1.5年之间的利息差额")

    print("保持5.1利率不变，不提前还款")
    # 三期调整利率  5.1%
    lilv = 5.1  # 5.1
    daikuan_zhouqi = 360 - 12 * 2 - 9
    # 截止还款期数，用于查看阶段性利息
    jiezhi_start = 0
    jiezhi_end = -1
    shengyu_benjin4 = deng_e_ben_xi(shengyu_benjin3, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)


    print("消费贷还商贷策略， 提前还款50w,其中10w为消费贷\n")
    # 三期调整利率  3.7%
    lilv = 5.1  # 5.1
    daikuan_zhouqi = 360 - 12 * 2 - 9
    # 截止还款期数，用于查看阶段性利息
    jiezhi_start = 0
    jiezhi_end = -1
    shengyu_benjin3 = deng_e_ben_xi(shengyu_benjin3-500000, lilv, daikuan_zhouqi, jiezhi_start, jiezhi_end)


    print("消费贷的利息")
    lilv = 3.4 # 5.1
    daikuan_zhouqi = 18
    interest_only_periods= 17  #  先息期数，即仅还利息的期数
    shengyu_benjin3 = xianxi_houben(100000, lilv, daikuan_zhouqi, interest_only_periods)

