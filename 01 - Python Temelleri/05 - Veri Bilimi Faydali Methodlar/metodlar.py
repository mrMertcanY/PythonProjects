for num in list(range(5, 21, 4)):
    print(num)


print("===========")

## enumerate

index = 0

for num in list(range(5, 15)):
    print(f"Güncel numara {num} güncel index: {index}")
    index += 1

print("===========")

for (index, value) in enumerate(list(range(5, 15))):
   print(value)



