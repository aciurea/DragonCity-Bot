## Python 

### Slice Array

`[1, 2, 3, 4, 5]`
- [:] shallow copy of the array
- `[start : stop : step]`
- `[-1]` -> `5` -> last item in the array
- `[-2]` -> `[4, 5]` -> last 2 items in the array
- `[:-1]` -> `[1, 2, 3, 4]` -> everything except the last item
- `[::-1]` -> `[5, 4, 3, 2, 1]` -> all the items in reverse order
- `[::-2]` -> `[5, 3, 1]` -> all the items from 2 to 2 in reverse order
- `[1::-1]` -> `[2, 1]` -> first 2 items in reverse order