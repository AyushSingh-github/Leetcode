class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        a = 0
        b =len(arr)-1
        l = []
        c = 0
        
        while c!=k:
            if abs(arr[a]-x) < abs(arr[b]-x):
                l.append(arr[a])
                a+=1
                c+=1
            elif abs(arr[a]-x) == abs(arr[b]-x):
                l.append(arr[a])
                a+=1
                c+=1
            else:
                l.append(arr[b])
                b-=1
                c+=1
                
        return sorted(l)
        '''
# * Binary Search and Two Pointers Solution | O(logn+k) Time | O(1) Space
# * n -> The length of arr array | k -> The given input

        insert_idx = bisect.bisect_left(arr, x)
        # * Using queue to build the result to support insertion from the front and the rear.
        queue = collections.deque([])
        left, right = insert_idx - 1, insert_idx
        while k:
            if left >= 0 and right < len(arr):
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    queue.appendleft(arr[left])
                    left -= 1
                else:
                    queue.append(arr[right])
                    right += 1
            elif left >= 0:
                queue.appendleft(arr[left])
                left -= 1
            elif right < len(arr):
                queue.append(arr[right])
                right += 1

            k -= 1

        return list(queue)