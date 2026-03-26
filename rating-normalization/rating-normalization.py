def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    mean = []
    for i in matrix:
        sum_per_user, count = 0, 0
        for j in i:
            if j!=0:
                count+=1
                sum_per_user+=j
        if count!=0:
            mean.append(sum_per_user/count)
        else:
            mean.append(0)
    print(mean)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=0:
                matrix[i][j]-=mean[i]
            else:
                matrix[i][j] = 0
    return matrix
            
            
    
            