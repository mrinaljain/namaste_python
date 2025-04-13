import camelcase

c = camelcase.CamelCase()

txt = "hello world"
m = c.hump(txt)
print(c.hump(txt))