import csv

def Q3():
    INF = 0x3f3f3f3f # if array doesn't have data

    # file open
    f = open('q3.csv', 'r', encoding='cp949')
    data = csv.reader(f)

    # print header 
    header = next(data)
    # print(header)

    # row init
    cnt = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for row in data:
        for i in range(4, 6):
            row[i] = -INF if row[i] == '' else int(row[i])
        if(row[4] != -INF and row[5] != -INF):
            str = ""
            for i in range(1, 10):
                str = f"{i}호선"
                if(row[1] == str):
                    cnt[i] += row[4] + row[5]
    arr = [0] * 10
    for i in range(0, 10):
        arr[i] = cnt[i]
    arr.sort()
    B1 = 0
    B2 = 0
    L1 = 0
    L2 = 0
    
    for i in range(1, 10):
        if(arr[9] == cnt[i]):
            B1 = i
        if(arr[8] == cnt[i]):
            B2 = i
        if(arr[1] == cnt[i]):
            L1 = i
        if(arr[2] == cnt[i]):
            L2 = i
            
    # print answer
    print("*** Subway Report for Seoul on March 2023 ***")
    print(f"1st Busiest Line: Line {B1} ({cnt[B1]})")
    print(f"2st Busiest Line: Line {B2} ({cnt[B2]})")
    print(f"1st Least Line: Line {L1} ({cnt[L1]})")
    print(f"2st Least Line: Line {L2} ({cnt[L2]})")
    # file close 
    f.close()

def main():
    Q3()
if __name__ =="__main__":
    main()
    