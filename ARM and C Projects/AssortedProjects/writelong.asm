		define(fd_r, w19)
		define(i_r, x20)
		define(nwritten_r, x21)
		define(buf_base_r, x22)

		buf_size = 8
		alloc = -(16 + buf_size) & -16
		dealloc = -alloc
		buf_s = 16
		upper_limit = 100
		AT_FDCWD = -100

fname:	.string "output.txt"
fmt1:	.string "Error opening file: %s\nAborting.\n"
fmt2:	.string "Error writing to file. Aborting.\n"
fmt3: 	.string "%d"


		.balign 4
		.global main
main:	stp		x29, x30, [sp, alloc]!
		mov 	x29, sp
		//open file 
		//int fd = openat(int dirfd, const char *pathname, int flags, mode_t mode )
		mov 	w0, AT_FDCWD 				// 1st arg (dirfd, -100 means current directory)
		ldr 	x1, =fname					// 2nd arg (pathname, "output.bin") 			
		mov  	w2, 01 | 0100 | 01000 		// 3rd arg (flags, 01 means write-only, 0100 means create file if it doesn't exist, 01000 means truncate an existing file)
		mov	 	w3, 0666					// 4th arg (mode, 0666 means rw for all)
		mov 	x8, 56 						// openat I/O request
		svc 	0 							// call system function
		mov 	fd_r, w0 					// record file decriptor

		// error check
		cmp 	fd_r, 0 
		b.ge 	openok

		ldr 	x0, =fmt1
		ldr 	x1, =fname
		bl 		printf
		mov 	w0, -1
		b 		exit

openok: add 	buf_base_r, x29, buf_s 		// calculate buf base
		mov 	i_r, 0
		b 		test

// 		snprintf (buff, sizeof(buf), "%d", n), convert int n to string 
// 		gcvt (float value, int ndigits, char *buf)， convert float to string
top: 	
		
		//scvtf 	d0, i_r
		//mov		w0, buf_size
		//mov 	x1, buf_base_r
		//bl 		gcvt
		mov 	w3, i_r
		mov	 	x0, buf_base_r
		mov		x1, buf_size
		ldr 	x2, =fmt3
		bl 		snprintf

		//str 	i_r, [buf_base_r] 			// copy i into buf
		//write file
		//long n_written = write(int fd, void *buf, unsigned long n);
		mov 	w0, fd_r 					// 1st arg (fd)
		mov		x1, buf_base_r 				// 2nd arg (buf)
		mov		w2, buf_size 				// 3rd arg (BUFSIZE)
		mov 	x8, 64 						// write I/O request
		svc 	0 							// call system function
		mov		nwritten_r, x0 				// record nwritten

		// error check
		cmp 	nwritten_r, buf_size 		// if nwritten == 8
		b.eq 	endif 						

		ldr 	x0, =fmt2
		bl 		printf
		b 		exit

		// bottom of the loop
endif:	add 	i_r, i_r, 1
test:	cmp 	i_r, upper_limit

		b.lt 	top
		
		// close  the file
		mov		w0, fd_r
		mov		x8, 57
		svc 	0

		mov		w0, 0
exit:  	ldp		x29, x30, [sp], dealloc
		ret
