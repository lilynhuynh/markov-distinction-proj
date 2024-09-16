"""
    Description:

    Dependencies:

    Author: Lily Huynh
"""

# Import dependencies
import numpy as np
import imageio.v2 as img

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

    def get_fights(self):
        for phase, phase_attacks in self.transition_matrices.items():
            weiner_dog = WeinerDog(phase_attacks)
            attack_sequence = weiner_dog.create_attack_sequence(list(phase_attacks)[0])
            weiner_dog.generate_phase_sequence_animation(attack_sequence, phase)

    def generate_full_fight(self):
        gif_list = [
            img.get_reader("markov-distinction-proj/assets/start.gif"),
            img.get_reader("markov-distinction-proj/assets/phase1_title.gif"),
            img.get_reader("markov-distinction-proj/assets/phase_1_attack.gif"),
            img.get_reader("markov-distinction-proj/assets/phase2_title.gif"),
            img.get_reader("markov-distinction-proj/assets/phase_2_attack.gif"),
            img.get_reader("markov-distinction-proj/assets/phase3_title.gif"),
            img.get_reader("markov-distinction-proj/assets/phase_3_attack.gif"),
            img.get_reader("markov-distinction-proj/assets/knockout.gif")
        ]
        final_gif = img.get_writer("markov-distinction-proj/examples/weiner_dog_markov_fight.gif")

        for gif in gif_list:
            for frame in gif:
                final_gif.append_data(frame)

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
    
    def create_attack_sequence(self, current_attack, sequence_length=5):
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
    
    def generate_phase_sequence_animation(self, attack_sequence, phase_num):
        animated_images = []
        for attack in attack_sequence:
            image_path = str("markov-distinction-proj/assets/" + attack + ".gif")
            animated_images.append(img.get_reader(image_path))

        phase_attack_sequence = img.get_writer("markov-distinction-proj/assets/" + phase_num + "_attack.gif")
        
        print("GENERATING ATTACKS")
        for gif in animated_images:
            for frame in gif:
                phase_attack_sequence.append_data(frame)
            print("GENERATED ONE ATTACK")

def main():
    boss = BossFight()

    test = boss.get_fights()
    print(test)

    boss.generate_full_fight()

if __name__ == "__main__":
    main()