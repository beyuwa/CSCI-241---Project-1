import os
import sys
import trace
import matplotlib.pyplot as plt #python -m pip install matplotlib

def testreader(filename): #filename should be a string
    bin = open(filename, 'r')
    
    # Reading from the file
    text = bin.readlines()
    
    insertsum = 0
    selectsum = 0
    yesphasetwo = False # if we have passed the insertion counting

    cur = '' #tentative number

    for line in text: # reading by line

        for j in line: # characters in line

            if j.isdigit() == True: # if this is a number
                cur += j # we add

            if j == ':' and cur != '': # if it's the text formatted like we want
                #print(cur) #code used for testing what i was snagging
                if 'def selection_sort(arr)' in line:
                    yesphasetwo = True
                
                if yesphasetwo == False: 
                    insertsum += int(cur)
                else:
                    selectsum += int(cur)

                if 'while j>0 and arr[j-1] > cur' in line: #special case for that one line
                    insertsum += int(cur)
                    #print('special case', cur)
                cur = ''
                # this loop does not account for loops like "while ... 0:", where it would read off
                # thankfully, none of those exist


            if j.isdigit() == False: # if it is a random number, say in j>1, it's gone.
                cur = ''
                
        cur = '' # edge case: if a number is a the end of the line, we get rid of it

    return (insertsum, selectsum)

runs = 0


# the only thing that should really change is the file names
# ex. R2 means random for 2 * 10^5

#R1
os.system('python3 -m trace --count -C . Sort.py 10000 random') #runs
os.system('mv Sort.cover R1.cover') # keep making a new SortX.cover
R1 = testreader('R1.cover')

#R2
os.system('python3 -m trace --count -C . Sort.py 20000 random') #runs
os.system('mv Sort.cover R2.cover') # keep making a new SortX.cover
R2 = testreader('R2.cover')

#R3
os.system('python3 -m trace --count -C . Sort.py 30000 random') #runs
os.system('mv Sort.cover R3.cover') # keep making a new SortX.cover
R3 = testreader('R3.cover')

#R4
os.system('python3 -m trace --count -C . Sort.py 40000 random') #runs
os.system('mv Sort.cover R4.cover') # keep making a new SortX.cover
R4 = testreader('R4.cover')

#R5
os.system('python3 -m trace --count -C . Sort.py 50000 random') #runs
os.system('mv Sort.cover R5.cover') # keep making a new SortX.cover
R5 = testreader('R5.cover')

#I1
os.system('python3 -m trace --count -C . Sort.py 10000 increasing') #runs
os.system('mv Sort.cover I1.cover') # keep making a new SortX.cover
I1 = testreader('I1.cover')

#I2
os.system('python3 -m trace --count -C . Sort.py 20000 increasing') #runs
os.system('mv Sort.cover I2.cover') # keep making a new SortX.cover
I2 = testreader('I2.cover')

#I3
os.system('python3 -m trace --count -C . Sort.py 30000 increasing') #runs
os.system('mv Sort.cover I3.cover') # keep making a new SortX.cover
I3 = testreader('I3.cover')

#I4
os.system('python3 -m trace --count -C . Sort.py 40000 increasing') #runs
os.system('mv Sort.cover I4.cover') # keep making a new SortX.cover
I4 = testreader('I4.cover')

#I5
os.system('python3 -m trace --count -C . Sort.py 50000 increasing') #runs
os.system('mv Sort.cover I5.cover') # keep making a new SortX.cover
I5 = testreader('I5.cover')

#D1
os.system('python3 -m trace --count -C . Sort.py 10000 decreasing') #runs
os.system('mv Sort.cover D1.cover') # keep making a new SortX.cover
D1 = testreader('D1.cover')

#D2
os.system('python3 -m trace --count -C . Sort.py 20000 decreasing') #runs
os.system('mv Sort.cover D2.cover') # keep making a new SortX.cover
D2 = testreader('D2.cover')

#D3
os.system('python3 -m trace --count -C . Sort.py 30000 decreasing') #runs
os.system('mv Sort.cover D3.cover') # keep making a new SortX.cover
D3 = testreader('D3.cover')

#D4
os.system('python3 -m trace --count -C . Sort.py 40000 decreasing') #runs
os.system('mv Sort.cover D4.cover') # keep making a new SortX.cover
D4 = testreader('D4.cover')

#D5
os.system('python3 -m trace --count -C . Sort.py 50000 decreasing') #runs
os.system('mv Sort.cover D5.cover') # keep making a new SortX.cover
D5 = testreader('D5.cover')



#print(runs)
plt.style.use('ggplot')

def straight_plot(numbers, numbers2, pos, labels):
    plt.plot(numbers, color='blue')
    plt.plot(numbers2, color='purple')
    plt.ylabel('Trial Runs')
    plt.xticks(ticks = pos, labels=labels)
    plt.show()

# def happy_plot(numbers, labels, pos):
#     plt.bar(pos, numbers, color='purple')
#     plt.ylabel('Trial Runs')
#     plt.xticks(labels=labels)
#     plt.show()

numbers = [D1[0], D2[0], D3[0], D4[0], D5[0]]
numbers2 = [D1[1], D2[1], D3[1], D4[1], D5[1]]
labels = ['D1', 'D2', 'D3', 'D4', 'D5']
pos = list(range(5))
straight_plot(numbers, numbers2, pos, labels)

numbers = [I1[0], I2[0], I3[0], I4[0], I5[0]]
numbers2 = [I1[1], I2[1], I3[1], I4[1], I5[1]]
labels = ['I1', 'I2', 'I3', 'I4', 'I5']
pos = list(range(5))
straight_plot(numbers, numbers2, pos, labels)

numbers = [R1[0], R2[0], R3[0], R4[0], R5[0]]
numbers2 = [R1[1], R2[1], R3[1], R4[1], R5[1]]
labels = ['R1', 'R2', 'R3', 'R4', 'R5']
pos = list(range(5))
straight_plot(numbers, numbers2, pos, labels)

