import sys

million = list(range(0, 1000001))

# min and max value of array

print('Mb in memory: {}'.format(sys.getsizeof(million) / 1000000))

print('Min value: {}'.format(min(million)))
print('Max value: {}'.format(max(million)))


print('Sum all of numbers: {}'.format(sum(million)))

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
