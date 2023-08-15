def get_average(*numbers, round_to=2):
    result = sum(numbers) / len(numbers)
    if round_to:
        result = round(result, round_to)
    return result


nums = range(12)
rounds = {'round_to': 0}
average = get_average(*nums, **rounds)

print(average)
