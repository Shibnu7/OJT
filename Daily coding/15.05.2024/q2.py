a,b = 0,1
x = [a,b]
while b<= 1234:
    a,b = b, a+b
    x.append(b)
    print("Fibinoci serise up to 1234:",x);