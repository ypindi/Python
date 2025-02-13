import pdb

def divide(a, b):
    pdb.set_trace()  # Debugger starts here
    return a / b

print(divide(10, 2))


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> py .\4_pdb.py
# > d:\yashwanth\htw_berlin\self_learnings\python\testing\4_pdb.py(5)divide()       
# -> return a / b
# (Pdb)
# (Pdb)
# (Pdb)
# (Pdb)
# (Pdb)
# (Pdb) step
# --Return--
# > d:\yashwanth\htw_berlin\self_learnings\python\testing\4_pdb.py(5)divide()->5.0  
# -> return a / b
# (Pdb)
# 5.0
# --Return--
# > d:\yashwanth\htw_berlin\self_learnings\python\testing\4_pdb.py(7)<module>()->None
# -> print(divide(10, 2))
# (Pdb) continue
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing>