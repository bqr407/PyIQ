# PyIQ
Cognitive thinking game to evaluate memory and processing skills

## Games

### General Math
Traditional problems including addition, subtraction, and multiplication

### Bubble Math
#### Math problems where the player needs to sum bubbled numbers on the screen and follow certain rules
There are two types of bubbles: small and large.
Small bubbles can have values like -5, 14, 5-2, 8+3, 9x1, 4x5, etc. Large bubble can have values like x2, x3, etc.
A large bubble is used as a multiplier, any small bubbles contained within it must be summed first and then the multiplier or the large bubble must be performed on that sum. You can think of a large bubble as an array

Example Bubble: 

        [5x2, 7, 4]
        
Answer: 

        (5x2)+7+4
        
        21

Example Bubble: 

        [[2, [3, 7]], 5]
  
Answer: 

        2(3+7)+5
        
        20+5
        
        25
        
Example Bubble: 

        [[3, [2, 4x2]], [2, [4, -4]], 3x1]
        
Answer: 

        3(8+2)+2(4-4)+3
        
        30+3
        
        33

### Length Based Memory Recall
#### Players will be tasked to remember either numeric or alphanumeric sequences which will be briefly flashed on the screen

Examples: 

          "3029"
          
          "abrj"
          
          "302402"
          
          "skr00ea"
          
### Recency Based Memory Recall
#### Players will be shown a series of words and tasked to rememember previous words shown between 2-4 times back from the current displayed word.


Example:  

          Ryan

          Nathan
          
          John (What was the name 2 spots back? Answer: Ryan)
          
          Brendan (What was the name 2 spots back? Answer: Nathan)
          
          Luke (What was the name 2 spots back? Answer: John)
          
          Daniel (What was the name 3 spots back? Answer: John)
          
          Adam (What was the name 2 spots back? Answer: Luke)
          
          Ethan (What was the name 1 spots back? Answer: Adam)
          
          Lucas (What was the name 3 spots back? Answer: Daniel)
          
          Brent (What was the name 1 spots back? Answer: Lucas)
          
          Nate (What was the name 4 spots back? Answer: Adam)
          
## Answering
#### Options will be given in multiple choice format: A, B, C, and D

## Timing
#### The following time restrictions will be used for problems:

General Math: 3 Seconds per Problem

Bubble Math: 5 Seconds per Problem

Memory Recall (both types): 3 Seconds per Problem

## Scoring
A problem's point value is based on it's complexity.

Points will be awarded using this formula:
    (remaining time + 1) * (x) # x is 5 for easy problems, 10 for medium problems, and 15 for hard problems
