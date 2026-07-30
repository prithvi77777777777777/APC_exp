#create a program to calculate area of triangle volume of sphere , total surface area of cylinder, area of sphere
i=int(input("enter choice for area of triangle press 1, for volume of sphere press 2, for total surface area of cylinder press 3, for area of sphere press 4:"))

match i:
    case 1:
        h=int(input("Enter height of triangle:"))
        b=int(input("Enter breadth of triangle:"))
        print("area of triangle:",((b*h)/2))
    case 2:
        r=float(input("Enter radius"))
        print("Volume of shpere is:",((4/3)*(22/7)*(r*r*r)))
    case 3:
        r=float(input("Enter radius:"))
        h=float(input("Enter height:"))
        print(" total surface area of cylinder is:",(2*(22/7)*r*(h+r)))
        #TSA = 2π r(h + r
    case 4:
        r=float(input("Enter radius:"))
        print("area of shpere is:",(4*(22/7)*r*r))
    case _:
        print("Invalid choice")
