class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # try to go from left to right, keep stack of asteroids encountered so far that survived:
        # for each asteroid, check if it collides with previous ones; if yes, pop until no more collisions; if it survives, add to stack
        
        survived = [asteroids[0]]
        for asteroid in asteroids[1:]:
            add_to_stack = True
            while asteroid < 0 and len(survived) > 0 and survived[-1] > 0: # collision
                if abs(asteroid) > survived[-1]: # current destroys previous
                    survived.pop()
                elif abs(asteroid) == survived[-1]: # both are destroyed
                    survived.pop()
                    add_to_stack = False
                    break
                else:
                    add_to_stack = False
                    break
            if add_to_stack:
                survived.append(asteroid)
        
        return survived