def calculate_pet_ages(human_years):
    """
    Calculate cat and dog ages based on human years.
    
    Args:
        human_years: Number of years since the pet was born
    
    Returns:
        List: [humanYears, catYears, dogYears]
    """
    if human_years < 0:
        return "Error: Years cannot be negative"
    
    # Calculate cat years
    if human_years == 0:
        cat_years = 0
    elif human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
    
    # Calculate dog years
    if human_years == 0:
        dog_years = 0
    elif human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]


# Main program
if __name__ == "__main__":
    try:
        human_years = int(input("How many human years ago did you get your pet? "))
        result = calculate_pet_ages(human_years)
        print(result)
    except ValueError:
        print("Error: Please enter a valid number")
