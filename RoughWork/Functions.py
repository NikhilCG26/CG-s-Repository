def computepay(h,r):
    if h <= 40 :
        p = h*r
        return p
    else :
        h1 = h - 40
        p = (h1*r*1.5)+(h*r)
        #print(p)
        #p = h*r*1.5
        return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)