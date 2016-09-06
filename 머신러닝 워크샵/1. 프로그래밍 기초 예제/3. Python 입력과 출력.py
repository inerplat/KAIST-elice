def main():
    r = input() # First line
    g = input() # Second line
    b = input() # Third line

    # change r, g, b into integer...

    print(rgb2hex(r, g, b))


def rgb2hex(r, g, b):
    rr = "%02X" % int(r)
    gg = "%02X" % int(g)
    bb = "%02X" % int(b)
    hex_color= '#'+rr+gg+bb
    return hex_color

if __name__ == "__main__":
    main()
