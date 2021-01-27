from Inventory import *
import random
import time

class BuyMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white", borderwidth=1, relief="sunken")
        self.master = master
        self.grid(padx=50)

        self.stockList = Listbox(self, borderwidth=0, highlightthickness=0)
        self.stockList = ["Alphabet", "Apple", "Amazon", "Johnson & Johnson", "BP", "Visa", "Facebook", "JPMorgan Chase", "Procter & Gamble", "NVIDIA",
                          "Microsoft", "Tesla"]
        self.master.after(0, self.fakewhile)
        self.cycles = 0
        self.create_widgets()

    def fakewhile(self):
        if self.cycles % 5 == 0:
            self.update_buy_prices()
        if self.cycles == 10:
            self.cycles = 0
        self.cycles = self.cycles + 1
        self.master.after(1000, self.fakewhile)

    def create_widgets(self):

        self.menuFont = ("italic", 10)

        self.menuTitle = Label(self, text="Stocks \n List", bg='white', font=("italic", 12, "underline"))
        self.menuTitle.grid(row=0, column=0)
        self.stockMenu = Listbox(self, height=12, selectmode=SINGLE, activestyle="underline", font=self.menuFont,
                                 width=17)
        self.stockMenu.grid(row=1, column=0, padx=5, pady=(3, 10))
        for d in self.stockList:
            self.stockMenu.insert(END, d)

        self.bpTitle = Label(self, text="Buy\n Price", bg='white', font=("italic", 12, "underline"))
        self.bpTitle.grid(row=0, column=1)
        self.buy_priceList = Listbox(self, activestyle="underline", bg='white', height=12, selectbackground="#44AAA1",
                                 selectforeground="black", takefocus=0,
                                 font=self.menuFont, width=10)
        self.buy_priceList.grid(row=1, column=1, pady=(3, 10))

        self.buy = ttk.Button(self, text="Buy", command=self.buy_stocks)
        self.buy.grid(row=2, column=0, columnspan=2)

    def update_buy_prices(self):
        self.buy_prices = self.generate_buy_prices()
        for i in range(len(self.buy_prices)):
            self.buy_priceList.delete(i, END)
            self.buy_priceList.insert(i, '{} $'.format(self.buy_prices[i]))


    def generate_buy_prices(self):
        Alphabet = round(random.uniform(1662.23,1823.35),2)
        Apple = round(random.uniform(105, 147),2)
        Amazon = round(random.uniform(3051, 3254),2)
        Johnson_Johnson = round(random.uniform(131, 174),2)
        BP = round(random.uniform(17, 35),2)
        Visa = round(random.uniform(191, 234),2)
        Facebook = round(random.uniform(245, 293),2)
        P_and_G = round(random.uniform(114, 153),2)
        JPMorgan = round(random.uniform(124, 158),2)
        NVIDIA = round(random.uniform(473, 526),2)
        Microsoft = round(random.uniform(196, 225),2)
        Tesla = round(random.uniform(734, 789),2)

        return [Alphabet, Apple, Amazon, Johnson_Johnson, BP, Visa, Facebook, P_and_G, JPMorgan, NVIDIA, Microsoft,
                Tesla]

    def buy_stocks(self):
        try:
            stockI = self.stockMenu.curselection()[0]
        except:
            messagebox.showwarning(title="Error", message="Please select a stock to buy")
            return

        w = PopupInput(self.master, money=self.master.money, stock=self.stockList[stockI],
                       stockPrice=self.buy_prices[stockI], buy=True)

        self.master.wait_window(w.top)
        try:
            amount = w.amount
            cost = amount * self.buy_prices[stockI]
            self.master.purchase(stockI, amount, cost)
        except:
            return
