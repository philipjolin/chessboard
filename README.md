### Chessboard Evaluation with the Relative Value System

This program will assess (numerically) who is winning in a game of chess, using the chess piece relative value system. 

Sample input and output below:
<br />
<br />
<i>
Please type 8 characters for the 8th row of the chessboard: RNBQKBNR <br />
Please type 8 characters for the 7th row of the chessboard: PPPPPPPP <br />
Please type 8 characters for the 6th row of the chessboard: -------- <br />
Please type 8 characters for the 5th row of the chessboard: -------- <br />
Please type 8 characters for the 4th row of the chessboard: -------- <br />
Please type 8 characters for the 3rd row of the chessboard: -------- <br />
Please type 8 characters for the 2nd row of the chessboard: pppppppp <br />
Please type 8 characters for the 1st row of the chessboard: rnbqkbnr <br />
 
White has a score of 40 and Black has a score of 40, so this game is a tie. 
 

Please type 8 characters for the 8th row of the chessboard: -----K-- <br />
Please type 8 characters for the 7th row of the chessboard: --N----- <br />
Please type 8 characters for the 6th row of the chessboard: -------- <br />
Please type 8 characters for the 5th row of the chessboard: -------- <br />
Please type 8 characters for the 4th row of the chessboard: ----k--- <br />
Please type 8 characters for the 3rd row of the chessboard: --q----- <br />
Please type 8 characters for the 2nd row of the chessboard: -------- <br />
Please type 8 characters for the 1st row of the chessboard: -------- <br />
 
White has a score of 10 and Black has a score of 3, so White is winning. 
</i> 

The program uses lowercase letters for the white pieces and uppercase letters for the black pieces, and the hyphen "-" for an empty space. By the chess piece relative value system, kings are not assigned a value, but queens are worth 10 points each, rooks are worth 5 points each, knights and bishops are worth 3 points each, and pawns are worth 1 point each. The program will ask the user for each row of the chessboard and receive a string from the user, and by looking through the strings provided for each row, the score for each player is computed. 
