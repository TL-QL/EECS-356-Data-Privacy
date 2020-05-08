import random

def random_select_rs(control, beacon, small_control, small_beacon):
    done = 0
    line1 = control.readline()
    small_control.write(line1)
    line2 = beacon.readline()
    small_beacon.write(line2)
    while not done:
        r=random.randint(0, 1)
        line1 = control.readline()
        line2 = beacon.readline()
        #print("r: "+ str(r))
        if r == 1:
            if line1 == '':
                done = 1
            else:
                small_control.write(line1)
                small_beacon.write(line2)
                #print(line1)
    small_beacon.close()
    small_control.close()
    control.close()
    beacon.close()
    print("Finished random!")

# control = open("control.txt",'r')
# beacon = open("beacon.txt",'r')
# small_control = open("small_control.txt",'w')
# small_beacon = open("small_beacon.txt",'w')
# random_select_rs(control,beacon,small_control,small_beacon)

def filter(query, control, filtered_query):
    rs = set()
    done = 0
    #print("rs:")
    while not done:
        line = control.readline()
        if line == '':
            done = 1
        else:
            lline = line.strip('\n').split('\t')
            rs.add(lline[0])
            #print(lline[0])
    #print("")
    #print("query:")
    control.close()
    #print(rs)
    done = 0
    while not done:
        line = query.readline()
        if line == '':
            done = 1
        else:
            lline = line.strip('\n').split(' ')
            #print(line)
            if lline[2] in rs:
                filtered_query.write(line)
    query.close()
    filtered_query.close()
    #print("")

def random_select(f1, small_query):
    query_id=[]
    i = 0
    line_num = 0
    done = 0
    while i < 1500:
        # 2014435
        r=random.randint(0,  2015198)
        if r not in query_id:
            query_id.append(r)
            i = i + 1

    while not done:
        line = f1.readline()
        if line == '':
            done = 1
        elif line_num in query_id:
            small_query.write(line)
        line_num = line_num + 1
    small_query.close()
    f1.close()

def my_random():
    i = 0
    rand = []
    while i < 40:
        r=random.randint(0, 81)
        if r not in rand:
            rand.append(r)
            i = i + 1
    print(rand)

def filt_zero(small_query, rs, ssss):
    done = 0
    rrs = []
    while not done:
        line = rs.readline()
        if line == '':
            done = 1
        else:
            lline = line.strip('\n').split('\t')
            rrs.append(lline[0])
    rs.close()
    done = 0
    while not done:
        line = small_query.readline()
        if line == '':
            done = 1
        else:
            lline = line.strip('\n').split(' ')
            if lline[2] in rrs:
                ssss.write(line)
    small_query.close()
    ssss.close()

def filtered_one(small_query,ssmall_query):
    done= 0
    size = 0
    while not done:
        size = size+1
        print(size)
        line=small_query.readline()
        if line=='':
            done=1
        else:
            lline = line.strip('\n').split(' ')
            rs = lline[2]
            snp = [lline[3], lline[6]]
            # print(rs)
            # print(snp)
            done_beacon = 0
            response = 0
            beacon = open("beacon_use_it.txt", 'r')
            while not done_beacon:
                line_beacon = beacon.readline()
                if line_beacon == '':
                    done_beacon = 1
                else:
                    lline_beacon = line_beacon.replace('\n', "").strip('\t').split('\t')
                    if lline_beacon[0] == rs:
                        for i in range(1, len(lline_beacon)):
                            if snp[0] in lline_beacon[i] and snp[1] in lline_beacon[i]:
                                response = 1
                                #print("NIU")
                                ssmall_query.write(line)
                                done_beacon = 1
                                break
            beacon.close()
            if response == 0:
                done_control = 0
                control = open("control_use_it.txt", 'r')
                while not done_control:
                    line_control = control.readline()
                    if line_control == '':
                        done_control = 1
                    else:
                        lline_control = line_control.replace('\n', "").strip('\t').split('\t')
                        if lline_control[0] == rs:
                            for i in range(1, len(lline_beacon)):
                                if snp[0] in lline_control[i] and snp[1] in lline_control[i]:
                                    response = 1
                                    #print("BIU")
                                    ssmall_query.write(line)
                                    done_control = 1
                                    break
                control.close()

    small_query.close()
    ssmall_query.close()

small_query = open("small_query.txt",'r')
ssmall_query = open("ssmall_query.txt",'w')
filtered_one(small_query,ssmall_query)




# control = open("control.txt", 'r')
# beacon = open("beacon.txt", 'r')
# small_control = open("small_beacon_rand.txt", 'w')
# small_beacon = open("small_control_rand.txt", 'w')
# random_select_rs(control, beacon, small_control, small_beacon)

# f = open("query.txt", 'r')
# control = open("small_control.txt",'r')
# filtered_query = open("filtered_query.txt", 'w')
# filter(f, control, filtered_query)
# f1 = open("filtered_query.txt", 'r')
# small_query = open("small_query.txt", 'w')
# random_select(f1, small_query)

#my_random()
# small_query = open("small_query.txt", 'r')
# rs= open("rs.txt", 'r')
# ssss= open("ssss.txt",'w')
# filt_zero(small_query, rs, ssss)
