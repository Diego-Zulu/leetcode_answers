# Python tips

This file includes tips and trick I found useful when interviewing on Python. It's kinda messy right now, but I'll be keep on cleaning it up and adding to it in the future.

## List

- How to create a Java TreeMap but in Python3 at leetcode: http://www.grantjenks.com/docs/sortedcontainers/

```
from sortedcontainers import SortedDict
```

Remember collections.OrderedDict and SortedDict are NOT the same. OrderedDict orders by insertion, and SortedDict by key order

- Iterate between string groups without spliting:
```
In [1]: def split_iter(string):
            return (x.group(0) for x in re.finditer(r"[A-Za-z']+", string))

In [2]: type(split_iter("A programmer's RegEx test."))
Out[2]: generator

In [3]: list(split_iter("A programmer's RegEx test."))
Out[3]: ['A', "programmer's", 'RegEx', 'test']
```

- Use a cmp function with `sorted` in python3 (>= 3.3 to be exact):

```
import functools
a = [3, 2, 1]
a = sorted(a, key=functools.cmp_to_key(lambda x, y: -1 if x < y else (1 if x > y else 0)))
print(a)

$ [1, 2, 3]
```

- Namedtuples can help make code cleaner:

```
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

print(pt1.x)

$ 1.0
```

- Unpacking can help make code cleaner:

```
# first and second will be assigned to x and y 
# remaining will be assined to z 
x, y, *z = (10, "Geeks ", " for ", "Geeks ", 50) 
```

- Get a random int:

```
import random
print(random.randint(1,100))

# Watch out! On python3 this method INCLUDES 100
```

- How to remove keys from a set:

```
s = set()

e = '1'

s.discard(e) # No error if e is missing
s.remove(e) # Throws KeyError if e is missing
```

- Read from standard input (blocking):

```
import sys

sys.stdin.readline()
```

- Differences between `sorted` and `list.sort`: https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort

```
- Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back. Use sorted() when you want to sort something that is an iterable, not a list yet.

- For lists, list.sort() is faster than sorted() because it doesn't have to create a copy. For any other iterable, you have no choice.
```

- Integer division:

```
int(a / b) == a//b
```

- Dividie and mod in same step:

```
carry, val = divmod(l1.val + l2.val + carry, 10)
# carry = sum / 10
# val = sum % 10
```

- Deal with exceptions in Python: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
```
try:
    # Code

except IOError:
    # Deal with IOError

else:
    # Run code if no exception was captured
finally:
    # Always gets called
```

- Count ocurrances of elements in iterable:

```
import collections

count = collections.Counter(iterable)

In [1]: Counter('abracadabra').most_common(3)
Out[1]: [('a', 5), ('r', 2), ('b', 2)]
```

- Split with a regex:
```
import re
text = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('\*|\n',text)) # ['The quick brown', 'fox jumps', 'over the lazy dog.'] 
# | separates characters, \ escapes special characters
```

- Deal with characters (although remember these are string operations):
```
'c'.lower() # To lower case
'c'.isalpha() # Is alpha character?
'c'.isalnum() # Is alphanumeric?
'c'.isdigit() # Is digit?
ord('a') # Get ascii code
chr(12) # Get character from ascii code
```

- Turn list into tuple:
```
tuple([1,2])
```

- Use `deque` as queue implementation:
```
from collections import deque

d = deque()
# Use d.popleft() and d.append(element).
# Or you can also use d.pop() and d.appendleft(element)
```

- How to redifine comparator in an object's class: Redefine `__lt__(self, other)` method

- Use `heapq` as heap implementation. It has useful methods like `nlargest` and `heapify` (which is linear time and in place https://bytes.com/topic/python/answers/37747-why-heapify-linear)

- A really big number:

```
float('inf')

import sys
sys.maxsize
```
- Remember you can zip list together to iterate them together:
```
zip(l1, l2)
```

- How to import type hints:
```
from typing import Dict, List
```

- You can use bisect for binary searching: https://docs.python.org/3/library/bisect.html
```
import bisect

# a -> Iterable
# x -> Elements

bisect.bisect_left(a, x, lo=0, hi=len(a))
```

- Convert hex string to int: https://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
```
# Without hex header
int("deadbeef", 16)

# With hex header
int("0xdeadbeef", 0)
```

- Other important info:

    1. Strings are non mutable in python

    2. https://www.bigocheatsheet.com/

    3. https://docs.python.org/2/library/collections.html