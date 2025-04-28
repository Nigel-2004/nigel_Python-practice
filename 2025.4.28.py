#Ask user for the name
name = input("what's your name? ")
#Say hello to user
print(f"hello,{name}")
#默认状态下end是将读取/n也就是提行，这里让end为nothing，就可以实现不提行

name = name.strip()
#去除多余空格
name = name.title()
#大写用户名
name = input("what's your name?").strip().title()
#split user's name into first name and last name
first , last = name.split("")

