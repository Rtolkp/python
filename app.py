#simple program
print("Hai khanna,How r u")

#Drawing shape of a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#using variables nad data types
character_name="khanna"
character_age="23"
char_name="Razia"
char_age="21"
print("my name is "+character_name+"",)
print("i am "+character_age+" years old",)
print("i like the name "+char_name+"",)
print("i did't like her age "+char_age+"",)

#working with strings
print("Kanna\nRazia")

#concatenation/appendng
phrase="KannaRazia"
print(phrase+ " loves each other")

#functions
phrase="kannarazia"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("r"))
print(phrase.replace("kanna","khanna"))

#working with numbers
print(2*4+2)
print(2*(4+2))
print(9/3)
print(10%3)
my_num=5
print(my_num)
print(str (my_num)+" is my favroute nbr")

#functions related to

my_num=5
print(abs(my_num))
print(pow(3,2))
print(max(4,6))
print(min(2,6))
print(round(3.2))
print(round(3.7))
import math
print(math.floor(2.3))
print(math.ceil(3.7))
print(math.sqrt(9))

#Getting input from user
name=input("enter a name")
age=input("enter your age")
print("hello" +name+ " your are " +age)

#building  a basic calculator
num1=input("enter a number")
num2=input("enter a number")
result=float(num1)+float(num2)
print(result)

#mad libs Game

color=input("enter a color")
noun=input("enter a noun")
celebrity=input("enter a celebrity")
print("roses are red")
print("violets are blue")
print("i love u")

print("roses are" +color)
print(noun+" are blue")
print(f"i love " +celebrity)

#lists
friends=["kanna", "khanna","razia", "ssv"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

#modify the value inside of array

friend=["whisky","risky","lifty"]
friend[1]="mike"
print(friend[1])

#list functions
lucky_numbers=[2,4,6,8]
friends=["kanna","khanna","razia","ssv"]
friends.extend(lucky_numbers)
print(friends)
friends.append("Razia")
print(friends)
friends.insert(2,"kr")
print(friends)
friends.remove("ssv")
print(friends)
friends.clear()
print(friends)

fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits)

fri=['kanna','razia','ssv','munna']
fri.sort()
print(fri)

lucky_numbers.reverse()
print(lucky_numbers)

frie=['kanna','razia','ssv']
print(frie.index("razia"))

fr=["k","e","s","i","s"]
print(fr.count('s'))









