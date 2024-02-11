thread1 = [threading.Thread(target=test1, args=(i,))for i in range(3)]
# # for t in thread1:
# #     t.start()

# shared_var = 0
# lock_var = threading.Lock()