from PopupInput import *
import Buy
import random

class Inventory(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white", borderwidth=1, relief="sunken")
        self.grid(padx=50)

        self.stockList = Listbox(self, borderwidth=0, highlightthickness=0)
        self.stockList = ["Alphabet", "Apple", "Amazon", "Johnson & Johnson", "BP", "Visa", "Facebook", "JPMorgan Chase", "Procter & Gamble", "NVIDIA",
                          "Microsoft", "Tesla"]
        self.userInv = [0 for i in range(12)]
        self.amount = [0 for i in range(12)]



        self.menuFont = ("italic", 10)
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Your Positions", bg='white', font=("italic", 12, "underline")).grid()
        self.inventory = Listbox(self, height=12,selectmode=SINGLE, font=self.menuFont, width=17,activestyle="underline")
        self.inventory.grid(row=1, column=0, padx=5, pady=(3, 10))
        for i in self.stockList:
            self.inventory.insert(END, i)

        self.spTitle = Label(self, text="Sell\n Price", bg='white', font=("italic", 12, "underline"))
        self.spTitle.grid(row=0, column=1)
        self.sell_priceList = Listbox(self, activestyle="underline", bg='white', height=12, selectbackground="#44AAA1",
                                      selectforeground="black", takefocus=0,
                                      font=self.menuFont, width=10)
        self.sell_priceList.grid(row=1, column=1, pady=(3, 10))

        Label(self, text="Stock \n Amount", bg='white', font=("italic", 12, "underline")).grid(row=0, column=2)
        self.amounts = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                               selectbackground="white", selectforeground="black")
        self.amounts.grid(row=1, column=2, pady=(3, 10))
        for i in range(12):
            self.amounts.insert(END, 0)

        Label(self, text="Investment", bg='white', font=("italic", 12, "underline")).grid(row=0, column=3)
        self.stockPrice = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                  selectbackground="white", selectforeground="black")
        self.stockPrice.grid(row=1, column=3, pady=(3, 10))
        for i in range(12):
            self.stockPrice.delete(i, END)
            self.stockPrice.insert(END, 0)

        Label(self, text="Current\nClosing Price", bg='white', font=("italic", 12, "underline")).grid(row=0, column=4)
        self.ifyousell = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                 selectbackground="white", selectforeground="black")
        self.ifyousell.grid(row=1, column=4, pady=(3, 10))
        for i in range(12):
            self.ifyousell.delete(i, END)
            self.ifyousell.insert(END,0)

        Label(self, text="Current\nProfit", bg='white', font=("italic", 12, "underline")).grid(row=0, column=5)
        self.difference = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                  selectbackground="white", selectforeground="black")
        self.difference.grid(row=1, column=5, pady=(3, 10))
        for i in range(12):
            self.difference.insert(END, 0)

        self.sell = ttk.Button(self, text="Sell", command=self.sell_stocks)
        self.sell.grid(row=2, column=0, columnspan=2)

    def update_sell_prices(self):
        self.sell_prices = self.generate_sell_prices()
        for i in range(len(self.sell_prices)):
            self.sell_priceList.delete(i, END)
            self.sell_priceList.insert(i, '{} $'.format(self.sell_prices[i]))
            self.ifyousell.delete(i, END)
            self.ifyousell.insert(i,'{} $'.format(round(self.sell_prices[i],2) * self.userInv[i]))

            self.difference.delete(i, END)
            self.difference.insert(i,5)

    def generate_sell_prices(self):

        Alphabet = round(random.uniform(1662.23, 1823.35), 2)
        Apple = round(random.uniform(105, 147), 2)
        Amazon = round(random.uniform(3051, 3254), 2)
        Johnson_Johnson = round(random.uniform(131, 174), 2)
        BP = round(random.uniform(17, 35), 2)
        Visa = round(random.uniform(191, 234), 2)
        Facebook = round(random.uniform(245, 293), 2)
        P_and_G = round(random.uniform(114, 153), 2)
        JPMorgan = round(random.uniform(124, 158), 2)
        NVIDIA = round(random.uniform(473, 526), 2)
        Microsoft = round(random.uniform(196, 225), 2)
        Tesla = round(random.uniform(734, 789), 2)

        return [Alphabet, Apple, Amazon, Johnson_Johnson, BP, Visa, Facebook, P_and_G, JPMorgan, NVIDIA, Microsoft,
                Tesla]

    def sell_stocks(self):
        try:
            stockI = self.inventory.curselection()[0]
        except:
            messagebox.showerror(title="Error", message="Please select a stock to sell")
            return

        w = PopupInput(self.master, self.master.money, self.stockList[stockI], self.master.inv.sell_prices[stockI],
                       buy=False, stockI=stockI)
        self.master.wait_window(w.top)
        try:
            numSell = w.amount
            self.master.sell(stockI, numSell)

            self.userInv[stockI] -= numSell
            self.amounts.delete(stockI)
            self.amounts.insert(stockI, self.userInv[stockI])
        except:
            return
