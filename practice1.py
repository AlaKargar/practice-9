
def jam(x,y):
    result={}
    result["h"]=x["h"]+y["h"]
    result["m"]=x["m"]+y["m"]
    result["s"]=x["s"]+y["s"]

    if result["s"]>=60:
        result["s"]-=60
        result["m"]+=1
    
    if result["m"]>=60:
        result["m"]-=60
        result["h"]+=1

    print("jam: ",result["h"], ":", result["m"], ":", result["s"])
def tafrigh(x,y):
    result={}
    result["h"]=x["h"]-y["h"]
    result["m"]=x["m"]-y["m"]
    result["s"]=x["s"]-y["s"]

    if result["s"]<=0:
        result["s"]+=60
        result["m"]-=1
    
    if result["m"]<=0:
        result["m"]+=60
        result["h"]-=1

    print("tafrigh: ", result["h"], ":", result["m"], ":", result["s"])
def zaman_sec(x,y):
  s1 = x["h"]* 3600 + x["m"] * 60 + x["s"]
  s2=  y["h"]* 3600 + y["m"] * 60 + y["s"]
  print("your time1 to seconds: ", s1)
  print("your time2 to seconds: ", s2)
  def sec_zaman(x,y):
    x["h"]= (s1 // 3600)
    x["m"] = (s1 % 3600)//60
    x["s"] = (s1 % 3600) % 60
    
    y["h"]= (s2 // 3600)
    y["m"] = (s2 % 3600)//60
    y["s"] = (s2 % 3600) % 60
    print("your time1 of sec: ", x["h"], ":", x["m"], ":", x["s"])
    print("your time2 of sec: ", y["h"], ":", y["m"], ":", y["s"])
  sec_zaman(t1,t2)

t1={"h":2, "m":30, "s":45}
t2={"h":3, "m":17, "s":40}

t3=jam(t1, t2)
t4=tafrigh(t1,t2)
t5=zaman_sec(t1,t2)

