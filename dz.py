# ============================================
# ДЗ: логические выражения + битовые операции
# ============================================

# ----- 1. Логические выражения -----
def expr1(A, B, C):
    return (A & B) | ((~A & 1) & (~C & 1))

def expr2(A, B, C):
    return (A & B) | ((~B & 1) & C)

def expr3(A, B, C):
    return (A & B) | (~C & 1)

print("A B C | expr1 expr2 expr3")
print("-" * 30)
for A in (0, 1):
    for B in (0, 1):
        for C in (0, 1):
            print(f"{A} {B} {C} |   {expr1(A,B,C)}     {expr2(A,B,C)}     {expr3(A,B,C)}")

# ----- 2. Побитовые операции -----
x, y = 0b01101001, 0b01010101
print("\n--- Побитовые операции ---")
print(f"x     = {x:08b} ({x})")
print(f"y     = {y:08b} ({y})")
print(f"x & y = {x & y:08b} ({x & y})")
print(f"x | y = {x | y:08b} ({x | y})")
print(f"x ^ y = {x ^ y:08b} ({x ^ y})")
print(f"~x    = {~x & 0xFF:08b} ({~x & 0xFF})")
print(f"x << 1 = {x << 1:08b} ({x << 1})")
print(f"x >> 1 = {x >> 1:08b} ({x >> 1})")

# ----- 3. Тождество -x == ~x + 1 -----
print("\n--- Тождество -x == ~x + 1 ---")
ok = all(-v == ~v + 1 for v in range(-100, 101))
print(f"Проверка для -100..100: {ok}")

# ----- 4. Множества через битовые векторы -----
to_set = lambda b: {i for i in range(8) if b & (1 << i)}
print("\n--- Множества ---")
print(f"A     = {x:08b} -> {to_set(x)}")
print(f"B     = {y:08b} -> {to_set(y)}")
print(f"A & B = {to_set(x & y)}  (пересечение)")
print(f"A | B = {to_set(x | y)}  (объединение)")
print(f"A ^ B = {to_set(x ^ y)}  (разность)")

# ----- 5. Переполнение signed / unsigned (эмуляция 32-бит) -----
print("\n--- Переполнение (32 бита) ---")
TMax = 2**31 - 1
TMin = -2**31
UMax = 2**32 - 1

def to_signed(u):
    u &= 0xFFFFFFFF
    return u - 2**32 if u >= 2**31 else u

print(f"TMax     = {TMax}")
print(f"TMax + 1 = {to_signed(TMax + 1)}")
print(f"TMin - 1 = {to_signed(TMin - 1)}")
print(f"UMax     = {UMax}")
print(f"UMax + 1 = {(UMax + 1) & 0xFFFFFFFF}")