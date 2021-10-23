# Bernoulli_Trial-Visualization
This is an effort to understand about Bernoulli Trial.

## Introduction
Before going, recall what [Bernoulli Trail](https://en.wikipedia.org/wiki/Bernoulli_trial) is. The goal is to validate the concept with the help of [Python](https://www.python.org/about/). Here, with Python, a real-life situation is created to illustrate the Bernoulli Trial. The effort is to give a picture about the Bernoulli Trail, not to explain it mathematically! 
## Scenario
Consider a person tossing a coin. Ensure that the coin is [fair](https://en.wikipedia.org/wiki/Fair_coin). The probability of getting Head or Tail is `0.5`. For understanding, consider getting Head is a success.  Now imagine, ten people are tossing the coin simultaneously. We are interested in the number of heads obtained. There are `11` possible [outcomes](https://en.wikipedia.org/wiki/Outcome_(probability)). There is a chance to get zero Head or there is a chance to get ten Heads and so many. But the probability of these outcomes is not the same. The mathematician [Jacob Bernoulli](https://en.wikipedia.org/wiki/Jacob_Bernoulli) introduce a method to find probability. By using the definition of the Bernoulli Trail, the probability can be calculated. Most people are aware of it. So not diving into the deep.

## What we do here
First, we will calculate the theoretical probability of each outcome. Then, will do the experiment too many times. Finally, compare the observed result with the theoretical result. Here the experiment is tossing a coin by ten people simultaneously. And then the number of Head/Tail is counted.

## The program Explained
The main methods used in this python program, `Bernoulli_Trial.py` are:
- ```randint()``` from the module [random](https://docs.python.org/3/library/random.html). The output of the event, tossing a coin, is obtained using this method.
- ```comb()``` from the module [math](https://docs.python.org/3/library/math.html). It is used to calculate the value of  [combination](https://en.wikipedia.org/wiki/Combination). Requirement: `Python3.8` or above.

The first part of the program makes sure that the method `randint()` represents a fair coin. For this, it is called repeatedly for a large number of times, say `1000`. Then verify that the probability of Head/Tail is `0.5`. It was observed that the probabilities are the same.

The `class Theoretical_result` calculates the theoretical value of each outcome according to the definition of the Bernoulli Trial. The results are stored in a list. The first element of the list represents the probability of getting zero Head/Tail in the experiment. The next element represents the probability of getting one Head/Tail in the experiment and so on.

The `class experiment` conduct the experiment and count the number of heads and tails obtained.

The `classexp_result` will count the number of heads and tails obtained when the experiment is repeated several times. It also stores the count of each outcome in a list as mentioned in the `class Theoretical_result`. There are two separate lists for Head and Tail.

The rest of the program will repeat the experiment many times. And also print the results. The lists `prob_head` and `prob_head` store the probability of getting Head and Tail in the way mentioned earlier.

## Output
The Output of the program is given below.
```
Probability of Head : 0.4982
Probability of Tail : 0.5018
Theoretical result obtained by using Bernoulli distribution for both HEAD and TAIL :
[0.00098, 0.00977, 0.04395, 0.11719, 0.20508, 0.24609, 0.20508, 0.11719, 0.04395, 0.00977, 0.00098]
Theoretically both Head and Tail have equal probability.
===========================================================
No of times the experiment conducted :  10
probabilty of head:
[0.0, 0.0, 0.0, 0.1, 0.1, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0]
probabilty of tail:
[0.0, 0.0, 0.0, 0.0, 0.5, 0.3, 0.1, 0.1, 0.0, 0.0, 0.0]
===========================================================
No of times the experiment conducted :  100
probabilty of head:
[0.01, 0.01, 0.06, 0.11, 0.19, 0.32, 0.23, 0.09, 0.06, 0.01, 0.01]
probabilty of tail:
[0.01, 0.01, 0.06, 0.09, 0.23, 0.32, 0.19, 0.11, 0.06, 0.01, 0.01]
===========================================================
No of times the experiment conducted :  1000
probabilty of head:
[0.001, 0.011, 0.045, 0.133, 0.228, 0.275, 0.22, 0.122, 0.062, 0.01, 0.003]
probabilty of tail:
[0.003, 0.01, 0.062, 0.122, 0.22, 0.275, 0.228, 0.133, 0.045, 0.011, 0.001]
===========================================================
No of times the experiment conducted :  10000
probabilty of head:
[0.0011, 0.0105, 0.0477, 0.1335, 0.2256, 0.2726, 0.2249, 0.1313, 0.0517, 0.0108, 0.0013]
probabilty of tail:
[0.0013, 0.0108, 0.0517, 0.1313, 0.2249, 0.2726, 0.2256, 0.1335, 0.0477, 0.0105, 0.0011]
===========================================================
No of times the experiment conducted :  100000
probabilty of head:
[0.00105, 0.0109, 0.04967, 0.12986, 0.22569, 0.27447, 0.22912, 0.12944, 0.04937, 0.01036, 0.00117]
probabilty of tail:
[0.00117, 0.01036, 0.04937, 0.12944, 0.22912, 0.27447, 0.22569, 0.12986, 0.04967, 0.0109, 0.00105]
===========================================================
No of times the experiment conducted :  1000000
probabilty of head:
[0.00107, 0.01081, 0.04898, 0.13016, 0.22794, 0.273, 0.22819, 0.1299, 0.04909, 0.01088, 0.00108]
probabilty of tail:
[0.00108, 0.01088, 0.04909, 0.1299, 0.22819, 0.273, 0.22794, 0.13016, 0.04898, 0.01081, 0.00107]
===========================================================
No of times the experiment conducted :  10000000
probabilty of head:
[0.00097, 0.00975, 0.04391, 0.11704, 0.20521, 0.24608, 0.20514, 0.11715, 0.04401, 0.00977, 0.00097]
probabilty of tail:
[0.00097, 0.00977, 0.04401, 0.11715, 0.20514, 0.24608, 0.20521, 0.11704, 0.04391, 0.00975, 0.00097]
===========================================================
```
## Conclusion

From the output, it can be concluded that when the number of the experiments increases, the observed probability move toward the theoretical probability. As the number of experiments approaches infinity, the observed and the theoretical probability will be the same. On the other hand, as the number of the experiment increases the probability for both Head and Tail comes closer to each other.

## Beofre Winding-up
Plot the probabilities and the number of counts on a graph sheet. Join those points with a smooth curve. There can see an amazing curve. This is called the Normal Distribution (Bell Curve).
The python program `The_Curve.py` will help to get that curve. The result is given below.

![abc](https://github.com/EdisonTT/Bernoulli_Trial-Visualization/blob/main/curve.png)

**Note**: It is not mandatory to get the same output as mentioned above even the same code is used. But the values will be close to each other. It is because everything is random here. But the theoretical result will be the same. Also, the efficiency of the code is not good. As the number of experiments becomes a larger one, it takes more time to complete execution.
