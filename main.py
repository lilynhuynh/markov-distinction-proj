"""
    Description: This project generates 5 different Weiner Dog fight sequences as gif files
    (pre-saved files already in 'examples' folder, but will overwrite for each run). Each fight
    sequence in each phase, total of 3 phases, are generated based on randomized probabilities
    in their respective transition matrices.

    Dependencies: numpy, imageio

    Author: Lily Huynh
    Last Updated: September 16th, 2024
"""

# Dependencies
import numpy as np
import imageio.v2 as img

class BossFight:
    """
    Parent class that initializes all transition matrices for each of the phases
    and creates a new WeinerDog instance for each phase. After each phase
    fight sequence has been generated as a new gif file, it concatenates all
    title screens (start, phase 1, phase 2, phase 3, knockout) with its respective
    phase attack sequence in between each phase title screen.

    Methods:
    -------
    get_fights():
        Generates the attack seqeuence and phase animation for each phase.

    generate_full_fight:
        Generates final attack sequence with title screens and generated attack
        sequences as a new gif file in the 'examples' folder.
    """

    # Total of 3 transition matrices for each phase
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
        """
        Creates a WeinerDog instance and generates each phases' fights.
        It always initializes the first attack in each phase to be the first
        attack in the phase attack dictionary.

        Parameters:
        self: The instance of the class containing this method.

        Returns:
        None, but generates new gif file for each phase attack sequence.
        """
        print("Starting fight generation...")
        for phase, phase_attacks in self.transition_matrices.items():
            weiner_dog = WeinerDog(phase_attacks)
            attack_sequence = weiner_dog.create_attack_sequence(list(phase_attacks)[0])
            weiner_dog.generate_phase_sequence_animation(attack_sequence, phase)
            print(phase, "generated...")

    def generate_full_fight(self, file_name):
        """
        After each phase attack gif is generated, it creates a full fight
        sequence gif and saves it into the examples folder.
        NOTE - this function takes a couple of seconds due to it handling
        each frame for every sequence plus the title screens.

        Parameters:
        self: The instance of the class containing this method.
        file_name: given file name to distinguish each fight generated.

        Returns:
        None, but generates a new gif file for the full fight sequence in the
        examples folder.
        """
        gif_list = [
            img.get_reader("assets/start.gif"),
            img.get_reader("assets/phase1_title.gif"),
            img.get_reader("assets/phase_1_attack.gif"),
            img.get_reader("assets/phase2_title.gif"),
            img.get_reader("assets/phase_2_attack.gif"),
            img.get_reader("assets/phase3_title.gif"),
            img.get_reader("assets/phase_3_attack.gif"),
            img.get_reader("assets/knockout.gif")
        ]
        final_gif = img.get_writer("examples/" + file_name + ".gif")

        print("Please wait as we generate your Weiner Dog fight...")
        for gif in gif_list:
            for frame in gif:
                final_gif.append_data(frame)
        print("Weiner Dog fight generated!!! Access complete gif in 'examples'")


class WeinerDog:
    """
    Child class to BossFight that takes the given transition matrix and generates
    a fight sequence for the given phase. It uses markov chain technique to
    generate the next attack based on the given transition matrix attack probabilities.
    Each fight sequence for the phase is of length 5 for optimization and saved
    as '{phase_num}_attack.gif' in the 'assets' folder.

    Attributes:
    ----------
    transition_matrix : dict
        A dictionary where each key represents the each attack
        available for that phase, and the values represent the list
        of possible attacks for that phase and their probabilities.

    Methods:
    -------
    __init__(self, transition_matrix):
        Initializes the WeinerDog with the given phase transition matrix and saves
        the different attacks as a list.

    get_next_attack():
        Generates the next attack based on the current attack given using numpy
        for a randomized selection based on the probabilities of the next attack
        using markov chain technique.

    create_attack_sequence():
        Creates and returns an array of the generated attacks for that phase.

    generate_phase_sequence_animation():
        Generates a new gif file with the concatenated list of attacks generated
        previously and saves that phase's attack sequence in the 'assets' folder.
    """
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.attacks = list(transition_matrix.keys())

    def get_next_attack(self, current_attack):
        """
        Decides which attack to choose based on the current attack based
        on the transition matrix.

        Parameters:
        self: The instance of the class containing this method.
        current_attack: current_attack (str) being done.

        Returns:
        The next attack chosen based on the transition matrix probabilities
        from the previous attack.
        """
        return np.random.choice(
            self.attacks,
            p=[self.transition_matrix[current_attack][next_attack] for next_attack in self.attacks]
        )
    
    def create_attack_sequence(self, current_attack, sequence_length=5):
        """
        Generates an attack sequence by calling the get_next_attack function
        that is the length of sequence_length (set as 5 for optimization)
        and starts on the current_attack given. The current_attack is always
        set as the first attack in that phase's transition matrix.

        Parameters:
        self: The instance of the class containing this method.
        current_attack (str): pre-set as the first attack of phase's transition matrix.
        sequence_length (int): pre-set to 5.

        Returns:
        An array of the generated attacks for that phase.
        """
        attack_sequence = []

        while len(attack_sequence) < sequence_length:
            next_attack = self.get_next_attack(current_attack)
            attack_sequence.append(next_attack)
            current_attack = next_attack

        return attack_sequence
    
    def generate_phase_sequence_animation(self, attack_sequence, phase_num):
        """
        Concatenates the listed attacks listed in the given attack_sequence
        array and generates a new gif file for that phase's attack sequence
        and saves it in the assets folder as "{phase_num}_attack.gif"

        Parameters:
        self: The instance of the class containing this method.
        attack_sequence: the given attack sequence array to concatenate into final gif.
        phase_num: current phase being generated.

        Returns:
        None, but generates a new gif file for the full fight sequence of that
        phase into the assets folder.
        """
        animated_images = []
        for attack in attack_sequence:
            image_path = str("assets/" + attack + ".gif")
            animated_images.append(img.get_reader(image_path))

        phase_attack_sequence = img.get_writer("assets/" + phase_num + "_attack.gif")
        
        for gif in animated_images:
            for frame in gif:
                phase_attack_sequence.append_data(frame)


def main():
    """
    Main function that calls the parent class 'BossFight' and generates
    5 different examples of a WeinerDog fight sequence from start to knockout.
    """
    boss = BossFight()

    # Example 1
    boss.get_fights()
    boss.generate_full_fight("weiner_dog_markov_fight_1")

    # Example 2
    boss.get_fights()
    boss.generate_full_fight("weiner_dog_markov_fight_2")

    # Example 3
    boss.get_fights()
    boss.generate_full_fight("weiner_dog_markov_fight_3")

    # Example 4
    boss.get_fights()
    boss.generate_full_fight("weiner_dog_markov_fight_4")

    # Example 5
    boss.get_fights()
    boss.generate_full_fight("weiner_dog_markov_fight_5")

if __name__ == "__main__":
    main()