from prices1 import *
from PopupInput import *
from Inventory import *
import time
import schedule


class BuyMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white", borderwidth=1, relief="sunken")
        self.master = master
        self.grid(padx=50)

        self.stockList = Listbox(self, borderwidth=0, highlightthickness=0)
        self.stockList = ["Alphabet", "Apple", "Amazon", "Bitcoin", "BP", "EORO", "Facebook", "GBP", "Gold", "Oil",
                          "Microsoft", "Tesla"]
        self.create_widgets()


    def create_widgets(self):

        self.menuFont = ("italic", 10)


        self.menuTitle = Label(self, text="Stocks \n List", bg='white', font=("italic", 12, "underline"))
        self.menuTitle.grid(row=0, column=0)
        self.stockMenu = Listbox(self, height=12, selectmode=SINGLE, activestyle="underline", font=self.menuFont, width=17)
        self.stockMenu.grid(row=1, column=0, padx=5, pady=(3, 10))
        for d in self.stockList:
            self.stockMenu.insert(END, d)



        self.bpTitle = Label(self, text="Buy\n Prices", bg='white', font=("italic", 12, "underline"))
        self.bpTitle.grid(row=0, column=1)
        self.priceList = Listbox(self, activestyle="underline", bg='white', height=12, selectbackground="#44AAA1",
                                 selectforeground="black", takefocus=0,
                                 font=self.menuFont, width=10)
        self.priceList.grid(row=1, column=1, pady=(3, 10))


        self.buy = ttk.Button(self, text="Buy", command=self.buy_stocks)
        self.buy.grid(row=2, column=0, columnspan=2)


    def update_prices(self):

        self.prices = self.generate_prices()
        for i in range(len(self.prices)):
            self.priceList.delete(i, END)
            self.priceList.insert(i,'{} $'.format(self.prices[i]))


    def generate_prices(self):

        a = float(prices1.alphabet())
        b = float(prices1.apple())
        c = float(prices1.amazon())
        d = float(prices1.J_and_J())
        e = float(prices1.bp())
        f = float(prices1.Visa_Inc())
        g = float(prices1.fb())
        h = float(prices1.JPMorgan())
        i = float(prices1.P_and_G())
        j = float(prices1.NVIDIA())
        k = float(prices1.ms())
        l = float(prices1.tesla())

        return [a, b, c, d, e, f, g, h, i, j, k, l]


    def buy_stocks(self):
        try:
            stockI = self.stockMenu.curselection()[0]
        except:
            messagebox.showwarning(title="Error", message="Please select a stock to buy")
            return

        w = PopupInput(self.master, money=self.master.money, stock=self.stockList[stockI],
                       stockPrice=self.prices[stockI], buy=True, )

        self.master.wait_window(w.top)
        try:
            amount = w.amount
            cost = amount * self.prices[stockI]
            self.master.purchase(stockI, amount, cost)
        except:
            return
