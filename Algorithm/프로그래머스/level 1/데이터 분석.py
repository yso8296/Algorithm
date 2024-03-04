dic = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}

def solution(datas, ext, val_ext, sort_by):
    array = []
    for data in datas:
        if int(data[dic[ext]]) < int(val_ext):
            array.append(data)
    array.sort(key = lambda x : x[dic[sort_by]])
    
    return array
    
            
            
            
            