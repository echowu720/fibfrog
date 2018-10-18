def solution(A):
    
    class Recorder:
        def __init__(self, pos, jump):
            self.position = pos
            self.jumps = jump
            return
        
    size = len(A) # the position of the destination
    
    # initialize fibonacci
    fib = [0, 1]
    while (1):
        tmp1 = fib[len(fib)-1]
        tmp2 = fib[len(fib)-2]
        
        fib.append(tmp1+tmp2)
        
        # if one of fib is greater than length of array then stop extending fib list
        if tmp1+tmp2 > size:
            break;
    fib.reverse()
    
    queue = []
    reached_position = [0]*size # initialize with 0 for recording which position has been visited by fib
    queue.append(Recorder(-1,0)) # the origin with the position of -1 and jumps of 0
    
    while len(queue)!=0:
        current_pos = queue[0].position
        current_jumps = queue[0].jumps
        queue.pop(0)
        
        for i in fib:
            next_position = current_pos + i
            if next_position == size:
                return current_jumps + 1
                
            # three cases
            # 1. jump over the destination
            # 2. jump to the position without leaf
            # 3. the next position has been reached by the previous fib number
            elif next_position > size or A[next_position] == 0 or reached_position[next_position] == 1:
                continue
            
            queue.append(Recorder(next_position, current_jumps+1))
            reached_position[next_position] = 1 # mark as visited
    return -1
    
    
    pass