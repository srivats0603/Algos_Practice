class Solution_count_negs:
  def countNegatives(self, grid):
    grid_size = (len(grid),len(grid[0]))
    if grid[grid_size[0]-1][grid_size[1]-1] >=0:
      return 0
    if grid[0][0] < 0:
      return (grid_size[0]*grid_size[1])
    neg_dict = {}
    total_negative = 0
    #find first negative number in each column, all the elements in that column in all the next rows will be negative
    for m in range(0,grid_size[0]):
      for n in range(0,grid_size[1]):
        if grid[m][n] < 0 :
          if n>0:
            neg_dict[m] = n
            break
          else:
            break
      if n == 0:
        break
    #print(neg_dict)
    if n == 0:
      total_negative = (grid_size[0]-m)*grid_size[1]
      #print("total negative rows {} and total negative elements now = {}".format(grid_size[0]-m,total_negative))
    for key in neg_dict.keys():
      total_negative += (grid_size[1]-neg_dict[key])
      #print("adding for row {} total negative elements {}".format(key,(grid_size[1]-neg_dict[key])))
      #print("total negative elements now =", total_negative)
    return total_negative