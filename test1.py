from concurrent.futures import ProcessPoolExecutor
import os,time,random
def task(n):
    print('%s is running' %os.getpid())
    time.sleep(2)
    return n**2


if __name__ == '__main__':
    p=ProcessPoolExecutor()  #不填则默认为cpu的个数
    l=[]
    start=time.time()
    for i in range(10):
        obj=p.submit(task,i)   #submit()方法返回的是一个future实例，要得到结果需要用obj.result()
        l.append(obj)

    p.shutdown()  #类似用from multiprocessing import Pool实现进程池中的close及join一起的作用
    print('='*30)
    # print([obj for obj in l])
    print([obj.result() for obj in l])
    print(time.time()-start)
