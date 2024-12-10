import pandas as pd

scores = {'國文':{'王小明':65, '李小美':90, '陳大同':81, '李小玉':79},
          '英文':{'王小明':92, '李小美':72, '陳大同':85, '李小玉':53},
          '數學':{'王小明':78, '李小美':76, '陳大同':91, '李小玉':47},
          '自然':{'王小明':83, '李小美':93, '陳大同':89, '李小玉':94},
          '社會':{'王小明':70, '李小美':56, '陳大同':77, '李小玉':80},}
df = pd.DataFrame(scores)
spam = df['自然']
foo = df[['國文','數學','自然']]
boo1 = df['國文'] >= 80
boo2 = df[boo1]
boo3 = df[df['國文'] >= 80]
print(boo1)
print(boo2)
print(boo3)

df.values[0])
df.values[0][2]
df.loc['李小玉','社會']
df.loc['王小明',['國文','社會']]

