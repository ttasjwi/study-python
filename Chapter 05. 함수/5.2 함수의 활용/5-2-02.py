# 피보나치 수열
dp = {  # 메모이제이션
    1: 1,
    2: 1
}


def fibonacci(n: int) -> int:
    if n in dp:  # dp에 저장되어 있으면 저장된 값을 호출한다.
        return dp[n]
    # dp에 저장되어 있지 않으면 재귀함수를 통해 저장되어 있지 않은 값을 계산해 저장후 반환한다.
    dp[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return dp[n]


print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))

