import numpy as np

#Data Preprocessing - Estimate the Transition Probability Matrices
# Using the Change Matrices (tabulate areas) from ArcGIS

change_matrices = {
    '00to06': np.array([
        [745267500, 10395000, 4477500, 0, 22500], # From Tereny antropogeniczne 2000
        [269460000, 3230437500, 205605000, 1080000, 1282500], # From Tereny rolne 2000
        [4320000, 7222500, 1529617500, 0, 1417500], # From Lasy i ekosystemy seminaturalne 2000
        [0, 0, 0, 5490000, 0], # From Obszary podmokłe 2000
        [90000, 0, 450000, 0, 87997500] # From Obszary wodne 2000
    ]),
    '06to12': np.array([
        [997470000, 16290000, 4882500, 0, 495000], # From Tereny antropogeniczne 2006
        [80887500, 3106755000, 58072500, 517500, 1822500],  # From Tereny rolne 2006
        [5467500, 16470000, 1715287500, 67500, 2857500], # From Lasy i ekosystemy seminaturalne 2006
        [0, 67500, 607500, 5895000, 0], # From Obszary podmokłe 2006
        [585000, 1755000, 1507500, 0, 86872500] # From Obszary wodne 2006
    ]),
    '12to18': np.array([
        [1082902500, 1192500, 315000, 0, 0], # From Tereny antropogeniczne 2012
        [24277500, 3115080000, 1980000, 0, 0], # From Tereny rolne 2012
        [2340000, 3172500, 1774845000, 0, 0], # From Lasy i ekosystemy seminaturalne 2012
        [0, 0, 0, 6480000, 0], # From Obszary podmokłe 2012
        [0, 247500, 0, 0, 91800000] # From Obszary wodne 2012
    ])
}

# Function to normalize the matrix by dividing each row by the sum of its elements
def normalize_matrix(change_matrix):
    row_sums = np.sum(change_matrix, axis=1)
    return change_matrix / row_sums[:, np.newaxis]

# Normalize each of the change matrices
normalized_matrices = {key: normalize_matrix(matrix) for key, matrix in change_matrices.items()}

# Set print options for matrices
np.set_printoptions(precision=3, suppress=True)

# Display the normalized transition matrices
for period, normalized_matrix in normalized_matrices.items():
    print(f"Normalized transition matrix ({period}):")
    print(normalized_matrix)

