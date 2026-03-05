for x in [1,2,3,4]:
    print(x)
    print(x*20)

names = ["Elie", "Tim", "Matt"]
first_letters = [n[0] for n in names]
print(first_letters)

nums = [1,2,3,4,5,5]
evens = [n for n in nums if n % 2 == 0]
print(evens)

a = [1,2,3,4,]
b = [3,4,5,6]
common = [n for n in a if n in b]
print(common)

words = ["Elie", "Tim", "Matt"]
reverse_lower = [w[::-1].lower() for w in words]
print(reverse_lower)

s1 = "first"
s2 = "second"
common_new = [c for c in s1 if c in s2]
print(common_new)

div_12 = [n for n in range(1,101)if n%12 == 0]
print(div_12)

vowels = set('aeiou')
no_vowels = [v for v in vowels if v not in 'aeiou']
print(no_vowels)

matrix = [[0,1,2] for _ in range(3)]
print(matrix)


