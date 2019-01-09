import unittest
from Secret_santa import *

class Test_Secret_santa(unittest.TestCase):
    

    #Helper functions 
    def compare_arrays(self,list1,list2):
        #returns whether or not both lists are equal to each other.
        if len(set(list1)) != len(set(list2)):
            return False
        else: 
            inds = list(set(list1))
            for x in inds:
                if list1.count(x) != list2.count(x):
                    return False
            return True

    def helper_completeness_checker(self,my_dict,inputs_from_test):
        #validates that all names have been used as a Santa 
        #and all names have been used as a kid
        names = list(inputs_from_test.keys())
        santas = list(my_dict.keys())
        kids = []
        for santa in santas:
            kids.append(my_dict[santa])
        return  ( self.compare_arrays(names,santas) and self.compare_arrays(names,kids) )


    def test_randomize_names_completeness(self):
        print("Testing completeness of the randomize_names function \n")
        #Test randomize_names makes sure that all names have been used as a Santa 
        #and all names have been used as a kid
        inputs = [
            {"a":"random_email@rn.com","b":"random_email@rn.com","c":"random_email@rn.com","d":"random_email@rn.com","e":"random_email@rn.com"},
            {"a":"random_email@rn.com","b":"random_email@rn.com","c":"random_email@rn.com","d":"random_email@rn.com","e":"random_email@rn.com","f":"random_email@rn.com","g":"random_email@rn.com"},
            {"a":"random_email@rn.com","b":"random_email@rn.com","c":"random_email@rn.com"}
        ]
        for x in inputs:
            obtained_dict = randomize_names(x)
            self.assertTrue(self.helper_completeness_checker(obtained_dict,x))
