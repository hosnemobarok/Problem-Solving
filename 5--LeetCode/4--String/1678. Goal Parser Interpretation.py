class Solution:
    def interpret(self, command: str) -> str:
        a = command.replace('()', 'o')
        return a.replace('(al)', 'al')