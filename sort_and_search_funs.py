def binary_search_iterative(sorted_obs, mt_exp_lvl_threshold):
    """
    Iteratively finds the index of the first row in a DataFrame where the value
    in the 'percent_mito'(Col 3) column is less than or equal to a given threshold.
    """
    low = 0
    high = len(sorted_obs) - 1
    result = len(sorted_obs)

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_obs.iloc[mid]['percent_mito']

        if mid_value <= mt_exp_lvl_threshold:
            result = mid       # qualifies - look left
            high = mid - 1
        else:
            low = mid + 1      # too high - move right

    return result

def binary_search_recursive(sorted_obs, mt_exp_lvl_threshold, low=0, high=None):
    """
    Recursively finds the index of the first row in a DataFrame where the value
    in the 'percent_mito'(Col 3) column is less than or equal to a given threshold.

    """
    if high is None:
        high = len(sorted_obs) - 1

    if low > high:
        return low  # insertion point = first index satisfying the condition

    mid = (low + high) // 2
    mid_value = sorted_obs.iloc[mid]['percent_mito']

    if mid_value <= mt_exp_lvl_threshold:
        return binary_search_recursive(sorted_obs, mt_exp_lvl_threshold, low, mid - 1) # qualifies — search left half for an earlier qualifying index
    else:
        return binary_search_recursive(sorted_obs, mt_exp_lvl_threshold, mid + 1, high) # too high — search right half

def insert_sort_iter(df, column, reverse=False):
    """
    Iteratively sorts DataFrame rows by column name
    Parameters:
    - df: input DataFrame to sort
    - column: name of column header to sort by
    - reverse: False for asending, True for descending 

    Output:
    - pd.DataFrame: a new sorted DataFrame with the original row names
    """
    records = df.to_dict('records')
    names = df.index.tolist()  
    n = len(records)

    for i in range(1, n):
        current_record = records[i]
        current_name = names[i]
        key_val = current_record[column]
        j = i - 1

        if reverse:
            while j >= 0 and records[j][column] < key_val:
                records[j + 1] = records[j]
                names[j + 1] = names[j]
                j -= 1
        else:
            while j >= 0 and records[j][column] > key_val:
                records[j + 1] = records[j]
                names[j + 1] = names[j]
                j -= 1 

        records[j + 1] = current_record
        names[j + 1] = current_name

    return pd.DataFrame(records, index=names) 

def insert_sort_rec(df, column, reverse=False, records=None, names=None, n=None):
    """
    Recursively sorts the first n - 1 rows before placing the nth record 
    """
    if records is None:
        records = df.to_dict('records')
        names = df.index.tolist()  
        n = len(records)

    if n <= 1:
        return pd.DataFrame(records, index=names)

    insert_sort_rec(df, column, reverse=reverse, records=records, names=names, n=n - 1)

    last_record = records[n - 1]
    last_name = names[n - 1]
    key_val = last_record[column]
    j = n - 2

    if reverse:
        while j >= 0 and records[j][column] < key_val:
            records[j + 1] = records[j]
            names[j + 1] = names[j]
            j -= 1
    else:
        while j >= 0 and records[j][column] > key_val:
            records[j + 1] = records[j]
            names[j + 1] = names[j]
            j -= 1

    records[j + 1] = last_record
    names[j + 1] = last_name

    return pd.DataFrame(records, index=names)

def selection_sort_iter(df, column, reverse=False):
    """
    Iteratively finds the target column value in unsorted rows and swaps row records
    """
    records = df.to_dict('records')
    names = df.index.tolist()  
    n = len(records)

    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if reverse:
                if records[j][column] > records[target_idx][column]:
                    target_idx = j
            else:
                if records[j][column] < records[target_idx][column]:
                    target_idx = j

        records[i], records[target_idx] = records[target_idx], records[i]
        names[i], names[target_idx] = names[target_idx], names[i]

    return pd.DataFrame(records, index=names)

def selection_sort_rec(df, column, reverse=False, records=None, names=None, index=0):
    """
    Recursively tracks the scan index, swapping row records before the next call
    """
    if records is None:
        records = df.to_dict('records')
        names = df.index.tolist()  

    n = len(records)

    if index >= n - 1:
        return pd.DataFrame(records, index=names)

    target_idx = index
    for j in range(index + 1, n):
        if reverse:
            if records[j][column] > records[target_idx][column]:
                target_idx = j
        else:
            if records[j][column] < records[target_idx][column]:
                target_idx = j

    records[index], records[target_idx] = records[target_idx], records[index]
    names[index], names[target_idx] = names[target_idx], names[index]

    return selection_sort_rec(df, column, reverse=reverse, records=records, names=names, index=index + 1)
