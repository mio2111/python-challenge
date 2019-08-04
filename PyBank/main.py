import os
import csv

budgets_data = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'budget_data.csv')

with open(budgets_data, newline="") as budget:
    csv_header = next(budget)   
    csv_reader = list(csv.reader(budget, delimiter=","))
  
    print(f"Header:{csv_header}")
    
    #*The total number of months included in the dataset
    num_months = len(csv_reader)
    total_profit = 0
  
        #each time loop through the data, add one to current row   
    #*The net total amount of "Profit/Losses" over the entire period
    for row in csv_reader:
        print(row)
        #num_months += 1
        total_profit += int(row[1])
    print("Total Months: ", num_months)
    print("Total: ", total_profit)

   #*The average of the changes in "Profit/Losses" over the entire period
        #define a list to store diff in profit from mo to mo
        #loop through the data and calc the diff and store it in the list;
        #calc the avg diff of profit
    
    def avg_profit(data):
        profit_diff = {}
        for index in range(len(data)):
            current = index
            next_row = index + 1
            if index == (len(data)) - 1:  
                break
            profit_diff[data[next_row][0]] = (int(data[next_row][1]) - int(data[current][1]))
        #return sum(profit_diff)/len(profit_diff)
        return profit_diff
    profit_diff = avg_profit(csv_reader)
    Months = profit_diff.keys()
    profit_diff_values = profit_diff.values()
    avg_change = sum(profit_diff_values)/len(profit_diff_values)
    max_change = max(profit_diff_values)
    min_change = min(profit_diff_values)
    Month_Max = list(Months)[list(profit_diff_values).index(max_change)]
    Month_Min = list(Months)[list(profit_diff_values).index(min_change)]
    print(f"Average Change: ${round(avg_change,2)}")        
    print(f"Greatest Increase in Profits: {Month_Max} (${max_change})")        
    print(f"Greatest Decrease in Profits: {Month_Min} (${min_change})")  

    file = open("Profit_Statement.txt","w") 
    file.write(f"Total Months: {num_months}")
    file.write(f"Total: {total_profit}")
    file.write(f"Average Change: ${round(avg_change,2)}")     
    file.write(f"Greatest Increase in Profits: {Month_Max} (${max_change})")
    file.write(f"Greatest Decrease in Profits: {Month_Min} (${min_change})")
    file.close()

   