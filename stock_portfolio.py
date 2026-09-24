
stock_prices = {
    "TCS": 3500,
    "INFY": 1800,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "ITC": 500
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} - ₹{price}")

total_investment = 0
number_of_stocks = int(
    input("\nHow many different stocks do you want to buy? ")
)


for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper().strip()

    if stock_name in stock_prices:

        quantity = int(
            input(f"Enter quantity of {stock_name}: ")
        )

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print(f"Investment in {stock_name}: ₹{investment}")

    else:
        print("❌ Stock not available.")
        print(
            "Please choose from:",
            ", ".join(stock_prices.keys())
        )


print("\n===================================")
print(f"Total Investment: ₹{total_investment}")
print("===================================")


save_file = input(
    "\nDo you want to save the result to a file? (yes/no): "
).lower().strip()

if save_file == "yes":

    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Report\n")
        file.write("======================\n")
        file.write(f"Total Investment: ₹{total_investment}\n")

    print("✅ Portfolio saved to portfolio.txt")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")
