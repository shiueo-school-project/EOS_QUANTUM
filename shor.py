import random
import math
import sys

sys.setrecursionlimit(100000000)


def main(N):
    # 1. 1보다 크고 N보다 작은 정수 a를 임의로 선택
    a = random.randint(2, N - 1)
    gcd = math.gcd(N, a)
    # 2. gcd(N,a) != 1이면, p를 찾은 것. -> 따라서 q = N/a
    if gcd != 1:
        return gcd, N // gcd
    print("a", a)

    # 3. f(x) = a^x(mod N)의 주기 r을 찾고, r이 짝수가 아니라면 1번부터 다시 시작
    def Period(N, a):
        for i in range(1, N):
            if (a**i) % N == 1:
                print("i", i)
                return i
        return -1

    r = Period(N, a)
    while 1:
        if r % 2 == 0:
            break
        else:
            print("r", r)
            main(N)
    # 4. 주기 r로부터 두개의 최대공약수 gcd(N, a^(r/2)+1), gcd(N, a^(r/2)-1)를 찾는다
    gcd1 = math.gcd(N, a ** (r // 2) + 1)
    gcd2 = math.gcd(N, a ** (r // 2) - 1)
    # 5. gcd_1, gcd_2중 하나라도 1 or N 이라면 1부터 다시 시작한다. 아니면 소인수들을 찾은 것이기 때문에 gcd_1, gcd_2를 리턴한다.
    while 1:
        if gcd1 == 1 or gcd2 == 1 or gcd1 == N or gcd2 == N:
            main(N)
        else:
            return gcd1, gcd2


if __name__ == "__main__":
    print(main(int(input())))
