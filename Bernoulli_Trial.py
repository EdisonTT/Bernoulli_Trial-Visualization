
#Illustarating the Bernoulli distribution by using a Fair coin. 

from random import randint
from math import comb

#To verify that the method 'randint' is unbiased.
#That is checking the probabilty of each outcomes {0(head) and 1(tail)} are equaly likely.
#0 - Head, 1 - Tail
event_count = 10000
count0 = 0
count1 = 0
for i in range(event_count):
    x = randint(0,1)
    if x == 0:
        count0 += 1
    else:
        count1 += 1
print('Probability of Head :', round((count0/event_count),5))
print('Probability of Tail :', round((count1/event_count),5))

#Theoretical approach of the solution using Bernoulli distribution.
#The results are stored in a list.

no_of_events_in_exp = 10

class Theoretical_result:
    def __init__(self, no_of_events_in_exp):
        self.no_of_events_in_exp = no_of_events_in_exp
        self.result = []
        for i in range(self.no_of_events_in_exp+1):
            self.result.append(round(comb(self.no_of_events_in_exp,i)*(0.5**self.no_of_events_in_exp),5))

#The following class will conduct the experiment and count the number of heads and tails obtained.

class experiment:
    def __init__(self):
        self.Head = 0
        self.Tail = 0
        for i in range(no_of_events_in_exp):
            x = randint(0,1)
            if x == 0:
                self.Head += 1
            else:
                self.Tail += 1

#The class exp_result will count the number of heads and tails obtained when the experiment is repeated a number of times.
#It also stores the count of each outcome in a list as mentioned in the class Theoretical_result.
#There are two separate lists for Head and Tail.

class exp_result:
    def __init__(self, result):
        self.Head_only = [x.Head for x in result]
        self.Tail_only = [x.Tail for x in result]
        self.Head_count = self.Head(self.Head_only)
        self.Tail_count = self.Tail(self.Tail_only)
    class Head:
        def __init__(self,abc):
            self.abc = abc
            self.count0 = abc.count(0)
            self.count1 = abc.count(1)
            self.count2 = abc.count(2)
            self.count3 = abc.count(3)
            self.count4 = abc.count(4)
            self.count5 = abc.count(5)
            self.count6 = abc.count(6)
            self.count7 = abc.count(7)
            self.count8 = abc.count(8)
            self.count9 = abc.count(9)
            self.count10 = abc.count(10)
        def Show_Count(self):
            return [self.count0,self.count1,self.count2,self.count3,self.count4,self.count5,self.count6,self.count7,self.count8,self.count9,self.count10]
    class Tail:
        def __init__(self,abc):
            self.abc = abc
            self.count0 = abc.count(0)
            self.count1 = abc.count(1)
            self.count2 = abc.count(2)
            self.count3 = abc.count(3)
            self.count4 = abc.count(4)
            self.count5 = abc.count(5)
            self.count6 = abc.count(6)
            self.count7 = abc.count(7)
            self.count8 = abc.count(8)
            self.count9 = abc.count(9)
            self.count10 = abc.count(10)
        def Show_Count(self):
            return [self.count0,self.count1,self.count2,self.count3,self.count4,self.count5,self.count6,self.count7,self.count8,self.count9,self.count10]    

#The code below will repeat the experiment many times.
#And also print the results.
#The lists prob_head and prob_head store the probability of getting Head and Tail in the way mentioned earlier.

print('Theoretical result obtained by using Bernoulli distribution for both HEAD and TAIL :')
ber_dis_res = Theoretical_result(no_of_events_in_exp)
print(ber_dis_res.result)
print('Theoretically both Head and Tail have equal probability.')
print('===========================================================')
no_of_exp = 10
exp_results = []
while no_of_exp <= 1000000:
    print('No of times the experiment conducted : ', no_of_exp)
    for i in range(no_of_exp):
        exp_results.append(experiment())
    final_result = exp_result(exp_results)
    print('probabilty of head:')
    prob_head = list(map(lambda x:round(x/no_of_exp,5), final_result.Head_count.Show_Count()))
    print(prob_head)
    print('probabilty of tail:')
    prob_tail = list(map(lambda x:round(x/no_of_exp,5), final_result.Tail_count.Show_Count()))
    print(prob_tail)
    no_of_exp *=10
    print('===========================================================')