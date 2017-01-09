ord_dct={}
def arrange_state(col_sep,lst_data):
    """
        Output of this function will be country name and its population of
        the year 2015. From highest to lowest of estimated population of 2015
    """
    dct_state = {}
    for lines in lst_data[1:len(lst_data)]:
        lst_lines = lines.split(col_sep)
        dct_state[lst_lines[4]] = lst_lines[12]
    ord_dct = OrderedDict(sorted(dct_state.items(),key=lambda x: int(x[1]),reverse=True))
    for key,value in ord_dct.items():
        print(key+":"+value)
    
def readcsv(col_sep,file_full_path):
    fp = open(file_full_path,"r")
    lst_data = fp.readlines()
    fp.close()
    arrange_state(col_sep,lst_data)
    pass

if __name__ == "__main__":
    from collections import OrderedDict
    file_full_path = "NST-EST2015-alldata.csv"
    readcsv(",",file_full_path)
