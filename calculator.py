def run_rate(runs, overs):
    """Calculate runs scored per over."""
    if runs < 0 or overs <= 0:
        raise ValueError("Runs must be non-negative and overs must be positive.")

    return round(runs / overs, 2)


def strike_rate(runs, balls):
    """Calculate runs scored per 100 balls."""
    if runs < 0 or balls <= 0:
        raise ValueError("Runs must be non-negative and balls must be positive.")

    return round((runs / balls) * 100, 2)


def required_rate(runs_needed, overs_remaining):
    """Calculate required runs per over."""
    if runs_needed < 0 or overs_remaining <= 0:
        raise ValueError("Runs needed must be non-negative and overs must be positive.")

    return round(runs_needed / overs_remaining, 2)


def main():
    print("===== CRICKET SCORE CALCULATOR =====")

    runs = int(input("Enter runs scored: "))
    overs = float(input("Enter overs played: "))
    balls = int(input("Enter balls faced: "))

    print("\n--- Player and Team Statistics ---")
    print("Run Rate:", run_rate(runs, overs))
    print("Strike Rate:", strike_rate(runs, balls))

    target = int(input("\nEnter target score: "))
    current_score = int(input("Enter current score: "))
    overs_remaining = float(input("Enter overs remaining: "))

    runs_needed = target - current_score

    print("Runs Needed:", runs_needed)
    print("Required Run Rate:", required_rate(runs_needed, overs_remaining))


if __name__ == "__main__":
    main()