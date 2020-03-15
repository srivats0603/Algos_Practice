class Solution_hIndex:
  def hIndex(self, citations):
    num_papers = len(citations)
    if num_papers == 0:
      return 0
    citations.sort(reverse=True)
    hIndex = 0
    for i in range(0,num_papers):
      if citations[i]>=(i+1):
        hIndex = i+1 
    return hIndex   