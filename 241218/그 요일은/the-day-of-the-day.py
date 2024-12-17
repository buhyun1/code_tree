days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def count_day(month, day):
    total_days = sum(days[:month]) 
    return total_days + day

def find_index(target_day):
    return week.index(target_day)

def count_week(index, total_days):
    count = total_days // 7
    if total_days % 7 >= index: 
        count += 1
    return count

def main():
    m1, d1, m2, d2 = map(int, input().split())
    target_day = input().strip()
    
    total_days = count_day(m2, d2) - count_day(m1, d1)
    target_index = find_index(target_day)
    
    print(count_week(target_index, total_days))

if __name__ == "__main__":
    main()
