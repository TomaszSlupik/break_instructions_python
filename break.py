# Instrukcja break w Pythonie jest używana w pętlach (takich jak for lub while) 
# do przerwania wykonywania pętli w momencie, gdy pewien warunek jest spełniony. 
# Gdy interpreter Pythona natrafi na break, opuszcza on natychmiastowo pętlę i 
# kontynuuje wykonywanie kodu poza nią.

# Napisz program, który porówna te dwie listy i zwróci wartość True w przypadku 
# gdy listy będą zawierały co najmniej jeden ten sam element. 
# W przeciwnym razie zwróci wartość False
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

while len(list1) > 0 and len(list2) > 0:
    print(True) 
    break

print('---')

# Sprawdź, czy każdy obiekt z tej listy jest obiektem klasy str. 
# Jeżeli tak wydrukuj wartość True, w przeciwnym przypadku wydrukuj wartość False. 

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

for hash in hashtags:
    if hash != str:
        print(False)
        break
    else:
        print(True)

print('---')

# sprawdzenie czy liczba 13 jest liczbą pierwszą:
number = 13

def checkNumber (number):
    for  i in range (2, int(number**0.5) + 1):
        if number % i == 0:
            print('13 - is not a prime number')
            break
        else:
            return '13 - is a prime number'

print(checkNumber(number))

print('---')

# Czy podany produkt występuje w liście 
products = ['T-shirt', 'Jeans', 'Sneakers', 'Backpack', 'Watch']

def checkProduct(query):
    for product in products:
        if product == query:
            print(f"Product found: {query}")
            break
    else:
        print ("Product not found")

query = 'Sneakers'

checkProduct(query)

print('---')

# Sprawdzenie czy występuje kurs 
courses = [
    'Introduction to Python',
    'Web Development',
    'Data Science',
    'Artificial Intelligence',
]
query = 'Big Data'

def checkCourse (query):
    for course in courses:
        if query == course:
            print(f"Course found {course}")
            break
    else:
        print("Course not found")

checkCourse(query)

print('---')

# wydrukowanie nazwisk pracowników wraz z pensją do momentu, 
# gdy znajdziemy pracownika z pensją poniżej minimalnej kwoty ustalonej na 55000
employees = [
    {'name': 'John', 'salary': 60000},
    {'name': 'Jane', 'salary': 55000},
    {'name': 'Bob', 'salary': 40000},
    {'name': 'Sara', 'salary': 70000},
    {'name': 'Mike', 'salary': 52000},
]
min_salary = 55000

for emloyee in employees:
    if emloyee['salary'] >= min_salary:
        print(f"{emloyee['name']} has a salary of ${emloyee['salary']}")
    else:
        print(f"STOP! {emloyee['name']} with ${emloyee['salary']}")
        break

print('---')

# Potrzebujesz znaleźć pierwszego kierowcę z oceną co najmniej 4.5 i wydrukować jego nazwisko
taxi_drivers = [
    ('John', 4.2),
    ('Jane', 4.45),
    ('Bob', 4.3),
    ('Alice', 4.8),
    ('Mike', 3.9),
]

for driver in taxi_drivers:
    if driver[1] > 4.5:
        print(f'Suitable driver found: {driver[0]}')
        break
else:
    print('No suitable driver found.')

print('---')


"""
Potrzebujesz znaleźć pierwszy post, który ma co najmniej 100 polubień 
i wydrukować jego treść. Jeśli żaden post nie ma co najmniej 100 polubień, 
wydrukuj poniższą wiadomość, że nie znaleziono popularnego postu:
'No popular post found.'
"""
posts = [
    {
        'text': 'Lorem ipsum dolor sit amet, consectetur elit.',
        'author': 'John',
        'likes': 52,
    },
    {
        'text': 'Nulla facilisi. Duis eu aliquam libero.',
        'author': 'Jane',
        'likes': 87,
    },
    {
        'text': 'Vestibulum at ipsum ac diam sollicitudin tempor.',
        'author': 'Bob',
        'likes': 113,
    },
    {
        'text': 'Curabitur lobortis luctus velit, et scelerisque eu.',
        'author': 'Alice',
        'likes': 78,
    },
    {
        'text': 'Suspendisse nec enim rutrum, vehicula lectus ut',
        'author': 'Mike',
        'likes': 99,
    },
]


for text in posts:
    if text['likes'] > 100:
        print(text['text'])
        break
else:
    print('No popular post found.')