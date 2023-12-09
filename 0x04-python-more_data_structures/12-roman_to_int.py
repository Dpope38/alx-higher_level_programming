def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string) - 1):
        if roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
            result -= roman_values[roman_string[i]]
        else:
            result += roman_values[roman_string[i]]
    
    result += roman_values[roman_string[-1]]
    return result
