# Markov Distinction Project
## Overview
This project was developed for CSCI3725 Computation Creativity to show our knowledge of creating a computational-creative system using Markov techniques learned in class.

My program was inspired by the game "[_Cuphead_](https://store.steampowered.com/app/268910/Cuphead/)" by Studio MDHR where a boss will have pre-set attacks that become more difficult as the phases increase. Each boss will has a total of 3 phases. I represented this idea with my boss character, **Weiner Dog**. **Weiner Dog** has three phases and its respective attacks:

#### Phase 1 - Normal
- **Slinky Smash**: His body extends and smashes to the left
- **Yucky Breath**: Like any doggy, they've got a deadly stench!
- **Boing Jump**: He bounces like a bouncy ball and smashes on impact

#### Phase 2 - Twisty
- **Extended Chomp**: He twists and does a deadly chomp
- **Tail Whip**: His tail extends and creates a powerful slash
- **Barrel Roll**: Watch out, he creates a donut shape and barrels anyone in his way

#### Phase 3 - Hot Dog
- **Hot Dog**: His hot dog buns become mustard and ketchup blasters
- **Plane Dog**: His recon plane comes in and sends a flurry of bullets
- **Dancing Hot Dog**: He turns on his jams and sends a shockwave with each beat bounce

This program uses **numpy** and **imageio** to compute the randomized probabilities of each attack and generate the gifs respectively. Every **Weiner Dog** animation was hand-drawn by myself.

### Version Control
This project uses Git and GitHub for tracking commits and managing project
development. Please see the GitHub repository for the full development of the application:
https://github.com/lilynhuynh/markov-distinction-proj

## Setup
> [!NOTE]
> Please install **numpy** and **imageio** prior to running the program. The markov operations and gif generations will not work properly if not installed beforehand.

## Usage
This program can be accessed by cloning the repository from the provided GitHub link above and running the main.py

> [!CAUTION]
> Please refer to the **Setup** section before running the program.

## Limitations
During each full fight sequence generation into a gif in the examples folder, it takes a while due to the number of frames it is reading and writing.

## Development
### Personal Impact of System
This system was personally meaningful to me because I have always loved playing and watching people play games. Recently, I have grown an interest in game development, in terms of creating the UI and character creation, since I have always enjoyed drawing and animating simple things. Thus, this project, allowed me to combine my interests with my profession and create a super cool Markov chain phase attack sequence for my character **Weiner Dog**! One, I love animals, and I made my character a dachshund because it had so much potential, especially in elasticity. Two, dachshunds are also known as "weiner dogs" or as I like to say, a "hot dog dawg". Thus, his final phase, **HOT DOG**, is his final form and I used a lot of memes related to dachshunds and hot dogs (specifically for [Plane Dog](https://youtu.be/D-UmfqFjpl0?si=tV1IgDk7Fo45ScDk) and [Dancing Hot Dog](https://youtu.be/k1Aq8Sb_aIw?si=PxlsFVyuWQ1yoROY))!

### Challenges
An important personal challenge I faced as a computer scientists while doing this project was relearning Python. As a computer scientist, it is important that we are versatile and knowledgeable of the variety of coding languages available, especially a major one like Python. I mainly coded in Java these past few years so relearning how to code in Python was a bit difficult as I sometimes end my statements in semicolons.

However, something that pushed me outside my comfort zone was learning how to use **imageio** since I wanted to create a flawless final animation from the concatenated gifs. Speaking of animations, it has also been a while since I have drawn and done animations so I was constantly looking up frame references to really encompass the fluid or quick movements I wanted in my **Weiner Dog**'s attacks! Also, since he had a total of three phases, that meant I had to do triple the transition matrices we originally did in class, thus, it was different to configure a system that operated multiple generated sequences based on each phases' transition matrices.

Some next steps for me personally are:
1. Incorporating player input to have their own set of moves to fight the boss **Weiner Dog**! (e.g. block, strike, and dodge)
2. A health bar for the boss **Weiner Dog** and based on the player inputs, the phase sequence will end if they lower the health bar to a certain amount.
3. Rather than based on the boss' current attack to generate the next attack, it will use the player's previous inputted move to choose the next attack.
4. (opt) Animate in a player character and background.

### Discussion - Is this system creative?
In my personal opinion, _creative_ is a very broad term 
- Discuss whether you believe the system is creative (why or why not)

## Acknowledgements
- Credits to sources and colleagues
- Inspired by Cuphead
    - Studied slinky tricks
    - Researched dachshund dog memes