# #  Multiple Line Code :)
myName = 'I\'m Jood Alghamdi'
MyAge = '23'
MyCountry = 'Saudi Arabia'
print(f'"Name : {myName}"'
      f'\n"Age : {MyAge}"'
      f'\n"Country: {MyCountry}"')
print('-------------------------------------------')
print(('Hello, my name is ' + myName + ' and iam ' + MyAge + ' years old and i live in ' + MyCountry).title())
print(f'{type(myName)}\n{type(MyAge)}\n{type(MyCountry)}')
print('-------------------------------------------')

# week 2 Assignment
print('\"Hello \'' + myName + '\', How You Doing \\ """ Your Age Is "' + str(MyAge)
      + '"" + And Your Country Is: ' + MyCountry)
print('-------------------------------------------')
print('\"Hello \'' + myName + '\', How You Doing \ \n""" Your Age Is "' + str(MyAge)
      + '"" + \nAnd Your Country Is: ' + MyCountry)
print('-------------------------------------------')
vari = 'Elzero'
print(vari[1] + '\n' + vari[2] + '\n' + vari[-1] + '\n')
print(vari[1:4] + '\n' + vari[0:-1:2] + '\n' + vari[-2::-2] + '\n')
vari = '#@#@Elzero#@#@'
print(vari.strip('#@'))
a, s, d, f, g = '9', '15', '130', '950', '1500'
print(a.zfill(4) + '\n' + s.zfill(4) + '\n'
      + d.zfill(4) + '\n' + f.zfill(4) + '\n' + g.zfill(4) + '\n')
namei = 'Jood'
print(namei.center(20, '$'))
print(namei.rjust(20, '$'))
namei = 'Jood Alghamdi'
print(namei.rjust(20, '$'))
print(namei.swapcase())
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
vari = 'Elzero'
print(vari.index('z'))
print('------------------------------------------')
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3', 'Love', 1))
print(msg.replace('<3', 'Love'))
MyAge = 23
print( (f'My name is {myName}, and my age is {MyAge}'
        f', and my country is {MyCountry} ').title())

# -----------------------------------------------------------------
# Assignment 3
# -----------------------------------------------------------------
print(type(10))
print(type(10.0))
print(type(10+2j))
print((1+2j).imag)
print((1+2j).real)
num = 10
print('{:.10f}'.format(num))
num = 159.650
print(num)
num=int(num)
print(f'{num} \n{type(num)}')
print( 97 // 20 )
# -----------------------------------------------------------------
# Assignment 4 - 021 to 023
# -----------------------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-len(friends)])
print(friends[-1])
print(friends[len(friends) - 1])
print(friends[::2])
print(friends[1::2])
print(friends[1:len(friends) - 1])
print(friends[-2:])
friends[-1], friends[-2] = 'Elzero', 'Elzero'
print(friends)
friends.pop()
friends.pop()
friends.insert(0, 'Nasser')
print(friends)
friends.append('Salem')
print(friends)
friends[0:2] = []
print(friends)
friends.pop()
print(friends)
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
print(len(friends))
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
# -----------------------------------------------------------------
# Assignment 5 - 024 to 025
# -----------------------------------------------------------------
myName = 'Jood',
print(myName)
print(type(myName))
print('------------------------------------')
# -------------------------------------
friends = ("Osama", "Ahmed", "Sayed")
temp = list(friends)
temp[0] = 'Elzero'
friends = tuple(temp)
print(friends)
print(type(friends))
print(len(friends))
print('------------------------------------')
# -------------------------------------
num = 1, 2, 3
alph = 'A', 'B', 'C'
neww = num + alph
print(neww)
print(len(neww))
print('------------------------------------')
# -------------------------------------
num = 1, 2, 3, 4
a, b, _, c = num
print(f'{a}\n{b}\n{c}')
# -----------------------------------------------------------------
# Assignment 6 - 026 to 032
# -----------------------------------------------------------------
my_list = [1, 2, 3, 3, 4, 5, 1]
uniq = list(set(my_list).intersection())
print(uniq)
print(type(uniq))
uniq.pop()
print(uniq)
print('--------------------------------------------------')
nums = {1, 2, 3}
letters = {'A', 'B', 'C'}
print(nums.union(letters))
nums.symmetric_difference_update(letters)
print(nums)
nums.remove('A')
nums.remove('B')
nums.remove('C')
print('--------------------------------------------------')
print(nums)
nums.clear()
print(nums)
nums.add("A")
nums.add("B")
print(nums)
nums.discard('C')
print('--------------------------------------------------')
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print('--------------------------------------------------')
skills = {
    'Java': '70%',
    'Python': '90%',
    'SQL': '80%'
}
print('Java Progress is {},'
      '\nPython Progress is {}'
      '\nSQL Progress is {}'.format(skills.get('Java'),
                                    skills.get('Python'),
                                    skills.get('SQL')))
def examm: 
      print('Study my dear!!')
exam 
# -----------------------------------------------------------------
# Assignment 7 - 033 to 037
# -----------------------------------------------------------------

# check the below
print(f'another formate is {skills.get('Java')}, Python Progress is {skills.get('Python')}, and so on...')
print(f'another formate is : SQL Progress is : {skills.get('SQL')}, \nand so on...')



# -----------------------------------------------------------------
# Assignment 8 - 033 to 037
# -----------------------------------------------------------------






