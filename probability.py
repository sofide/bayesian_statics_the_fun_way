"""
A fever is any temperature greater than 100.4 degrees Fahrenheit. Given the following measurements, what is the probability that the patient has a fever?
100.0, 99.8, 101.0, 100.5, 99.7
"""


data = [100.0, 99.8, 101.0, 100.5, 99.7]

mean = sum(data) / len(data)

dsv = sum([((x - mean) ** 2) for x in data]) / len(data)

std = dsv ** 0.5

import numpy as np
from scipy.stats import norm

mu = mean
sigma = std

floor = 100.4
ceil = 200
prob = norm.cdf(ceil, mu, sigma) - norm.cdf(floor, mu, sigma)

print(f"prob: {prob}")


"""
Suppose in Chapter 11 we tried to measure the depth of a well by timing coin drops and got the following values:
2.5, 3, 3.5, 4, 2

The distance an object falls can be calculated (in meters) with the following formula:

distance = 1/2 × G × time2

where G is 9.8 m/s/s. What is the probability that the well is over 500 meters deep?
"""

data = [2.5, 3, 3.5, 4, 2]

mean = sum(data) / len(data)

std = np.std(data)
mu = mean

sigma = std

from math import sqrt

# seconds if distance is 500 meters
# distance = 1/2 × G × time**2
# 500 = 1/2 * 9.8 * time**2
time_expected = sqrt((2 * 500) / 9.8)
print(f"time expected for a 500 meters well: {time_expected}")

prob = 1 - norm.cdf(time_expected, mu, sigma)
print(f"prob 500 meters: {prob}")

"""
What is the probability there is no well (i.e., the well is really 0 meters deep)? 
You’ll notice that probability is higher than you might expect, given your observation that there is a well. 
There are two good explanations for this probability being higher than it should. 
The first is that the normal distribution is a poor model for our measurements; 
the second is that, when making up numbers for an example, I chose values that you likely wouldn’t 
see in real life. 

Which is more likely to you?
"""
ceil = 0
floor = -1
prob = norm.cdf(ceil, mu, sigma) - norm.cdf(floor, mu, sigma)   
print(f"prob 0 meters: {prob}")