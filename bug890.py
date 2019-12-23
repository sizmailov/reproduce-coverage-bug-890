import multiprocessing
import os

if not os.path.exists("./tmp"): os.mkdir("./tmp")
os.chdir("./tmp")

with multiprocessing.Manager() as manager:
    pass

print("ok")
