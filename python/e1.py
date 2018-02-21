"""
Donald G Reinertsen, The Principles of Product Development Flow

E1: The Principle of Quantified Overall Economics: Select actions based on
quantified overall economic impact. (p. 28)

"Let's begin with a simple problem. Should we relase a product from the
development lab to the factory before we have eliminated all defects?"

In software development context, this dilemma is somewhat mitigated by
staging and automated testing. But, you will have a lot more eyes finding
defects in production so if you can accurately quantify the value of these
things, you can make a principled decision. But how to quantify these
parameters?
"""
def weeks_to_seconds(weeks):
    return weeks * 7 * 24 * 3600

def cycle_time_cost(floor_fix_cost, floor_ttd, lab_fix_cost, lab_ttd):
    """ttd = Time to Defect or time it requires to discover defects in
    a particular context.

    Returns the cost of cycle time gained by pushing from lab to floor in
    dollars per second.
    """
    cycle_time_gained = lab_ttd - floor_ttd
    additional_cost = floor_fix_cost - lab_fix_cost
    cost_per_second = additional_cost / cycle_time_gained

    return {
        'total cost': additional_cost,
        'cycle time gained': cycle_time_gained,
        'cost per second': cost_per_second,
        'cost per day': cost_per_second * 3600,
        'cost per week': cost_per_second * 3600 * 24 * 7
    }

def main():
    production_bug_cost = 20000
    production_ttd = weeks_to_seconds(1)
    dev_bug_cost = 2000
    dev_ttd = weeks_to_seconds(5)
    print(cycle_time_cost(production_bug_cost, production_ttd, dev_bug_cost, dev_ttd))

if __name__ == '__main__':
    main()
