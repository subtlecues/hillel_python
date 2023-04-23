### lucky ticket fucntion.
# check next file for multiprocessing

count = 0

for ticket_num in range(1, 1000000):

    stringed_number = str(ticket_num)


    stringed_number = "0" * (6 - len(stringed_number)) + stringed_number


    first_half = stringed_number[:3]
    second_half = stringed_number[3:]


    first_sum = sum(int(d) for d in first_half)
    second_sum = sum(int(d) for d in second_half)

    if first_sum == second_sum:
        count += 1

print("Number of lucky tickets:", count)
