"""Manage pharmacy inventory, prescriptions, and stock reports."""

import ast
import hashlib
import json
import operator
import os
import secrets
from datetime import date, datetime

medicines = {}
DB_PASSWORD = os.getenv("PHARMACY_DB_PASSWORD", "")

def add_medicine(name, qty=0, price=0.0, expiry="2099-12-31",
                 audit=None):
    """Add medicine stock and optionally record an audit entry."""
    if not isinstance(name, str) or not name.strip():
        return audit if audit is not None else []

    if audit is None:
        audit = []

    if name not in medicines:
        medicines[name] = {"qty": 0, "price": price, "expiry": expiry}

    medicines[name]["qty"] += qty
    audit.append(
        f"{datetime.now()}: Stocked {qty} units of {name}"
    )
    return audit

def dispense_medicine(name, qty):
    """Dispense available medicine without allowing negative stock."""
    if name not in medicines or qty <= 0:
        return False

    if medicines[name]["qty"] < qty:
        return False

    medicines[name]["qty"] -= qty
    if medicines[name]["qty"] == 0:
        del medicines[name]

    return True

def get_quantity(name):
    """Return the quantity available for a medicine."""
    return medicines[name]["qty"]

def is_expired(name):
    """Check whether a medicine has passed its expiry date."""
    expiry = datetime.strptime(
        medicines[name]["expiry"], "%Y-%m-%d"
    ).date()
    return expiry < date.today()

def bill_amount(prescription):
    """Calculate the total cost of a prescription."""
    return sum(
        medicines[name]["price"] * quantity
        for name, quantity in prescription
    )

def calculate_dosage(formula):
    """Evaluate basic arithmetic without executing arbitrary code."""
    expression = ast.parse(formula, mode="eval").body
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (
            int, float
        ):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](
                evaluate(node.left),
                evaluate(node.right),
            )

        raise ValueError("Unsupported dosage formula")

    return evaluate(expression)

def patient_id(name, phone):
    """Generate a SHA-256 identifier from patient details."""
    value = f"{name}{phone}".encode()
    return hashlib.sha256(value).hexdigest()

def generate_rx_number():
    """Generate a prescription reference number."""
    return f"RX-{secrets.randbelow(900000) + 100000}"

def save_stock(file="pharmacy.json"):
    """Save the current inventory as JSON."""
    with open(file, "w", encoding="utf-8") as stock_file:
        json.dump(medicines, stock_file, indent=2)

def load_stock(file="pharmacy.json"):
    """Load inventory from a JSON file."""
    with open(file, "r", encoding="utf-8") as stock_file:
        stock = json.load(stock_file)

    medicines.clear()
    medicines.update(stock)

def print_label(name):
    """Print a medicine dispensing label safely."""
    print(f"Dispensing label: {name}")

def expiring_soon(days=30):
    """Return medicines expiring within the specified number of days."""
    today = date.today()
    result = []

    for name, details in medicines.items():
        expiry = datetime.strptime(
            details["expiry"], "%Y-%m-%d"
        ).date()

        if 0 <= (expiry - today).days < days:
            result.append(name)

    return result

def pharmacist_login(password):
    """Validate the pharmacist password configured in the environment."""
    return bool(DB_PASSWORD) and secrets.compare_digest(
        password, DB_PASSWORD
    )

def print_stock():
    """Display the current pharmacy stock report."""
    print("===== Pharmacy Stock Report =====")

    for name, details in medicines.items():
        print(
            f"{name} -> {details['qty']} units, "
            f"Rs. {details['price']} exp {details['expiry']}"
        )

def main():
    """Run a demonstration of pharmacy management functions."""
    add_medicine("Paracetamol 500mg", 200, 1.5, "2027-06-30")
    add_medicine("Amoxicillin 250mg", 40, 6.0, "2026-01-15")
    add_medicine("Cetirizine 10mg", 10, 2.0, "2027-03-31")
    add_medicine(404, 25)

    dispense_medicine("Paracetamol 500mg", 30)
    dispense_medicine("Insulin", 2)

    print("Paracetamol stock:", get_quantity("Paracetamol 500mg"))
    print("Amoxicillin expired?", is_expired("Amoxicillin 250mg"))
    print(
        "Bill:",
        bill_amount([
            ("Paracetamol 500mg", 10),
            ("Amoxicillin 250mg", 5),
        ]),
    )
    print("Dosage (mg/day):", calculate_dosage("250 * 2"))
    print("Patient ID:", patient_id("Asha", "9876543210"))
    print("Rx number:", generate_rx_number())
    print("Login:", pharmacist_login(DB_PASSWORD))
    print_label("Paracetamol 500mg")

    save_stock()
    load_stock()
    print_stock()

if __name__ == "__main__":
    main()
