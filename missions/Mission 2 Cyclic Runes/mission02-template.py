#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

###########
# Task 1a #
###########

def fractal(the_rune, n):
    if n == 1:
        return the_rune
    else:
        top = the_rune
        btm = quarter_turn_right(stack(quarter_turn_left(the_rune),quarter_turn_left(the_rune)))
        return fractal(btm, n-1)


# Test
show(fractal(heart_bb, 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1b #
###########

def fractal_iter(the_rune, n):
    qtl_rune = quarter_turn_left(the_rune) # prepare for stacking
    for i in range (0,n-1):
        frac_btm = stack(qtl_rune, qtl_rune) # stack two horizontally
        frac_full = stack(the_rune, quarter_turn_right(frac_btm)) # stack one copy of the rune on top
        qtl_rune = quarter_turn_left(frac_full) # this will become the new thing to stack horizontally
    return quarter_turn_right(qtl_rune) # un-rotate 

# Test
# show(fractal_iter(heart_bb,5))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(params):
    # Fill in code here
    return

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1


###########
# Task 1d #
###########

def dual_fractal_iter(params):
    # Fill in code here
    return

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1


##########
# Task 2 #
##########

def steps(params):
    # Fill in code here
    return

# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))

# for vscode. uncomment this later.
root = graphics.master 
root.mainloop()