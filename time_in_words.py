h = int(input())
m = int(input())

text = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9: 'nine', 10:'ten',
       11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quater', 16:'sixteen', 17:'seventeen', 
       18:'eighteen', 19: 'ninteen', 20:'twenty', 21:'twenty one', 22:'twenty two', 23:'twenty three', 
       24:'twenty four', 25:'twenty five', 26:'twenty six', 27:'twenty seven', 28:'twenty eight', 
       29: 'twenty nine', 30: 'half'}

output_msg = ''
past_to = ' past '
if m == 0:
    output_msg = text[h] + " o' clock"
    past_to = ' '
elif m > 30: 
    m = 60 - m
    past_to = ' to '
    h = (h + 1) % 12
if past_to != ' ':
    output_msg = text[m]
    if m != 15 and m !=30 and m != 1: output_msg += ' miniutes'
    elif m == 1: output_msg += ' miniute'
    output_msg += past_to + text[h]

print(output_msg)