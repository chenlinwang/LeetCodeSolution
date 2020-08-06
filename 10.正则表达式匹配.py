#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.01%)
# Likes:    1430
# Dislikes: 0
# Total Accepted:    104.5K
# Total Submissions: 348.2K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
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
            end = set()
            stateRules = {}
            stateMaps = {}            
            sameStateCount = {}
            stateNameMappings = {}            

            def getStateName(token: str) -> str:
                ## setup the state count
                if token not in sameStateCount:
                    sameStateCount[token] = 0
                    return token
                else:
                    sameStateCount[token] += 1
                    return '{}{}'.format(token,sameStateCount[token])
            
            last = len(p)
            if last >= 4:
                idx = 2
                np = p[:2]
                while idx < last-1:
                    if p[idx] == p[idx-2] and p[idx-1] == '*' and p[idx+1] == '*':
                        idx += 2
                    else:
                        np += p[idx]
                        idx += 1
                if idx < last:
                    np += p[idx]              
                # print("{} optimized to {}".format(p,np))
                p = np
            for idx in range(len(p)):
                if p[idx] != '*':
                    sn = getStateName(p[idx])
                    stateNameMappings[idx] = sn
            if p[len(p)-1] != '*':
                end.add(stateNameMappings[len(p)-1])

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
                    stateMap[token] = set()
                
                stateMap[token].add(tokenStateName)
            
            idx = 0
            last = len(p) - 1
            if idx >= last:
                return {'start': start, 'end': end, 
                    'stateRules': {}, 'stateMaps': {} }
            formerToken = p[idx]
            latterToken = p[idx+1]
            fsn = stateNameMappings[idx]
            fsrs = getStateRuleSet(fsn)          

            while True:
                if latterToken == '*':
                    fsrs.add((formerToken,formerToken))
                    insertStateMap(fsn,formerToken,fsn)
                    # move on
                    idx += 1
                    if idx < last:
                        latterToken = p[idx+1]
                        lsn = stateNameMappings[idx+1]
                        # need to back fire to add the new rule and maps
                        jdk = idx
                        while jdk >= 2:
                            if  p[jdk] == '*':
                                if p[jdk-2] != '*':
                                    sn = stateNameMappings[jdk-2]
                                    srs = getStateRuleSet(sn)
                                    srs.add((p[jdk-2],latterToken))
                                    insertStateMap(sn,latterToken,lsn)
                                    break
                                else:
                                    sn = stateNameMappings[jdk-3]
                                    srs = getStateRuleSet(sn)
                                    srs.add((p[jdk-3],latterToken))
                                    insertStateMap(sn,latterToken,lsn)
                                    jdk -= 2
                        if jdk == 1 and p[jdk] == '*':
                            start.add(lsn)
                        if idx == 1:
                            start.add(lsn)
                    else:
                        end.add(fsn)
                        # need to back fire to add the new rule and maps
                        jdk = idx
                        while jdk >= 0:
                            if p[jdk] == '*':                                                           
                                end.add(stateNameMappings[jdk-1])
                                jdk -= 2
                            else:
                                end.add(stateNameMappings[jdk])
                                break
                        break
                else:
                    lsn = stateNameMappings[idx+1]
                    fsrs.add((formerToken, latterToken))
                    insertStateMap(fsn,latterToken,lsn)
                    # move on
                    idx += 1
                    if idx < last:                        
                        formerToken = latterToken
                        fsn = lsn
                        fsrs = getStateRuleSet(fsn)
                        latterToken = p[idx+1]
                    else:
                        end.add(lsn)
                        break
            return {'start': start, 'end': end, 
                    'stateRules': stateRules, 'stateMaps': stateMaps }

    def isMatch(self, s: str, p: str) -> bool:        
        #edge case
        if len(p) == 0:
            return True if len(s) == 0 else False

        automator = self.compileAutomator(p)
        # print(automator)        
        start = automator['start']
        end = automator['end']
        stateMaps = automator['stateMaps']
        stateRules = automator['stateRules']
        # edge case
        if len(s) == 0:
            if p[-1] != '*':
                return False
            intersetStartEnd = start.intersection(end)            
            for n in intersetStartEnd:
                srs = stateRules[n]            
                if (n,n) in srs:
                    sm = stateMaps[n]
                    nn = sm[n]                    
                    if n in nn:
                        return True
            return False
        # check start and end
        if s[0] not in start and '.' not in start:
            return False
        else:
            idx = 0
            last = len(s) - 1
            if idx >= last:
                intersetStartEnd = start.intersection(end)
                if s[0] in intersetStartEnd:
                    return True
                else:
                    for i in intersetStartEnd:
                        if i[0] == '.':
                            return True
                    return False

            formerToken = s[idx]
            latterToken = s[idx+1]            
            def checkForNextTransition(idx:int, formerToken:str, fsn: str, latterToken: str) -> bool:
                # print("f:{},fsn:{},l:{}".format(formerToken, fsn, latterToken))
                if fsn not in stateRules:                    
                    return False
                else:                    
                    fsrs = stateRules[fsn]                    
                    # print('checking ({},{}) in {}'.format(formerToken,latterToken,fsrs))
                    if (formerToken,latterToken) not in fsrs and (formerToken,'.') not in fsrs and ('.',latterToken) not in fsrs and ('.','.') not in fsrs:
                        return False
                    else:                        
                        fm = stateMaps[fsn]
                        possibleNextStateNames = set()
                        if latterToken in fm:
                            possibleNextStateNames = possibleNextStateNames.union(fm[latterToken])
                        if '.' in fm:
                            possibleNextStateNames = possibleNextStateNames.union(fm['.'])
                        # print(possibleNextStateNames)
                        idx += 1     
                        if idx < last:                            
                            latterLatterToken = s[idx+1]                                        
                            for lsn in possibleNextStateNames:
                                result = checkForNextTransition(idx,latterToken, lsn, latterLatterToken)
                                if result:                                
                                    return True
                            return False
                        else:
                            for lsn in possibleNextStateNames:
                                if lsn in end:
                                    return True
                            return False
            for fsn in start:
                result = checkForNextTransition(idx,formerToken,fsn,latterToken)
                if result:
                    return True
            return False

if __name__ == '__main__':
    s = Solution()    
    print(s.isMatch('ab','c*b*b*.*ac*.*bc*a*'))
# @lc code=end