### decisiontool python package/distribution
created by David Laing
2016-12-16

[![Build Status](https://travis-ci.org/laingdk/decisiontool.svg?branch=master)](https://travis-ci.org/laingdk/decisiontool)

A python package/distribution that guides you through difficult decisions.

### To install package:
```
pip install git+https://github.com/laingdk/decisiontool.git
```

### Example of usage in Python:
```
from decisiontool.utils import guideme
from decisiontool.utils import expected_utility
from decisiontool.utils import doption

>>>guideme()
Please give this decision a title: Summer Job
I'm going to ask you to list out all the options you're currently considering. When you've listed everything you can think of, just press 'enter' without typing anything in the prompt.

New option: Facebook
New option: Google
New option:

These are all the options you're considering:

Google
Facebook

Next, I'm going to ask you to list out criteria for your decision. For example, if you were deciding which job to take, you might say 'salary', or if you're decising on a house, you might say 'location'. Once again, when you've listed everything you can think of, just press 'enter' without typing anything in the prompt.

New criterion: Salary
New criterion: Location
New criterion: Connections
New criterion:

These are all the criteria you've defined:

Salary
Location
Connections

Now we're going to assign weights to these criteria.
On a scale from 1 to 5, how important is the criterion `Salary`? 5
On a scale from 1 to 5, how important is the criterion `Location`? 4
On a scale from 1 to 5, how important is the criterion `Connections`? 3

Now we're going to set values for each criteria for each option. Please enter a number between 1 and 5 based on how well each option fulfills each criterion.

How well does the option `Google` satisfy the criterion `Salary`? 5
How well does the option `Google` satisfy the criterion `Location`? 3
How well does the option `Google` satisfy the criterion `Connections`? 5
How well does the option `Facebook` satisfy the criterion `Salary`? 4
How well does the option `Facebook` satisfy the criterion `Location`? 5
How well does the option `Facebook` satisfy the criterion `Connections`? 4

Here are your options, each with its own criteria:

Google {'Salary': 5, 'Location': 3, 'Connections': 5}
Facebook {'Salary': 4, 'Location': 5, 'Connections': 4}

Now we're going to set values for the probability of each option. Please enter a number between 0 and 100 based on how certain you are that this option is actually possible. If you're certain, enter 100 (for 100%). If the option is very risky, enter something closer to 0.

How certain is the option `Google`? 50
How certain is the option `Facebook`? 60
Here are your options, each with its own criteria and its own probability:

Option:  Google
     Probability:  0.5
     Criteria:
      {'Salary': 5, 'Location': 3, 'Connections': 5}
Option:  Facebook
     Probability:  0.6
     Criteria:
      {'Salary': 4, 'Location': 5, 'Connections': 4}

And here is the expected utility for each decision:
Option:  Google
     Expected utility:  26.0
Option:  Facebook
     Expected utility:  31.2
```

### To run tests:
1. clone repo
2. install pytest (`pip install -U pytest`)
3. navigate to root directory of `decisiontool` (this is the repo you just cloned) and run `pytest`
