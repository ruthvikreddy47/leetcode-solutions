class Solution:
    def topKFrequent(self, numbers, target):
        frequency = {}
        freqArr = [0] * (len(numbers) + 1)

        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1

        for key, val in frequency.items():
            index = freqArr[val]
            if isinstance(index, list):
                index.append(key)
            else:
                freqArr[val] = [key]

        result = []
        for arr in reversed(freqArr):
            if isinstance(arr, list):
                for num in arr:
                    result.append(num)
                    if target == len(result):
                        return result

        return result 