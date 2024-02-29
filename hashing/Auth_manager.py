'''
AuthenticationManager(int timeToLive) constructs the AuthenticationManager and sets the timeToLive.
generate(string tokenId, int currentTime) generates a new token with the given tokenId at the given currentTime in seconds.
renew(string tokenId, int currentTime) renews the unexpired token with the given tokenId at the given currentTime in seconds. 
If there are no unexpired tokens with the given tokenId, the request is ignored, and nothing happens.
countUnexpiredTokens(int currentTime) returns the number of unexpired tokens at the given currentTime.
'''

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # store timeToLive and create a dictionary
        self.token = dict()
        self.time = timeToLive  

        
    def generate(self, tokenId: str, currentTime: int) -> None:
        # store the tokenId with currentTime
        self.token[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        # calculate the limit time to filter unexpired token
        limit = currentTime - self.time

        #filter token and renew its Time
        if tokenId in self.token and self.token[tokenId] > limit:
            self.token[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        #calculate the limit time to filter unexpired tokens
        limit = currentTime - self.time
        c = 0
        for i in self.token:
            if self.token[i] > limit:
                c += 1
        return c
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        

    def process_expiry(self, currentTime: int) -> None:
        for tokenId, expiry in list(self.tokens.items()):
            if expiry <= currentTime:
                del self.tokens[tokenId]


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = self.ttl + currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return
        
        if self.tokens[tokenId] <= currentTime:
            self.process_expiry(currentTime)
            return
            
        del self.tokens[tokenId]
        self.generate(tokenId, currentTime)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.process_expiry(currentTime)
        return len(self.tokens) 
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)