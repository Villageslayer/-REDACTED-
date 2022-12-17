Name = "Alex Georgiou"
Age = "prob 20 something"
Adress = "Düsseldorferstr. 16/16a dachgeschoss"


eingabe = input("Name")   # ask input 

def f(x):
    match x:
        case 'Name':
            return Name 
        case 'Age' :
            return Age
        case 'Adress':
            return Adress
