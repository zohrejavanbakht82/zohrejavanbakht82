def sum(f1,f2):
    result_s = {}
    result_s["s"] =f1["s"] * f2["m"] + f1["m"] * f2["s"]
    result_s["m"] = f1["m"] * f2["m"]
    return result_s
def mul(a,b):
    result_m = {}
    result_m["s"] = a["s"] * b["s"]
    result_m["m"] = a["m"] * b["m"]
    return result_m
def division(f1,f2):
    result_d = {}
    result_d["s"] = f1["s"] * f2["m"]
    result_d["m"] = f1["m"] * f2["s"]
    return result_d
def sub(a,b):
    result = {}
    result["s"] = a["s"] * b["m"] - a["m"] * b["s"]
    result["m"] = a["m"] * b["m"]
    return result
def show(a):
    print(f"{a['s']} / {a['m']}")
    
f1 = {"s": 2, "m": 3}
f2 = {"s":5 , "m": 4}
result = sum(f1,f2)
show(result)
result1 = mul(f1,f2)
show(result1)
result_3 = division(f1,f2)
show(result_3)
result4 = sub(f1,f2)
show(result4)
