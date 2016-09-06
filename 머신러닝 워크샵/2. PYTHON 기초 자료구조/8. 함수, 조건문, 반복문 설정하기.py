#1
def sum_even_numbers(start, end):
    sum=0
    for i in range(start,end+1):
        if i%2 == 0:
            sum=sum+i
    return sum
print(sum_even_numbers(1, 10))
