def addPhone(manu,model,price,l,test):
    """
    Function used fro adding a (manufacturer, model, price) touple to the list of phones.
    input:manu - the manufacturer (string),model -the model(string),price-the price(int),l - the list of phones
    output:the modified list
    """
    x=(manu,model,price)
    l.append(x)
    if test == 0:
        print("\n\tPhone added successfully!")
    return l

def removePhone(manu,model,l,test):
    """
    Function used for removing a phone from the list of phones.If the phone is not found, a message is printed.
    input:manu - the manufacturer (string),model -the model(string),l - the list of phones
    output:the modified list
    """
    ok=False
    for i in range(0,len(l)):
        if l[i][0]==manu and l[i][1] ==model:
            l.pop(i)
            ok=True
            if test == 0:
                print("\n\tPhone removed successfully!")

    if ok ==False and test==0:
        print("\n\tThe is no phone with thiese details.")
    return l

def updatePhone(manu,model,price,l,test):
    """
    Function used for updating the price of a phone from the list of phones.If the phone is not found, a message is printed.
    input:manu - the manufacturer (string),model -the model(string),price-the price(int),l - the list of phones
    output:the modified list
    """
    """
    Function used fro adding a (manufacturer, model, price) touple to the list of phones.
    input:manu - the manufacturer (string),model -the model(string),price-the price(int),l - the list of phones
    output:the modified list
    """
    ok = False
    for i in range(0, len(l)):
        if l[i][0] == manu and l[i][1] == model:
            l[i]=(manu,model,price)
            ok = True
            if test == 0:
                print("\n\tPhone updated successfully!")
    if ok == False and (test == 0):
        print("\n\tThe is no phone with thiese details.")
    return l

def listAll(l):
    """
    Function used for printing the list of phones sorted by increasing price.For that it is used a temporary list which is sorted.
    If the list is empty, a message is printed.
    input:the list of phones
    output:the list is printed
    """
    print("\n")
    for i in range(0, len(l)):
        print("Manufacturer:"+ l[i][0] +" Model:" +l[i][1] + " Price:" + str(l[i][2])+"\n")
    if len(l)==0:
        print("\n\tThe list is empty")

def sortedPhone(l):
    """
    Function used for printing the entire list of phones sorted by increasing price.If the list is
    empty, a message is printed.
    input:the list of phones
    output:the list is printed
    """
    print("\n")
    if len(l)==0:
        print("\n\tThe list is empty")
    else:
        tmp=l
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                if int(tmp[i][2])>int(tmp[j][2]):
                    tmp[i],tmp[j]=tmp[j],tmp[i]
        for i in range(0, len(tmp)):
            print("Manufacturer:" + tmp[i][0] + " Model:" + tmp[i][1] + " Price:" + str(tmp[i][2]) +"\n")

def addElements(l):
    addPhone("samsung", "edge 7", 2300, l, 1)
    addPhone("samsung", "edge 10", 2800, l, 1)
    addPhone("iphone", "s67", 24, l, 1)
    addPhone("motorola", "g56f", 250, l, 1)
    addPhone("iphone", "black", 125, l, 1)
    addPhone("nokia", "lumia", 160, l, 1)
    addPhone("nokia", "xperia", 2450, l, 1)
    addPhone("HTC", "desire", 2400, l, 1)
    addPhone("HTC", "rexs", 2300, l, 1)
    addPhone("Phone 4", "Phone", 2425, l, 1)
    return l
#Tests
def Tests():
    """
    Function used for tests
    """
    l=[]
    testAddPhone(l)
    testRemovePhone(l)
    testUpdatePhone(l)
    l=[]
    return l

def testAddPhone(l):
    assert len(l)==0
    addPhone("samsung","edge 7",2400,l,1)
    assert len(l) == 1
    addPhone("motorola", "x", 500, l, 1)
    addPhone("iphone", "5s", 1400, l, 1)
    assert len(l) == 3
    addPhone("samsung ", "y", 20, l, 1)
    addPhone("iphone", "6s", 2900, l, 1)
    assert len(l) == 5

def testRemovePhone(l):
    l = []
    addPhone("samsung", "edge 7", 2400, l, 1)
    assert len(l) == 1
    removePhone("samsung", "edge 7",l,1)
    assert len(l) == 0

    addPhone("samsung", "edge 7", 2400, l, 1)
    assert len(l) == 1
    addPhone("iphone", "5s", 1000, l, 1)
    assert len(l) == 2
    removePhone("iphone", "5s", l, 1)
    assert len(l) == 1

def testUpdatePhone(l):
    l = []
    addPhone("samsung", "edge 7", 2400, l, 1)
    assert len(l) == 1
    updatePhone("samsung", "edge 7", 1000, l, 1)
    assert len(l) == 1
    assert l[0][2] == 1000
    updatePhone("samsung", "edge 7", 2000, l, 1)
    assert len(l) == 1
    assert l[0][2] == 2000

    addPhone("iphone", "6s", 1000, l, 1)
    assert len(l) == 2
    updatePhone("iphone", "6s", 1500, l, 1)
    assert len(l) == 2
    assert l[1][2] == 1500





