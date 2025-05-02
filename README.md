# CPSC-Projects 🎓
A collection of computer science projects completed during my undergraduate coursework. This repository showcases various assignments and personal projects developed to enhance my understanding of programming concepts and problem-solving skills.
 
## 📁 Project Overview
- **ARM and C Projects**: Low-level programming exercises in ARM assembly and C, covering topics like embedded systems startup code, memory-mapped I/O, and microcontroller interfacing.
  
- BeginnerCode: Introductory exercises focusing on fundamental programming constructs such as loops, conditionals, and basic data structures.

- CandyCrush: A simplified version of the popular Candy Crush game, emphasizing array manipulation and game logic implementation.

- Guitar: A virtual guitar simulator that demonstrates sound synthesis and real-time user interaction.

- Hangman: The classic Hangman game implemented with a focus on string processing and user input handling.

- KAREL: Solutions and challenges using the Karel the Robot programming environment to teach algorithmic thinking.

- Movie: A movie database application that allows users to add, search, and manage movie entries, highlighting object-oriented programming principles.

- Pig Game: An implementation of the Pig dice game, emphasizing turn-based logic and random number generation.

## 🛠 Technologies Used
- Languages: Python, C, ARM Assembly

- Concepts: Object-Oriented Programming, Data Structures, Algorithms, Game Development, File I/O

## 🚀 Getting Started
### Clone the repository:
```
git clone https://github.com/KeatonBuddy/CPSC-Projects.git
```
### Navigate to a project directory:
```
cd CPSC-Projects/Hangman
```
### Run the project:
- ARM assembly examples
Assemble and link (ARM toolchain required):
```
arm-none-eabi-as hello_world.s -o hello_world.o
arm-none-eabi-ld hello_world.o -o hello_world.elf
qemu-arm hello_world.elf
```

- For Python projects:
```
python hangman.py
```
- For C projects:

```
gcc main.c -o main
./main
```
(Ensure you have the necessary compilers/interpreters installed on your system.)

## 📚 Educational Purpose
These projects were developed as part of my learning journey in computer science. They serve as practical applications of theoretical concepts covered in coursework and self-study.

## 🤝 Contributing
While this repository primarily serves as a personal archive of academic projects, feedback and suggestions are welcome. Feel free to fork the repository and submit pull requests for improvements or enhancements.
