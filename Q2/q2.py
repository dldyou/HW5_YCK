import csv

def Q2():
    INF = 0x3f3f3f3f # if array doesn't have data

    # file open
    f = open('q2.csv', 'r', encoding='cp949')
    data = csv.reader(f)

    # print header 
    header = next(data)
    # print(header)

    # row init
    # row is [0]: date / [1]: point / [2]: avg / [3]: low / [4]: high 
    maxi = -INF
    mini = INF
    maxD = []
    minD = []

    for row in data:
        for i in range(3, 5):
            row[i] = INF if row[i] == '' else float(row[i])
        if(row[2] != INF and row[3] != INF and row[4] != INF):
            diff = row[4] - row[3]
            if(maxi < diff):
                maxi = diff
                maxD = []
                maxD.append(row[0])
            elif(maxi == diff):
                maxD.append(row[0])
            if(mini > diff):
                mini = diff
                minD = []
                minD.append(row[0])
            elif(mini == diff):
                minD.append(row[0])
            
    # print answer
    print("*** Annual Temperature Report for Seoul in 2022 ***")
            
    print("Day with the Largest Temperature Variation: ", end="")
    for str in maxD:
        print(str, end=" ")
    print()
    print(f"Maximum Temperature Difference: {maxi:.2f} Celcius")
    
    print("Day with the Smallest Temperature Variation: ", end="")
    for str in minD:
        print(str, end=" ")
    print()
    print(f"Minimum Temperature Difference: {mini:.2f} Celcius")
            
    # file close 
    f.close()

def main():
    Q2()
if __name__ =="__main__":
    main()
    