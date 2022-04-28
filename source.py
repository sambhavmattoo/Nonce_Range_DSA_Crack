import json

f = open('smattoo7_input.json')
data = json.load(f)

p = data['p']
q = data['q']
g = data['g']
m = data['m']
h = data['h']
y = data['y']
r = data['r']
s = data['s']

k = 0

g_i = 1
for i in range(1, 2**16):
    g_i = g_i * g
    if r == (((g_i) % p) % q):
        k = i
        print(k, " was found to be k.")
        break
    else:
        print(i, " was found to not be k.")

if (k == 0):
    print("k's value is out of brute-force range.")

else:
    x = 0
    H_m = int(h, 16)
    x = (((s*k - H_m)*pow(r,-1,q))%q)
    if x == 0:
        print("Huh. Secret key not found.")
    else:
        with open('report.txt', 'w') as f1:
            f1.write('%d' % k)
            f1.write('\n')
            f1.write('%d' % x)