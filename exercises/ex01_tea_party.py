"""Planning A Tea Party!"""

__author__: str = "730739313"


def main_planner(guests: int) -> None:
    """Compounds functions together to determine all elements"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # In this line multiple functions had to be called, and different arguments had to be defined in order to yield an output
    # This is because the cost is dependent on # of teabags and treats so must call tea_bags and treats, and define their arguments in accordance with main_planner
    return None


def tea_bags(people: int) -> int:
    """Determine how many tea bags Needed!"""
    return people * 2


def treats(people: int) -> int:
    """Determines amount of treats Needed based on number of tea bags!"""
    return int(tea_bags(people=people) * 1.5)


# It is important to classify the function as an int here because multiplication of an int and a float yields a float by default


def cost(tea_count: int, treat_count: int) -> float:
    """Configures the cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


# This function doesn't feel complete because there is no way to determine the tea count or treat count by calling the function alone.
# This issue is resolved later and the function is defined through calling it within the main_planner function and defining it's parameter by means of other functions.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
