def sum1(a,b):
    result = {}
    result["h"] = a["h"] + b["h"]
    result["m"] = a["m"] + b["m"]
    result["s"] = a["s"] + b["s"]
    if result["s"] >60 :
        result["s"] -= 60
        result["m"] +=1
    if result["m"] > 60 :
        result["m"] -= 60
        result["h"] += 1

    return result
def sub(a,b):
    result = {}
    result["h"] = a["h"] - b["h"]
    result["m"] = a["m"] - b["m"]
    result["s"] = a["s"] - b["s"]
    if result["s"] < 0 :
        result["m"] -= 1
        result["s"] += 60
    if result["m"] < 0 :
        result["h"] -= 1
        result["m"] +=60
    if result["h"] < 0:
        print("Error")
    return result
def show1(a):
    print(f"{a['h']} : {a['m']} : {a['s']}")

d1 = {"h" : 10 ,"m" : 15 ,"s" : 13}
d2 = {"h" : 9 ,"m" : 35 ,"s" : 20}
result2 =sum1(d1,d2)
show1(result2)
result3 = sub(d1,d2)
show1(result3)