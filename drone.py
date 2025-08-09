#import time module to work with time within the program
import time

#variable to hold drones state
state = "ready"

#variable to control program loop
running = True

while running:

#---READY
    if state == "ready":

        print(f"Drone ready. \nEnter 'Takeoff' to take flight.\nEnter 'Off' to turn off drone.")

        user_input = input(": ").lower()

        #TURN OFF DRONE
        if user_input == "off":
            print("Drone powering off...")
            time.sleep(1)
            running = False

        elif user_input == "takeoff":
            print("\nTransitioning to 'Takeoff' state...")
            
            #STATE CHANGE
            state = "taking_off"

#---TAKING OFF    
    elif state == "taking_off":
        print("\nDrone is taking off...")

        #COUNTS INCREASE IN ALTITUDE
        for i in range(3, 0, -1):
            print(f"Altitude:{4-i} meters")
            time.sleep(1)

        #STATE CHANGE
        state = "hovering"

#---HOVERING
    elif state == "hovering":

        print("\nThe drone is hovering...")
        print("\nEnter 'Land' to end flight")
        user_input = input(": ").lower()

        if user_input == "land":
            print("\nThe drone is preparing to land...")
            
            #STATE CHANGE
            state = "landing"

#---LANDING
    elif state == "landing":
        print("\nDrone is landing...")

        #COUNTS DECREASE IN ALTITUDE
        for i in range(3, -1, -1):
            print(f"Altitude: {i} meters")
            time.sleep(1)

        print("\nThe drone has landed...\n")

        #STATE CHANGE
        state = "ready"