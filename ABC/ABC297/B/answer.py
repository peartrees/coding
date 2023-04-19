s = input()

ans = "No"


B_st_index = s.index("B")
B_rd_index = s.rindex("B")

R_st_index = s.index("R")
R_rd_index = s.rindex("R")

K_index = s.index("K")


if (B_rd_index - B_st_index) % 2 == 1:
    if (R_st_index < K_index) and (K_index < R_rd_index):
        ans = "Yes"

print(ans)