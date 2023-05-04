import csv

def Q4():
    INF = 0x3f3f3f3f # if array doesn't have data

    # file open
    f = open('q4.csv', 'r', encoding='cp949')
    data = csv.reader(f)

    # print header 
    header = next(data)
    # print(header)

    # row init
    maxi = [0] * 5
    mini = [INF, INF, INF, INF, INF]
    maxstr = ["", "", "", "", ""]
    minstr = ["", "", "", "", ""]
    
    for row in data:
        for i in range(4, 6):
            row[i] = -INF if row[i] == '' else int(row[i])
        if(row[4] != -INF and row[5] != -INF):
            str = ""
            for i in range(1, 5):
                str = f"{i}?Ш╕?Да"
                if(row[1] == str):
                    sum = row[4] + row[5]
                    if(maxi[i] < sum):
                        maxstr[i] = row[3]
                        maxi[i] = sum
                    if(mini[i] > sum):
                        minstr[i] = row[3]
                        mini[i] = sum
                    
    # print answer
    print("*** Subway Report for Seoul on March 2023 ***")
    for i in range(1, 5):
        print(f"Line {i}:")
        print(f"Busiest Station: {maxstr[i]} ({maxi[i]})")
        print(f"Least used Station: {minstr[i]} ({mini[i]})")
    
    # file close 
    f.close()

def main():
    Q4()
if __name__ =="__main__":
    main()
    