
def calculate_duration(SH, SM, EH, EM):
    start_time = SH * 60 + SM
    end_time = EH * 60 + EM
    duration = end_time - start_time
    hours = duration // 60
    minutes = duration % 60
    return f"{hours} hours {minutes} minutes"

N = int(input())
for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())
    print(calculate_duration(SH, SM, EH, EM))
