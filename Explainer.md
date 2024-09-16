# Python Programming Language Lessons
## Starting Afresh with Python

### Installing Python 
Now that you're here, let's start with installing python. But before we get to deep with installing a new version, let's check if there is any on our system:
    `python` 

If there is a response other than error, it means there is a version of python installed on your machine. To close the python dialog screen just enter `exit()`. Else, you'll have to head to [python website](https://python.org/) to download a new python software. Once the download has been completed, you can go ahead to install but there is an important step you must not skip and that's to make sure you check the `Add Python 3.* to PATH` checkbox. This is a vital step as it helps make the python file global on our system and now we will be able to access it anywhere on our computer.

Once the installation has been completed, you can confirm the installation by typing `python` on your command line and hit enter. Again, to close it just press `exit()` or crtl Z and hit enter.

### Running the magic code
There's a tradition that many have come to believe in the programming world, that when you start learning a programming language, making `hello world` your first completed command will bring you good luck. So, either true or false, it has become a long-held tradition so let's start with that as weel.

To run hello world, open your command line type the following: <br>
```python
  print("Hello World!")
```

This should return `Hello World` on your command line. Congratulations, now you can update your Linkedln and Twitter profile and add `"Python Programmer"`... Lol, just kidding. But, seriously you should be proud that you have officially started your python programming journey today. Way to go champ!

### Using an IDE
For starters, an IDE stands for Integrated Development Environment. This simply refers to writing your code in a file other than the command line. Some of the popular IDE you'll deal with when interact with other pythonisters include VS Code, Sublime Text, pycharm (and some others that I can't think of right now).

For this lessons, we'll be heavily using the VS Code IDE. First, let's download [VS Code](https://code.visualstudio.com), then set up the necessary extensions to make our work easy. 

Once VS code has been downloaded and installed, lets's open it to install the extensions to make our coding easier. Once opened, you'll be welcomed with soem prelimenary setting ups such as themes, langauage and so on. But, once you get that out of the way, we can now move on to installing extension. The extension dialog is one of the dialogs on the left part of the screen. click the extension and type python in the search bar, you want to install the python extension from microsoft.

Once, that is out of the way, the next extension to install is the "Code Runner" by Jun Han. Once that is installed you'll notice a play icon at the top right corner of your screen. This icon is specifically important as it will make running our code easier in the future. Let's run our "Hello World" again but now with the IDE.

first, let's create a file and name it hello.py. Inside the file, type the following command:
```python
print("Hello World!")
```
then save the file. After the file has been saved, let's attempt to run the code using the code runner we installed the last time. To do this, simply click on the play icon on the top right corner of your screen. this should automatically open the command line and give an output that says 
```python
Hello World!
```
. If you get any result other than this, some ways to debug this includes:
* Confirm the python extension installed properly
* Confirm the Code Runner is installed properly
* confirm the commands are properly written and none of the quotes are mismatched
* ensure the print statement is not capitalized
* Python also gives an error report known as a traceback, you might want to read this error report as well as it could give a good insight into the cause of the error.
* one last step could be that the python software has not been installed properly. For this, you might have to uninstall the software abd reinstall, this time ensuring the "Add to PATH" is properly checked to make it accessible by other softwares that need to connect to it.

By following any or all of the debugging steps above, the error should now be fixed easily and you should be able to get the desired result on the output of your VS Code.

## Handling Data in Python

### Variables
Variables are like conatiners that take the shape of whatever is saved inside it. It is a container that makes it easy to reuse a piece of data without losing roll. All programming language use variable because it make work easier. Suppose you need to change a name that is used in 20 places in your file, instead of changing it in 20 places, you can just change it in the variable and it is automatically updated across the file everywhere it is used.

To declare a variable, we start by giving it a name then we say it is equal to what we want to save in the variable. For example, suppose we want to print hello world multiple time, we can just save it in a variable called my_world. This will look as follows:
```python
my_world = "Hello World"
print(my_world)
print(my_world)
print(my_world)
print(my_world)
```

When we run the code, it should print "Hello World" on the terminal 4 times.

Now, suppose we want to change this from "Hello World" to "Goodbye Folks", we won't have to do that in 4 places, we just need to change it in the variables and it updates in the other part of the program. So, here is how that will look:
```python
my_world = "Goodbye Folks"
print(my_world)
print(my_world)
print(my_world)
print(my_world)
```
You can give your variable any name; although, it is conventionally advised to be descriptive of what is to be saved in the variable. However, moving forward here are some basic rules to know about variables:
- No number before a variable name e.g 24Game. However, you can add number in any other part of the variable name if needed e.g `game24 || Ga24me || game_24`.
- Make the name short and straight to the point e.g `firstName || score || log` etc.
- You can't put space in a compound variable i.e when your variable name is more than one word, you can't put space between them instead, you can join them with hyphens and/or underscore. e.g `main_score || first-name || added_before_name` etc.
- last but not least is that all programming language have a set of words that are reserved to be used within the language to perform an action or constants. This words are known as keywords and some example in python include `print, def, class, while, try, input` etc. This keywords are forbidden to be used as variable names as it could confuse the interpreter to think you are trying to do something else.


### DataTypes
One of the important early concept to learn in programming is datatype. Basically, most programming language have a way they label datatypes but the most common data types are:
- Strings: this includes letters and character (literally, anything can be in a string). A string is basically any character enclosed in a quote e.g "hello 1".
- Integers (aka Int): these are whole numbers from 0 till 9 e.g 489777. The rule of integers is that whole numbers can't start with 0 for example 0288.
- Float (aka double): This is any number with decimal points in it e.g 0.2345

In python, these datatypes are known as primitive datatypes. Python has other datatypes known as advanced datatype. This includes:
- List
- Tuple
- Dictionary
- and many others.
We'll talk about every single one of them, but for now, let's start wth string.

#### String
As earlier stated, strings are basically a series of characters ranging from alphabets, numbers and other basic characters. But a more simpler way to see it is that, a string is any character enclosed between a quote. Unlike other programming languages like C, python support both single and double quote characters as string.

However, beyond just getting the characters enclosed within the quotes, python strings have quite a number of actions we can perform on a string such as removing a part of it; changing it to uppercase; changing it to lowercase and many others. This string actions are called `methods`. To bring you up to speed, let's deal with a few supported python string methods.

**String Methods** <br>
Methods gives us a degree of flexibility to deal with strings in a number of ways. You begin to see the importance more when you need to handle an input form a user such as changing the names to proper noun by capitalizing the first letter of names, or removing extra space in a string and so on. 

A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.

To use method on a string, we use the dot notation after the string e.g "hello".title() This will change the first letter in hello to an uppercase letter which will print Hello. However, the best way to handle method is to save the string in a variable and use the method on the variable. e.g
```python
message = "hello world"
print(message.title())
```
this will change the first letter of the two words to uppercase to print `Hello World`. The title case method is useful in a scenario where you want to bridge the gap of cases and make all input the same. This can be use in an ecommerce website where all search result are matched with a title case so whether you type a full uppercase or lowercase string in the search it will all be converted to a title case so that it can be matched with the same thing without case error.

other case related string methods include:
- .upper() changes all the letters to uppercase
- .lower() changes all the letters to lowercase

Notice the parentheses () in front of the title method? this is because methods are defined as a function and sometimes we need to supply other information to this method, therefore, the extra information goes between the parentheses.

Note: When a method does not require extra information, the parentheses are added but left blank.

**Formatted String**
This is a kind of string that uses variables inside the string. Here is an example, suppose we already have a variable that stores the salary of an employee and we want to save it with another information in a new variable without losing the original salary which we can update later. To do this, we use the formatted string method, this requires us to add an f before the quotes and the variable inside a curly braces. Here is how it looks:
```python
salary = 25000

message = f"The new salary is {salary}"
print(salary)
print(message)
```
in this code, we will get two lines printed, one being `25000` from the salary variable and the other being `The new salary is 25000` which is a combination of the string and the salary varaiable.

We can work with the formatted string just as freely as we would any string. In fact, we can also add a method to the variable inside it. For example we can make it print an uppercase version of a name that we save in another variable:
```python
name = "Tobiloba"

message = f"hello {name.upper()}"
print(message)
```

Another useful method we need to get familiar with is the strip method - which is used to remove whitespace from a string. For example, suppose we want to remove any extra space from the password that users enter, this method method presents an opportunity to do that without any stress.

The strip method have 3 ways it can be used:
- .rstrip() - removes right whitespace
- .lstrip() - removes left whitespace
- .strip() - removes whitespace from both sides

While we are talking about the format string, let's also talk about some special character that can be used inside a string. some of this special characters include:
* \n - which adds a new line to the string at the point we added it. e.g
  ```python
  message = "my much desired foods include rice, \nbean, and \nSpaghetti."
  print(message)
  ```
this will print
  ```
  my much desired foods include rice,
  beans, and
  spaghetti.
  ```

* \t - This add a tab (four spaces) before the part of the string where it was added. e.g
  ```python
  message = "my much desired foods include rice, \n\tbean, and \n\tSpaghetti."
  print(message)
  ```
this will print
  ```
  my much desired foods include rice,
      beans, and
      spaghetti.
  ```

#### Numbers
Here is the first thing to understand: everything you know about numbers still applies here. So, it's worthy of note to revisit your knowledge of numbers operations associativity and precedence i.e how they connect to each other and which operations comes first in a situation where there are more operation to be done.

For example, suppose we have an operation that has addition, subtraction, and multiplication in it. The precendence of the operation will simply go as follows: it will perform the multiplicity first, then addition, and ends with the subtraction. This does not even matter how the arrangement is made in the operation even if the multiplication is placed last, it will still be the first to be performed.

**Important (special) Number Notes**
- double astericks are use to denote a power e.g to say 3 raised to the power of 2, we say <br>`3 ** 2`
- You will get arbitrary number at the end of your float operations at time. e.g 
    ```
    0.2 + 0.1
    = 0.3000000000000000004
    ```
this is normal so, be prepared for it in the situation where it has to be perfect.
- division always result in a float i.e the division of any number by another in python will always result in a value with a decimal point. e.g
    ```
    4/2
    = 2.0
    ```
- You can use underscore to visualize a large number properly and you will still get the correct result. e.g suppose we want to represent 31 trillion i.e 31 followed by twelve zeros. we can visualize it properly as:
    ```python
    GDP = 31_000_000_000_000
    print(GDP)
    ```
if we print this, we should get `31000000000000`. Funny thing is that this does not even have to follow a pattern i.e it can be group of 3s, 2s, or 4s, or even a combination of different groups and we will still get the correct result. Furthermore, this does not interfere with any operation so we can do any other operations like addition, subtraction or any other.
- when treating a variable as constant, such as the pie constant, it is good practice to make the variable name all in caps. e.g
    ```python
    PIE = 3.14156
    print(PIE * 4)
    ```

**Comment**
Commenting is what make coding interesting: both for the writer and anyone else who will be reading the code in the future. Think of it this way, you could learn programming for a year and forget it in less that 2 months, it's the comments in your code that reminds you what those gibberish means when next you open it.

There are 2 ways to comment in python:
- A single line comment. To begin a single line comment we precede it with a hash symbol (#)
```python
# This is a single line comment
```
We use single line comment for instant less bulky commenting in our code like what a function or variable is suppose to do.
- Multi line comment: A multi line comment is wrapped in six double quote, 3 at the top and 3 below it. here is an example.
```python
"""
This is a multi line comment in python.
it is used when we have a lot to document about a code base.
This could be a descrption of the class or a mini documentation.
You get the idea.
"""
```
Here is a last note, writing a clean code is more important than anything else. so, whenever you think of it here is what can be your guide: zen of python.

on your terminal, start with initializing the python terminal by typing `python` and once the terminal has started, type `import this` and you're good to go.
  ```python
  """
      Beautiful is better than ugly.
      Explicit is better than implicit.
      Simple is better than complex.
      Complex is better than complicated.
      Flat is better than nested.
      Sparse is better than dense.
      Readability counts.
      Special cases aren't special enough to break the rules.
      Although practicality beats purity.
      Errors should never pass silently.
      Unless explicitly silenced.
      In the face of ambiguity, refuse the temptation to guess.
      There should be one-- and preferably only one --obvious way to do it.
      Although that way may not be obvious at first unless you're Dutch.
      Now is better than never.
      Although never is often better than *right* now.
      If the implementation is hard to explain, it's a bad idea.
      If the implementation is easy to explain, it may be a good idea.
      Namespaces are one honking great idea -- let's do more of those!
  """
  ```

## Lists in Python
A list is a collection of items in a particular order. We can add anything in a list i.e the elements in a list don't have to be of the same data types. To represent a list in python, we place the elements in a square bracket [] and separate each of them with a comma. 

Further, because the content of a list is always more than one, it is therefore a good practice to make the name of our list in plural form. e.g:
```python
entry = ["Taiwo", "Bose", 5, "Pelemo", True, {Nigeria : Naira}]
```

To access the elements on the list is possible in 3 differnt ways:
1. We can simply print all the elements of the string using the print statement e.g to print the example above we say:
```python
print(entry)
```

for this, we get the result `["Taiwo", "Bose", 5, "Pelemo", True, {Nigeria : Naira}]`

2. The other approach is to use the element index. here is the thing about list in python, the element of a list in python are ordered i.e the occupy a position and this position start from 0. This mean that the first element in the list occupy position 0, the second occupy position 1, the third occupies position 2 and so on. Therefore, to access any element from the list we can just use the knowledge of their position in the list to draw up the element. An easy way to get the index is to just say n-1 where n is the position of the element which mean the first element will be 1-1 = 0.

For example, suppose we want to access Pelemo from the example above, we can see that this elemen
t is the 4th in the list which mean it has an index of 3. To access it we simply write the name of the list followed by the index of the item wrapped in a square bracket: 
```python
print(entry[3])
```

this will give `Pelemo` as a result. This result is neat and clean, and above all can be passed into a string method. For example, suppose we have a list of names, we can print a result in title case e.g 
```python
names = ["beatrice", "samuel", "joseph", "daniel"]
print(names[0].title)
```

this will return the first element in the list as a title case object returning `Beatrice`. At this point, it is also worthy to note that python also support negative indexing which starts counting from the back. However, unlike the regular indexing which begins the count from zero, negative index starts from 1. Therefore, to acces the last element in the list we use -1 as our index.

We can can do anything with a list object and that includes that we can use the objects in a string or anything else. Here is an example of a list element in a string.
```python
print(f"my best friend's name is {names[1].title}. He's 23years old")
```
The output will be `my best friend's name is Samuel. He's 23years old`

### Handling Dynamic lists
For the most part of using a list, you will want to be able to manipulate your list i.e add, remove, update the elements. This kind of handling of a list is known as a dynamic list. Games are one of the special places where list manipulation are most important. For exmaple in a game that increase the number of obstacles as the time progress and reduce them when they are hit will be using a list to add and remove this obstacles. So, let's learn about modifying the list.

**Updating an element**
To change an element to soemthing else in a list is as straightforward as simply accessing the element by the index and assigning it the new value. here is an example, suppose we have a list with things to buy at the market and along the way we decided we want to change soap to diswasher in the list, we simply say:
```python
shopping_cart = ["Bread", "Soap", "Eggs", "Milk"]
print(shopping_cart)

shopping_cart[1] = "dishwasher"
print(shopping_cart)
```

in the code, the first time we print the shopping_cart, it will give us `["Bread", "Soap", "Eggs", "Milk"]`, but because we change the element at the index 1 from `soap` to `dishwasher`, now when we print the shopping_cart again it will give us `["Bread", "dishwasher", "Eggs", "Milk"]`