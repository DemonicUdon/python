try:
    f = open("myContact.txt", encoding='utf-8')
    print(f.readlines())
except:
    print("Error")
finally:
    f.close()
