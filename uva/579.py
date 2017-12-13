while True:
    h, m = map(int, input().split(':'))
    if h == 0 and m == 0:
        break

    a0m = m / 60
    a0h = (h + m / 60) / 12
    amh = (abs(a0m - a0h)) * 360
    if amh > 180:
        amh = 360 - amh 
    print('%.3f' % amh)
    
