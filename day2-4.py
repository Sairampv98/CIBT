if __name__ == '__main__':
   
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #cuboidz = [[0,0,k] for k in range(z+1) ]
    #print(cuboidz)
    #cuboidy = [[0,j,0] for j in range(y+1) ]
    #print(cuboidy)
    #cuboidx = [[i,0,0] for i in range(x+1) ]
    #print(cuboidx)
    #cuboid = cuboidz+cuboidy[1:]+cuboidx[1:]+[[x,y,z]]
    cuboid_method1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)if (i+j+k)!=n ] 
    print(cuboid_method1)
    cuboid_method2 = [[[[i,j,k] for k in range(z+1) if (i+j+k)!=n] for j in range(y+1)] for i in range(x+1) ]
    print("---------------------------------")
    print(cuboid_method2)

