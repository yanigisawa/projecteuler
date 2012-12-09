#!/usr/local/bin/python

"""
Source code from: http://www.mathblog.dk/project-euler-51-eight-prime-family/


using System;
using System.Diagnostics;


namespace euler {
    class Problem51 {

        public static void Main(string[] args) {
            new Problem51().BruteForce();
        }
       
        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();

            int[][] fiveDigitPattern = get5digitPatterns();
            int[][] sixDigitPattern = get6digitPatterns();
            int result = int.MaxValue;
            
            for (int i = 11; i < 1000; i += 2) {
                
                //Only 1,3,7,9 are valid endings
                if (i % 5 == 0) continue;
                
                int[][] patterns = (i < 100) ? 
                    fiveDigitPattern : sixDigitPattern;

                for(int j = 0; j <patterns.GetLength(0); j++){
                    for(int k = 0; k <= 2; k++){

                        //Don't generate candidates with leading zero
                        if (patterns[j][0] == 0 && k == 0) continue;
                        
                        int[] pattern = fillPattern(patterns[j], i);
                        int candidate = generateNumber(k, pattern);
                                                
                        if (candidate < result && isPrime(candidate)) {
                            if (familySize(k, pattern) == 8)
                                result = candidate;                                                            
                            break;                            
                        }
                    }                   
                }
            }
              
            clock.Stop();
            Console.WriteLine("First prime in the eight prime family is {0}", result);            
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

        private int familySize(int repeatingNumber, int[] pattern) {
            int familySize = 1;
            
            for (int i = repeatingNumber + 1; i < 10; i++) {
                if (isPrime(generateNumber(i, pattern))) familySize++;                
            }

            return familySize;
        }

        private int[] fillPattern(int[] pattern, int number) {
            int[] filledPattern = new int[pattern.Length];            
            int temp = number;

            for (int i = filledPattern.Length - 1; 0 <= i; i--) {
                if (pattern[i] == 1) {
                    filledPattern[i] = temp % 10;
                    temp /= 10;
                } else {
                    filledPattern[i] = -1;
                }
            }
            return filledPattern;
        }

        private int generateNumber(int repNumber, int[] filledPattern) {
            int temp = 0;
            for (int i = 0; i < filledPattern.Length; i++) {
                temp = temp * 10;
                temp += (filledPattern[i] == -1) ? 
                    repNumber : filledPattern[i];
            }                        
            return temp;
        }

        private int[][] get5digitPatterns() {
            int[][] retVal = new int[4][];

            retVal[0] = new int[]{1,0,0,0,1};
            retVal[1] = new int[]{0,1,0,0,1};
            retVal[2] = new int[]{0,0,1,0,1};
            retVal[3] = new int[]{0,0,0,1,1};            

            return retVal;
        }

        private int[][] get6digitPatterns() {
            int[][] retVal = new int[10][];

            retVal[0] = new int[] { 1, 1, 0, 0, 0, 1 };
            retVal[1] = new int[] { 1, 0, 1, 0, 0, 1 };
            retVal[2] = new int[] { 1, 0, 0, 1, 0, 1 };
            retVal[3] = new int[] { 1, 0, 0, 0, 1, 1 };
            retVal[4] = new int[] { 0, 1, 1, 0, 0, 1 };
            retVal[5] = new int[] { 0, 1, 0, 1, 0, 1 };
            retVal[6] = new int[] { 0, 1, 0, 0, 1, 1 };
            retVal[7] = new int[] { 0, 0, 1, 1, 0, 1 };
            retVal[8] = new int[] { 0, 0, 1, 0, 1, 1 };
            retVal[9] = new int[] { 0, 0, 0, 1, 1, 1 };
          
            return retVal;
        }


        private bool isPrime(int n) {
            if (n <= 1) return false;            
            if (n == 2) return true;            
            if (n % 2 == 0) return false;            
            if (n < 9) return true;            
            if (n % 3 == 0) return false;
            
            int counter = 5;
            while ((counter * counter) <= n) {
                if (n % counter == 0) return false;                
                if (n % (counter + 2) == 0) return false;                
                counter += 6;
            }

            return true;
        }
     
    }
}

"""

import sys
sys.path.append("../helpers")
from primes import MillerRabin

    
def get5digitPatterns():
    retVal = []

    retVal.append([1,0,0,0,1])
    retVal.append([0,1,0,0,1])
    retVal.append([0,0,1,0,1])
    retVal.append([0,0,0,1,1])

    return retVal

def get6digitPatterns():
    retVal = []

    retVal.append([ 1, 1, 0, 0, 0, 1 ]) 
    retVal.append([ 1, 0, 1, 0, 0, 1 ])
    retVal.append([ 1, 0, 0, 1, 0, 1 ])
    retVal.append([ 1, 0, 0, 0, 1, 1 ])
    retVal.append([ 0, 1, 1, 0, 0, 1 ])
    retVal.append([ 0, 1, 0, 1, 0, 1 ])
    retVal.append([ 0, 1, 0, 0, 1, 1 ])
    retVal.append([ 0, 0, 1, 1, 0, 1 ])
    retVal.append([ 0, 0, 1, 0, 1, 1 ])
    retVal.append([ 0, 0, 0, 1, 1, 1 ])
    
    return retVal
    
def fillPattern(pattern, number):
    filledPattern, temp = [], number

    for i in range(len(pattern) - 1, -1, -1): # decrementing loop; -1 is step
        if (pattern[i] == 1): 
            filledPattern.append(temp % 10)
            temp = temp / 10
        else: 
            filledPattern.append(-1)
    return filledPattern

def generateNumber(repNumber, filledPattern):
    temp = 0
    for i in range(len(filledPattern)):
        temp = temp * 10

        if filledPattern[0] == -1: 
            temp += repNumber
        else:
            temp += filledPattern[i]
    return temp

def familySize(repeatingNumber, pattern):
    familySize = 1
    
    for i in range(repeatingNumber + 1, 10):
        if (isPrime(generateNumber(i, pattern))) : familySize += 1

    return familySize

def isPrime(n):
    if (n <= 1): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    
    counter = 5
    while ((counter * counter) <= n): 
        if (n % counter == 0): return False
        if (n % (counter + 2) == 0): return False
        counter += 6

    return True


def problem51():

    fiveDigitPattern = get5digitPatterns()
    sixDigitPattern = get6digitPatterns()
    result = 1000000

    for i in range(11, 1000):

        # Only 1,3,7,9 are valid endings
        if (i % 5 == 0): continue

        if (i < 100):
            patterns = fiveDigitPattern
        else:
            patterns = sixDigitPattern

        for j in range(len(patterns[0]) - 1):
            for k in range(3):

                # Don't generate candidates with leading zero
                if (patterns[j][0] == 0 and k == 0): continue

                pattern = fillPattern(patterns[j], i)
                candidate = generateNumber(k, pattern)
                print "Pattern: {0} - Candidate: {1}".format(patterns[j], candidate)

                if (candidate < result and isPrime(candidate)):
                    if (familySize(k, pattern) == 8):
                        result = candidate                                                            
                break
    print result
            

problem51()
#x = get5digitPatterns()
#print x[1]
#y = fillPattern(x[0], 15)
#print "Candidate: {0}".format(generateNumber(2, y))
