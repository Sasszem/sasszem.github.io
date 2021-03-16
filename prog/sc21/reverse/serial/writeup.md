# SerialHacker

- easy

A freshly downloaded flag-dispenser from The Pirate Bay, the only thing you need is a valid serial key. The description said it's not a virus and they NEVER lie, ignore the comments.

All jokes aside the executable is NOT malicious, however Windows Defender or other AVs might pop an alert.

_author: chronos_

Attached file:
- [xXx_free_flagz_by_m1lfbANGER42069_RU_xXx.exe](xXx_free_flagz_by_m1lfbANGER42069_RU_xXx.exe)

## Writeup

(I did not make proper notes because it was so easy I did not need them)

I've used DexTools to reverse the file, and I've found the constraints for the flag. It calculates a few values, checks them, and if they are ok, it generates the flag using a strigt and the exact same values - so as we know what they should be, we can just do the calculations ourselves:

```python
# return b.Length == 23 && b[5] == '-' && b[11] == '-' && b[17] == '-' && this.c(b.Substring(0, 5)) && this.d(b.Substring(6, 5)) && this.e(b.Substring(12, 5)) && this.f(b.Substring(18, 5));

# means AAAAA-BBBBB-CCCCC-DDDDD

# no lowercase
# sum(A) = 385
# product(B)%512 = 420
# E[0]=E[4] and E[1]=E[3] and E[2]="E"
# F[1]=F[0]+1 and F[2]=F[1]+1 and F[3]=F[2]+2 and F[4]=F[3]+3

#b.b

a = "b`*/y%d2cg1r]t*+\\2(^*#f^*lt"

num = 385 # sum(a)
num *= num

print(num)

num2 = 420 # prod(b)
num2 %= 512
num2 = num2*1000+num2

print(num2)

num3=ord("E") # add [1]-[3] and [0]-[4] to [2]
num3 = num3 * num3 * num3 * num3 * 10 + 7;

print(num3)

num4 = (ord("Ϩ")+ord("d")+2*ord("\n")+3)*ord('Ƥ') + ord("E")
print(num4)


x = str(num) + str(num2) + str(num3) + str(num4)
print(x)
print(len(x))
for i in range(27):
    print(chr(ord(a[i])+int(x[i])),end="")
```