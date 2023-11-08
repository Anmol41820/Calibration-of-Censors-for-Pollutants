import numpy as np
import pickle as pkl

# Define your prediction method here

def my_fit( Z_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your model using training CRPs
	# The first 64 columns contain the config bits
	# The next 4 columns contain the select bits for the first mux
	# The next 4 columns contain the select bits for the second mux
	# The first 64 + 4 + 4 = 72 columns constitute the challenge
	# The last column contains the response
	
	### start code ###
	R = 64
	S = 4

	# Slicing the data into various parts
	X = Z_train[:, 0:R]
	S1 = Z_train[:, R:R+S]
	S2 = Z_train[:, R+S:R+S+S]
	Y = Z_train[:, -1].reshape(Z_train.shape[0],1)

	# finding the decimal values from the binary values of the XOROR's number
	L1 = np.dot(S1, 2**np.arange(S-1,-1,-1)).reshape(-1,1)
	L2 = np.dot(S2, 2**np.arange(S-1,-1,-1)).reshape(-1,1)

	# modifing the values - mainly swapping the l1 and l2 and reversing the answer bit(y) if l1 > l2 
	condition = L1 < L2
	L1_new = np.where(condition, L1, L2)
	L2_new = np.where(condition, L2, L1)
	Y = np.where(condition, Y, 1-Y)

	# Creating m that is the linear model corroesponding to that treining example
	M = L2_new - 1 + (L1_new * (2 * 2**S - L1_new - 3)) / 2
	M_value = 2**(S-1) * (2**S - 1)


	indices = [np.where(M == i)[0] for i in range(M_value)]
	model = [LinearSVC(fit_intercept=True, max_iter=5000, penalty= 'l2', loss='squared_hinge', tol=1e-7, C=1.0, intercept_scaling = 2).fit(X[indices[i]], Y[indices[i]].ravel()) for i in range(M_value)]
	### end code ###

	return model					# Return the trained model


# df is a dataframe containing timestamps, weather data and potentials

def my_predict( df ):
	
	# Load your model file
	
	# Make two sets of predictions, one for O3 and another for NO2
	
	# Return both sets of predictions
	return ( pred_o3, pred_no2 )