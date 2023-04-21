# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    throughputArr = []
    AvgFilledSlotsArr = []
    transactionsArr = []

    # Varying Times
    for each in range(1, 13):

        tau = 1/5
        omega = 6
        T = each
        transactions = int(T / tau)
        P00 = 0

        transactionsArr.append(transactions)
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
        
        print(Coefficient)


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
        print("----------")
        print(Coefficient)
        print(P00)

        total_P = 0
        for i in range(transactions):
            for j in range(transactions - i):
                P[i][j] = Coefficient[i][j] * P00
                total_P += P[i][j]
        print(P)
        print(total_P)
        total_throughput = 0
        for i in range(transactions):
            Throughput[i][transactions - i - 1] = (((T/tau) - (transactions - i - 1)) / omega) * P[i][transactions - i - 1]
            total_throughput += Throughput[i][transactions - i - 1]
        print("-----Throughput----")
        print (Throughput)
        print(total_throughput)
        throughputArr.append(total_throughput)
        total_AVGSLT = 0
        for i in range(transactions):
            for j in range(transactions - i):
                AvgFilledSlots[i][j] = i * P[i][j]
                total_AVGSLT += AvgFilledSlots[i][j]
        
        print("-----------AvgFilledSlots-------------")
        print(AvgFilledSlots)
        print(total_AVGSLT)
        AvgFilledSlotsArr.append(total_AVGSLT)

        


    y = [1, 2, 3, 4, 5]


    plt.plot(transactionsArr, AvgFilledSlotsArr)

    # Add labels and title
    plt.xlabel('Number of Transactions')
    plt.ylabel('Average Filled Slots')
    plt.title('Average Filled Slots VS Number of Transactions')

    plt.show()

    y = [1, 2, 3, 4, 5]


    plt.plot(transactionsArr, throughputArr)

    # Add labels and title
    plt.xlabel('Number of Transactions')
    plt.ylabel('Throughput')
    plt.title('Throughput VS Number of Transactions')

    plt.show()

    # Varying Omega
    throughputArr = []
    AvgFilledSlotsArr = []
    omegaArr = []

    for each in range(3, 16):


        tau = 1/5
        omega = each
        T = 6
        transactions = int(T / tau)
        P00 = 0
        omegaArr.append(omega)

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
        
        print(Coefficient)


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
        print("----------")
        print(Coefficient)
        print(P00)

        total_P = 0
        for i in range(transactions):
            for j in range(transactions - i):
                P[i][j] = Coefficient[i][j] * P00
                total_P += P[i][j]
        print(P)
        print(total_P)
        total_throughput = 0
        for i in range(transactions):
            Throughput[i][transactions - i - 1] = (((T/tau) - (transactions - i - 1)) / omega) * P[i][transactions - i - 1]
            total_throughput += Throughput[i][transactions - i - 1]
        print("-----Throughput----")
        print (Throughput)
        print(total_throughput)
        throughputArr.append(total_throughput)
        total_AVGSLT = 0
        for i in range(transactions):
            for j in range(transactions - i):
                AvgFilledSlots[i][j] = i * P[i][j]
                total_AVGSLT += AvgFilledSlots[i][j]
        
        print("-----------AvgFilledSlots-------------")
        print(AvgFilledSlots)
        print(total_AVGSLT)
        AvgFilledSlotsArr.append(total_AVGSLT)

        

    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    plt.plot(omegaArr, AvgFilledSlotsArr)

    # Add labels and title
    plt.xlabel('Omega')
    plt.ylabel('Avg. Filled Slots')
    plt.title('Average Filled Slots VS Omega')

    plt.show()

    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    plt.plot(omegaArr, throughputArr)

    # Add labels and title
    plt.xlabel('Omega')
    plt.ylabel('Throughput')
    plt.title('Throughput VS Omega')

    plt.show()





