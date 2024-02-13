if __name__ == '__main__':
    records = [] # create a list of empty records
    name_list = [] # create a list of empty name_list
    score_list = [] # create a list of empty score_list
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score]) # append all the names and score from the user
        name_list.append(name) # appending all the name to name_list
        score_list.append(score)   # appending all the score to score_list
    score_list = list(set(score_list)) # to remove duplicate elements in the score_list use set function and converting them into list again
    score_list.sort()   # sorting the score_list in ascending order to find the second lowest in the records
    second_low = score_list[1]   # creating a second_row var and storing the score_list second value in it.
    out = [i[0] for i in records if i[1] == second_low]   # performing a for loop in the records to get name of the second-low & sorting them 
    out.sort()
    for i in out: # another for loop to get the result of the second_lowe names if they have same low marks
        print(i)
