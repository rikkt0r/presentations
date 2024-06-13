with open(__file__, "r") as f:
    print("Present: %s" % __file__)

nsf = "no_such_file"
try:
    with open(nsf, "r") as f:
        pass
except FileNotFoundError:
    print("Missing: %s" % nsf)

