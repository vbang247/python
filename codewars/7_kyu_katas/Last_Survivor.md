## Last Survivor
**Instructions**

```Python
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'
```
**Given Code**
```python
def last_survivor(letters, coords): 
    # your code here
    pass
```
**Solution**
```python
def last_survivor(letters, coords): 
    # your code here
    list_retu = [i for i in letters]
    for j in coords:
        list_retu.pop(j)
    return "".join(list_retu)
```
---
[See on CodeWars.com](https://www.codewars.com/kata/609eee71109f860006c377d1)
