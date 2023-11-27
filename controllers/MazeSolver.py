from controller import Robot
from controller import DistanceSensor

def Wall_follower(epuck):

    timestep = int(epuck.getBasicTimeStep())
    max_speed = 6.0
    
    left_motor = epuck.getDevice('motor_1')
    right_motor = epuck.getDevice('motor_2')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(epuck.getDevice(sensor_name))
        prox_sensors[ind].enable(timestep)
        
        
        
    while epuck.step(timestep) != -1:
        #for ind in range(8):
            #print ("ind: {}, val: {}".format(ind, prox_sensors[ind].getValue()))
            
        left_wall = prox_sensors[5].getValue() > 0.80
        front_wall = prox_sensors[7].getValue() > 0.80
          
        left_speed = max_speed
        right_speed = max_speed 
          
        if front_wall:
            # print("Turn right in place")  
            left_speed = max_speed
            right_speed = -max_speed
             
        else:
            if left_wall:
                # print("Drive Forward")
                left_speed = max_speed
                right_speed = max_speed   
                 
            else:
                # print("Turn Left")
                left_speed = max_speed/8
                right_speed = max_speed  
               
                      
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

                     
if __name__ == "__main__":

    epuck = Robot()
    Wall_follower(epuck)