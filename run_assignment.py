import assignment as test 
test.create("testing",25)

test.create("test",70,3600) 

test.read("testing")

test.read("test")
 
test.delete("test")


thread1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
thread1.start()
thread1.sleep()
