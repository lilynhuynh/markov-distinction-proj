"""
    Description:

    Dependencies:

    Author: Lily Huynh
"""

# Import dependencies
import numpy as np
import imageio as img

class BossFight: # Create class for fight sequence
    transition_matrices = {
        "phase_1" : {
            "slinky_smash" : {"slinky_smash": 0.5, "yucky_breath" : 0.3, "boing_jump" : 0.2},
            "yucky_breath" : {"slinky_smash": 0.4, "yucky_breath" : 0.1, "boing_jump" : 0.5},
            "boing_jump" : {"slinky_smash": 0.1, "yucky_breath" : 0.6, "boing_jump" : 0.3}
        },
        "phase_2" : {
            "extended_chomp" : {"extended_chomp" : 0.3, "tail_whip" : 0.5, "barrel_roll" : 0.2},
            "tail_whip": {"extended_chomp" : 0.1, "tail_whip" : 0.5, "barrel_roll" : 0.4},
            "barrel_roll" : {"extended_chomp" : 0.3, "tail_whip" : 0.3, "barrel_roll" : 0.4}
        },
        "phase_3" : {
            "hot_dog" : {"hot_dog" : 0.7, "plane_dog": 0.2, "dancing_hot_dog" : 0.1},
            "plane_dog" : {"hot_dog" : 0.1, "plane_dog": 0.3, "dancing_hot_dog" : 0.6},
            "dancing_hot_dog": {"hot_dog" : 0.2, "plane_dog": 0.6, "dancing_hot_dog" : 0.2}
        }
    }

    def generate_full_fight(self):
        frames = np.vstack([
            img.imread("assets/start.gif"),
            img.imread("assets/phase1_title.gif"),
            img.imread("assets/phase1_attack.gif"),
            img.imread("assets/phase2_title.gif"),
            img.imread("assets/phase2_attack.gif"),
            img.imread("assets/phase3_title.gif"),
            img.imread("assets/phase3_attack.gif"),
            img.imread("assets/knockout.gif")
        ])

        img.imwrite("examples/weiner_dog_markov_fight.gif", frames)

class WeinerDog: # Create class for WeinerDog based on the phase
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.attacks = list(transition_matrix.keys())

    def get_next_attack(self, current_attack):
        """
            Decides which attack to choose based on current attack

            Args:
            - current_attack (str) - current attack that is being done
        """
        return np.random.choice(
            self.attacks,
            p=[self.transition_matrix[current_attack][next_attack] for next_attack in self.attacks]
        )
    
    def create_attack_sequence(self, current_attack="slinky_smash", sequence_length=10):
        """
            Generate a attack sequence based on the given transition matrix
            for the phase

            Args:
            - current_attack (str) - pre-set to "slinky smash"
            - sequence_length (int) - pre-set to 10
        """
        attack_sequence = []

        while len(attack_sequence) < sequence_length:
            next_attack = self.get_next_attack(current_attack)
            attack_sequence.append(next_attack)
            current_attack = next_attack

        return attack_sequence
    
    def generate_phase_sequence(self, attack_sequence, phase_num):
        animated_images = []
        for attack in attack_sequence:
            image_path = str("assets/" + attack + ".gif")
            animated_images.append(img.imread(image_path))
        img.mimsave(str("assets/phase" + phase_num + "_attack.gif"), animated_images)
