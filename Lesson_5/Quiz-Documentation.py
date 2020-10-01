# QUIZ: Documentation Quiz Section

# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible!

def readable_timedelta(days):
    # insert your docstring here
    """readable_timedelta - to convert a number of days into the consquent amount of weeks and days
    INPUT:
    days - the number of days specified in the argument
    OUTPUT:
    weeks - the fewest amount of weeks contained within the amount of days specified in the argument
    remainder - the remainder of days left when the argument is divided by 7 (the amount of days in a week)
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)