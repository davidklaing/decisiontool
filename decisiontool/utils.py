def guideme():
    """
    Help the user make a decision through a guided interactive process.
    """
    dtitle = input("Please give this decision a title: ")
    alloptions = set()
    allcriteria = set()
    cweight = dict()
    prev_crit = None
    prev_opt = None
    print("I'm going to ask you to list out all the options you're currently considering. When you've listed everything you can think of, just press 'enter' without typing anything in the prompt.")
    print(" ")
    while prev_opt is not "":
        current_opt = input("New option: ")
        prev_opt = current_opt
        current_opt = doption(current_opt)
        alloptions.add(current_opt)
    alloptions.remove(current_opt)
    print(" ")
    print("These are all the options you're considering: ")
    print(" ")
    for option in alloptions:
        print(option.name)
    print(" ")
    print("Next, I'm going to ask you to list out criteria for your decision. For example, if you were deciding which job to take, you might say 'salary', or if you're decising on a house, you might say 'location'. Once again, when you've listed everything you can think of, just press 'enter' without typing anything in the prompt.")
    print(" ")
    while prev_crit is not "":
        current_crit = input("New criterion: ")
        prev_crit = current_crit
        allcriteria.add(current_crit)
    allcriteria.remove(current_crit)
    print(" ")
    print("These are all the criteria you've defined: ")
    print(" ")
    for crit in allcriteria:
        print(crit)
    print(" ")
    print("Now we're going to assign weights to these criteria.")
    for crit in allcriteria:
        prompt = "On a scale from 1 to 5, how important is the criterion `" + crit + "`? "
        cweight[crit] = int(input(prompt))
    print(" ")
    print("Now we're going to set values for each criteria for each option. Please enter a number between 1 and 5 based on how well each option fulfills each criterion.")
    print(" ")
    for option in alloptions:
        for crit in allcriteria:
            prompt = "How well does the option `" + option.name + "` satisfy the criterion `" + crit + "`? "
            option.criteria[crit] = int(input(prompt))
    print(" ")
    print("Here are your options, each with its own criteria: ")
    print(" ")
    for option in alloptions:
        print(option.name, option.criteria)
    print(" ")
    print("Now we're going to set values for the probability of each option. Please enter a number between 0 and 100 based on how certain you are that this option is actually possible. If you're certain, enter 100 (for 100%). If the option is very risky, enter something closer to 0.")
    print(" ")
    for option in alloptions:
        prompt = "How certain is the option `" + option.name + "`? "
        option.probability = int(input(prompt))/100
    print("Here are your options, each with its own criteria and its own probability: ")
    print(" ")
    for option in alloptions:
        print("Option: ", option.name)
        print("     Probability: ", option.probability)
        print("     Criteria: ")
        print("     ", option.criteria)
    print(" ")
    print("And here is the expected utility for each decision: ")
    for option in alloptions:
        print("Option: ", option.name)
        tot_exp_util = 0
        for crit in allcriteria:
            tot_exp_util += expected_utility(cweight[crit], option.criteria[crit], option.probability)
        print("     Expected utility: ", tot_exp_util)

def expected_utility(weight, value, probability):
    return weight*value*probability

class doption:

    def __init__(self, name = None):
        self.name = name
        self.criteria = dict()
        self.probability = None
