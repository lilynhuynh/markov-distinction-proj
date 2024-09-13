"""
    Description:

    Dependencies:

    Author: Lily Huynh
"""

# Import dependencies
import numpy as np



class BossFight: # Create class for fight sequence
    transition_matrices = {
        "phase_1" : {
            "slinky_smash" : {"slinky_smash": 0.5, "yucky_breath" : 0.3, "boing_jump" : 0.2},
            "yucky_breath" : {"slinky_smash": 0.4, "yucky_breath" : 0.1, "boing_jump" : 0.5},
            "boing_jump" : {"slinky_smash": 0.1, "yucky_breath" : 0.6, "boing_jump" : 0.3}
        },
        "phase_2" : {
            "extended_chomp" : {"extended_chomp" : 0.3, "squeeze_attack" : 0.5, "barrel_roll" : 0.2},
            "squeeze_attack": {"extended_chomp" : 0.1, "squeeze_attack" : 0.5, "barrel_roll" : 0.4},
            "barrel_roll" : {"extended_chomp" : 0.3, "squeeze_attack" : 0.3, "barrel_roll" : 0.4}
        },
        "phase_3" : {
            "hot_dog" : {"hot_dog" : 0.7, "plane_dog": 0.2, "dancing_hot_dog" : 0.1},
            "plane_dog" : {"hot_dog" : 0.1, "plane_dog": 0.3, "dancing_hot_dog" : 0.6},
            "dancing_hot_dog": {"hot_dog" : 0.2, "plane_dog": 0.6, "dancing_hot_dog" : 0.2}
        }
    }

class WeinerDog: # Create class for WeinerDog based on the phase
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.attacks = list(transition_matrix.keys())

    def get_next_attack(self, current_attack):
        """
            Decides which attack to choose based on current attack

            Args: current_attack (str) - current attack that is being done
        """
        return np.random.choice(
            self.attacks,
            p=[self.transition_matrix[current_attack][next_attack] for next_attack in self.attacks]
        )