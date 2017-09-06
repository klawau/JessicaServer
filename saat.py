import time
def saat(td):
    td = float(td)
    
    newsaat = 0
    newdakika = 0
    td = time.time()-td
    while td >= 3600:
        td -= 3600
        newsaat += 1
    while td >= 60:
        td -= 60
        newdakika += 1
    return str(newsaat)+"NoVa"+str(newdakika)
