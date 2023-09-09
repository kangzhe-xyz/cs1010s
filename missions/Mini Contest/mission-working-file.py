from runes import *

def beside_frac(frac, pic1, pic2):
    qtl_pic1, qtl_pic2 = quarter_turn_right(pic1), quarter_turn_right(pic2)
    return quarter_turn_left(stack_frac(frac, qtl_pic1, qtl_pic2))

# show(beside_frac(3/10, circle_bb, ribbon_bb))
def besiden(n, pic):
    """
    Same as stackn but with beside
    """
    return quarter_turn_right(stackn(n, quarter_turn_left(pic)))

# # # # # # # # # show(besiden(3, heart_bb))

def triangle_rune(pic, n):
    pattern_so_far = blank_bb
    for i in range(0, n):
        layer = beside_frac((i+1)/n, besiden(i + 1, pic), besiden(n-i+1, blank_bb))
        pattern_so_far = stack_frac(i/(i+1),pattern_so_far,layer)

    for i in range(n-1, 0, -1):
        layer = beside_frac((i)/n, besiden(i, pic), besiden(n-i+2, blank_bb))
        pattern_so_far = stack_frac((2*n-i-1)/(2*n-i),pattern_so_far,layer)

    return pattern_so_far

show(triangle_run(circle_bb, 4))
# for vscode. uncomment this later.
root = graphics.master 
root.mainloop()