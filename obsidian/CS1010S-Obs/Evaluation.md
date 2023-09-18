```python
print(print(print(1)), (2), print(3,))
#          ^ here first                => prints 1
#    ^ then here, print(1) -> None so  => prints None
#                           ^ now here => prints (3,)
# finally evaluate everything,         => prints None 2 None
```
Scan left-to-right for closed brackets:
So the output console will be 
```plaintext
1
None
(3,)
None 2 None
```
