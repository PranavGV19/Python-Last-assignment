class MF():
    def SubFields():
        print("Sub-Fields in AI are")
        list = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing','Natural Language Processing']
        for temp in list:
            print(temp)
    def oddeven():
        num = int(input("Enter a number to check: "))
        if num%2==0:
            print(f"{num} is an Even Number")
        else:
            print(f"{num} is an Odd number")
    def percentage():
    
        m1 = int(input("Subject1= "))
        m2 = int(input("Subject2= "))
        m3 = int(input("Subject3= "))
        m4 = int(input("Subject4= "))
        m5 = int(input("Subject5= "))
        
        Total = m1 + m2 + m3 + m4 + m5
        print("Total: ", Total)
        
        Percent = (Total / 500) * 100
        print("Percentage: ", Percent)
    def triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        area = (height * breadth) / 2
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle: ", area)

        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth = float(input("Breadth: "))
        perimeter = height1 + height2 + breadth
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle: ", perimeter)

    def eligible():
        gender = input("Enter your gender: ")
        age = int(input("Enter your age: "))
        if gender == "Male":
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("INELIGIBLE")
        elif gender == "Female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("INELIGIBLE")
        else:
            print("INVALID GENDER")