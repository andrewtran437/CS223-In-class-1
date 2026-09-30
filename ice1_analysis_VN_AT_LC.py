import anndata as ad
import pandas as pd

# from cs223_in_class1 import sort_funs
# from cs223_in_class1 import sort_funs
from sort_funs  import recursive_insertion_sort, binary_search_iterative, binary_search_recursive
from util_funs import *

# Load the .h5ad file into an AnnData object
adata = ad.read_h5ad("pbmc_sample.h5ad") 
# print(adata)
# print(adata.obs.columns[:100]) # View cell metadata column names (obs)
# print(adata.var.columns[:100]) # View gene/feature metadata column names (var)

def filter_mt_cells(anndata_obj, mt_exp_lvl_threshold,gene_exp_threshold,sort): 
    # pass
    obs_copy = anndata_obj.obs.copy()

    # sort the copy in descending order by Col 3 (percent_mito),
    # using the recursive insertion sort defined above
    if sort == 'recursive_insert':
        sorted_obs = recursive_insertion_sort(obs_copy, 'percent_mito')
    elif sort == 'iterative_insert':
        sorted_obs = iterative_insertion_sort(obs_copy, 'percent_mito')
    elif sort == 'recursive_selection':
        sorted_obs = recursive_selection_sort(obs_copy, 'percent_mito')
    elif sort == 'iterative_selection':
        sorted_obs = iterative_selection_sort(obs_copy, 'percent_mito')
    elif sort == 'recursive_merge':
        sorted_obs = recursive_merge_sort(obs_copy, 'percent_mito')
    elif sort == 'iterative_merge':
        sorted_obs = iterative_merge_sort(obs_copy, 'percent_mito')
    elif sort == 'recursive_quick':
        sorted_obs = recursive_quick_sort(obs_copy, 'percent_mito')
    elif sort == 'iterative_quick':
        sorted_obs = iterative_quick_sort(obs_copy, 'percent_mito')
    else:
        # sorted_obs = recursive_insertion_sort(obs_copy, 'percent_mito')
        sorted_obs = obs_copy.sort_values(by='percent_mito', ascending=False)

    keep_col = ((sorted_obs['percent_mito'] <= mt_exp_lvl_threshold) & (sorted_obs['n_genes'] >= gene_exp_threshold))
    cells_to_keep = sorted_obs.index[keep_col]
    filtered_adata = anndata_obj[cells_to_keep].to_memory() if anndata_obj.isbacked else anndata_obj[cells_to_keep].copy()

    return filtered_adata

# (7)(b) Sorting
#  Recursive insert sort by Col 3 (percent_mito)
filtered = filter_mt_cells(adata, mt_exp_lvl_threshold=0.1, gene_exp_threshold=200, sort='recursive_insert')\

# Iterative insert sort

# Recursive Selection sort
# Iterative Selection sort

# Recursive Merge sort
# Iterative Merge sort

# Recursive Quick sort
# Iterative Quick sort

# (7)(c) Binary Search (mitochondrial threshold filtering)
def filter_mt_threshold(sorted_obs, mt_exp_lvl_threshold):
    cutoff_idx = binary_search_recursive(sorted_obs, mt_exp_lvl_threshold)
    filtered_df = sorted_obs.iloc[cutoff_idx:].copy()
    return filtered_df

# print(filtered)
print(f"Cells before: {adata.n_obs}, Cells after: {filtered.n_obs}")

filtered.write_h5ad("pbmc_sample_filtered.h5ad")
filtered.obs.to_csv("pbmc_sample_filtered_obs.csv")

# (7)(d) Binary Search (mitochondrial threshold filtering)
