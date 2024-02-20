def zarb(x,y):
    result={}
    result["s"]=x["s"]*y["s"]
    result["m"]=x["m"]*y["m"]
    return result
def taghsim(x,y):
    result2={}
    result2["s"]=x["s"]*y["m"]
    result2["m"]=x["m"]*y["s"]
    return result2
def jam(x,y):
    if x["m"]!=y["m"]:
        result3={}
        result3["s"]=((x["s"])*y["m"])+((y["s"])*x["m"])
        result3["m"]=x["m"]*y["m"]
    else:
        result3={}
        result3["s"]=x["s"]+y["s"]
        result3["m"]=x["m"]
    return result3
def tafringh(x,y):
    if x["m"]!=y["m"]:
        result3={}
        result3["s"]=((x["s"])*y["m"])-((y["s"])*x["m"])
        result3["m"]=x["m"]*y["m"]
    else:
        result3={}
        result3["s"]=x["s"]-y["s"]
        result3["m"]=x["m"]
    return result3

a={"s":1, "m":2}
b={"s":3, "m":4}

c=zarb( a,b)
print("zarb: ",c)

d=taghsim(a,b)
print("taghsim: ",d)

e=jam( a,b)
print("jam: ",e)

f=tafringh(a,b)
print("tafrigh: ", f)