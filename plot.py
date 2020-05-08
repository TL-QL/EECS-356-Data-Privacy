import matplotlib.pyplot as plt

def plot():
    # x-axis
    num_query = []
    # y-axis
    power_non = []
    power_rtf = []

    for i in range(1033):
        num_query.append(i+1)
    
    power_n = open("power_non.txt", 'r')
    power_r = open("power_rtf.txt", 'r')
    for i in range(1033):
        line = power_n.readline().strip('\n')
        line2 = power_r.readline().strip('\n')
        #print(line)
        power_non.append(float(line))
        power_rtf.append(float(line2))

    plt.plot(num_query, power_non, label = "Non-Flipping") 
    plt.plot(num_query, power_rtf, label = "RTF")

    plt.xlabel('Number of queries asked')
    plt.ylabel('Power')
    plt.title('Power of Optimal Attack for Non_flipping and RTF Strategies')
    plt.legend()

    plt.show() 

#plot()

def plot2():
    # x-axis
    num_query = []
    # y-axis
    num_flipped = []
    count = 0
    count_o = 0
    
    flipped = open("temp.txt", 'r')
    for i in range(1033):
        line = flipped.readline().strip('\n').split("\t")
        if int(line[0]) == 1:
            count_o = count_o + 1
            if int(line[1]) == 0:
                count = count + 1
            num_flipped.append(count)
            num_query.append(count_o)

    plt.plot(num_query, num_flipped, label="Real-time Flipping Method") 
    #plt.plot(num_query, power_rtf, label = "RTF")

    plt.xlabel('Number of queries whose response = 1')
    plt.ylabel('Number of queries flipped')
    plt.title('Rare First Order')
    plt.legend()

    plt.show() 

#plot2()

def plot3():
    # x-axis
    num_query = []
    # y-axis
    num_flipped = []
    count = 0
    count_o = 0
    
    flipped = open("temp_0.txt", 'r')
    for i in range(1032):
        line = flipped.readline().strip('\n').split("\t")
        if int(line[0]) == 1:
            count_o = count_o + 1
            if int(line[1]) == 0:
                count = count + 1
            num_flipped.append(1-float(count)/count_o)
            num_query.append(count_o)

    plt.plot(num_query, num_flipped, label="Real-time Flipping Method") 
    #plt.plot(num_query, power_rtf, label = "RTF")

    plt.xlabel('Number of queries whose response = 1')
    plt.ylabel('Utility')
    plt.title('Rare First Order')
    plt.legend()

    plt.show() 

plot3()


def plot4():
    # x-axis
    num_query = []
    # y-axis
    num_flipped = []
    count = 0
    count_o = 0
    
    flipped = open("temp.txt", 'r')
    for i in range(1032):
        line = flipped.readline().strip('\n').split("\t")
        if int(line[0]) == 1:
            count_o = count_o + 1
            if int(line[1]) == 0:
                count = count + 1
            num_flipped.append(count)
            num_query.append(count_o)

    plt.plot(num_query, num_flipped, label="Real-time Flipping Method") 
    #plt.plot(num_query, power_rtf, label = "RTF")

    plt.xlabel('Number of queries whose response = 1')
    plt.ylabel('Number of queries flipped')
    plt.title('Rare First Order')
    plt.legend()

    plt.show() 

#plot4()