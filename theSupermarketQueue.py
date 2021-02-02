#Codewars - 6 kyu

#There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
#input
#    customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
#    n: a positive integer, the number of checkout tills.
#output
#    The function should return an integer, the total time required.


# Alternative solution:
# def queue_time(customers, n):
#     l=[0]*n
#     for i in customers:
#         l[l.index(min(l))]+=i
#     return max(l)



def queue_time(customers, n):
    tills = {}
    for i in range (n):
        tills[i] = 0
    for c in customers:
        tills[(min(tills.keys(), key=(lambda k: tills[k])))] += c
    return tills[(max(tills.keys(), key=(lambda k: tills[k])))]
