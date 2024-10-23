full_name = "Victor Barbosa"
text = """"Hello, my name is Victor Barbosa 
and I am a software engineer."""
text_2 = "Hello, my name is Victor Barbosa \
and I am a software engineer."

print(full_name)
print(text)
print(text_2)

# formating strings
print("Hello, my name is" + full_name)
print("Hello, my name is", full_name)
print("Hello, my name is {}".format(full_name))
print(f"Hello, my name is {full_name}")
print("Hello, my name is %s" % full_name)