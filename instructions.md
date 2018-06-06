## Visionect Python tutoring, group 1

### How is this test graded.

**Correct results** `50%`
- Program works according to the instructions.
(Output is just like instructions demand it to be)
**Style** `30%`
- How elegant the solution is.
(Using functions, using the simplest way to solve the problem, leaving no unused variables, arrays...)
**Code readability** `20%`
- How well formatted the code is, how fast can someone else understand it.
(If I give my code to the total stranger, will he/she understand what I meant?)
**Surprise me** `10%` (bonus)
- If you make something outside the scope of the test but its a nice addition.

#### Criteria
 `0% - 49%` : Didn't pass.
 `50% - 64%`: Talk about the test solution, if there is insufficient knowledge about solved test, didn't pass.
 `65% - 100%`: Passed
 `101% - 110%`: Passed and you get a 6pack of some good beer. Choose dark or light :)

### Test instructions

----


**The test exercise will try to predict a 2018 NBA finals game results.**

()
1. Import (manually typing is OK) [resent results](https://en.wikipedia.org/wiki/Cavaliers%E2%80%93Warriors_rivalry#Results_(2014%E2%80%9315_season%E2%80%93present)) into suitable data structure. Use games from 1-26.
These results will be used as a learning set for our predictions.

2. Let's make some statistics first:
 -Print out, how many times Golden State and Cleveland won overall.
 -Print out, how many times each team won at home and away.
 -Average points scored by each team.
 -Trend, which team is better lately? (feel free to find a way how to do it)

3. Create an algorithm that will print out the prediction for the next game. Use games 27 and 28 to test the predictions. The result should be logical (e.g. 32:18, or 174:198 don't make sense.)
 -There will be min 2 and max 3 more games until the deadline. Test your predictions against these matches too by including games 27 and 28 into learning set. Are predictions any better?

4. Run your algorithm 10 000 times and print out, what is average prediction.

5. Create a betting system where user will input their prediction only once.
*{Use games 29,30,(31) as actual results}*
 -Print out the user's prediction
 -Print out the prediction your program calculated.
 Check the actual result and test your program and user's prediction:
 -If winner is correctly predicted, award is 10€.
 -If winner is correctly predicted and points of one team are missed by less than 8%, award is additional 15€.
 or
 -If winner is correctly predicted and points of both teams are missed by less than 8%, award is additional 40€
 -If result of one team is totally correct, award is additional 100€.
 or
 -If result of the game is totally correct, award is additional 500€.

