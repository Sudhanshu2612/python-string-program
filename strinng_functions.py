
# To print the choices   again and again till exit
def print_choices(list):
    play   = True
    print("\n\n\nChoose any  one  operationn  from  below or  choose  0 to exit:\n1) Total number of sequences\n2) Number of pattern occurrences\n3) Number of sequences with length >= min_len\n4) Number of sequences with GC% >= min_GC\n5) Number of sequences with length >= min_len and GC% >= min_GC")
    choice = input()
    if(choice == '0'):
        print("Exiting")
        exit()
    elif(choice == '1'):
        no_Of_Sequences(list)
        if play   ==  True:
            print_choices(list)
    elif(choice == '2'):
        print("Please enter the pattern to search")
        pattern = input()
        print("Please select  the no. of sequence to search for in the list")
        num = int(input())
        search_seq(list,num,pattern)
        if play   ==  True:
            print_choices(list)
    elif(choice ==  '3'):
        print("Please  enter  the minimum length:")
        length = int(input())
        more_than_Length(list, length)
        if play   ==  True:
            print_choices(list)
    elif(choice  ==  '4'):
        print("Please  enter the min_GC (e.g. 50%) ")
        GC = int(input())
        GC_content =  cal_GC_conntent(list)
        more_than_GC(GC_content,GC)
        if play   ==  True:
            print_choices(list)
        
    elif(choice == '5'):
        print("Please  enter  the minimum length:")
        length = int(input())
        print("Please  enter the min_GC (e.g. 50%) ")
        GC = int(input())
        more_than_Length(list, length)
        GC_content =  cal_GC_conntent(list)
        more_than_GC(GC_content,GC)
        if play   ==  True:
            print_choices(list)

#Reading  data  from the file
def  Read_data(file_path):
    my_file = open(file_path, "r")
    content = my_file.read()
    seq_list = content.split(",") #I  am considering that  your sequences are separated by  ','  if  they are separated
                                      #by some other means like ' ' space then please replace ',' with space                  
    my_file.close()
    return seq_list

#Calculating  the  no of sequennces
def no_Of_Sequences(seq_list):
    print("total no. of strings are :{}".format(len(seq_list)))
    return(len(seq_list))
    
def  search_seq(seq_list,choice,seq):
    str =  seq_list[choice]
    flag = False
    count = 0
    for i in range(len(str)):
        if (str[i:i + len(seq)] == seq):       
            count=count+1
            flag = True
    if (flag == False):
        print("NONE")

    print("string '{}' appears '{}' time in '{}' sequence".format(seq,count,str))
    return count

#calculating no. of   string more than given length
def more_than_Length(seq_list,length):
    count =0
    for seq in seq_list:
        if(len(seq) >= length ):
            count = count + 1
    print("No. of sequences greater than  length  '{} ' are '{}' ".format(length,count))

#calculating GC content of every  sequence  and store GC score in  list respectively
def cal_GC_conntent(seq_list):
    GC_content =[]
    for seq  in  seq_list:
        g_count=0
        c_count=0
        for s in seq:
            if s == ('g' or 'G'):
                g_count  =  g_count+1
            if  s  == ('c' or 'C'):
                c_count =   c_count+1
        GC_value  =  (g_count+c_count)/len(seq)
        GC_percentage = GC_value *  100
        GC_content.append(GC_percentage)
    return  GC_content

#search for  no. of score more than minnimum  given by user in list this  way it is  more easy
def more_than_GC(list,val):
    count  =  0
    for gc in list:
        if(gc>=val):
            count = count+1
    print("no.  of sequences with gc_score more than {}  are {}".format(val,count))


list = Read_data("seqs.txt")
play   = True
print("Choose any  one  operationn  from  below or  choose  0 to exit:\n1) Total number of sequences\n2) Number of pattern occurrences\n3) Number of sequences with length >= min_len\n4) Number of sequences with GC% >= min_GC\n5) Number of sequences with length >= min_len and GC% >= min_GC")
choice = input()
if(choice == '0'):
    print("Exiting")
    exit()
elif(choice == '1'):
    no_Of_Sequences(list)
    if play   ==  True:
        print_choices(list)
elif(choice == '2'):
    print("Please enter the pattern to search")
    pattern = input()
    print("Please select  the no. of sequence to search for in the list")
    num = int(input())
    search_seq(list,num,pattern)
    if play   ==  True:
        print_choices(list)
elif(choice ==  '3'):
    print("Please  enter  the minimum length:")
    length = int(input())
    more_than_Length(list, length)
    if play   ==  True:
        print_choices(list)
elif(choice  ==  '4'):
    print("Please  enter the min_GC (e.g. 50%) ")
    GC = int(input())
    GC_content =  cal_GC_conntent(list)
    more_than_GC(GC_content,GC)
    if play   ==  True:
        print_choices(list)
    
elif(choice == '5'):
    print("Please  enter  the minimum length:")
    length = int(input())
    print("Please  enter the min_GC (e.g. 50%) ")
    GC = int(input())
    more_than_Length(list, length)
    GC_content =  cal_GC_conntent(list)
    more_than_GC(GC_content,GC)
    if play   ==  True:
        print_choices(list)
    
