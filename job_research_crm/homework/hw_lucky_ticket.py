###lucky ticket with multiprocessing


import multiprocessing


def count_lucky_tickets(start, end):
    count = 0
    for ticket_num in range(start, end):
        stringed_number = str(ticket_num)
        stringed_number = "0" * (6 - len(stringed_number)) + stringed_number
        first_half = stringed_number[:3]
        second_half = stringed_number[3:]
        first_sum = sum(int(d) for d in first_half)
        second_sum = sum(int(d) for d in second_half)
        if first_sum == second_sum:
            count += 1
    return count


if __name__ == '__main__':
    num_processes = 4
    ticket_number_range = range(1, 1000000)
    one_process_range = len(ticket_number_range) // num_processes

    pool = multiprocessing.Pool(processes=num_processes)

    results = []

    for process_number in range(num_processes):
        start = process_number * one_process_range
        end = start + one_process_range
        if process_number == num_processes - 1:
            end = len(ticket_number_range)
        result = pool.apply_async(count_lucky_tickets, (start, end))
        results.append(result)

    total_count = sum(result.get() for result in results)

    print("Number of lucky tickets:", total_count)
