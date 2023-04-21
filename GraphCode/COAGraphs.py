# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    throughputArr = []
    AvgFilledSlotsArr = []
    timeArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for varyOmg in range(3, 10, 3):
        throughputARR__ = []
        AvgFilledSlotsArr__ = []


        # Varying Times
        for each in timeArr:
            tau = 1/5
            omega = varyOmg
            T = each
            transactions = int(T / tau)
            P00 = 0

            A = np.zeros((transactions, transactions), dtype=np.longdouble)
            B = np.zeros((transactions, transactions), dtype=np.longdouble)
            Coefficient = np.zeros((transactions, transactions), dtype=np.longdouble)
            P = np.zeros((transactions, transactions), dtype=np.longdouble)
            Throughput = np.zeros((transactions, transactions), dtype=np.longdouble)
            AvgFilledSlots = np.zeros((transactions, transactions), dtype=np.longdouble)

            for i in range(transactions - 1):
                for j in range(transactions - i - 1):
                    b = np.power(2, i + j)
                    B[i][j] = b

                    if j == 0 or i == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = A[i][j - 1] * (1 + (i / j))
                    Coefficient[i][j] = A[i][j]/B[i][j]
                    P00 += Coefficient[i][j]
            
            #print(Coefficient)


            for i in range(transactions):
                #print(P[i][transactions - i - 1], "   ---   Index: ",i ," ", transactions - i - 1)
                if i == 0:
                    Coefficient[i][transactions - i - 1] = Coefficient[i][transactions - i - 2] * (tau/omega)
                elif transactions == i:
                    Coefficient[i][transactions - i - 1] = Coefficient[i - 1][transactions - i - 1] * (tau/omega)
                else:
                    Coefficient[i][transactions - i - 1] = (Coefficient[i-1][transactions - i - 1] + Coefficient[i][transactions - i - 2]) * (tau/omega)
                P00 += Coefficient[i][transactions - i - 1]
            
            P00 = 1/P00
            #print("----------")
            #print(Coefficient)
            #print(P00)

            total_P = 0
            for i in range(transactions):
                for j in range(transactions - i):
                    P[i][j] = Coefficient[i][j] * P00
                    total_P += P[i][j]
            #print(P)
            #print(total_P)
            total_throughput = 0
            for i in range(transactions):
                Throughput[i][transactions - i - 1] = (((T/tau) - (transactions - i - 1)) / omega) * P[i][transactions - i - 1]
                total_throughput += Throughput[i][transactions - i - 1]
            #print("-----Throughput----")
            #print (Throughput)
            #print(total_throughput)
            throughputARR__.append(total_throughput)
            total_AVGSLT = 0
            for i in range(transactions):
                for j in range(transactions - i):
                    AvgFilledSlots[i][j] = i * P[i][j]
                    total_AVGSLT += AvgFilledSlots[i][j]
            
            #print("-----------AvgFilledSlots-------------")
            #print(AvgFilledSlots)
            #print(total_AVGSLT)
            AvgFilledSlotsArr__.append(total_AVGSLT)
        
        AvgFilledSlotsArr.append(AvgFilledSlotsArr__)
        throughputArr.append(throughputARR__)
            
    print("------- 1st Part ---------")
    print("AvgFilledSlotsArr: ")
    print(AvgFilledSlots)
    print("throughputArr: ")
    print(throughputArr)
    print("timeArr:")
    print(timeArr)

    y = [1, 2, 3, 4, 5]


    plt.plot(timeArr, AvgFilledSlotsArr[0])
    plt.plot(timeArr, AvgFilledSlotsArr[1])
    plt.plot(timeArr, AvgFilledSlotsArr[2])


    # Add labels and title
    plt.xlabel('Number of Transactions')
    plt.ylabel('Average Filled Slots')
    plt.title('Average Filled Slots VS Number of Transactions')

    plt.show()

    y = [1, 2, 3, 4, 5]


    plt.plot(timeArr, throughputArr[0])
    plt.plot(timeArr, throughputArr[1])
    plt.plot(timeArr, throughputArr[2])


    # Add labels and title
    plt.xlabel('Number of Transactions')
    plt.ylabel('Throughput')
    plt.title('Throughput VS Number of Transactions')

    plt.show()



    # Varying Omega
    throughputArr = []
    AvgFilledSlotsArr = []
    omegaArr = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


    for varyT in range(6, 13, 3):
        throughputARR__ = []
        AvgFilledSlotsArr__ = []

        for each in omegaArr:

            tau = 1/5
            T = varyT
            transactions = int(T / tau)
            P00 = 0
            

            A = np.zeros((transactions, transactions), dtype=np.longdouble)
            B = np.zeros((transactions, transactions), dtype=np.longdouble)
            Coefficient = np.zeros((transactions, transactions), dtype=np.longdouble)
            P = np.zeros((transactions, transactions), dtype=np.longdouble)
            Throughput = np.zeros((transactions, transactions), dtype=np.longdouble)
            AvgFilledSlots = np.zeros((transactions, transactions), dtype=np.longdouble)


            for i in range(transactions - 1):
                for j in range(transactions - i - 1):
                    b = np.power(2, i + j)
                    B[i][j] = b

                    if j == 0 or i == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = A[i][j - 1] * (1 + (i / j))
                    Coefficient[i][j] = A[i][j]/B[i][j]
                    P00 += Coefficient[i][j]
            
            #print(Coefficient)


            for i in range(transactions):
                #print(P[i][transactions - i - 1], "   ---   Index: ",i ," ", transactions - i - 1)
                if i == 0:
                    Coefficient[i][transactions - i - 1] = Coefficient[i][transactions - i - 2] * (tau/omega)
                elif transactions == i:
                    Coefficient[i][transactions - i - 1] = Coefficient[i - 1][transactions - i - 1] * (tau/omega)
                else:
                    Coefficient[i][transactions - i - 1] = (Coefficient[i-1][transactions - i - 1] + Coefficient[i][transactions - i - 2]) * (tau/omega)
                P00 += Coefficient[i][transactions - i - 1]
            
            P00 = 1/P00
            #print("----------")
            #print(Coefficient)
            #print(P00)

            total_P = 0
            for i in range(transactions):
                for j in range(transactions - i):
                    P[i][j] = Coefficient[i][j] * P00
                    total_P += P[i][j]
            #print(P)
            #print(total_P)
            total_throughput = 0
            for i in range(transactions):
                Throughput[i][transactions - i - 1] = (((T/tau) - (transactions - i - 1)) / omega) * P[i][transactions - i - 1]
                total_throughput += Throughput[i][transactions - i - 1]
            #print("-----Throughput----")
            #print (Throughput)
            #print(total_throughput)
            throughputARR__.append(total_throughput)
            total_AVGSLT = 0
            for i in range(transactions):
                for j in range(transactions - i):
                    AvgFilledSlots[i][j] = i * P[i][j]
                    total_AVGSLT += AvgFilledSlots[i][j]
            
            #print("-----------AvgFilledSlots-------------")
            #print(AvgFilledSlots)
            #print(total_AVGSLT)
            AvgFilledSlotsArr__.append(total_AVGSLT)
        AvgFilledSlotsArr.append(AvgFilledSlotsArr__)
        throughputArr.append(throughputARR__)

    print("------- 2nd Part ---------")
    print("AvgFilledSlotsArr: ")
    print(AvgFilledSlots)
    print("throughputArr: ")
    print(throughputArr)
    print("omegaArr:")
    print(omegaArr)

    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    plt.plot(omegaArr, AvgFilledSlotsArr[0])
    plt.plot(omegaArr, AvgFilledSlotsArr[1])
    plt.plot(omegaArr, AvgFilledSlotsArr[2])


    # Add labels and title
    plt.xlabel('Omega')
    plt.ylabel('Avg. Filled Slots')
    plt.title('Average Filled Slots VS Omega')

    plt.show()

    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    plt.plot(omegaArr, throughputArr[0])
    plt.plot(omegaArr, throughputArr[1])
    plt.plot(omegaArr, throughputArr[2])


    # Add labels and title
    plt.xlabel('Omega')
    plt.ylabel('Throughput')
    plt.title('Throughput VS Omega')

    plt.show()





