import pandas as pd;
import matplotlib.pyplot as plt; #for plot creation


file = 'World Population.xlsx'; #file path
data = pd.read_excel(file); #read file

#frequency dictionary
digFrequency = {i: 0 for i in range(1, 10)};


#for test
#should give us size of data 
# rows, columns = data.shape;
# print(f'rows: {rows} and Columns: {columns}');

#the loop
for i in data.columns:
    for j in data[i]:
        #ensure we only deal with numbers and no possible non numeric value
        if isinstance(j, (int, float)): 
            #gers first char of data probably as a string cause python
            firstDig = str(j)[0]; 
            #check if first digit is a numeric value, or an int since only one digit
            if firstDig.isdigit():
                #convert the variable to a integer
                firstDig = int(firstDig);
                #looks for the digit in digFrequency
                if firstDig in digFrequency: #probably a bit redundant but just to be safe
                    #update frequency
                    digFrequency[firstDig] +=1;


#to print the table
#title
print("First digit frequency table:")

#loop from 1-9 and print first digits and their frequencies from digFrequency
for i in range(1, 10): 
    print(f'{i}: {digFrequency[i]}');

#create a data frame from the dicitonarry 
freqDF = pd.DataFrame(list(digFrequency.items()), columns=['First Digit', 'Frequency']);

#build the tbale using plt 
#this is the labels for the x axis, for the first digits
xLabel = freqDF['First Digit'].astype(str);
#values of the frequency
yvalues = freqDF['Frequency'];

#this creates a bar chart using the first digits and each of their frequencies
plt.bar(xLabel, yvalues);
#set titel of chart
plt.title("First Digit Frequencies");
#x labe
plt.xlabel("First Digits");
#y label
plt.ylabel("Frequency");
#rotation of the x axist labels
plt.xticks(rotation = 0);
#draws gridlines along y axis
# plt.grid(axis='y');

#display the plot
plt.show();








