/*Project part 1 for Keaton Banik, Bomberman in C*/

/*Imports*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>


/*Function to log player name, score and time played to the project.log file*/
void logtofile(char const *data, float score, float time){
  FILE* outfile;
  outfile = fopen("project.log", "a+");
  fprintf(outfile,"%s %.2f %.2f\n", data, score, time);
  fclose(outfile);
}


/*SORTING FUNCTIONS*/

/*Swap function (int) for bubble sort*/
void swapInt (int *x, int *y){
  int temp = *x;
  *x = *y;
  *y = temp;
}


/*Swap function (floats) for bubble sort*/
void swapFloat(float *x, float *y){
  float temp = *x;
  *x = *y;
  *y = temp;
}
/*Main bubblesort function*/
void bubblesort(int r, float ftable[r], int itable[r]){

  for(int i = 0; i < r - 1; i++){
    for(int j = 0; j < r-i-1;j++){
      if(ftable[j] < ftable[j+1]){ //Checks if index j is less than j+1 (next index), if so, swap
	swapFloat(&ftable[j], &ftable[j+1]);
	swapInt(&itable[j], &itable[j+1]); //Keeps track of indexs for printing
      }
    }
  }
}


/*Checks if File Exists with name 'program.log'*/
int fileExists(){
  FILE *file;
  if (file = fopen("project.log", "r")){
    fclose(file);
    return 0;
  }
  else{
    return 1;
  }
}

/*Function to display top 'n' scores to the console*/
void displayTopScores(int n){
  int rows;
  char ch;
  FILE *inFile;
  int num;

  if(fileExists() == 1){
    printf("CURRENTLY NO LEADERBOARD \n \n");
    return;
  }
  
  inFile = fopen("project.log", "r");

  char temp[50];
  /*determines number of rows in project.log file (# of rows = # of scores)*/
  while(!feof(inFile)){
    ch = fgetc(inFile);
    if(ch == '\n'){
      rows++;
    }
  }
  fclose(inFile);

  
  inFile = fopen("project.log", "r");
  /*Initalizes Tables for Scores and times out of # of rows in project.log*/
  float scoreTable[rows];
  float timeTable[rows];
  int iTable[rows];

  /*inputs data from project.log into scoreTable and timeTable*/
  for (int i = 0; i <rows ; i++){
    fscanf(inFile, "%s", temp);
    
    fscanf(inFile, "%s", temp);
    scoreTable[i] = strtof(temp,NULL); // input index i score into scoreTable[i]

    fscanf(inFile, "%s", temp);
    timeTable[i] = strtof(temp,NULL);// input index i time into timeTable[i]
    iTable[i] = i;
  }
  fclose(inFile);

  /*Uses bubblesort functions to sort scores in scoreTable[] and iTable (index table)*/
  bubblesort(rows, scoreTable, iTable);
  
  /*Checks if requested n top scores is greater than rows in .log
    If so, output # of rows Top scores rather than n top scores*/
  if(n > rows){
    num = rows;
  }
  else{
    num = n;
  }
  /*Prints Top score in format: Name-> Score: Time:*/
  printf("Top Scores Are: \n");
  for (int i = 0; i < num; i++){ //Loops through project.log to the iTable[i]'th name
    inFile = fopen("project.log", "r");
    for(int j = 0; j<rows; j++){
      fscanf(inFile, "%s",temp);
      if(j == iTable[i]){
	printf("%s -> ", temp);//outputs name
	break;
      }
      else{
	fscanf(inFile, "%s",temp);
	fscanf(inFile, "%s",temp);
      }
    }
    fclose(inFile);
    printf("Score: %.2f, Time: %.2f \n \n", scoreTable[i],timeTable[iTable[i]]); //Outputs Score and Time

    }
  
}

/*Random Float Function with a max of m and a negative flag*/
float randNum(int m, bool neg){
  if (neg){
    return - (((float)rand()/ (float)(RAND_MAX)) * m);
  }

  else{
    return ((float)rand()/ (float)(RAND_MAX)) * m;
  }

  
}

/*Initalizes table arrays with random numbers (40% +, 40% -) and special characters (20%) and 1 exit tile*/
void initialize(int r, int c, float table[r][c], float out[r][c]){
  srand((time(0)));
  
  for (int i = 0 ; i < r; i++){
    for(int j = 0; j < c; j ++){
      float test = randNum(100, false);
      out[i][j] = 103;
      if( test >=0 && test < 40){//Positive Number
	table[i][j] = randNum(15,false);
      }
      else if (test >= 40 && test < 80){//Negative Number
	table[i][j] = randNum(15, true); 
      }

      else if (test >=80 && test <95){//Double Bomb Range
	table[i][j] = 100;
      }
      else{
	table[i][j] = 106;//Double Score
      }
	 
    }
    
  }

    int randRow = rand() % r;
    int randCol = rand() % c;

    table[randRow][randCol] = 101;//Exit tile
    

}


/*Displays inputed Table, Score, Lives and Bombs remaining*/
void display(int r, int c, float table[r][c], int lives, float score, int bombs){

    for (int i = 0; i < r; i++){
      for (int j = 0; j < c; j++){
	if (table[i][j] == 100){
	  printf("%6.2c    ", '$');
	}
	else if(table[i][j] == 101) {
	  printf("%6.2c    ", '*');
       
	}
	else if(table[i][j] == 103){
	  printf("%6.2c    ", 'X');
	}
	else if(table[i][j] == 104){
	  printf("%6.2c    ", '+');
	}
	else if(table[i][j] == 105){
	  printf("%6.2c    ", '-');
	}
	else if(table[i][j] == 106){
	  printf("%6.2c    ", '#');
	}
	else {
	  printf("%6.2f    ", table[i][j]);
	}
      }
      printf("\n");
    }

    printf("Lives: %d \n", lives);
    printf("Score: %.2f \n", score);
    printf("Bombs: %d \n", bombs);
}
  

/*Changes out[] to reflect user inputed "bomb"*/

void doBomb(int r, int c, float table[r][c], float out[r][c], int x, int y, int radius){
  int temp = radius;//checks for double bomb range

  /*Loops to change (radius) tiles around point x,y in out[] to reflect the data in table[]*/
  for (int i = 0; i < r; i++){
      for (int j = 0; j < c; j++){


	for (int k = temp; k >0; k--){
	  for (int h = temp; h >0; h--){

	    if( i == x || i == x-k || i == x+k){
	      if(j == y || y == j-h|| y == j+h){


		if(table[i][j] == 100){ //X -> $
		  out[i][j] = 100;
		}
		else if(table[i][j] == 101){//X -> *
		  out[i][j] = 101;
		}
		else if(table[i][j] == 106){//X -> #
		  out [i][j] = 106;
		}
	
		else if(table[i][j] > 0){//X -> +
		  out[i][j] = 104;
		}
		else if(table[i][j]<0){//X -> -
		  out[i][j] = 105;
		}

	      }
	    }
	  }
	}

       }
    }
  }

/*Checks if $ tile was uncovered, if so, returns 2^n if n = # of $ uncovered*/
int doubleBombCheck(int r, int c, float table[r][c], float out[r][c]){
  int total = 1;
  int power = 0;
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (out[i][j] == 100 && table[i][j]){
	power++;
      }

    }
  }
  while (power != 0){
    total *= 2;
    power--;
  }
  return total;
}

/*Checks if # tile was uncovered, if so, returns 2^n if n = number of # uncovered*/
int doubleScoreCheck(int r, int c, float table[r][c], float out[r][c]){
  int total = 1;
  int power = 0;
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (out[i][j] == 106 && table[i][j]){
	power++;
      }

    }
  }
  while (power != 0){
    total *= 2;
    power--;
  }
  return total;
}

/*Makes data in already revealed tiles = 0, so that overlapping bombs dont return points*/
void zeroTiles(int r, int c, float table[r][c], float out[r][c]){
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (out[i][j] != 103){
	table[i][j] = 0.0;

      }  

    }
  }

}

/*Prints amount of Negative numbers in the array*/
void numOfNegs(int r, int c, float table[r][c]){
  int negs = 0;
  
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (table[i][j] < 0){
	negs++;

      }

    }
  }

  int total = r*c;
  float percent =100.0 * ( (float)negs/(float)total );
  printf("Total Negative Numbers %d/%d = %.2f% \n", negs, total, percent);

}


/*Function to calculate current revealed score*/
float calcScore(int r, int c, float table[r][c], float out[r][c], int mult){
  float score = 0;
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (out[i][j] == 104 || out[i][j] == 105){ // if out[] is a revealed # (aka not a #, X, $, *) add to score
	score = score + table[i][j];
	
      }
      
    }
  }

  return score * mult;//return score and multiply by current score multiplier
}

/*Checks if game has ended*/
bool checkEnd(int r, int c, float table[r][c], float out[r][c]){
  for (int i = 0; i < r; i++){
    for (int j = 0; j < c; j++){
      if (out[i][j] == 101){
	return true;
      }

    }
  }

  return false;
}



/*Main Function*/
void main(int argc, char * argv[]){

  if(argc != 4){
    printf("INCORRECT AMOUNT OF ARGUMENTS, PLEASE INPUT ./program [name] [rows] [cols] \n");
    exit(2);
  }



  
/*Initialize Variables*/
  int rowSize = atoi(argv[2]);
  int colSize = atoi(argv[3]);
  float score = 0.0;
  int lives = 3;
  int bomb = 3;
  int exitTile = 0;
  bool gameEnd = false;
  int doubleBomb = 1;
  int doubleScore = 1;
  char const *username = argv[1];
  int timeTotal;
  
  /*Initialize Tables*/
  float tableData[rowSize][colSize];
  float tableOut[rowSize][colSize];
  
  bool program = true;
  char input;

  /*Checks if commandline args are within range, if not return error*/
  if (rowSize < 10){
    printf("You have inputed a value outside the range for argument 1! \n");
    exit(0);
  }
  else if(colSize <10){

    printf("You have inputed a value outside the range for argument 2! \n");
    exit(1);
  }

  /*Continue if command line args are within range*/
  else{
    /*While loop for main menu*/
     while(program == true){
       score = 0.0;
       lives = 3;
       bomb = 3;
       exitTile = 0;
       gameEnd = false;
       doubleBomb = 1;
       doubleScore = 1;
       

       printf("~~WELCOME TO BOMBERMAN~~ \n");
       printf("To start the game enter 's' \n");
       printf("To view the leaderboard enter 'l' \n");
       printf("To reset the leaderboard enter 'r' \n");
       printf("To quit the game enter 'q' \n");

       printf("Enter your command: ");
       scanf(" %c", &input);


       printf("\n");
       
       /*If user inputs to quit*/
       if(input == 'q'){
	 printf("Quitting Game. \n");
	 program = false;
       }
       /*If user inputs to see leaderboard*/
       else if (input == 'l'){
	 printf("Displaying Leaderboard \n \n");
	 displayTopScores(10);
       }
       /*if user wants to reset the current leaderboard*/
       else if(input == 'r'){
	 printf("Resetting Leaderboard \n \n");
	 remove("project.log");
       }

       /*If user wants to start the game*/
       else if (input == 's'){

           /*Inilizaing game variables and tables*/
	 time_t start = time(NULL);
	 initialize(rowSize, colSize,tableData,tableOut);
	 display(rowSize, colSize, tableData,lives,score,bomb);
	 numOfNegs(rowSize,colSize, tableData);
	 printf("\n");
	 printf("\n");
	 printf("\n");
	 display(rowSize, colSize,tableOut,lives,score,bomb);

     /*While loop for game*/
	 while (!gameEnd){
	   int xCoords;
	   int yCoords;
	   printf("Enter bomb position between 0-%d for x and 0-%d for y (x,y): ",rowSize-1, colSize-1 );
	   scanf("%d %d", &xCoords, &yCoords);
       /*Checks if coords are valid for size of board*/
	   if (xCoords < 0 || xCoords > rowSize-1){
	     printf("Invalid bomb coordinate for X, try again   \n");
	   }
	 
	   else if (yCoords < 0 || yCoords > colSize-1){
	     printf("Invalid bomb coordinate for Y, try again  \n");
	   }

	   else{
	     /*Checks current score and updates tables on current bomb location and range*/
	     doBomb(rowSize, colSize, tableData, tableOut, xCoords, yCoords, doubleBomb);
	     score = calcScore(rowSize,colSize,tableData, tableOut, doubleScore);
	     doubleBomb = doubleBombCheck(rowSize, colSize, tableData, tableOut);
	     doubleScore = doubleScoreCheck(rowSize, colSize, tableData, tableOut);

	     printf("\n");printf("\n");
          /*Output bonus message/Lives lost message */
	     if(doubleBomb > 1){
	       printf("BOOM! Bomb range increased by %d times for the next bomb! \n", doubleBomb);
	     }

	     if(doubleScore > 1){
	       printf("!!! TIMES %d SCORE MULTIPLIER !!!\n", doubleScore);
	     }

	     if (score < 0){
	       lives--;
	       printf("LIFE LOST, SCORE RESET TO 0 \n");
	     }

	     bomb--;

         /*Display Data and check is game has ended*/
	     display(rowSize, colSize,tableOut,lives,score,bomb);
	     gameEnd = checkEnd(rowSize,colSize,tableData, tableOut);
	     zeroTiles(rowSize,colSize, tableData,tableOut);

	     if( score <0){
	       score =0;
	     }
	     if (lives <= 0){
	       gameEnd = true;
	     }
	     if (bomb <= 0){
	       gameEnd = true;
	     }
	     if (gameEnd){
	       exitTile = 1;
	     }

	   }

       /*Game ended message and reason*/
	   if (gameEnd && lives <= 0){
	     printf("GAME OVER! \nRAN OUT OF LIFES X_X \n");
	   }
	   else if (gameEnd && bomb <= 0){
	     printf("GAME OVER! \nRAN OUT OF BOMBS X_X \n");
	   }
	   else if (gameEnd && exitTile == 1){
	     printf("GAME OVER! \nFOUND EXIT!! \n");
	   }
	 }
     /*Determines Time of game and logs to file the username, score and time of the current game*/
	 time_t end = time(NULL);
	 timeTotal = (end - start);
	 logtofile(username, score, timeTotal);

	     


       }
     }
  }
}
