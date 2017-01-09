def create_histogram(lst_country_name,lst_data,col_sep):
    """
        Function will receive list of country names,csv data and column separator
        output will be a text assuming a model of histogram where x axis is year and y will be range of population
        it will be shown country wise
    """
    for line in lst_data:
        country_name = line.split(col_sep)[4]
        if country_name in lst_country_name:
            print("Details of "+country_name+":",end="\n")
            print("x-2010,y-("+line.split(col_sep)[6]+"-"+line.split(col_sep)[7]+"),value="+line.split(col_sep)[7],end="\n")
            print("x-2011,y-("+line.split(col_sep)[7]+"-"+line.split(col_sep)[8]+"),value="+line.split(col_sep)[8],end="\n")
            print("x-2012,y-("+line.split(col_sep)[8]+"-"+line.split(col_sep)[9]+"),value="+line.split(col_sep)[9],end="\n")
            print("x-2013,y-("+line.split(col_sep)[9]+"-"+line.split(col_sep)[10]+"),value="+line.split(col_sep)[10],end="\n")
            print("x-2014,y-("+line.split(col_sep)[10]+"-"+line.split(col_sep)[11]+"),value="+line.split(col_sep)[11],end="\n")
            print("x-2015,y-("+line.split(col_sep)[11]+"-"+line.split(col_sep)[12]+"),value="+line.split(col_sep)[12],end="\n\n\n")
    
def readcsv(col_sep,file_full_path):
    fp = open(file_full_path,"r")
    lst_data = fp.readlines()
    fp.close()
    lst_country = []
    for line in lst_data:
        lst_country.append(line.split(col_sep)[4])
    create_histogram(lst_country
                            ,lst_data,col_sep)
    pass

if __name__ == "__main__":
    from collections import OrderedDict
    file_full_path = "NST-EST2015-alldata.csv"
    readcsv(",",file_full_path)
