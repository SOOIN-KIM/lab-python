

def experiment(type,n, t):
    '''

    :param type: 실험 타입(동전 던지기 or 주사위 던지기,...)
    :param n: 동전 or 주사위의 갯수
    :param t: 실험 횟수
    :return: 리스트
    '''
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t):  # 실험 횟수만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 동전 갯수만큼 반복
            rand = random.choice(type)  # 'H' or 'T'
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 tuple로 변환 후 저장
        # Counter 클래스는 tuple의 갯수는 셀 수 있지만,
        # list의 갯수는 셀 수 없음!
        cases.append(tuple(case))
    return cases


if __name__== '__main__':
    '''
    scratch06\ex01.py
    확률

    사건 공간(universe of events)
    사건(event)
    확률(probability)
    '''
    from collections import Counter
    import random

    coin = ['H', 'T']
    dice = [1, 2, 3, 4, 5, 6]
    trials = 10_000

    # 동전 1개를 10,000번 던지느 실험
    # 앞면이 나올 확률과 뒷면이 나올 확률이 1/2임을 증명
    heads, tails = 0, 0  # 앞면과 뒷면이 나오는 횟수를 저장할 변수
    for _ in range(trials):  # 10,000번 반복
        random_coin = random.choice(coin)  # 동전 던진 결과(앞 또는 뒤)
        if random_coin == 'H':
            heads += 1
        else:
            tails += 1
    p_h = heads / trials  # 앞면이 나올 확률 = 앞면횟수 / 전체 횟수
    p_t = tails / trials  # 뒷면이 나올 확률
    print('P(H) =', p_h)
    print('P(T) =', p_t)

    # 동전 2개를 던지는 실험(10,000번)
    # 1) 앞면의 갯수가 1개일 확률 = 1/2
    # 2) 첫번째 동전이 앞면일 확률 = 1/2
    # 3) 적어도 한개의 동전이 앞면인 확률 =3/4

    coin1 = ['H', 'T']
    coin2 = ['H', 'T']
    heads1, tails1 = 0, 0
    heads2, tails2 = 0, 0

    for _ in range(trials):
        random_coin1 = random.choice(coin1)
        random_coin2 = random.choice(coin2)
        if random_coin1 == 'H' and random_coin2 == 'H':
            heads1 += 1
            heads2 = + 1
        elif random_coin1 == 'H' and random_coin2 == 'T':
            heads1 += 1
            tails2 += 1
        elif random_coin1 == 'T' and random_coin2 == 'H':
            tails1 += 1
            heads2 += 1
        else:
            tails1 += 1
            tails2 += 1

    p_h1h2 = (heads1 + heads2) / trials
    p_h1t2 = (heads1 + tails1) / trials
    p_t1h2 = (tails1 + heads2) / trials
    p_t1t2 = (tails1 + tails2) / trials
    # 1)
    print(p_h1t2 * p_t1h2)
    # 2)
    print(p_h1h2 * p_h1t2)
    # 3)
    print(1 - (p_h1h2 * p_h1t2 * p_t1h2))

    # 동전 3개를 던지는 실험(10,000번)
    coin1 = ['H', 'T']
    coin2 = ['H', 'T']
    coin3 = ['H', 'T']
    heads1, tails1 = 0, 0
    heads2, tails2 = 0, 0
    heads3, tails3 = 0, 0

    trials = 10_000

    x = []
    for _ in range(trials):
        random_coin1 = random.choice(coin1)
        random_coin2 = random.choice(coin2)
        random_coin3 = random.choice(coin3)

    coin_exp = experiment(coin, 2, 10_000)
    print(coin_exp[0:10])  # 첫 10개의 결과 확인

    # 동전 던지기 실험 경우의 수
    coin_event_counts = Counter(coin_exp)
    print(coin_event_counts)


    def how_many_heads(x):
        counter = Counter(x)
        return counter['H']


    num_of_cases = 0
    for ev, cnt in coin_event_counts.items():
        if how_many_heads(ev) == 1:
            num_of_cases += cnt
    p_h1 = num_of_cases / trials
    print('P(앞면이 1개일 확률) =', p_h1)

    num_of_cases = 0
    for ev, cnt in coin_event_counts.items():
        # if ev == ('H','H') or ev ==('H','T'):
        if ev[0] == 'H':
            num_of_cases += cnt
    p_first_h = num_of_cases / trials
    print('P(첫번째 동전이 앞면) =', p_first_h)

    num_of_cases = 0
    for ev, cnt in coin_event_counts.items():
        if how_many_heads(ev) == 1 or how_many_heads(ev) == 2:
            num_of_cases += cnt
    p = num_of_cases / trials
    print('P(적어도 1개가 앞면) =', p)

    # 여사건 이용
    for ev, cnt in coin_event_counts.items():
        if how_many_heads(ev) == 0:
            num_of_cases += cnt
    p = num_of_cases / trials
    print('P(적어도 1개가 앞면) =', 1 - p)

    # H = 1, T = 0 약속 -> coin[1,0] # 첫번째가앞면인지 두번째가 앞면인지 알 수 없다.
    coin2 = [1, 0]
    cases = []
    for _ in range(trials):
        num_of_heads = 0
        for _ in range(2):
            num_of_heads += random.choice(coin2)
        cases.append(num_of_heads)
    print(cases[0:10])
    coin_event_counts = Counter(cases)
    print('P(H=0) =', coin_event_counts[0] / trials)
    print('P(H=1) =', coin_event_counts[1] / trials)
    print('P(H=2) =', coin_event_counts[2] / trials)

    # 주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률
    # 주사위 2개를 던졌을 때, 적어도 하나가 나올 확률

    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]

    # dice_exp = experiment(dice,2,10_000)
    # dice_event_count = Counter(dice_exp)
    # print(dice_event_count)
    #
    # def how_many_sum8(x):
    #     counter = Counter(x)
    #     return counter[2,6], counter[3,5], counter[4,4],counter[5,3], counter[6,2]
    #
    # num_of_sum8 = 0
    # for ev,cnt in dice_event_count.items():
    #     if how_many_sum8(ev) ==

    # 1)
    dice_exp = experiment(dice, 2, 10_000)
    print(dice_exp[0:5])

    event_counts = Counter(dice_exp)
    print(len(event_counts))
    print(event_counts)

    num_of_cases = 0
    for ev, cnt in event_counts.items():
        # if ev[0] + ev[1] ==8:
        if sum(ev) == 8:
            num_of_cases += cnt
    p = num_of_cases / trials
    print('P(두 눈의 합=8) =', p, 5 / 36)

    # 2)
    num_of_cases = 0
    for ev, cnt in event_counts.items():
        if ev[0] % 2 == 0 or ev[1] % 2 == 0:
            num_of_cases += cnt
    p = num_of_cases / trials
    print('P(적어도 하나가 짝수) =', p, 27 / 36)