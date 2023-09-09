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
        frac_btm = beside(the_rune, the_rune)
        return stack(the_rune, fractal(frac_btm,n-1))
    
# show(fractal(heart_bb,4))

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

def beside_n(n: int, the_rune):
    """
    An implementation of `beside()`, but n times.
    """
    qtl = quarter_turn_left(the_rune)
    return quarter_turn_right(stackn(n, qtl))

# Test
# show(beside_n(5, heart_bb))


def dual_fractal(rune_one, rune_two, n): 
    if n == 1:
        return rune_one
    else:
        frac_btm = beside(rune_two,rune_two)
        return(stack(rune_two if n % 2 else rune_one, dual_fractal(rune_one, frac_btm, n-1)))

# Test
show(dual_fractal(heart_bb, rcross_bb, 6))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1


###########
# Task 1d #
###########

def dual_fractal_iter(rune_one, rune_two, n):
    qtl_one = quarter_turn_left(rune_one) # prepare for stacking
    qtl_two = quarter_turn_left(rune_two) # prepare for stacking
    if n % 2 == 0: # check even or odd to determine which one to use for the bottom layer
        for i in range (0,n-1):
            if i % 2 != 0: # ping pong between both odd and even
                frac_btm = stack(qtl_one, qtl_one) # stack two horizontally
                frac_full = stack(rune_two, quarter_turn_right(frac_btm)) # stack one copy of the rune on top
                qtl_two = quarter_turn_left(frac_full) # this will become the new thing to stack horizontally
            else:
                frac_btm = stack(qtl_two, qtl_two) # stack two horizontally
                frac_full = stack(rune_one, quarter_turn_right(frac_btm)) # stack one copy of the rune on top
                qtl_one = quarter_turn_left(frac_full) # this will become the new thing to stack horizontally
    else: 
        for i in range (0,n-1):
            if i % 2 == 0: # ping pong between both odd and even
                frac_btm = stack(qtl_one, qtl_one) # stack two horizontally
                frac_full = stack(rune_two, quarter_turn_right(frac_btm)) # stack one copy of the rune on top
                qtl_two = quarter_turn_left(frac_full) # this will become the new thing to stack horizontally
            else:
                frac_btm = stack(qtl_two, qtl_two) # stack two horizontally
                frac_full = stack(rune_one, quarter_turn_right(frac_btm)) # stack one copy of the rune on top
                qtl_one = quarter_turn_left(frac_full) # this will become the new thing to stack horizontally
        
    if n == 1:
        return rune_one
    else:
        return quarter_turn_right(qtl_one) # will always finish off with qtl_one

# Test
# show(dual_fractal_iter(heart_bb,nova_bb,4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1


##########
# Task 2 #
##########
def mosaic(a,b,c,d):
    patterns_right = quarter_turn_left(stack(a,b))
    patterns_left = quarter_turn_left(stack(d,c))
    return quarter_turn_right(stack(patterns_right, patterns_left))

def steps(a,b,c,d):
    a = overlay_frac(3/4,blank_bb,a)
    b = overlay_frac(1/2,blank_bb,b)
    c = overlay_frac(1/4,blank_bb,c)
    d = overlay_frac(0,blank_bb,d)
    return mosaic(a,b,c,d)

# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))

# for vscode. uncomment this later.
root = graphics.master 
root.mainloop()