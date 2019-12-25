#This file contains different practice problem related to panda data frame
#Data frame can be constructed through a dict of equal-length lists or Numpy arrays
import pandas as pd
data={
'state':['ohio','ohio','ohio','Nevada','Nevada','Nevada'],
'year':[2000,2001,2002,2001,2002,2003],
'pop':[1.5,1.7,3.6,2.4,2.9,3.2]
}
frame=pd.DataFrame(data)

#frame.head()->First 5 values
#frame.tail()->Last 5 values
#pd.DataFrame(data,columns=[])
#pd.DataFrame(data,columns=[],index=[])
#A column in a data frame can be retrieved as a Series either by dict-like notation or attribute
# dataframe['columnname'] or dataframe.columnname
#Assignment of new column value by dataframe['columnname']=value for a single value or
#dataframe['columnname']=list of values
#When we are assigning lists or arrays to a column, the value's length must match the length of the DataFrame. If you assign a Series
#its labels will be realigned exactly to the DataFrame's index, inserting missing values in any holes.
#dataframe.columns returns the columns
#dataframe.index returns the rows/indices
#del deletes the given column for example: del frame['columnname']
#If nested dict is passed to the DataFrame, panda will interpret the outer dict keys as the columns and the inner keys as the row indices
#example dataframe=pd.DataFrame({'column':{'row':...},})
#swapping the rows and columns by dataframe.T 
#Can set index and columns names example: frame.index.name="" and frame.columns.name=""
#Values attribute returns the data contained in the DataFrame as a two-dimentional ndarray ...frame.values
#Index objects are immutable and can't be modified by the user
#Unlike python sets, a pandas index can contain duplicate labels
#obj.reindex()->rearrange the data according to the new index
#reindex->create a new object with the data conformed to a new index 
#ffill->Forward fill the values
# With DataFrame, reindex can alter either the (row) index, columsn, or both. When passed only a sequence, it reindexes the rows in the result
#Columns can be reindexed with the column keyword frame.reindex(columns=[])
# Dropping one or more entries from an axis is easy if you already have an index array or list without those entries. As that can require a bit of 
#mungling and set logic, the drop method will return a new object with indicated value or values deleted from an axis
#drop can take a value or list of values
#In dataframe, drop with the sequence of row labels(axis 0) will drop values from the rows
#Values from the columns can be dropped by passign axis=1 or axis='columns'
#Using the parameter inplace=True will modify the given series or dataframe so be careful
#obj[...] works as indexing
