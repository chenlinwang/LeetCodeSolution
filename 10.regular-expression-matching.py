#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.55%)
# Likes:    4360
# Dislikes: 713
# Total Accepted:    442.9K
# Total Submissions: 1.7M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def compileAutomator(self, p: str) -> dict:
        if len(p) == 0:
            return {'start': None, 'end': None, 
                    'stateRules': {}, 'stateMaps': {} }
        else:
            start = set([p[0]])            
            end = set([])
            stateRules = {}
            stateMaps = {}            
            sameStateCount = {}

            def getStateName(token: str) -> str:
                ## setup the state count
                if token not in sameStateCount:
                    sameStateCount[token] = 0
                    return token
                else:
                    sameStateCount[token] += 1
                    return '{}{}'.format(token,sameStateCount[token])

            def getStateRuleSet(stateName: str) -> set:
                ## get the states
                if stateName not in stateRules:
                    stateTransitionRuleSet = set()
                    stateRules[stateName] = stateTransitionRuleSet
                return stateRules[stateName]
            
            def insertStateMap(stateName: str, token: str, tokenStateName: str) -> dict:
                if stateName not in stateMaps:
                    stateTransitionMap = dict()
                    stateMaps[stateName] = stateTransitionMap
                stateMap = stateMaps[stateName]

                if token not in stateMap:
                    stateMap[token] = []
                
                stateMap[token].append(tokenStateName)
            
            idx = 0
            last = len(p) - 1
            if idx >= last:
                return {'start': start, 'end': end, 
                    'stateRules': {}, 'stateMaps': {} }
            formerToken = p[idx]
            latterToken = p[idx+1]
            fsn = getStateName(formerToken)
            fsrs = getStateRuleSet(fsn)

            while True:
                idx += 1
                if latterToken == '*':
                    fsrs.add((formerToken,formerToken))                    
                    insertStateMap(fsn,formerToken,fsn)
                    if idx < last:
                        latterToken = p[idx+1]
                        if idx == 1:
                            start.add(latterToken)
                    else:
                        if idx >= 2:
                            if p[idx-2] != '*':
                                end.add(p[idx-2])
                            else:
                                if idx >= 3:
                                    end.add(p[idx-3])
                        end.add(formerToken)
                        break
                else:
                    lsn = getStateName(latterToken)
                    fsrs.add((formerToken, latterToken))
                    insertStateMap(fsn,latterToken,lsn)
                    if idx < last:
                        formerToken = latterToken
                        fsn = lsn
                        fsrs = getStateRuleSet(fsn)
                        latterToken = p[idx+1]
                    else:
                        end.add(latterToken)
                        break
            return {'start': start, 'end': end, 
                    'stateRules': stateRules, 'stateMaps': stateMaps }

    def isMatch(self, s: str, p: str) -> bool:
        # edge case
        if len(s) == 0:
            return True if len(p) == 0 else False

        automator = self.compileAutomator(p)
        print(automator)
        start = automator['start']
        end = automator['end']
        stateMaps = automator['stateMaps']
        stateRules = automator['stateRules']
        # check start and end
        if s[0] not in start and '.' not in start:
            return False
        elif s[-1] not in end and '.' not in end:
            return False
        else:
            idx = 0
            last = len(s) - 1
            if idx >= last:
                return len(stateRules) == 0
            
            formerToken = s[idx]
            latterToken = s[idx+1]
            fsn = formerToken

            def checkForNextTransition(idx:int, formerToken:str, fsn: str, latterToken: str) -> bool:
                print("f:{},fsn:{},l:{}".format(formerToken, fsn, latterToken))
                if fsn not in stateRules and '.' not in stateRules:                    
                    return False
                else:
                    if fsn in stateRules:
                        fsrs = stateRules[fsn]
                    else:
                        fsrs = stateRules['.']
                    print('checking ({},{}) in {}'.format(formerToken,latterToken,fsrs))
                    if (formerToken,latterToken) not in fsrs and (formerToken,'.') not in fsrs and ('.',latterToken) not in fsrs and ('.','.') not in fsrs:
                        return False
                    else:
                        idx += 1     
                        if idx < last:                            
                            latterLatterToken = s[idx+1]
                            fm = stateMaps[fsn]
                            possibleNextStateNames = fm[latterToken]
                            for lsn in possibleNextStateNames:
                                result = checkForNextTransition(idx,latterToken, lsn, latterLatterToken)
                                if result:
                                    return True
                            return False
                        else:
                            return True            
            return checkForNextTransition(idx, formerToken, fsn, latterToken)
# @lc code=end