## Moving Zeros To The End
**Instructions**

```Python
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```
**Given Code**
```python
def move_zeros(array):
    return array
```
**Solution 1**
```python
def move_zeros(array):
    array_to_return = []
    for i in array:
        if i != 0:
            array_to_return.append(i)
    for i in range(1, len(array)-len(array_to_return)+1):
        array_to_return.append(0)
  #  print(array_to_return)
    return array_to_return
```
**Solution 2**
```python
def move_zeros(array):
    array_to_return = [i for i in array if i!=0]
  #  for i in range(1, len(array)-len(array_to_return)+1):
  #      array_to_return.append(0)
  #  print(array_to_return)
    
    return array_to_return+[0] * (len(array)-len(array_to_return))
```
---
[See on CodeWars.com](https://www.codewars.com/kata/52597aa56021e91c93000cb0)
