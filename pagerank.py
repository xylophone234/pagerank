import numpy as np
def pagerank(fn_chuck,size,max_iter=300,eps=1e-10):
    '''
    pagerank need a size*size matrix which every column sum equal to 1.0
    This big file must save in some files with filename like 'xxx_0_1000.npy','xxx_1000_1500.npy',
    means the matrix from row 1000 to row 1500
    params:
        fn_chunk:string,a file name,it's content is a chunk file name per line,
                    like 'xxx_0_1000.npy\nxxx_1000_1500.npy
        size:int,the sqare matrix size
        max_iter:int,the number of max iter
        eps:float,the erros you can accept
    returns:
        pagerank value: ,size rows 1 column
        error:current error
    '''
    x1=np.zeros((size,1))+1.0/size
    x2=np.zeros((size,1))
    n_iter=0
    error = np.abs(x1-x2).mean()
    chunk_fn_list=[line.rstrip() for line in open(fn_chuck)]
    while n_iter<max_iter and error > eps:
	# print '%s iter of %s max_iter' % (n_iter,max_iter)
        for fn in chunk_fn_list:
            chunk_start,chunk_end = fn.split('.')[0].split('_')[-2:]
            chunk_start,chunk_end = int(chunk_start),int(chunk_end )
            x2[chunk_start:chunk_end]=np.dot(np.load(fn),x1)
        error = np.abs(x1-x2).mean()
        x1,x2 = x2,x1	
	print 'iter: %s   error: %s' % (n_iter,error) 
	n_iter +=1
    return x2,error
