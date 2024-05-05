# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

# so the triangle can always be build upon, but only need to be built as the n get's larger.

triangle = [[1], [1,1]]

def pascal(n):
    
    if n > len(triangle):
        print('in first if statement to create rows')
        # check to see if the triangle already has n rows
    
        # triIndex is the last index of the current triangle. Want to build the triangle up to the value of n

        for triIndex in range(len(triangle)-1, n):
            
            prevRow = triangle[triIndex] # setting the value of a previous row
           
            currentRow = [1] # setting the first term of the row that is being built, always 1 in pascals triangle
            
            # now creating and appending terms to the currentRow based on the prevRow values. using triIndex as the high end of the range b/c it will continue to change. triIndex is not included so don't have to worry about an if statement to check which index it is at. this loop will not create a term at an index equal to triIndex.
            for rowIndex in range(0, triIndex): 
                
                # create a term that gets appened to the currentRow using pascal's logic of using the previous rows terms.
                term = prevRow[rowIndex] + prevRow[rowIndex + 1] 
                
                currentRow.append(term)
                
            # when all but the last term is created, add 1 for the last term.  
            currentRow.append(1)
            triangle.append(currentRow)  
        
    # print the triangle
    if n <= len(triangle):
        print('in second if statement since rows are already there')
        for i in range(0,n):
            print(triangle[i])
            
    

        

pascal(2)
pascal(1)
pascal(5)
pascal(3)
            
