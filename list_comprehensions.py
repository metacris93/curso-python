def run():
    list = [ i for i in range(1, 100001) if i % 36 == 0 ]
    print(list)

def dict_run():
    dict = { i : i**3 for i in range(1,101) }
    print(dict)

if __name__ == "__main__":
    run()
    dict_run()
