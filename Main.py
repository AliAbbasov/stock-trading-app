from Buy import *
from Inventory import *


class Main(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.grid(sticky=N + S + E + W)

        self.money = 1000
        self.normFont = ("italic", 12)

        self.hour = time.strftime("%H")
        self.minute = time.strftime("%M")
        self.day = time.strftime("%A")
        self.create_widgets()
        self.update_time()


    def create_widgets(self):

        self.tFrame = Frame(self)

        self.tFrame.grid(columnspan=2, sticky=N, pady=15)

        self.title = ttk.Label(self.tFrame, text="Welcome to Mega Trade", font=("italic", 24, "bold"))
        self.title.grid(padx=20, pady=10)

        self.mLabel = ttk.Label(self.tFrame, text="You have : {} $".format(round(self.money)), font=self.normFont)
        self.mLabel.grid(sticky=W + E, padx=230, pady=10)

        self.menu = BuyMenu(self)
        self.menu.grid(row=2, column=0, pady=15, sticky=E + W + N + S, )

        self.inv = Inventory(self)
        self.inv.grid(row=2, column=1, pady=15, sticky=E + W + N + S, )

    def update_time(self):

        # if self.day == "Sunday" or self.day == "Saturday":
        #     self.deactivate()
        # if "01" <= self.hour <= "18":
        #     self.deactivate()

        if self.menu.stockMenu.curselection():
            i = self.menu.stockMenu.curselection()[0]
            self.menu.stockMenu.selection_clear(first=i)
        elif self.inv.inventory.curselection():
            i = self.inv.inventory.curselection()[0]
            self.inv.inventory.selection_clear(first=i)

        self.menu.update_buy_prices()
        self.inv.update_sell_prices()

    def purchase(self, stockI, amount, cost):

        self.inv.userInv[stockI] += amount
        self.money -= cost

        self.mLabel['text'] = "Your money: {} $".format(round(self.money, 2))

        self.inv.amounts.delete(stockI)
        self.inv.amounts.insert(stockI, self.inv.userInv[stockI])

        cost1 = self.menu.buy_prices[stockI] * (self.inv.userInv[stockI])
        self.inv.stockPrice.delete(stockI)
        self.inv.stockPrice.insert(stockI, '{}'.format(round(cost1, 2)))

    def sell(self, stockI, amount):

        cost = self.inv.sell_prices[stockI] * amount
        self.money += cost

        self.mLabel['text'] = "Your money: {} $".format(round(self.money, 2))

        cost1 = self.inv.sell_prices[stockI] * (self.inv.userInv[stockI] - amount)
        self.inv.stockPrice.delete(stockI)
        self.inv.stockPrice.insert(stockI, '{}'.format(round(cost1, 2)))



    def deactivate(self):
        self.menu.buy['state'] = DISABLED
        self.inv.sell['state'] = DISABLED


root = Tk()
bgimage = PhotoImage(file=r"Pictures/Mega_Trade_Pic.png")
Label(root, image=bgimage).place(relwidth=1, relheight=1)
root.iconbitmap(r'Pictures/mega_trade.ico')
root.title("Mega Trade app")
root.resizable(width=False, height=False)
app = Main(root)
app.mainloop()
