from lib.getdata import getQuotes
import json
import time
import datetime

if __name__ == '__main__':

    # load ticker names from input folder
    with open("./input/IQ100.txt", "r") as input_file:
        symbs = input_file.read().split('\n')

    flag = True
    timeinterval = 1800
    while(1):
        t = time.time()
        if (int(t) % timeinterval == 0 and flag):
            timestamp = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
            #print timestamp

            content = getQuotes(symbs)
            sum = 0
            for i in content:
                #print i['LastTradePrice']
                sum += float(i['LastTradePrice'].replace(',', ''))

            date = datetime.datetime.fromtimestamp(t).strftime('%Y_%m_%d')
            output_filename = date

            with open("./output/" + output_filename + ".csv", "a") as output_file:
                line = timestamp + "," + str(sum) + "\n"
                output_file.write(line)

            print line
            flag = False
        elif (int(t) % timeinterval != 0):
            flag = True
        
            
