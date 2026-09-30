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
