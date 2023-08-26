#
# CS1010S --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

# test
# show(heart_bb)

##########
# Task 1 #
##########

def mosaic(a,b,c,d):
    patterns_right = quarter_turn_left(stack(a,b))
    patterns_left = quarter_turn_left(stack(d,c))
    return quarter_turn_right(stack(patterns_right, patterns_left))

# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))


##########
# Task 2 #
##########

def simple_fractal(a):
    patterns_right = quarter_turn_right(stack(a,a))
    patterns_left = quarter_turn_right(a)
    return quarter_turn_left(stack(patterns_left,patterns_right))

# Test
# show(simple_fractal(heart_bb))


##########
# Task 3 #
##########

def egyptian(p,n):
    # pattern's borders. got this hint from tutorials.
    pattern_borders = stackn(n-2,p)
    # left and right borders
    border_lr_bottom = stack_frac(1/(n-1),p,pattern_borders) # bottom n-1
    border_lr_full = stack_frac(1/n, p, border_lr_bottom) # stack one more on top of border_lr_bottom
    # middle section top and bottom
    middle_tb = stackn(n-2,quarter_turn_left(p)) # turn left first
    middle_tb = quarter_turn_right(middle_tb) # turn it back
    middle_top =  stack_frac(1/(n-1),middle_tb,p)
    middle_full = stack_frac(1 - 1/n,middle_top,middle_tb)
    # stack left to right 
    # left middle. rotate first then use stack
    border_lr_full = quarter_turn_left(border_lr_full) # turn left first
    middle_full = quarter_turn_left(middle_full) # turn left first
    lm = stack_frac(1/(n-1),border_lr_full,middle_full)
    # left middle right. same approach
    lmr = quarter_turn_right(stack_frac(1 - 1/n,lm,border_lr_full)) # turn it back
    return lmr

# Test
show(egyptian(heart_bb, 5))

# for vscode. uncomment this later.
root = graphics.master 
root.mainloop()