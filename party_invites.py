guests = ['rahul', 'anil', 'udhav', 'amol', 'harshal']
print(guests)
canceled_guest = guests.pop(3)
print(canceled_guest.title()+" won't be able to make it to the party") 
guests.insert(3,'anmol')
print(guests)
guests.insert(0,'sumit')
guests.append('kunal')
print(guests)
del guests[-1]
print(guests)
