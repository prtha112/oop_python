from Calculate import Tax

price = 200
mytax1 = Tax(price)
ans1 = mytax1.caltax()
print(ans1)

newrate = 0.05
mytax2 = Tax(price, newrate)
ans2 = mytax2.caltax()
print(ans2)
