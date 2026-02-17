import tkinter as tk
import random

root = tk.Tk()
root.title("ERC20 Token Generator")
root.geometry("300x250")

# Labels
title_label = tk.Label(root, text="ERC20 Token Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

name_label = tk.Label(root, text="Token Name: ", font=("Arial", 11))
name_label.pack()

symbol_label = tk.Label(root, text="Token Symbol: ", font=("Arial", 11))
symbol_label.pack()

supply_label = tk.Label(root, text="Total Supply: ", font=("Arial", 11))
supply_label.pack()

# Generate function
def generate_token():
    token_names = ["MyToken", "AlphaCoin", "BlockCoin", "CryptoToken", "SmartToken"]
    symbols = ["MTK", "ALP", "BLK", "CTK", "SMT"]

    name = random.choice(token_names)
    symbol = random.choice(symbols)
    supply = random.randint(1000, 1000000)

    name_label.config(text=f"Token Name: {name}")
    symbol_label.config(text=f"Token Symbol: {symbol}")
    supply_label.config(text=f"Total Supply: {supply}")

# Button
generate_btn = tk.Button(root, text="Generate", command=generate_token)
generate_btn.pack(pady=15)

root.mainloop()