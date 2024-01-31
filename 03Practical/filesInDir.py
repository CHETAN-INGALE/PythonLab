import os

dir_list = os.listdir(".")

for item in dir_list:
  if os.path.isfile(item):
    print(item)