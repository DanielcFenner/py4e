hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    sum = (40 * r) + ((h - 40) * (r * 1.5))
    print(sum)
else:
    print(h * r)
