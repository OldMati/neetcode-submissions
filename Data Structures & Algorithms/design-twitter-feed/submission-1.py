import heapq

class Twitter:

    def __init__(self):
        self.followers = {}
        self.following = {}
        self.feed = {} # userId => list of postids
        self.curr_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.feed:
            # if len(self.feed[userId]) == 10
            self.feed[userId].append((self.curr_time, tweetId))
        else:
            self.feed[userId] = [(self.curr_time, tweetId)]
        self.curr_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.feed.get(userId, [])
        heap = feed[:]
        following = self.following.get(userId, [])
        print()
        print(f'{userId=}')
        print(f'{following=}')
        for follower in following:
            heap.extend(self.feed.get(follower, []))
        
        print('feed heap: ', heap)
        print()
        res = []
        # heapify heap by greatest time added
        heapq.heapify_max(heap)
        while len(heap) > 0 and len(res) < 10:
            res.append(heapq.heappop_max(heap)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set([followeeId])
        
        if followeeId in self.followers:
            self.followers[followeeId].add(followerId)
        else:
            self.followers[followeeId] = set([followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)