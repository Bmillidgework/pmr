#Simple implementation of a kalman filter if I want to get round to that

from _future__import division
import numpy as np
import matplotlib.pyplot as plt

#A kalman filter is gaussian belief propagation in a linear dynamical system with a discrete vectorised state space. All beliefs are approximated by multivariate gaussians.

#The linear dynamical system is defined as follows:
# x(t) = Ax(t-1) + Bu(t) + e
#Where x(t) is the state at time t. A is the state transition matrix mapping x(t-1) to x(t). B is the control matrix which determines how controlled inputs to the system affect the dynamical evolution of thestate space. e is gaussian additive noise.
#We also receice measurements in the following format: z(t) = Cx(t) + d.
#Where z is the vector of measurements we receive. C is a matrix determining how the state of the system affects the measurements - i.e. how the measurements measure the system. d is another additive gaussian noise variable. 
#We initialise variables as follows

A = []
B = []
C = []
R = []
u_init = []

# Probably initialise as a multivariate gaussian with some values.
x_init = []


def Kalman_step(old_mu, old_sigma, control, measurement):
	#Update the beliefs about the system for a single timestep including a known control and a measurement of the system

	#get our intermediate mu
	mu_intermediate = np.dot(A, old_mu) + np.dot(B, control)
	#get our intermediate sigma
	sigma_intermediate = np.dot(np.dot(A, old_sigma), A.T) + R
	#compute the kalman gain
	K = np.dot(np.dot(sigma_intermediate, C.T), (np.linalg.inv(np.dot(np.dot(C, sigma_intermediate), C.T) + Q)))
	#compute updated mu taking into account the measurement
	new_mu = old_mu + np.dot(K, (measurement - np.dot(C, old_mu)))
	#compute updated sigma
	new_sigma = np.dot((np.identity, np.dot(K, C)), old_sigma)
	#return our results
	return new_mu, new_sigma
	

# The kalman filter can also be rewritten in terms of the canonical or natural representation of the gaussian. This type of filter is called the information filter, and is implemented below

def get_canonical_form(mu, sigma):
	#gets the canonical form in terms of omega, xi from the gaussian in moments form with mu sigma
	omega  = np.linalg.inv(sigma)
	xi = np.dot(omega, mu)
	return omega, xi

def get_moments_form(omega, xi):
	#gets the moments form of the gaussian when given the canonical form
	sigma = np.linalg.inv(omega)
	mu = np.dot(sigma, xi)
	return mu, sigma


def implementation_filter_step(xi, omega, control, measurement):
	om_inverse = np.linalg.inv(omega)
	#get intermediate omega - or precision matrix
	omega_intermediate = np.linalg.inv((np.dot(np.dot(A, omg_inverse), A.T) + R)
	#get intermediate xi
	xi_intermediate = np.dot(omega, (np.dot(np.dot(A, om_inverse), xi) + np.dot(B, u)))
	#get new omega and xi
	Q_inv = np.linalg.inv(Q)
	new_omega = np.dot(np.dot(C.T, Q_inv, C) + omega_intermediate
	new_xi = np.dot(np.dot(C, Q_inv), measurements) + xi_intermediate
	return new_xi, new_omega
	
