def arithmetic_arranger(problems: list[str], results: bool = False) -> str:
    top = ""
    bottom = ""
    dashes = ""
    sol_f = ""
    if len(problems) > 5:
        return "Error: Too many problems."

    for i, p in enumerate(problems):
        p = p.split(' ')

        if p[0].isdigit() is False or p[2].isdigit() is False:
            return "Error: Numbers must only contain digits."

        res = max(p, key=len)
        sol = (' '.join(p))
        solutions = eval(sol)

        if len(res) > 4:
            return "Error: Numbers cannot be more than four digits."

        if p[1] != '+' and p[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if len(p[0]) < len(p[2]):
            b4_spaces = len(p[2]) +  2 
            length_sol = len(str(solutions))
            rw1_space = b4_spaces - len(p[0])
            w = " " * rw1_space
            top += w + p[0] + "    "
            bottom += p[1] + " " + p[2] + "    "
            dashes += b4_spaces * "-" + "    "
            sol_f += " " * (b4_spaces - length_sol) + str(solutions) + "    "

        if len(p[0]) == len(p[2]):
            b4_spaces = len(p[0]) + 2
            rw1_space = b4_spaces - len(p[0])
            w = " " * rw1_space
            top += w + p[0] + "    "
            bottom += p[1] + " " + p[2] + "    "
            dashes += b4_spaces * "-" + "    "
            sol_f += w + str(solutions) + "    " 

        if len(p[0]) > len(p[2]):
            w = " " * ((len(p[0]) + 2) - (len(p[2]) + 1))
            length_sol = len(str(solutions))
            top = "  " + p[0] + "    "
            bottom += p[1] + w + p[2] + "    "
            dashes += (len(p[0]) + 2) * "-" + "    "
            sol_f += ((len(p[0]) + 2) - length_sol) * " " + str(solutions) + "    "  # type: ignore

    top = top.rstrip()
    top += top.join("\n")
    bottom = bottom.rstrip()
    bottom += bottom.join("\n")
    dashes = dashes.rstrip()
    sol_f = sol_f.rstrip()

    if results:
        dashes += dashes.join("\n")
        return top + bottom + dashes + sol_f
    return top + bottom + dashes