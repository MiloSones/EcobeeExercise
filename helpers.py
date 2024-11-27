def get_input(max_option):
    user_input = input(f"Enter your choice (1-{max_option}): ")
    try:
        number = int(user_input)
        if 1 <= number <= max_option:
            return number
        return -1
    except ValueError:
        return -1