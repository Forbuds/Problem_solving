2차원 리스트 원소 포함 여부
#lock에 0이 존재하지 않는지?
if all(0 not in l for l in lock):
        return True

#lock에 0이 하나라도 존재하는지?
if any(0 in l for l in lock):
        return True