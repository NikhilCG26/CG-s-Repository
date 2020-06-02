data = 'from nikhilcg@yahoo.com Sat Jan 5 04:12:15 2010'
atpos = data.find('@')
print(atpos)
spos = data.find(' ',atpos)
print(spos)

host = data[atpos+1 : spos]
print(host)