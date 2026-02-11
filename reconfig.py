
def psd_TEgraph(G,k):
    ord=G.order()
    V = G.vertices()
    S = Subsets(V,k)
    TEV = []
    TEE = []
    ptm = -1
    for s in S:
       
        ptms=pt_plus(G,s)
        if (ptms > -1):
            TEV.append(s)
           
           
    N = len(TEV)
                 
    for i in range(N):
           
        for j in range(i+1,N):
            L = len(list(set(TEV[i]) & set(TEV[j])))
               
            if L == k-1:
                TEE.append((TEV[i],TEV[j]))
    TEG = Graph([TEV,TEE],multiedges=False)
    
    return TEG            


# F-2 other zero forcing functions (Leslie Hogben)
#
# Zero forcing number Z(G)
def Z(g):
    z=len(zero_forcing_set_bruteforce(g))
    return z
#
# All zero forcing sets of G of size k
# input: a graph G and a positive integer k 
# output: a list of all zero forcing sets G of size k
def ZFsets(G,k):
    ord=G.order()
    V = G.vertices()
    S = Subsets(V,k)
    ZFS=[]
    for s in S:
        A=zerosgame(G,s)
        if len(A)==ord:
            ZFS.append(s)
    return ZFS 

# F-R1 Zero Forcing Reconfiguration graph functions
# adapted from code by Chassidy Bozeman


# input: A graph G and a positive integer k
# output: All zero forcing sets G up to size k


def ZFS_up_to_size_k(G,k):
    S=[]
    for i in [Z(G)..k]:
        ZFS_size_i=ZFsets(G,i)
        S=S+ZFS_size_i
    return S
    
    
# input: A graph G and a positive integer k 
# output: The TAR ZF reconfiguration graph on zero forcing sets up to size k. 
       
def ZTAR_reconfig(G,k):
     
    S=ZFS_up_to_size_k(G,k) 
    # creates a list of all zf sets up to size k.
    
    H=Graph()
    # creates empty graph    
       
    H.add_vertices(S) 
    # add zf sets up to size k to the vertices of H
       
    # The following part determines if the size of two zero forcing sets differ            
    # by one and if one is a subset of the other. If both are true, an edge is added. 
   
   
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if len(S[i])-len(S[j]) in {-1,1}: 
                    if set(S[i]).issubset(set(S[j])): 
                        H.add_edge(S[i],S[j])  
                    else:
                        if set(S[j]).issubset(set(S[i])):
                            H.add_edge(S[i],S[j])            
    return H



#input: A graph G 
#output: The TE=TJ Z reconfiguration graph on zero forcing of size Z(G)



def ZTE_reconfig(G):
     
    z=Z(G)
    S=ZFsets(G,z) 
    #creates a list of all zf sets of size k.
    
    H=Graph()
    #creates empty graph
    
       
    H.add_vertices(S) 
    # add minimum zero forcing sets to the vertices of H
    
    # The part below is for token exchange (toke jumping). If two zero forcing sets have the                        
    # same size and they differ by one element, then an edge is added between them.
   
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if len(S[i])==len(S[j]): 
                if len(set(S[i]).difference(set(S[j])))==1:
                        H.add_edge(S[i],S[j])
                              
    return H 

# F-2 Power domination functions
# by Brian Wissman

# input: a graph G and a subset of its vertices V
# output: true/false depending if V is a power dominating set of G

def isPowerDominatingSet(G,V):  
    N=[]
    for i in V:
        N+=G.neighbors(i)
    NVert=uniq(N+list(V))
   
    A=zerosgame(G,NVert)
    if len(A)==G.order():
        return True
    else:
        return False

# input: a graph G
# output: a power dominating set of G that achieves the power domination number
def minPowerDominatingSet(G):
    V = G.vertices()
    for i in range(1,len(V)+1):
        S = subsets(V,i)
        for s in S:
            if isPowerDominatingSet(G,s):
                return s
                
# input: a graph G
# output: the power domination number of G
def PowerDom(G):
    V = G.vertices()
    for i in range(1,len(V)+1):
        S = subsets(V,i)
        for s in S:
            if isPowerDominatingSet(G,s):
                p=len(s)
                return p 
       	
# F-3 power dominating sets
# input: a graph G and a positive integer k 
# output: a list of all power dominating sets G of size k
def PDsets(G,k):
    ord=G.order()
    V = G.vertices()
    S = subsets(V,k)
    PDS=[]
    for s in S:
        if isPowerDominatingSet(G,s):
            PDS.append(s)
    return PDS 
       	
# F-R2 Token Addition and TAR and 
# by Chassidy Bozeman edited by Leslie Hogben



# input: A graph G and a positive integer k
#output: All power dominating sets G up to size k


def PDS_up_to_size_k(G,k):
    S=[]
    for i in range(1,k+1):
        PDS_size_i=PDsets(G,i)
        S=S+PDS_size_i
    return S
    
    
#input: A graph G and a positive integer k 
#output: The TAR PD reconfiguration graph on power dominating set up to size k. 
       
def PDTAR_reconfig(G,k):
     
    S=PDS_up_to_size_k(G,k) 
    #creates a list of all dominating sets up to size k.
    
    H=Graph()
    #creates empty graph
    
       
    H.add_vertices(S) 
    # add power dom sets up to size k to the vertices of H
    
    
    # The following part determines if the size of two power dominating sets differ            
    # by one and if one is a subset of the other. If both are true, an edge is added. 
   
   
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if len(S[i])-len(S[j]) in {-1,1}: 
                    if set(S[i]).issubset(set(S[j])): 
                        H.add_edge(S[i],S[j])  
                    else:
                        if set(S[j]).issubset(set(S[i])):
                            H.add_edge(S[i],S[j])            
    return H



# Token Jumping = Token Exchange
#input: A graph G and integer k 
#output: The TAR PD reconfiguration graph on PDS of size up to k

def PDTE_reconfig(G):
     
    p=PowerDom(G)
    S=PDsets(G,p) 
    #creates a list of all dominating sets of size p=PD(G).
    
    H=Graph()
    #creates empty graph    
       
    H.add_vertices(S) 
    # add power dom sets of size k to the vertices of H
    
    # The part below is for token exchange. If two power dominating sets have the                        
    # same size and they differ by one element, then an edge is added between them.
   
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if len(S[i])==len(S[j]): 
                if len(set(S[i]).difference(set(S[j])))==1:
                        H.add_edge(S[i],S[j])
                              
    return H 
   
    TEG = Graph([TEV,TEE])
    
    return TEG






def skew_TEgraph(G,k):

    ord=G.order()

    V = G.vertices()

    S = Subsets(V,k)

    TEV = []

    TEE = []

    ptm = -1

    for s in S:

       

        ptms=prop_time_unlooped(G,s)

        if (ptms > -1):

            TEV.append(s)

            

            

    N = len(TEV)

                 

    for i in range(N):

           

        for j in range(i+1,N):

            L = len(list(set(TEV[i]) & set(TEV[j])))

               

            if L == k-1:

                TEE.append((TEV[i],TEV[j]))

   

    

    TEG = Graph(TEE)

    return TEG

def psd_TSgraph_ext(G,k):
    ord=G.order()
    V = G.vertices()
    S = Subsets(V,k)
    TSV = []
    TSE = []
    ptm = -1
    TSN = []
    for s in S:
       
        ptms=pt_plus(G,s)
        if (ptms > -1):
            TSV.append(s)
           
           
    N = len(TSV)
                 
    for i in range(N):
           
        for j in range(i+1,N):
            L = len(list(set(TSV[i]) & set(TSV[j])))
               
            if L == k-1:
                TSN = set(TSV[j]) - (set(TSV[i]) & set(TSV[j]))
                for m in TSN:
                    for q in set(TSV[i])- (set(TSV[i]) & set(TSV[j])):
                        if m in G.neighbors(q):
                            TSE.append((TSV[i],TSV[j]))
   
   
    TSG = Graph([TSV,TSE],multiedges=False)
    
    return TSG

def psd_TSgraph(G,k):
    ord=G.order()
    V = G.vertices()
    S = Subsets(V,k)
    TSV = []
    TSE = []
    ptm = -1
    TSN = []
    for s in S:
       
        ptms=pt_plus(G,s)
        if (ptms > -1):
            TSV.append(s)
           
           
    N = len(TSV)
                 
    for i in range(N):
           
        for j in range(i+1,N):
            L = len(list(set(TSV[i]) & set(TSV[j])))
               
            if L == k-1:
                TSN = set(TSV[j]) - (set(TSV[i]) & set(TSV[j]))
                TSM = set(TSV[i]) - (set(TSV[i]) & set(TSV[j]))
               
                for m in TSN:
                    for q in TSM:
                        if m in G.neighbors(q):
                            TSE.append((TSV[i],TSV[j]))
                            
   
    TSG = Graph([TSV,TSE],multiedges=False)
    
    return TSG

def std_TSgraph(G,k):
    ord=G.order()
    V = G.vertices()
    S = Subsets(V,k)
    TSV = []
    TSE = []
    ptm = -1
    TSN = []
    for s in S:
       
        ptms=ptz(G,s)
        if (ptms > -1):
            TSV.append(s)
           
           
    N = len(TSV)
                 
    for i in range(N):
           
        for j in range(i+1,N):
            L = len(list(set(TSV[i]) & set(TSV[j])))
               
            if L == k-1:
                TSN = set(TSV[j]) - (set(TSV[i]) & set(TSV[j]))
                TSM = set(TSV[i]) - (set(TSV[i]) & set(TSV[j]))
               
                for m in TSN:
                    for q in TSM:
                        if m in G.neighbors(q):
                            TSE.append((TSV[i],TSV[j]))
                            
   
    TSG = Graph([TSV,TSE],multiedges=False)
    
    return TSG
