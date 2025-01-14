# MIT License
# 
# Copyright (c) 2019 Stichting SingularityNET
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

# Reputation Scenario Test Data Generation
import time

# import datetime
from datetime import date
from reputation_buying import reputation_simulate
from reputation_service_api import *
from aigents_reputation_api import AigentsAPIReputationService

def dict_sorted(d):
	first = True
	s = "{"
	for key, value in sorted(d.items(), key=lambda x: x[0]): 
		template = "'{}': {}" if first else ", '{}': {}"
		s += template.format(key, value)
		first = False
	s += "}"
	return s


good_transactions = 1
bad_transactions = 1
threshold = 40 # 3-4-5 stars
#threshold = 60 # 4-5 stars
#threshold = 80 # 5 stars

good_agent = {"buyers":[1,800], "products":[1001,1800], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[801,1000], "products":[1801,2000], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 1001

good_agent = {"buyers":[1,400], "products":[1001,1400], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[401,500], "products":[1401,1500], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 501

good_agent = {"buyers":[1,80], "products":[101,180], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[81,100], "products":[181,200], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 101

#good_agent = {"buyers":[1,80], "products":[101,180], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
#bad_agent = {"buyers":[81,100], "products":[191,200], "qualities":[0.0,0.25], "transactions": bad_transactions}
#days = 51

#good_agent = {"buyers":[1,8], "products":[11,18], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
#bad_agent = {"buyers":[9,10], "products":[19,20], "qualities":[0.0,0.25], "transactions": bad_transactions}
#days = 11

good_agent = {"buyers":[1,3], "products":[6,8], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[4,5], "products":[9,10], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 5

#rs = AigentsAPIReputationService('http://localtest.com:1180/', 'john@doe.org', 'q', 'a', False, 'test', True)
rs = PythonReputationService()
rs.set_parameters({'fullnorm':True,'weighting':False,'logratings':False,'denomination':False,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
verbose = True


"""
# Blending Anti-biased with Predictiveness

print("RS=Anti-biased_def5_dec5_c9", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':0.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.9,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':0.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased_def5_dec5_c1", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':0.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.1,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Predictive_def5_dec5_c9", end =" ")
rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.9,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Predictive_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Predictive_def5_dec5_c1", end =" ")
rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.1,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Pred+A-B_def5_dec5_c9", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.9,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Pred+A-B_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Pred+A-B_def5_dec5_c1", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.1,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
"""

"""
# Exploring Anti-biased

print("RS=Anti-biased_def5_dec5_c5_P", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

rs = AigentsAPIReputationService('http://localtest.com:1180/', 'john@doe.org', 'q', 'a', False, 'test', True)
rs.set_parameters({'fullnorm':True,'weighting':False,'logratings':False,'denomination':False,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})

print("RS=Anti-biased_def5_dec5_c5_J", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
"""



# Exploring threshold and PLRo 

#print("RS=A-B_def5_dec5_c9", end =" ")
#rs.set_parameters({'rating_bias':True,'predictiveness':0.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.9,'ratings':1.0,'spendings':0.0})
#print("RS=Pred_def5_dec5_c1", end =" ")
#rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.1,'ratings':1.0,'spendings':0.0})

for threshold in [40,60,80]:
	print('threshold='+str(threshold))
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 0, None, verbose)	
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 0, rs, verbose)	
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 50, rs, verbose)
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 70, rs, verbose)
	reputation_simulate(good_agent,bad_agent, date(2018, 1, 1), days, True, threshold, 100, rs, verbose)


"""
# Exploring PLRo-s and different RS-es except Predictive so far

print("RS=None", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 0, None, verbose)

print("RS=Regular", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 0, rs, verbose)

print("RS=Regular", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Regular", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 70, rs, verbose)

print("RS=Regular", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 100, rs, verbose)
"""

"""
# For grand presentation
rs = AigentsAPIReputationService('http://localtest.com:1180/', 'john@doe.org', 'q', 'a', False, 'test', True)
rs.set_parameters({'fullnorm':True,'weighting':False,'logratings':False,'denomination':False,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})

print("RS=None", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 0, None, verbose)

print("RS=Regular", end =" ")
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Weighted", end =" ")
rs.set_parameters({'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=TOM-based", end =" ")
rs.set_parameters({'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':True ,'default':0.0,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
	
print("RS=SOM-based", end =" ")
rs.set_parameters({'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.0,'decayed':0.5,'ratings':0.5,'spendings':0.5})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased_def5_dec5_c9", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.9,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Predictive_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Predictive_def9_dec1_c1", end =" ")
rs.set_parameters({'rating_bias':False,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.9,'decayed':0.1,'conservatism':0.1,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased&Predictive_def5_dec5_c5", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)

print("RS=Anti-biased&Predictive_def9_dec1_c5", end =" ")
rs.set_parameters({'rating_bias':True,'predictiveness':1.0,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.9,'decayed':0.1,'conservatism':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
"""

"""
# Testing Predictiveness
rs = AigentsAPIReputationService('http://localtest.com:1180/', 'john@doe.org', 'q', 'a', False, 'test', True)
rs.set_parameters({'fullnorm':True,'weighting':False,'logratings':False,'denomination':False,'unrated':False,'default':0.5,'decayed':0.5,'conservatism':0.5,'ratings':1.0,'spendings':0.0})

print("RS=Predictive0.5_c0.5", end =" ")
rs.set_parameters({'predictiveness':0.5,'conservatism':0.5,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive1.0_c0.5", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.5,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive1.0_c0.9", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.9,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive1.0_c0.1", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.1,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive_c0.1_def0.1", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.1,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.1,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive_c0.1_def0.9", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.1,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.9,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive_c0.1_dec0.1", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.1,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.1,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
print("RS=Predictive_c0.1_dec0.9", end =" ")
rs.set_parameters({'predictiveness':1.0,'conservatism':0.1,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False ,'default':0.5,'decayed':0.9,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
"""

"""
# Testing Parents
rs = AigentsAPIReputationService('http://localtest.com:1180/', 'john@doe.org', 'q', 'a', False, 'test', True)
print("RS=Parents1.0", end =" ")
rs.set_parameters({'parents':1.0,'predictiveness':0.0,'rating_bias':False,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, threshold, 30, rs, verbose)
"""


"""
# Confirming effect of "gaming competition cutting gaming profits"

good_agent = {"buyers":[1,80], "products":[201,280], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[81,100], "products":[281,300], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 20

print("RS=Biased", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, 80, 30, rs, verbose)

good_agent = {"buyers":[1,80], "products":[201,280], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[81,120], "products":[281,320], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 20

print("RS=Biased", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, 80, 30, rs, verbose)

good_agent = {"buyers":[1,80], "products":[201,280], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[81,140], "products":[281,340], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 20

print("RS=Biased", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, 80, 30, rs, verbose)

good_agent = {"buyers":[1,80], "products":[201,280], "qualities":[0.5,0.75,1.0], "transactions": good_transactions}
bad_agent = {"buyers":[81,160], "products":[281,360], "qualities":[0.0,0.25], "transactions": bad_transactions}
days = 20

print("RS=Biased", end =" ")
rs.set_parameters({'rating_bias':True,'fullnorm':True,'weighting':True ,'logratings':False,'denomination':True ,'unrated':False,'default':0.5,'decayed':0.5,'ratings':1.0,'spendings':0.0})
reputation_simulate(good_agent,bad_agent, datetime.date(2018, 1, 1), days, True, 80, 30, rs, verbose)
"""


if rs is not None:
	del rs
