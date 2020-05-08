import sys
import random
import math
def main():
    '''
    db_file = sys.argv[1] 
    query_file = sys.argv[2]
    beacon_file = sys.argv[3]
    control_file = sys.argv[4]
    '''
    # read and open required file for both attack and flipping process
    db_file = "Beacon_CEU.txt" 
    query_file = "ssmall_query.txt"
    beacon_file = "beacon_use_it.txt"
    control_file = "control_use_it.txt"
  
    f2 = open(query_file, 'r')
    
    '''
    # Randomly select people in the beacon and in the control group
    # 84 people for each
    beacon = open(beacon_file,"w")
    control = open(control_file,"w")
    random_select(f1, control, beacon)
    '''

    # Output file has 5 columns
    # Column titles are shown below  
    # For queries that have been asked, the Real_Answer column is "A" (Asked)
    # For queries that do not go through RTF, the Power column is "-"
    out = open("output_non.txt","w")
    out.write("Query Results")
    out.write("\n")
    out.write("Marker_ID SNP Response t_alpha Power")
    out.write("\n")
    out.write("\n")

    # Number of asked queries (including the current query)
    size = 0
    # list to save power (LRT val) for coutrol group 
    lrt_control = []
    maf_control = []
    maf_control_zero = []
    # list to save power (LRT val) for beacon group
    lrt_beacon = []
    maf_beacon = []
    maf_beacon_zero = []
    done = 0

    # initialized lists for saving power (LRT val) for control group and beacon group
    for i in range(40):
        lrt_control.append(0.0)
        maf_control.append([])
        maf_control_zero.append([])
        lrt_beacon.append(0.0)
        maf_beacon.append([])
        maf_beacon_zero.append([])

    # main loop for attack and flipping process
    while not done:
      # open and read the query file
        line = f2.readline()

        size = size + 1
        print(size)
        # finish the main loop after reading the entire query file
        if line == '':
            done = 1

        else:
            query = line.strip('\n').split(' ')

            snp = [query[3], query[6]]
            rs = query[2]
            out.write(rs + " "+snp[0]+snp[1]+" ")
            print(rs + " "+snp[0]+snp[1])
            
            # Retreive response from beacon
            f4 = open(beacon_file, 'r')
            done_beacon = 0
            response = 0
            while not done_beacon:
                line_beacon = f4.readline()
                if line_beacon == '':
                    done_beacon = 1
                else:
                    lline_beacon = line_beacon.replace('\n', "").strip('\t').split('\t')
                    if lline_beacon[0] == rs:
                        for i in range(1, len(lline_beacon)):
                            if snp[0] in lline_beacon[i] and snp[1] in lline_beacon[i]:
                                response = 1
                                done_beacon = 1
            out.write(str(response)+" ")
            print("Response: "+str(response))

            # Calculate lambda for control group and t_alpha
            f3 = open(control_file, 'r')
            done_control = 0
            while not done_control:
                line_control = f3.readline()
                if line_control == '':
                    done_control = 1
                    print("Marker ID does not exist!")
                    out.write(" X X X")
                    out.write("\n")
                else:
                    lline_control = line_control.replace('\n', "").strip('\t').split('\t')
                    if lline_control[0] == rs:
                        lrt_control = cal_lambda_control(lrt_control, lline_control, snp, query[7], size, maf_control, maf_control_zero, response)
                        # print("Control:")
                        # print(lrt_control)
                        t_alpha = find_t_alpha(lrt_control)
                        print("t_alpha: "+str(t_alpha))
                        out.write(str(t_alpha))
                        out.write(" ")
                        done_control = 1
            f3.close()

            f4 = open(beacon_file, 'r')
            done_beacon = 0
            power = 0
            while not done_beacon:
                line_beacon = f4.readline()
                if line_beacon == '':
                    done_beacon = 1
                else:
                    lline_beacon = line_beacon.replace('\n', "").strip('\t').split('\t')
                    if lline_beacon[0] == rs:
                        lrt_beacon = cal_lambda_beacon(lrt_beacon, lline_beacon, snp, query[7], size, maf_beacon, maf_beacon_zero, response)
                        # print("Beacon:")
                        # print(lrt_beacon)
                        power = round(cal_power(lrt_beacon, t_alpha),4)
                        print("Power: "+str(power))
                        out.write(str(power))
                        out.write("\n")
                        done_beacon = 1
            f4.close()
            print("")
            print("MAF_control:")
            # print(maf_control)
            print(maf_control_zero)
            print("lrt_control:")
            print(lrt_control)
            print("MAF_beacon:")
            print(maf_beacon)
            # print(maf_beacon_zero)
            print("lrt_beacon:")
            print(lrt_beacon)
            print(" ")
    f2.close()
    out.close()
            



def cal_lambda_control(lrt_control, lline_control, snp, maf, N, maf_control, maf_control_zero, response):
    # print("SNP: ")
    # print(snp)
    # print("ll_control")
    # print(lline_control)
    # print("MAF_control:")
    # print(maf_control)
    for i in range(1, len(lline_control)):
        if snp[0] in lline_control[i] and snp[1] in lline_control[i]:
            if response == 1:
                maf_control[i-1].append(maf)
            else:
                maf_control_zero[i-1].append(maf)
        temp = 0
        for j in range(len(maf_control[i-1])):
            if maf_control[i-1][j] == 0:
                temp = temp + math.log(round((1-math.pow(1-0.00001, 2*N))/(1-0.0001* math.pow(1-0.00001,2*N-2)),8))
            else:
                temp = temp + math.log(round((1-math.pow(1-float(maf_control[i-1][j]), 2*N))/(1-0.0001* math.pow(1-float(maf_control[i-1][j]),2*N-2)),8))
        for j in range(len(maf_control_zero[i-1])):
            temp = temp + math.log(round(math.pow(1-float(maf_control_zero[i-1][j]), 2)/0.0001,8))
        lrt_control[i-1] = temp
    return lrt_control

def find_t_alpha(lrt_control):
    i = 0
    t1 = 1000000000
    t2 = 1000000000
    t3 = 1000000000
    while i < 40:
        if lrt_control[i] < t1:
            t1 = lrt_control[i]
        elif lrt_control[i] < t2:
            t2 = lrt_control[i]
        elif lrt_control[i] < t3:
            t3 = lrt_control[i]
        i = i + 1
    return float(t2+t3)/2


def cal_lambda_beacon(lrt_beacon, lline_beacon, snp, maf, N, maf_beacon, maf_beacon_zero, response):
    for i in range(1, len(lline_beacon)):
        if snp[0] in lline_beacon[i] and snp[1] in lline_beacon[i]:
            if response == 1:
                maf_beacon[i-1].append(maf)
            else:
                maf_beacon_zero[i-1].append(maf)
        temp = 0
        for j in range(len(maf_beacon[i-1])):
            if float(maf_beacon[i-1][j]) == 0:
                temp = temp + math.log(round((1-math.pow(1-0.00001, 2*N))/(1-0.0001* math.pow(1-0.00001,2*N-2)),8))
            else:
                temp = temp + math.log(round((1-math.pow(1-float(maf_beacon[i-1][j]), 2*N))/(1-0.0001* math.pow(1-float(maf_beacon[i-1][j]),2*N-2)),8))
        for j in range(len(maf_beacon_zero[i-1])):
            temp = temp + math.log(round(math.pow(1-float(maf_beacon_zero[i-1][j]), 2)/0.0001,8))
        lrt_beacon[i-1] = temp
    return lrt_beacon

def cal_power(lrt_beacon, t_alpha):
    power = 0
    for lrt in lrt_beacon:
        if lrt < t_alpha:
            power = power + 1
    print("Risk: "+str(power))
    return float(power)/40





if __name__ == "__main__":
    # "Beacon_CEU.txt"
   #main(sys.argv[1:])
   main()