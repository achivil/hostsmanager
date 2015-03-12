#! /usr/bin/env python

import sys

"""
def initHosts():
    defaultGroupName = 'default'
    newLine = '# group: default'
"""

class hostsGroup:
    def __init__(self):
        self.active = ''
        self.choosen = ''
        self.groupsDict = {}
        self.__readFile()

    def setChoosen(self, groupName):
        self.choosen = groupName

    def alterActive(self):
        if self.active == self.choosen:
            return
        else:
            self.deactiveGroup()
            self.active = self.choosen
            self.activeGroup()
        self.__writeFile()

    def activeGroup(self):
        print self.groupsDict
        group = self.groupsDict[self.active]
        newGroup = []
        for item in group:
            newGroup.append(item.split('# ')[1])
        print 'active group : ', self.active
        self.groupsDict[self.active] = newGroup

    def deactiveGroup(self):
        group = self.groupsDict[self.active]
        newGroup = []
        for item in group:
            print item
            newGroup.append('# ' + item)
        print 'deactive group : ', self.active
        self.groupsDict[self.active] = newGroup

    def __readFile(self):
        # filepath = '/etc/hosts'
        filepath = 'hosts'
        with open(filepath, 'rb') as f:
            groupItem = {}
            for line in f.readlines():
                # print line
                if '# group' in line:
                    if groupItem.has_key('groupName'):
                        if groupItem['hostList'][0][0] != '#':
                            self.active = groupItem['groupName']
                        self.groupsDict[groupItem['groupName']] = groupItem['hostList'];
                        groupItem = {}
                    groupName = (line.split(':')[1])[1:-1]
                    print groupName
                    groupItem['groupName'] = groupName
                    groupItem['hostList'] = []
                    continue
                if line and line != '\n':
                    groupItem['hostList'].append(line)
            if groupItem['hostList'][0][0] != '#':
                self.active = groupItem['groupName']
            self.groupsDict[groupItem['groupName']] = groupItem['hostList'];

    def __writeFile(self):
        filepath = 'hosts'
        with open(filepath, 'wb') as f:
            for key in self.groupsDict.keys():
                groupInfo = '# group: ' + key + '\n'
                print groupInfo
                f.write(groupInfo)
                for item in self.groupsDict[key]:
                    print item
                    f.write(item)
        print 'Done'



def main():
    argvs = sys.argv
    useGroup = argvs[1]

    group = hostsGroup()
    group.setChoosen(useGroup)
    group.alterActive()


if __name__ == '__main__':
    main()
