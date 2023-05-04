import csv

def Q1():
    INF = 0x3f3f3f3f # if array doesn't have data

    # file open
    f = open('q1.csv', 'r', encoding='cp949')
    data = csv.reader(f)

    # print header 
    header = next(data)
    # print(header)

    # row init
    # row is [0]: date / [1]: point / [2]: avg / [3]: low / [4]: high 
    cnt = 0
    avg = 0
    avg_lo = 0
    avg_hi = 0

    for row in data:
        for i in range(2, 5):
            row[i] = INF if row[i] == '' else float(row[i])
        if(row[2] != INF and row[3] != INF and row[4] != INF):
            cnt += 1
            avg += row[2]
            avg_lo += row[3]
            avg_hi += row[4]
            
    avg /= cnt
    avg_lo /= cnt
    avg_hi /= cnt
    # print answer
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print(f"Average Temperature: {avg:.1f} Celsius")
    print(f"Average Minimum Temperature: {avg_lo:.1f} Celsius")
    print(f"Average Maximum Temperature: {avg_hi:.1f} Celsius")

    # file close 
    f.close()

def main():
    Q1()
if __name__ =="__main__":
    main()
    