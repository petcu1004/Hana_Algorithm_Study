#[WIP]

def solution(genres, plays):
    answer = []
    d=dict()
    for i in range(len(genres)):
        if genres[i] in d:
            d[genres[i]].append(plays[i])
        else:
            d[genres[i]]=[plays[i]]
    # print(d)
    # print(max(d.keys()))
    # print(max(d.values()))
    # print(sorted(d.values()))
    # print(sorted(plays, reverse=1))
    
    dd=dict()
    c=list()
    for i in range(len(genres)):
        dd[plays[i]]=genres[i]
    for i in sorted(plays, reverse=1):
        c.append(dd.get(i))
        # print(dd.get(i))
        # print(c)
    # print(list(set(c)))
        
        
    # print(d.get(max(d.keys())))
    # for i in range(len(plays)):
    
    # print(type(d.get(p)))
    c=list(set(c))
    cnt=0
    for i in range(len(c)):
        p=max(d.keys())
        d.get(p).sort()
        for j in range(len(d.get(p))-1, -1, -1):
            if cnt==2:
                del d[p]
                # cnt=0
                print(c)
                c.remove(p)
                
            print(plays.index(d.get(p)[j]))
            cnt+=1
            # if cnt==2:
            #     del d[p]
            #     # cnt=0
            #     print(c)
            #     c.remove(p)
            #     break
            #     # print(c)

            
    
        
    
    
    return answer