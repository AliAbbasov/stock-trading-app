from PopupInput import *


class Inventory(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white", borderwidth=1, relief="sunken")
        self.grid(padx=50)

        self.stockList = Listbox(self, borderwidth=0, highlightthickness=0)
        self.stockList = ["Alphabet", "Apple", "Amazon", "Bitcoin", "BP", "EORO", "Facebook", "GBP", "Gold", "Oil",
                          "Microsoft", "Tesla"]
        self.userInv = [0 for i in range(12)]

        self.menuFont = ("italic", 10, "underline")
        self.create_widgets()

    def create_widgets(self):

        Label(self, text="Your Inventory", bg='white', font=("italic", 12, "underline")).grid()
        self.inventory = Listbox(self, height=0, font=self.menuFont, width=18, activestyle="none")
        self.inventory.grid(row=1, column=0, padx=5, pady=(3, 10))
        for i in self.stockList:
            self.inventory.insert(END, i)

        self.spTitle = Label(self, text="Sell\n Prices", bg='white', font=("italic", 12, "underline"))
        self.spTitle.grid(row=0, column=1)
        self.priceList = Listbox(self, activestyle="underline", bg='white', height=12, selectbackground="#44AAA1",
                                 selectforeground="black", takefocus=0,
                                 font=self.menuFont, width=10)
        self.priceList.grid(row=1, column=1, pady=(3, 10))


        Label(self, text="Stocks\n Amount", bg='white', font=("italic", 12, "underline")).grid(row=0, column=2)
        self.amounts = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                               selectbackground="white", selectforeground="black")
        self.amounts.grid(row=1, column=2, pady=(3, 10))
        for i in range(12):
            self.amounts.insert(END, 0)



        Label(self, text="Amount of\n Money", bg='white', font=("italic", 12, "underline")).grid(row=0, column=3)
        self.stockPrice = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                  selectbackground="white", selectforeground="black")
        self.stockPrice.grid(row=1, column=3, pady=(3, 10))
        for i in range(12):
            self.stockPrice.delete(i, END)
            self.stockPrice.insert(END, 0)




        Label(self, text="Current prices", bg='white', font=("italic", 12, "underline")).grid(row=0, column=4)
        self.ifyousell = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                 selectbackground="white", selectforeground="black")
        self.ifyousell.grid(row=1, column=4, pady=(3, 10))
        for i in range(12):
            self.ifyousell.insert(END, 0)




        Label(self, text="Profit", bg='white', font=("italic", 12, "underline")).grid(row=0, column=5)
        self.difference = Listbox(self, height=0, font=("italic", 10), width=10, activestyle='none',
                                  selectbackground="white", selectforeground="black")
        self.difference.grid(row=1, column=5, pady=(3, 10))
        for i in range(12):
            self.difference.insert(END, 0)


        self.sell = ttk.Button(self, text="Sell", command=self.sell_stocks)
        self.sell.grid(row=2, column=0, columnspan=2)

    def sell_stocks(self):
        try:
            stockI = self.inventory.curselection()[0]
        except:
            messagebox.showerror(title="Error", message="Please select a stock to sell")
            return

        w = PopupInput(self.master, self.master.money, self.stockList[stockI], self.master.menu.prices[stockI],
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
