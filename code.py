def add_all_the_numbers(actual_list, input_range):
    start = int(input_range[0])
    end = int(input_range[1])
    sum_of = 0
    for i in range(start, end+1):
        if i in actual_list:
            count_of = actual_list.count(i)
            sum_of += (i * count_of)
    return sum_of
actual_list = list(map(int, input().split()))
num = int(input())
for i in range(num):
    input_range = input().split()
    result = add_all_the_numbers(actual_list, input_range)
    print(result)
