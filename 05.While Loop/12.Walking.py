command = input()                                       
steps_counter = 0                                       
                                                        
while command != 'Going home':                          
    current_command = int(command)                      
    steps_counter += current_command                    
                                                        
    if steps_counter >= 10000:                          
        break                                           
    command = input()                                   
                                                        
if command == 'Going home':                             
    command = int(input())                              
    steps_counter += command                            
                                                        
if steps_counter < 10000:                               
    steps_needed = 10000 - steps_counter                
    print(f'{steps_needed} more steps to reach goal.')  
else:                                                   
    steps_over = steps_counter - 10000                  
    print('Goal reached! Good job!')                    
    print(f'{steps_over} steps over the goal!')
