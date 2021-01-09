from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class PopupInput(Frame):
    def __init__(self, master, money, stock, stockPrice, buy=True, stockI=None):

        ttk.Frame.__init__(self, master)
        self.grid()
        self.master = master

        okayCommand = (self.register(self.is_okay), "%S")
        self.stockI = stockI

        self.money = money
        self.stock = stock
        self.stockPrice = stockPrice
        self.defFont = ("italic", 12)
        self.bOrS = "buy" if buy else "sell"
        self.top = Toplevel(master)
        self.top.iconbitmap(r'Pictures\mega_trade.ico')
        self.howMuch = ttk.Label(self.top, text="How much {} stock would you like to {}?".format(stock, self.bOrS),
                                 font=self.defFont)
        self.howMuch.grid(padx=20, pady=(5, 0), columnspan=2)

        self.userInp = ttk.Entry(self.top, font=self.defFont, validate='key', validatecommand=okayCommand)

        self.userInp.grid(columnspan=2)

        if buy:
            self.userInp.insert(0, self.money // self.stockPrice)
        elif not buy:
            self.userInp.insert(0, self.master.inv.userInv[stockI])

        self.ok = ttk.Button(self.top, text="Ok", command=self.confirm_order)
        self.ok.grid(ipadx=20)

        self.cancel = ttk.Button(self.top, text="Cancel", command=self.destroy)
        self.cancel.grid(row=2, column=1, )

    def confirm_order(self):
        if self.bOrS == "buy":
            if int(self.userInp.get()) * self.stockPrice > self.master.money:
                messagebox.showerror(title="Error!",
                                     message="You do not have enough money to buy that much {} stock".format(
                                         self.stock))

            else:
                self.amount = int(self.userInp.get())
                if messagebox.askokcancel(title="Are you sure?",
                                          message="Do you want to buy {} {} stock for {}$ ?".format(self.amount,
                                                                                                    self.stock,
                                                                                                    round(
                                                                                                        self.amount * self.stockPrice),
                                                                                                    2)):
                    self.destroy()

        elif self.bOrS == "sell":
            if int(self.userInp.get()) > 150 :
                messagebox.showerror(title="Error", message="You do not have that much of {} stock! ".format(self.stock))

            else:
                self.amount = int(self.userInp.get())
                if messagebox.askokcancel(title="Are you sure?",
                                          message="Do you want to sell {} {} stock for {}$ ?".format(self.amount,
                                                                                                     self.stock,
                                                                                                     round(
                                                                                                         self.amount * self.stockPrice),
                                                                                                     2)):
                    self.destroy()

    def is_okay(self, what):
        try:
            int(what)
            return True
        except:
            self.bell()
            return False

    def destroy(self):
        self.top.destroy()
