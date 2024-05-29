# Create a list to store these monthly expenses and using that find out
my_exp_for_months = [2200,2350,2600,2130,2190]

#1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

print(my_exp_for_months[1] - my_exp_for_months[0])
print(my_exp_for_months[0] + my_exp_for_months[1]+ my_exp_for_months[2])
print(2000 in my_exp_for_months)
my_exp_for_months.append(1980)
print(my_exp_for_months)
my_exp_for_months[3] = my_exp_for_months[3] - 200
print(my_exp_for_months)

#2
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print(len(heros))
heros.append('black panther')
print(heros)
black_panther = heros.pop(-1)
heros.insert(3,black_panther)
print(heros)
heros[1:4] = ['doctor strange']
print(heros)
heros.sort()
print(heros)

#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
def numbers(max):
    odd_numbers = []
    for i in range(1,max):
        if i % 2 == 1: 
            odd_numbers.append(i)
    return odd_numbers
print(numbers(10))