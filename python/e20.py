"""
Donald G Reinertsen, The Principles of Product Development Flow

E20: The Newsboy Principle: High probability of failure does not equal bad
economics. (p. 49)

"If a newsboy make 50 cents on each newspaper he sells and loses 25 cents on
each newspaper that is not sold, how many papers should he have in stock to
deal with uncertain demand?"
"""
import random

AVG_DAILY_SALES = 100
DAILY_SIGMA = 33
NEWSPAPER_COST = 25 # cents
NEWSPAPER_BENEFIT = 75

def daily_demand():
    demand = int(round(random.gauss(AVG_DAILY_SALES, DAILY_SIGMA)))
    return max(0, demand)

def sim_day_results(newsboy_stock):
    papers_demanded = daily_demand()
    papers_sold = min(papers_demanded, newsboy_stock)
    costs = newsboy_stock * NEWSPAPER_COST
    revenue = papers_sold * NEWSPAPER_BENEFIT
    profit = revenue - costs
    return profit

def scenarios():
    # Results track profits at each sale percentage.
    max_stock = int(round(AVG_DAILY_SALES * 2.0))
    results = []

    for stock in range(max_stock):
        daily_results = []

        for day in range(300):
            daily_result = sim_day_results(stock)
            daily_results.append(daily_result)

        avg_daily_result = sum(daily_results) / len(daily_results)
        result = (stock, avg_daily_result)
        results.append(result)

    sorted_results = sorted(results, key=lambda r: r[1], reverse=True)
    return sorted_results

def main():
    print(scenarios())

if __name__ == '__main__':
    main()
