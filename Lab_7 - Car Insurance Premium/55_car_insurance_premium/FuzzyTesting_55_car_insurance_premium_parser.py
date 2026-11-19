from datetime import date

def normalize_registration(plate):
    """
    Removes spaces, dashes, and dots from a registration number and upper-cases it.
    Safely handles None, non-string, or empty inputs without crashing.
    """
    if not isinstance(plate, str):
        return ""

    plate = plate.strip().upper()
    for ch in [' ', '-', '.']:
        plate = plate.replace(ch, '')
    return plate

def total_claim_amount(text):
    """
    Adds up valid non-negative whole-number claim amounts separated by semicolons.
    Safely ignores empty or malformed entries and handles non-string inputs.
    """
    if not isinstance(text, str) or not text.strip():
        return 0

    total = 0
    for raw_amount in text.split(';'):
        cleaned = raw_amount.strip()
        if not cleaned:
            continue
        try:
            amount = int(cleaned)
            if amount >= 0:
                total += amount
        except ValueError:
            continue
    return total

def driver_age(dob, current_year=2026):
    """
    Works out the driver's age from a valid DD/MM/YYYY date of birth.
    Returns None if the input is malformed, non-string, or not a valid calendar date.
    """
    if not isinstance(dob, str):
        return None
    if not isinstance(current_year, int) or isinstance(current_year, bool):
        return None

    parts = dob.strip().split('/')
    if len(parts) != 3:
        return None

    try:
        day = int(parts[0].strip())
        month = int(parts[1].strip())
        year = int(parts[2].strip())
        date(year, month, day)
    except ValueError:
        return None

    if year < 1900 or year > current_year:
        return None

    return current_year - year

def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    print("Driver age in 2026:", driver_age(value))

if __name__ == "__main__":
    main()