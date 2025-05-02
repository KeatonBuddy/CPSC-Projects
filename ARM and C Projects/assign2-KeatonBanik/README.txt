-Main Fucntion is in assign2a.s (without macros) and assign2b.asm / assign2b.s (with macros)

COMPILATION INSTRUCTIONS:

FOR assign2a.s (without macros):
	- use gcc compiler in the following format -> gcc assign2a.s -g -o assign2a
	- use gdb compiler in the following format -> gdb assign2a
	- run the main fucntion by typing "r" and then pressing the "enter" key and following the prompts in the command line

FOR assign2b.asm (with macros):
	- use m4 to convert assign2b.asm to assign2b.s in the following format -> m4 assign2b.asm > assign2b.s
	- use gcc compiler in the following format -> gcc assign2b.s -g -o assign2b
	- use gdb compiler in the following format -> gdb assign2b
	- run the main fucntion by typing "r" and then pressing the "enter" key and following the prompts in the command line

There are two script files, assign2a.script and assign2b.script to show all error detection and what the function outputs to the user.

P.S. Thank you for the extension :D