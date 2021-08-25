import tkinter as tk
from tkinter import font
from tkinter import *
from bs4 import BeautifulSoup
import requests, os, sys, signal, time, glob, pandas as pd, pygetwindow as gw
from csv import writer
from datetime import date


jarvis_mode = True
if jarvis_mode == True:
    intro = "program_intro.mp4"
    os.startfile(intro)
    time.sleep(18)
    vid = gw.getWindowsWithTitle('Movies & TV')[0]
    vid.close()
else:
    pass

root = tk.Tk(className=" Ryan Clark's Trading  Matrix ")
x = 1700
y= 1500
root.geometry(str(x)+"x"+str(y))
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

title = tk.Label(root, text="Trading Matrix")
title.pack()

background_image=tk.PhotoImage(file=File path)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Universal_Font = "Arial"
Label_Font = "Arial"
Header_Font = "Courier New Bold Italic"
Confirm_Font = "Courier"
Value_Font = "Courier"

avail_elements = ['EPS', 'PE', '10d Volume', 'Market Cap', 'Name', 'Year_Low_Price', 'Year_Ago_Price_Change',
                       'Revenue TTM','Net Profit TTM', 'Today_Close', 'Prev Prev Closing', 'HOY', 'HOY_Date', "Investor Relations",
                       "ROA", "Debt to Equity", "Dividend Yield", "Beta", "Current Ratio", "Quick Ratio",
                       "Trailing P/E Ratio", "Forward P/E Ratio", "P/E Growth", "Annual Sales", "Price / Sales",
                       "Cash Flow", "Price / Cash Flow", "Book Value", "Price / Book"]


def __label(text,x,y,font):
    l = tk.Label(root, text=text)
    l.config(font=(font))
    l.pack()
    l.place(x=x, y=y)

def __button_window(window, text, command,x,y):
    btn = tk.Button(window, text=text, command=command)
    btn.pack()
    btn.place(x=x, y=y)

def label__(window, text, x, y, font):
    l = tk.Label(window, text=text)
    l.config(font=(font))
    l.pack()
    l.place(x=x, y=y)

def __scale_widget(window, min, max, orient, x, y):
    scale = Scale(window, from_=min, to=max, orient=orient)
    scale.pack()
    scale.place(x=x, y=y)

def __entry(window, x, y):
    e = tk.Entry(window)
    e.pack()
    e.place(x=x, y=y)

def search():
    Ticker = sbar.get()
    link = ("https://www.cnbc.com/quotes/?symbol=" + Ticker + "&qsearchterm=" + Ticker)
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    e = str(soup)

    label_reference = ['EPS', 'PE', '10d Volume', 'Market Cap', 'Name', 'Year_Low_Price', 'Year_Ago_Price_Change',
                       'Revenue TTM','Net Profit TTM', 'Today_Close', 'Prev Prev Closing', 'HOY', 'HOY_Date', "Investor Relations",
                       "ROA", "Debt to Equity", "Dividend Yield", "Beta", "Current Ratio", "Quick Ratio",
                       "Trailing P/E Ratio", "Forward P/E Ratio", "P/E Growth", "Annual Sales", "Price / Sales",
                       "Cash Flow", "Price / Cash Flow", "Book Value", "Price / Book"]

    identifiers = ["eps", '"pe"', "tendayavgvol", "mktcap", '"name"', 'yrloprice', 'yragopricechange', 'revenuettm',
                   'NETPROFTTM', 'todays_closing', 'prev_prev_closing', 'yrhiprice', 'yrhidate']

    labels = ["Price Now", "Volume", "Average Volume", "Market Capitalization", "P/E Ratio", "Dividend Yield", "Beta",
              "Stock Exchange", "Industry", "Sub-Instrument", "Sector", "Current Symbol", "Previous Symbol", "CUSIP", "CIK", "Web",
              "Phone", "Debt to Equity", "Current Ratio", "Quick Ratio", "Trailing P/E Ratio", "Forward P/E Ratio",
              "P/E Growth", "Annual Sales", "Price / Sales", "Cash Flow", "Price / Cash Flow", "Book Value",
              "Price / Book", "EPS", "Net Income", "Net Margins", "ROE", "ROA", "Employees", "Outstanding Shares",
              "Market Cap", "Next Earnings", "Optional"]
    dataset = {}
    link = ("https://www.marketbeat.com/stocks/NASDAQ/" + Ticker)
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    values = []
    a = soup.find_all('strong')
    for strong_tag in a:
        values.append(strong_tag.text)

    i = 0
    z = len(labels)
    while i < z:
        dataset[labels[i]] = values[i]
        i = i + 1
    def extractor(identifier):
        f = e.index(identifier)
        x = e[f:].index('":"') + f + 3
        z = e[x:].index('","') + x
        identifier = e[x:z]
        return identifier

    def name_extractor():
        f = e.index('"name"')
        x = 50
        g = f + x
        snip = e[f:g]
        start = snip.index('">') + 2
        end = snip.index(' - Stock')
        name = snip[start:end]
        return name

    selected_elements = []
    with open("placeholder.txt", "r") as r:
        line = r.readlines()
        for elem in line:
            try:
                x = len(str(elem))
                elem = elem[:x-1]
                selected_elements.append(label_reference.index(elem))
            except:
                selected_elements.append("No source data")
    rvalues = []
    i = 0
    z = len(identifiers)
    x = 20
    while i < z:
        try:
            dex = identifiers[i]
            if dex == '"name"':
                value = name_extractor()
            elif dex == 'Investor Relations':
                value = "button needed"
            else:
                value = extractor(identifiers[i])
            rvalues.append(value)
        except:
            pass
        i = i + 1

    fin_values=[]
    i = 0
    z = len(selected_elements)
    x = 20
    lines = []
    while i < z:
        try:
            dex = selected_elements[i]
            if dex == 13:
                ir = "button needed"
                fin_values.append(ir)
            else:
                try:
                    el = avail_elements[dex]
                    val = rvalues[dex]
                    add = [el, val]
                    fin_values.append(rvalues[dex])
                    lines.append(add)
                except:
                    finder = label_reference[dex]
                    val = dataset.get(finder)
                    fin_values.append(val)
        except:
            fin_values.append("No source data")
        i = i + 1

    with open("temp0.csv", "w", newline='') as f:
        wr = writer(f)
        header1 = 'Element'
        header2 = 'Value'
        header = [header1, header2]
        wr.writerow(header)
        for line in lines:
            wr.writerow(line)

    ### place values in labels with corresponding element ###
    a = pd.read_csv("scoring_targets.csv")
    b = pd.read_csv("temp0.csv")
    b = b.dropna(axis=1)
    merged = a.merge(b, on='Element')
    merged.to_csv("Test_Output.csv", index=False)
    df = pd.read_csv("Test_Output.csv")
    dp = pd.DataFrame(df)
    labels = dp["Element"].tolist()
    valx = dp['Value_x'].tolist()
    valy = dp['Value_y'].tolist()
    indices = []
    labelp = []
    for l in labels:
        labelp.append(label_reference.index(l))
    i = 0
    z = len(valx)
    while i < z:
        indx = valx[i]/valy[i]
        indices.append(round(indx, 2))
        i = i + 1

    i = 0
    z = len(fin_values)
    x = 250
    y = 250
    x_dev = 0
    y_dev = 0

    while i < z:
        y = y + 22
        if fin_values[i] == "button needed":
            x = x + x_dev
            y = y + y_dev
            __button_window(root, "IR", investor_relations, x, y)
        elif selected_elements[i] in labelp:
            __label(str(fin_values[i]), x + x_dev, y + y_dev, Value_Font)
            w = labels[i]
            v = labels.index(w)
            __label(indices[v], x + 325, y, Value_Font)
        else:
            __label(str(fin_values[i]), x + x_dev, y + y_dev, Value_Font)
        i = i + 1

    btn = tk.Button(root, text="Notes", command=comment_window, bg="green")
    btn.pack()
    btn.place(x=125, y=5)

    h = tk.Label(root, text=rvalues[label_reference.index('Name')], fg="purple", bg='yellow', relief='raised')
    h.place(x=50, y=120)
    h.config(font=("Verdana 15 underline", 50))
    f = font.Font(h, h.cget("font"))
    f.configure(underline=True)
    h.configure(font=f)

    def __values(text, x, y, font):
        v = tk.Label(root, text=text)
        v.place(x=x, y=y)
        v.config(font=(Value_Font))

    label_reference_secondary = ["Daily Change %", "Last Price", "Daily Price Movement", "Next Earnings"]
    identifiers_secondary = ["change_pct", "last", "change", "next_earnings_date"]

    def extractor_secondary(identifier):
        f = e.index('"name"')
        x = 1750
        g = f + x
        snip = e[f:g]
        snip = snip.split('"')
        id = snip.index(identifier)
        identifier = snip[id + 2]
        return identifier

    def percent_daily():
        f = e.index('"name"')
        x = 1750
        g = f + x
        snip = e[f:g]
        snip = snip.split('"')
        indentifier = snip.index("change_pct")
        pct_change = snip[indentifier + 2]
        return pct_change

    def recent_price():
        f = e.index('"name"')
        x = 1750
        g = f + x
        snip = e[f:g]
        snip = snip.split('"')
        indentifier = snip.index("last")
        banner_price = snip[indentifier + 2]
        return banner_price


    price_banner = recent_price()
    price_banner = round(float(price_banner), 2)
    percent_banner = percent_daily()
    change_banner = round(float(price_banner) * (float(percent_banner) / 100), 2)
    banner = "------------"+rvalues[label_reference.index('Name')]+"---------------" + str(
        "Price: $" + str(price_banner)) + "   " + str("Percent Change: " + percent_banner + "%") + "  " + str(
        "Change: $" + str(change_banner)) + "------------"+rvalues[label_reference.index('Name')]+"---------------"

    class Window(tk.Frame):
        def __init__(self, master=None):
            tk.Frame.__init__(self, master)
            self.master = master

    canvas = tk.Canvas(root, width=500, height=45)
    canvas.pack()
    canvas.place(x=200, y=70)
    canvas.config(bg="yellow")
    canvas_text = canvas.create_text(250, 25, text='')
    test_string = banner
    # Time delay between chars, in milliseconds
    delta = 50
    delay = 0
    x = 0
    while x < 50:
        for i in range(len(test_string) + 1):
            s = test_string[:i]
            update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
            canvas.after(delay, update_text)
            delay += delta
        x += 1

def target_values():
    tvals = tk.Toplevel(root)
    tvals.geometry("750x900")
    z = len(avail_elements)
    i = 0
    y = 20
    x = 75
    label__(tvals, "Ideal Values", x + 225, 20,"Arial")
    x1 = x + 265
    entries = []
    b = pd.read_csv("scoring_targets.csv")
    valx = b['Value'].tolist()
    elem = b['Element'].tolist()
    while i < z:
        y = y + 35
        if avail_elements[i] in elem:
            c = elem.index(avail_elements[i])
            label__(tvals, avail_elements[i] + " (Current = "+str(valx[c])+")", x, y, "Arial")
        else:
            label__(tvals, avail_elements[i], x, y, "Arial")
        e = tk.Entry(tvals)
        e.pack()
        e.place(x=x1, y=y)
        entries.append(e)
        i = i+1

    def save_targets():
        values = []
        element = []
        lines = [["Element", "Value"]]
        i=0
        while i < z:
            val = entries[i].get()
            if len(val) < 1:
                pass
            else:
                values.append(int(val))
                element.append(avail_elements[i])
                result = [avail_elements[i], val]
                lines.append(result)
            i = i+1
        with open("scoring_targets.csv", "w", newline='') as f:
            for line in lines:
                wr = writer(f)
                wr.writerow(line)
        f.close()

        print(values, element)
    __button_window(tvals, "Save Values", save_targets, x + 350, 20)

def elements():
    el = tk.Toplevel(root)
    x = 500
    y = 700
    el.geometry(str(x) + "x" + str(y))
    avail_elements = ['EPS', 'PE', '10d Volume', 'Market Cap', 'Name', 'Year_Low_Price', 'Year_Ago_Price_Change',
                       'Revenue TTM','Net Profit TTM', 'Today_Close', 'Prev Prev Closing', 'HOY', 'HOY_Date', "Investor Relations",
                       "ROA", "Debt to Equity", "Dividend Yield", "Beta", "Current Ratio", "Quick Ratio",
                       "Trailing P/E Ratio", "Forward P/E Ratio", "P/E Growth", "Annual Sales", "Price / Sales",
                       "Cash Flow", "Price / Cash Flow", "Book Value", "Price / Book"]
    var_list = []
    selected_elements = []


    def chck_btn(btnid, window, text, x, y, variable):
        btnid = Checkbutton(window, text=text, variable=variable)
        btnid.deselect()
        btnid.pack()
        btnid.place(x=x, y=y)

    def yes():
        z = len(selected_elements)
        i = 0
        y = 251
        aligned_horizontally_coordinate = 52
        while i < z:
            y = y + 22
            label__(root, selected_elements[i], aligned_horizontally_coordinate, y, Label_Font)
            i = i+1


    def no():
        pass

    def selected():
        for var in var_list:
            if var.get() == 1:
                dex = var_list.index(var)
                label = avail_elements[dex]
                selected_elements.append(label)
            else:
                pass
        confirm = tk.Toplevel(el)
        x = 350
        y = 250
        confirm.geometry(str(x) + "x" + str(y))
        z = int(len(selected_elements)/2)
        pone = selected_elements[:z]
        ptwo = selected_elements[z:]
        l = tk.Label(confirm, text="Do you want to use to following elements? "+ "\n" + str(pone) + "\n" +
                                   str(ptwo) + "\n" + str(len(selected_elements))+" elements selected")
        l.pack()
        l.place(relx=.10, rely= .10)
        l.config(font=("Arial"))
        btn = tk.Button(confirm, text="Yes", command=yes)
        btn.pack()
        btn.place(relx = 0.4, rely = .7, anchor = CENTER)
        btn = tk.Button(confirm, text="No", command=no)
        btn.pack()
        btn.place(relx=0.6, rely= .7, anchor=CENTER)
        with open("placeholder.txt", "w") as f:
            for ele in selected_elements:
                f.write(ele + "\n")

    z = len(avail_elements)
    i = 0
    y = 20
    x = 75
    while i < z:
        variable = "Var" + str(i)
        var_list.append(variable)
        i = i+1
    i = 0
    while i < z:
        y = y + 22
        var_list[i] = IntVar()
        chck_btn(avail_elements[i], el, avail_elements[i], x, y, var_list[i])
        i = i+1
    __button_window(el, "Use Selected Elements? ", selected, 200, 0)

## Placing element numbers ##
x = 30
i = 1
z = 11
y = 250
while i < z:
    y = y + 22
    label__(root, str(i)+".", x, y, Label_Font)
    i = i + 1
def line(parent, x1, y, x2):
    parent.create_line(x1, y, x2, y, dash=True)
def score(parent, x, y, entryid):
    entryid = tk.Entry(parent)
    entryid.pack()
    entryid.place(x=x, y=y)

entrynames = []
i = 0
z = 11
while i < z:
    x = str(i)
    entrynames.append("e"+x)
    i = i+1

canvas = Canvas(root, width=600, height=218)
canvas.pack()
canvas.place(x=50, y=272)
i = 0
x1 = 50
x2 = 200
x3 = 300
x4 = 450
x = 400
y = 11

while i<z:
    if i == 0:
        line(canvas, x1, y, x2)
        line(canvas, x3, y, x4)
    else:
        y = y + 22
        line(canvas, x1, y, x2)
        line(canvas, x3, y, x4)
    i = i+1

e_boxes = []
x = 400
y = 0
i=0
while i < z:
    e = tk.Entry(canvas)
    e.pack()
    e.place(x=x, y=y)
    e_boxes.append(e)
    y = y + 22
    i = i + 1


def calc_score():
    score = []
    for e in e_boxes:
        val = e.get()
        if len(val) < 1:
            pass
        else:
            score.append(int(val))

    score = sum(score)
    __color_label(score, 490, 510, "red")
    a = pd.read_csv("scoring_targets.csv")
    b = pd.read_csv("temp0.csv")
    b = b.dropna(axis=1)
    merged = a.merge(b, on='Element')
    merged.to_csv("Test_Output.csv", index=False)
    df = pd.read_csv("Test_Output.csv")
    indices = []
    for line in df:
        indx = 1 - (df['Value_x'] / df['Value_y'])
        indices.append(indx)
    z = len(indices)
    i = 0
    y = 200
    while i < z:
        y = y + 20
        base = indices[i]
        i = i + 1

def save_elements():
    saved = []
    save_name = tk.Toplevel(root)
    save_name.geometry("300x100")
    value = tk.Entry(save_name)
    value.pack()
    def save_fin():
        file_name = value.get()
        with open("placeholder.txt", "r") as f:
            x = f.readlines()
        for ele in x:
            saved.append(ele)
        with open(file_name+"_element_list.txt", "w+") as w:
            for el in saved:
                w.write(el)
        f.close()
        w.close()
        confirm = tk.Toplevel(root)
        confirm.geometry("470x50")
        label__(confirm, "Elements saved", 0, 0, Confirm_Font)

    __button_window(save_name,"Save", save_fin, 125, 45)

def load_elements():
    saved = []
    selector = tk.Toplevel(root)
    lb = Listbox(selector, width=40, height=200)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    myFiles = glob.glob('*_element_list.txt')
    for file in myFiles:
        lb.insert(len(myFiles), file)
    lb.pack()
    lb.place(x=0, y=0)
    lb.size()
    selector.geometry("350x250")

    def load():
        items = [myFiles[int(item)] for item in lb.curselection()]
        item = str(items)
        fle = item[2:len(item)-2]
        with open(fle, "r") as f:
            x = f.readlines()
        with open("placeholder.txt", "w") as f:
            for ele in x:
                saved.append(ele)
                f.write(ele)
        f.close()
        z = len(saved)
        i = 0
        y = 250
        aligned_horizontally_coordinate = 52
        while i < z:
            y = y + 22
            label__(root, saved[i], aligned_horizontally_coordinate, y, Label_Font)
            i = i + 1

    def view():
        quick_view = []
        items = [myFiles[int(item)] for item in lb.curselection()]
        item = str(items)
        fle = item[2:len(item) - 2]
        with open(fle, "r") as f:
            x = f.readlines()
        for ele in x:
            quick_view.append(ele)
        qv = tk.Toplevel(root)
        z = len(quick_view)
        i = 0
        y = 0
        while i < z:
            y = y+20
            label__(qv, str(i+1) + ". "+quick_view[i], 0, y, Universal_Font)
            i = i+1

    __button_window(selector, "Load", load, 250, 0)
    __button_window(selector, "View", view, 250, 30)


e_vals =[]
__button_window(root, "Select Targets", target_values, 570, 185)
__button_window(root, "Calculate", calc_score, 550, 520)
__button_window(root, "Select Matrix Elements",elements,65,540)
__button_window(root, "Load Elements",load_elements,130,510)
__button_window(root, "Save Elements",save_elements,30,510)

## Search Box ##
canvas1 = tk.Canvas(root, width=60, height=10)
canvas1.pack()
sbar = tk.Entry(root)
canvas1.create_window(55, 5, window=sbar)
canvas1.place(x=5, y=55)

def __header(base, text, color, font, size, x, y):
    h = tk.Label(base, text=text, fg=color)
    h.place(x=x, y=y)
    h.config(font=(font, size))

__header(root, "Enter Ticker", "black", Universal_Font, 12, 5, 15)
search_bar = 'sbar'
sb = tk.Button(root, text="Search", command=search)
sb.pack()
sb.place(x=130,y=50)

__header(root, "Element", "blue", Header_Font, 18, 50, 215)
__header(root, "Value", "black", Header_Font, 18, 250, 215)
__header(root, "Score", "grey", Header_Font, 20, 480, 215)
__header(root, "Index", "red", Header_Font, 20, 570, 215)


############
#Watch List#
############


def watch_list():
    Ticker = sbar.get()
    df = pd.read_csv("Watch_list.txt", sep="\n")
    rn = df[df['Watch List'] == Ticker]
    table = pd.DataFrame(rn)
    if len(rn) == 0:
        with open("Watch_list.txt", "a+", newline='') as write:
            csv_writer = writer(write)
            csv_writer.writerow([Ticker])
            watch_list_confirm = tk.Toplevel(root)
            l = tk.Label(watch_list_confirm, text="Successfully added to Watch List")
            l.pack()

    else:
        watch_list_confirm = tk.Toplevel(root)
        l = tk.Label(watch_list_confirm, text="Already Exists on Watch List")
        l.pack()


def __color_label(text,x,y,bg):
    l = tk.Label(root, text=text, bg=bg)
    l.pack()
    l.place(x=x, y=y)


__button_window(root, "Add to Watchlist", watch_list, 825, 280)

df = pd.read_csv("Watch_list.txt")
watchlist = df.values.tolist()
watchlist.sort()
lb = Listbox(root)
for comp in watchlist:
    lb.insert(len(watchlist), comp)
lb.pack()
lb.place(x=700, y=250)

__color_label("Watch List", 700, 230, 'green')

def get_selection():
    items = [watchlist[int(item)] for item in lb.curselection()]
    sbar.insert(0,items)
    search()

__button_window(root, "Search", get_selection,825,250)


def remove_watch():
    remove = [watchlist[int(item)] for item in lb.curselection()]
    keep = []
    with open("Watch_list.txt", "r") as read:
        lines = read.readlines()
    with open("dummy.txt", "w+") as write:
        for line in lines:
            if line.strip("\n") != remove:
                write.write(line)
    os.remove("Watch_list.txt")
    os.rename("dummy.txt", "Watch_list.txt")

__button_window(root, "Remove from Watchlist", remove_watch, 825, 310)


##################
#SEPARATE WINDOWS#
##################

###### INVESTOR RELATIONS ######

def investor_relations():
    def executives():
        Ticker = sbar.get()
        link = ("https://money.cnn.com/quote/profile/profile.html?symb=" + Ticker)
        html = requests.get(link).content
        soup = BeautifulSoup(html, 'html.parser')
        soup.prettify()
        Positions = []
        Executive_Names = []

        ex = soup.find_all(class_="wsod_officerName")
        ex = list(ex)
        for el in ex:
            el = str(el)
            beg = el.index('">') + 2
            end = el.index("</td>")
            Executive_Names.append(el[beg:end])

        ex = soup.find_all(class_="wsod_officerTitle")
        ex = list(ex)
        for el in ex:
            el = str(el)
            beg = el.index('">') + 2
            end = el.index("</td>")
            Positions.append(el[beg:end])
        Executives = pd.DataFrame(Executive_Names, index=Positions, columns=["Names"])
        return Executives
    executives = executives()
    IR = tk.Toplevel(root)
    x = 500
    y = 500
    IR.geometry(str(x) + "x" + str(y))
    l = tk.Label(IR, text=executives)
    l.pack()


###### COMMENT #####

def comment_window():
    Ticker = sbar.get()
    link = ("https://www.cnbc.com/quotes/?symbol=" + Ticker + "&qsearchterm=" + Ticker)
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    e = str(soup)
    f = e.index('"fullchange_pct"')
    g = f + 500
    snap = e[f:g]

    def company_name():
        f = e.index('"name"')
        x = 50
        g = f + x
        snip = e[f:g]
        start = snip.index('">') + 2
        end = snip.index(' - Stock')
        company = snip[start:end]
        return company
    company = company_name()

    comment = tk.Toplevel(root)
    x = 800
    y = 700
    comment.geometry(str(x) + "x" + str(y))
    cbox = tk.Text(comment, height=40, width=60)
    cbox.config(state="normal")
    cbox.pack()
    cbox.place(x=10, y=25)

    def __label_window(text,x,y):
        l = tk.Label(comment, text=text)
        l.pack()
        l.place(x=x, y=y)

    def view_comments():
        view_comment = tk.Toplevel(comment)
        view_comment.geometry("500x650")
        df = pd.read_csv("Notes.csv")
        rn = df[df['Company'] == company]
        table = pd.DataFrame(rn)
        if len(rn) == 0:
            l = tk.Label(view_comment, text="Error: No Comments")
        else:
            l = tk.Label(view_comment, text=table)
        l.place(x=0, y=0)
        l.pack()

    def save_confirmation():
        save_confirm = tk.Toplevel(comment)
        l = tk.Label(save_confirm, text="Save Successful")
        l.pack()

    def __button_window(text,command,x,y):
        btn = tk.Button(comment, text=text, command=command)
        btn.pack()
        btn.place(x=x, y=y)

    def save_note():
        note = cbox.get("1.0","end")
        try:
            df = pd.read_csv("Notes.csv")
            df_use = df.groupby("Company")
            entry = df_use.count()
            entry = entry._get_item_cache("Entry")
            entry = str(entry[0])
        except:
            entry = 0

        i = note.index("\n")
        note = note[:i]
        company = company_name()
        headers = ['Entry', 'Company', 'Note', 'Date']
        rows = [entry, company, note, date.today()]
        with open("Notes.csv", "a+", newline='') as write:
            csv_writer = writer(write)
            csv_writer.writerow(rows)
        cbox.delete("1.0","end")
        save_confirm = tk.Toplevel(comment)
        l = tk.Label(save_confirm, text="Save Successful")
        l.pack()

    __button_window("Save Note", save_note, 500, 150)
    __button_window("View Comments", view_comments, 650, 150)
    __label_window("Please enter your notes in the box", 575, 20)
    __label_window(company, 0, 0)

root.mainloop()
