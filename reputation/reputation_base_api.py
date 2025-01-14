# MIT License
# 
# Copyright (c) 2018-2019 Stichting SingularityNET
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Abstract Reputation Service wrapper around
"""        

import os
import subprocess
from reputation_api import *
#from reputation_api import *

class ReputationServiceBase(RatingService,RankingService):

	def __init__(self, name, verbose=False):
		self.name = name #service parameter, no impact on algorithm, name of the storage scheme
		self.verbose = verbose #service parameter, no impact on algorithm, impact on log level 
		self.parameters = {}
		self.parameters['default'] = 0.5 # default (initial) reputation rank
		self.parameters['decayed'] = 0.0 # decaying (final) reputaion rank, may be equal to default one
		self.parameters['conservatism'] = 0.5 # blending factor between previous (default) rank and differential one 
		self.parameters['precision'] = 0.01 # Used to dound/up or round down financaial values or weights as value = round(value/precision)
		self.parameters['weighting'] = True # forces to weight ratings with financial values, if present
		self.parameters['denomination'] = False # forces to denominate weighted ratings with sum of weights
		self.parameters['fullnorm'] = True # full-scale normalization of incremental ratings
		self.parameters['liquid'] = True # forces to account for rank of rater
		self.parameters['logranks'] = True # applies log10 to ranks
		self.parameters['logratings'] = True # applies log10(1+value) to financial values and weights
		self.parameters['downrating'] = False # boolean option with True value to translate original explicit rating values in range 0.5-0.0 to negative values in range 0.0 to -1.0 and original values in range 1.0-0.5 to interval 1.0-0.0, respectively
		self.parameters['update_period'] = 1 # number of days to update reputation state, considered as observation period for computing incremental reputations
		self.parameters['aggregation'] = False #TODO support in Aigents, aggregated with weighted average of ratings across the same period
		self.parameters['unrated'] = False # whether to store default ranks of unrated agents and let them decay 
		self.parameters['ratings'] = 1.0 # to which extent account contribution of explicit and implicit ratings to reputation
		self.parameters['spendings'] = 0.0 # to which extent account contribution of spendings ("prrof-of-burn") to reputation
		self.parameters['parents'] = 0.0 # to which extent reputation of the "child" (product) is affected by the reputation of the "parent" (vendor)
		self.parameters['predictiveness'] = 0.0 # to which extent account rank is based on consensus between social consensus and ratings provided by the account
		self.parameters['rating_bias'] = False # whether to weigth ratings based on pessimism of the prior ratings
		

	"""
	Utility wrapper around get_ranks, returns None in case of error, so ranks  = get_ranks_dict(...) should be checked for None, and if it is None, the get_ranks(...) may be used to decipher the error code.
	Input: filter as dict of the following:
		date - date to provide the ranks
		ids - list of ids to retrieve the ranks
	Output:
		dictionary of key-value pairs with reputation "ranks" by "id" on success, None on error
	"""
	def get_ranks_dict(self,filter):
		ranks_dict = {}
		res, ranks = self.get_ranks(filter)
		if res != 0:
			return None
		for rank in ranks:
			ranks_dict[rank['id']] = rank['rank']
		return ranks_dict
	
	"""
	TODO: implement in derived imlementations
	"""
	def set_parent(self,parent_id,list_of_children_ids):
		return 0
	
