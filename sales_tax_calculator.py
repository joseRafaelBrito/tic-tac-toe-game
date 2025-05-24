def calculate_total_cost(amount, tax_rate):
    """
    Calculate the total cost including tax
    :param amount: The purchase amount before tax
    :param tax_rate: The tax rate as a percentage (e.g., 8.5 for 8.5%)
    :return: Dictionary containing subtotal, tax amount, and total
    """
    tax_amount = amount * (tax_rate / 100)
    total = amount + tax_amount
    return {
        "subtotal": amount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total": total
    }

def format_currency(amount):
    """
    Format a number as currency with 2 decimal places
    :param amount: The amount to format
    :return: Formatted string with $ and 2 decimal places
    """
    return f"${amount:.2f}"

def main():
    print("Sales Tax Calculator")
    print("-------------------")
    
    while True:
        try:
            # Get input from user
            amount = float(input("\nEnter the purchase amount: $"))
            tax_rate = float(input("Enter the tax rate (%): "))
            
            # Calculate total
            result = calculate_total_cost(amount, tax_rate)
            
            # Display results
            print("\nReceipt:")
            print(f"Subtotal: {format_currency(result['subtotal'])}")
            print(f"Tax Rate: {result['tax_rate']}%")
            print(f"Tax Amount: {format_currency(result['tax_amount'])}")
            print(f"Total: {format_currency(result['total'])}")
            
            # Ask if user wants to calculate another amount
            another = input("\nCalculate another amount? (y/n): ").lower()
            if another != 'y':
                break
                
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 