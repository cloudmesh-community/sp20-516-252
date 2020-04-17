Engineering Cloud Computing

## Course Notes on Updating 

### Cloudmesh installation commands
```
$ pip install cloudmesh-installer -U
$ cloudmesh-installer install packgeName
$ cloudmesh-installer git clone packageName
```
### check ssh key

```
$ cd ~/.ssh
$ vi id_rsa.pub # view public key
$ $ ~/.ssh/id_rsa.pub # path to public key (Permission denied)
```

### remove a known host key

`ssh-keygen -R hostname`

To add ssh key:

```
eval `ssh-agent -s`
ssh-add
```

## Week 3 Lab Activities 

### Notes
cmd5: package used to create command line shells.
cmd5 can be activated with the cms command
`(EVN3) $ cms`
(Intro to Python Chapter 6.7.1)


### 4.3.2.1 Review: venv in Python 3

* To activate the virtual env in MacOS

`source ENV3/bin/activate`

# * ???? How to modify `.bashrc` file so that the python venv is loaded
 automatically 
upon the start of a new terminal?

To switch from Zsh to Bash 
 ```chsh -s /bin/bash```
 Then enter user password.
 
 Type `nano .bashrc`. It will open or create the document using nano.
 Set path to where virtual environment is at the very end of the document
 , then save, quit:
 `source ~/ENV3/bin/activate`

 * Why need `venv` for this class?
 
 Since several users share one physical server to raise the hardware utilization
   percentage, several environments on one physical machine is needed. Each
    users are not allowed to access other's data. Creating virtual
     environment allows each users to be isolated securely and reliably from
      each other.

### 4.3.3.1.3 Dicts
* How do you merge contents in two dicts?

Use function `dict1.update(dic2)`

Example:
```dict1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
# Create second dictionary
dict2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}
print(dict1)
dict1.update(dict2)

print('Updated dictionary 1 :')
print(dict1)
```
     
 ### 4.3.3.1.4 f-String in Python3
 * What does locals do?
 * What does ** in the format statement do?
 
 In string interpolation we normally have to pass all variables to the
  "format" function,
 for example:
 ```
print "Hi, I am {name} and I am {age} years old".format(age=26, name="John")
Hi, I am John and I am 26 years old
```
To simplify the process, we can tell format to directly access local variables.
`locals` function creates a dictionary with all local variables.

While `format` requires key-value parameters, `locals()` returns a dictionary
 `**` converts dictionary to key-value
parameters.
```
name = "John"
age = 26
msg = f"my name is {name}, and I am {age} old".format(**locals());
print(msg)
``` 

### 4.3.3.1.5 python Classes
* What is `self` in classes?
* Why does `self` needs to be used in regular method definitions in classes?

By using `self` we can access the attributes and methods of the class in
 python. In such a way, the instance is passed to method automatically, but
  not received automatically. The first paramter of methods is the instance
   the method is called on. `self` is a convention, not a real python keyword
   , so other parameter name can be used in place of it.

```
class this_is_class:  
    def show(name_other_than_self):  
        print("we have used another name")
```
* What can I do with  `init` and why is it used?

Constructors are used to instantiate an object. Constructors initialize
/ assign values when an object of class is created.

```buildoutcfg
def __init__(self):
    # constructor body
```

### 4.3.3.1.6 Python Modules
* What is the difference between `pip install .` and `pip install -e .`

* How do I uninstall a python module?

* What to do if your python virtual environment is broken?



References

1. <https://dzone.com/articles/how-to-implement-string-interpolation
-in-python-br>
2. <https://www.quora.com/Why-do-we-need-virtual-machines-in-cloud
 -environments>
3. <https://natelandau.com/my-mac-osx-bash_profile/>
4. <https://thispointer.com/how-to-merge-two-or-more-dictionaries-in-python/>
5. <https://www.geeksforgeeks.org/self-in-python-class/>
6. <https://www.geeksforgeeks.org/constructors-in-python/>