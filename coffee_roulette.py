import pandas as pd
import random
import csv

# orginal list of all names must be even
df = pd.read_excel(r'C:\Users\GOHILV\OneDrive - FUJITSU\Documents\Coffee_Rout\listofnames.xlsx')
# previous pairs
df_previous_pairs = pd.read_csv(r'C:\Users\GOHILV\OneDrive - FUJITSU\Documents\Coffee_Rout\PreviousPairs.csv', header = None)

#coloumn headings for previous pairs
df_previous_pairs.columns = ["namesA", "namesB"]

# previous pairs into tuples
df_previous_pairs['tuple'] = list(zip(df_previous_pairs['namesA'], df_previous_pairs['namesB']))
#print(df_previous_pairs)

#previous pairs tuples to list
previous_pair_tuple = df_previous_pairs['tuple'].tolist()


# turn column with names into list
lst1 = df['NAMES'].tolist()



#randonly selects from list of names and deletes it from orginal list
def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)

# while their are still names in the orginal list create tuples
pairs = []
interim_pairs=[]
lst = lst1.copy()

def main_loop(lst):
    # build the tuples form the orginal list of names 
    while lst:
        rand1 = pop_random(lst)
        rand2 = pop_random(lst)
        pair = rand1, rand2
        pairs.append(pair)
    #print("all pairs " , pairs)

    
    # for each pair we created above, check if it already been in the previous pair tuple. If yes then delete from my pair
    #print("new pairs we created from list " , pairs)
    for tu in previous_pair_tuple:
        for tup in pairs:
            if tup == tu: 
                a=pairs.index(tup)    
                pairs.pop(a)

    #print("the list of previous pair tuples that have lready met " , previous_pair_tuple)

    reverse_previous_pair = [t[::-1] for t in previous_pair_tuple]
   # print("Reversed previous pair is a the reverse of the previous pair tuples that have already met " , reverse_previous_pair)
    # reverse the previous pair tuple. Check if the tuples i created are in the previous pair tuple
    for tu in reverse_previous_pair:
        for tup in pairs:
            if tup == tu:
                a=pairs.index(tup)
                pairs.pop(a)

    # code will be runing in loop. We keep building new tuples ad checking if the tuples in it have already met. this is done above.
    # if it longer than the interim pairs then we make interim pairs qual to it and loop again to find a longer list of tuples that have not met. 
    if len(pairs) >= len(interim_pairs):
        interim_pairs.clear()
        interim_pairs.append(pairs) 

    
    #print("this is the list " ,  interim_pairs)
  
    return interim_pairs

# we run the pairs builing functio above 10 times to get the longest valid tuple of pairs possible
final_list=[]
def runa(lst):
    for i in range (10):
        final_list=main_loop(lst)
    #print("this is the new list, ", final_list)
    if len(final_list) == 0:
        for i in range (10):
            final_list=main_loop(lst)
        #print("this is the new list a, ", final_list)
    final_list=[item for t in final_list for item in t]
    
    # appends to previous pairs
    with open('PreviousPairs.csv', 'a') as csvfile:
        fwriter = csv.writer(csvfile)

        for x in final_list:
            print("this is X", x)
            fwriter.writerow(x)

    with open('/Users/GOHILV/OneDrive - FUJITSU/Documents/PreviousPairs.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
       # fwriter(final_list)
        for x in final_list:
            print("this is AB", x)
            fwriter.writerow(x)
        

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# writer.writerow(row)

# # close the file
# f.close()
        
    
    # overwrites the previously recommended new pair. i.e. this is the latest pair. 
    with open('NewPair.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile)
        print("this is the new pairs list, if it is empty, run the script again. If it is populated then run the second script to email out",  final_list)
        for x in final_list:
            print("this is it " , x)
            fwriter.writerow(x)

runa(lst)



