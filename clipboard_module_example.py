import clipboard

#example 1
# clipboard.copy('abc') 


#example 2. For this, you need to have something already copied to your clipboard
data = clipboard.paste()
print(data)