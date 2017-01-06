def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    houses = set()

    # Code goes here
    cohort_data = open(filename)  # open the data file
    for line in cohort_data:  # iterate over each line in the file
        split_line = line.split("|")  # split each line on |
        house = split_line[2]  # assign a variable to the house
        if len(house) > 0:  # check for empty string
            houses.add(house)  # if house is non-empty, add to houses

    cohort_data.close()
    return houses

unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Puts ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...],
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    # Code goes here
    cohort_data = open(filename)
    for line in cohort_data:
        line = line.rstrip()
        split_lines = line.split("|")
        cohort = split_lines[4]
        name = split_lines[0] + " " + split_lines[1]

        if cohort == "Winter 2016":
            winter_16.append(name)
        elif cohort == "Spring 2016":
            spring_16.append(name)
        elif cohort == "Summer 2016":
            summer_16.append(name)
        elif cohort == "Fall 2015":
            fall_15.append(name)
        elif cohort == "G":
            ghosts.append(name)

    winter_16.sort()
    spring_16.sort()
    summer_16.sort()
    fall_15.sort()
    ghosts.sort()

    all_students = [winter_16, spring_16, summer_16, fall_15]

    cohort_data.close()

    return all_students

sort_by_cohort("cohort_data.txt")


def students_by_house(filename):
    """TODO: Sort students by house.


    Iterates over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Returns all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    # Code goes here
    cohort_data = open(filename)
    for line in cohort_data:
        line = line.rstrip()
        split_line = line.split("|")
        last_name = split_line[1]
        cohort = split_line[4]
        house = split_line[2]

        if cohort == "G":
            ghosts.append(last_name)
        elif cohort == "I":
            instructors.append(last_name)
        elif house == "Gryffindor":
            gryffindor.append(last_name)
        elif house == "Hufflepuff":
            hufflepuff.append(last_name)
        elif house == "Slytherin":
            slytherin.append(last_name)
        elif house == "Dumbledore's Army":
            dumbledores_army.append(last_name)
        elif house == "Ravenclaw":
            ravenclaw.append(last_name)

    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    ravenclaw.sort()
    ghosts.sort()
    instructors.sort()

    all_students = [gryffindor, hufflepuff, slytherin, dumbledores_army,
                    ravenclaw, ghosts, instructors]
    filename.close()

    return all_students

#print students_by_house("cohort_data.txt")


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    # Code goes here
    cohort_data = open(filename)
    for line in cohort_data:
        line = line.rstrip()
        split_line = line.split("|")
        name = split_line[0] + " " + split_line[1]
        house = split_line[2]
        advisor = split_line[3]
        cohort = split_line[4]

        tup = (name, house, advisor, cohort)
        student_list.append(tup)

    cohort_data.close()

    return student_list

#print all_students_tuple_list("cohort_data.txt")


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Uses the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    # Code goes here
    first_name = raw_input("What's the student's first name? > ")
    last_name = raw_input("What's the student's last name? > ")
    full_name = first_name + " " + last_name

    for tup in student_list:
        if tup[0] == full_name:
            return tup[3]
    return "Student not found."

print find_cohort_by_student_name(all_students_tuple_list("cohort_data.txt"))
##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Uses the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here
    # name = raw_input("Choose a student > ")
    # for tup in student_list:
    #     if name == tup[0]:
    #         house = tup[1]
    #         cohort = tup[3]
            
    #     else:
    #         print "That is not the name of a student."
    # return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print hogwarts_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
