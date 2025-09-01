print("Question 1.")
def task1_sum_of_two_numbers(a, b):
	add = a + b
	return add
print(task1_sum_of_two_numbers(2, 3))
print("Question 2.")
def task2_square_number(n):
	square = n ** 2
	return square
print(task2_square_number(5))
print("Question 3.")
def task3_greet_user(name):
	print("Hello",name)
task3_greet_user("Timothy")
print("Question 4.")
def task4_area_of_rectangle(length, width):
	area = length * width
	return area
print(task4_area_of_rectangle(10,5))
print("Question 5.")
def task5_perimeter_of_square(side):
	perimeter = 4 * side
	return perimeter
print(task5_perimeter_of_square(5))
print("Question 6.")
def task6_celsius_to_fahrenheit(celsius):
	fahrenheit = (celsius * 9/5) + 32
	return fahrenheit
print(task6_celsius_to_fahrenheit(4))
print("Question 7.")
def task7_find_max(a, b, c):
	if a >= b and a >= c:
		return a
	elif b >=a and b >=c:
		return b
	elif c >=a and c >=b:
		return c
print(task7_find_max(7, 9, 10))
print("Question 8.")

def task8_even_or_odd(n):
	if n % 2 ==0:
		return "Even"
	else:
		return "Odd"
print(task8_even_or_odd(3))

print("Question 9.")
def task9_count_vowels(word):
	vowels = 'aeiou'
	count = 0
	for words in vowels:
		if words in word:
			count +=1
	return count
print(task9_count_vowels("apple"))

print("Question 10.")
#list_numbers = [1, 2, 3, 4]
def task10_multiply_list(numbers):
	product = 1
	for num in numbers:
		num *= product
		product = num
	return product
print(task10_multiply_list([1, 2, 3, 4]))
print("Question 11.")
def task11_reverse_string(text):
	reverse_string = ""
	for char in range(len(text) -1,-1,-1):
		reverse_string = reverse_string+ text[char]
	return reverse_string
print(task11_reverse_string("hello"))
print("Question 12.")
def task12_is_prime(n):
    if n <= 1:
        return False  

    for i in range(2, n):  
        if n % i == 0:
            return 

    return True 
print(task12_is_prime(3))

print("Question 13. ")
variable = "global"
def task13_scope_demo():
	variable = "local"
	print("this is a local variable:",variable)
task13_scope_demo()
print("this is a global variable:",variable)

print("Question 14.")
def task14_sum_list(numbers):
	total = 0
	for num in numbers:
		total +=num
	return total
print(task14_sum_list([1, 2, 3, 4]))
print("Question 15.")
def task15_average_of_list(numbers):
	total_numbers = len(numbers)
	sum_numbers = 0
	for num in numbers:
		sum_numbers +=num
	average = sum_numbers / total_numbers
	return average
print(task15_average_of_list([1, 2, 3, 4]))
print("Question 16.")
def task16_factorial(n):
    factorial = 1           
    for i in range(1, n + 1):   
        factorial *= i      
    return factorial

print(task16_factorial(5))  
print("Question 17.")
def task17_palindrome_check(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(task17_palindrome_check("madam"))  
print("Question 18.")
def task18_convert_minutes_to_hours(minutes):
    hours = minutes // 60 
    remaining_minutes = minutes % 60   
    return f"{hours} hour(s) {remaining_minutes} minute(s)"
print(task18_convert_minutes_to_hours(130))  
print("Question 19.")
def task19_find_min(numbers):
	min_numbers = numbers[0]
	for num in numbers:
		if num < min_numbers:
			min_numbers = num
	return min_numbers
print(task19_find_min([1, 2, 3, 4,0]))

print("Question 20.")
def task20_simple_interest(principal, rate, time):
	interest = (principal * rate * time) / 100
	return interest
print(task20_simple_interest(5000,10,10))
print("Question 21.")
def task21_calculator(a, b, operation):
	if operation == "+":
		return a+b
	elif operation == "-":
		return a-b
	elif operation == "*":
		return a*b
	elif operation == "/":
		if b != 0:
			return a /b
		else:
			return "error division by 0"
	else:
		return "invalide operation"
print(task21_calculator(2, 4, "+"))
print("Question 22.")
def task22_string_length(text):
    count = 0
    for char in text:  
        count += 1      
    return count
print(task22_string_length("password"))
print("Question 23.")
def task23_grade_student(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 40 <= score <= 49:
        return "D"
    elif 30 <= score <= 39:
        return "E"
    elif 0 <= score <= 29:
        return "F"
    else:
        return "Invalid score"
print(task23_grade_student(90))
print("Question 24.")
def task24_swap_values(a, b):
    return b, a
print(task24_swap_values(2,3))
print("Question 25.")
count = 0  # global variable
count = 0
def task25_scope_counter():
    global count  
    count += 1
    print("Current count:", count)
task25_scope_counter()

print("Question 26.")
def task26_calculate_bmi(weight, height):
	 bmi = weight / (height ** 2)
	 return round(bmi, 2)
print(task26_calculate_bmi(70, 1.75))
print("Question 27.")
def task27_discounted_price(price, discount_percent):
	discount = (discount_percent * price)/100
	price_after_dicount  = price - discount
	return  price_after_dicount
print(task27_discounted_price(1000, 20))
print("Question 28.")
def task28_movie_ticket_price(age):
	if age < 12:
		return 500
	elif 12 <= age < 18:
		return 700
	elif 18 <= age <60:
		return 1000
	elif age >=60:
		return 600
	else:
		return "invalid option"
print(task28_movie_ticket_price(1))
print("Question 29.")
def task29_shopping_total(prices):
	total_cost = 0
	for price in prices:
		total_cost +=price
	return total_cost
print(task29_shopping_total([200,300,500,100]))

print("Question 30.")
def task30_convert_to_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

print(task30_convert_to_seconds(1,1,1))  
print("Question 31 .")
def task31_find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2 
    if n % 2 == 0:  
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:  
        median = numbers[mid]
    return median
print(task31_find_median([3, 1, 2]))
print("Question 32.")
def task32_parking_fee(hours):
    if hours <= 2:
        return 200
    else:
        return 200 + (hours - 2) * 100
print(task32_parking_fee(4))  
print("Question 33.")
'''
def task33_word_count(sentence):
	tempcount = 0
	count = 1
	for word in sentence:
		if word == " ":
			tempcount +=1
			if tempcount ==1:
				count +=1
			else:
				tempcount +=1
		else:
			tempcount = 0
	return count
print(task33_word_count( "I love Python"))
'''
def task33_word_count(sentence):
	count = 1
	for word in sentence:
		if word == " ":
			count +=1
	return count
print(task33_word_count("i love python"))
print("Question 34.")
print("Question 35.")
def task34_capitalize_names(names):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for name in names:
        first = name[0]
        capital = first
        for i in range(len(lowercase)):
            if first == lowercase[i]:
                capital = uppercase[i]
                break

        rest = ""
        for j in range(1, len(name)):
            rest += name[j]

        result.append(capital + rest)

    return result


print(task34_capitalize_names(["john", "mary"]))
print("Question 35.")
def task35_student_pass_fail(score):
	if score >=50:
		return "Pass"
	else:
		return "fail"
print(task35_student_pass_fail(49))
print("Question 36.")
def task36_calculate_fine(days_late):
    if days_late <= 5:
        fine = days_late * 20
    elif days_late <= 10:
        fine = 5 * 20 + (days_late - 5) * 50
    else:
        fine = 5 * 20 + 5 * 50 + (days_late - 10) * 100
    return fine
print(task36_calculate_fine(7))  
print("Question 37.")
def task37_convert_currency(amount, rate):
    converted = amount * rate
    return converted

print(task37_convert_currency(100, 1500)) 
print("Question 38.")
def task38_gas_station_bill(liters, price_per_liter):
    total_cost = liters * price_per_liter
    return total_cost

print(task38_gas_station_bill(20, 700))
print("Question 39.")
def task39_is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(task39_is_leap_year(2023))
print("Question 40.")
def task40_password_strength(password):
    if len(password) < 8:
        return "Weak"
    digits = ['0','1','2','3','4','5','6','7','8','9']
    has_digit = False
    for ch in password:
        for d in digits:
            if ch == d:
                has_digit = True
    uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    has_upper = False
    for ch in password:
        for up in uppercase_letters:
            if ch == up:
                has_upper = True
    if has_digit and has_upper:
        return "Strong"
    else:
        return "Weak"
print(task40_password_strength("mypassword9")) 

print("Question 41.")
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
	total = quantity * price_per_shirt
	if quantity >= discount_threshold:
		total = total * (1 - discount_rate)
		return total
print(task41_shirt_order(12, 2000))
print("Question 42.")
def task42_find_mode(numbers):
	if not numbers:
		return None
	return max(numbers, key=numbers.count)
print(task42_find_mode([1, 2, 2, 3, 3]))
print("Question 43.")
def task43_student_average(scores):
    total = 0
    count = 0
    for subject in scores:
        total = total + scores[subject]
        count = count + 1
#count by zero not allow
    if count == 0:
        return 0 
    return total / count
print(task43_student_average({"math": 80, "english": 70}))      # 75.0
print("Question 44.")
def task44_calculate_age(current_year, birth_year):
	age = current_year -birth_year
	return age
print(task44_calculate_age(2025,2004))
print("Question 45.")
def task45_salary_after_tax(salary, tax_rate=0.15):
	net_salary = salary * (1 - tax_rate)
	return net_salary
print(task45_salary_after_tax(100000))
print("Question 46")
def task46_water_bill(units):
	if units <= 30:
		return units * 50
	elif units <= 50:
		return (30 * 50) + (units - 30) * 75
	else:
		return (30 * 50) + (20 * 75) + (units - 50) * 100
print(task46_water_bill(25))
print(task46_water_bill(40))
print("Question 47")
def task47_find_longest_word(sentence):
    longest = ""
    current = ""
    for ch in sentence:
        if ch != " ":      
            current += ch
        else:                  
            if len(current) > len(longest):
                longest = current
            current = ""   
    if len(current) > len(longest):
        longest = current
    return longest
print(task47_find_longest_word("I love programming")) 
print("Question 48.")
def task48_banking_withdraw(balance, withdraw_amount):
	if withdraw_amount <= balance:
		return balance - withdraw_amount
	else:
		return "Insufficient funds"
print(task48_banking_withdraw(500, 600))
print("Question 49.")
def task49_calculate_grade_point(score):
	if 70 <= score <= 100:
		return 5 
	elif 60 <= score <= 69:
		return 4
	elif 50 <= score <= 59:
		return 3
	elif 45 <= score <= 49:
		return 2
	elif 40 <= score <= 44:
		return 1
	elif 0 <= score < 40:
		return 0
	else:
		return "Invalid score"
print(task49_calculate_grade_point(85))
print("Question.50")
def task50_weather_advice(temperature, raining):
    if raining:
        return "Take an umbrella"
    elif temperature > 30:
        return "Wear light clothes"
    elif temperature < 15:
        return "Wear a jacket"
    else:
        return "Weather is fine"
print(task50_weather_advice(25, True))   
print(task50_weather_advice(20, False))

