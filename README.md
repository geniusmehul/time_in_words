# time_in_words
Problem from HackerRank https://www.hackerrank.com/challenges/the-time-in-words/problem

Given the time in numerals we may convert it into words.<br>
        5:00 -> five o' clock<br>
        5:01 -> one miniute past five<br>
        5:10 -> ten mimiutes past five<br>
        5:15 -> quater past five<br>
        5:30 -> half past five<br>
        5:40 -> twenty miniutes to six<br>
        5:45 -> quater to six<br>
        5:47 -> thirteen to six<br>
        5:28 -> twenty eight miniutes past five
        
At _miniute = 0_ use o'clock. For _1 <= miniute <= 30_, use past. For _miniute > 30_ use to.

## Function Description
Complete the timeInWords function in the editor below. It should return a time string as described.
timeInWords has the following parameter(s):
* h: an integer representing hour of the day
* m: an integer representing minutes after the hour

## Input Format
The first line contains _h_,  the hours portion The second line contains _m_, the minutes portion

## Constraints
1 <= h <= 12<br>
0 <= m < 60

## Output Format
Print the time in words as described.
