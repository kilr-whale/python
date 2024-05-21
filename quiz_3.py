url = ("http://google.com")
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str))+ str(my_str.count("e"))+"!"
print("{}의 생성된 비밀번호 : {}".format(url, password))