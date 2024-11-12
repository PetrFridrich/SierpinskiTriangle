from sierpinski import Sierpinski

def main():

    triangle = Sierpinski(max_depth=6, altitude=500)
    triangle.draw_triangles() 
    
    return None


if __name__ == '__main__':

    print('Hello, home!')

    main()