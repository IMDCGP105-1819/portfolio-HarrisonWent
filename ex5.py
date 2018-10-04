counter = 99
for counter in range (99,-1,-1):
  if counter == 0:
    print("No more bottles if beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall...")
    break
  print(counter, "bottles of beer on the wall,", counter, "bottles of beer.")
  print("Take one down, pass it around,", counter-1, "bottles of beer on the wall...")
