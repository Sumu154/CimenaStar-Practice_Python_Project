# 
class StarCinema:
  hall_list = []
  
  @classmethod
  def entry_hall(self, hall):
    self.hall_list.append(hall)
    print(hall.rows)



class Hall:
  def __init__(self, hall_no, rows, cols) -> None:
    self.hall_no = hall_no
    self.rows = rows
    self.cols = cols
    self.seats = {}
    self.show_list = []         # haller shb show thakbe etar vitor
    StarCinema.entry_hall(self)

 
  def entry_show(self, show_id, movie_name, time):
    show = (show_id, movie_name, time)
    self.show_list.append(show)
    

    self.seats[show_id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    print(f"Show {show_id} - '{movie_name}' added at {time} in hall {self.hall_no}")


  def book_seats(self, show_id, seat_pos):
    if show_id not in self.seats:
      print('Invalid show ID')
      return
    
    for i,j in seat_pos:
      if i<0 or i>=self.rows or j<0 or j>=self.cols:
        print(f"Invalid seat position: row {i}, col {j}.")
        continue
      
      if self.seats[show_id][i][j] == 1:
        print(f"Seat Row {i}, Col {j} is already booked.")
      else:
        self.seats[show_id][i][j] = 1
        print(f"Seat Row {i}, Col {j} booked successfully.")
    
    print('Updating seat matrix...')
    for i in range(self.rows):
      print('\t', end='')    # Add a single left-side tab before each row
      for j in range(self.cols):
          print(self.seats[show_id][i][j], end=' ')
      print() 


  def view_show_list(self):
    print('ID \t Movie Name \t Time')
    for i in self.show_list:
        print(f"{i[0]} \t {i[1]} \t\t {i[2]}")
    print('\n')


  def view_available_seats(self, show_id):
    if show_id not in self.seats:
      print("Invalid show ID.")
      return
    
    # show as a list
    print(f"\tAvailable seats for show {show_id}:")
    for i in range(self.rows):
      for j in range(self.cols):
        if self.seats[show_id][i][j] == 0:
            print(f"\tSeat ({i}, {j})")
    
    print()

    # show as a matrix
    for i in range(self.rows):
      print('\t', end='')  # Add a single left-side tab before each row
      for j in range(self.cols):
          print(self.seats[show_id][i][j], end=' ')
      print() 


# end of class Hall



h1 = Hall(1, 4, 4)
h1.entry_show(1, 'jawan', '2/10/2024')

run = True
while(run):
  print('Welcome! Here are the options')
  print('1: VIEW ALL SHOW TODAY')
  print('2: VIEW AVAILABLE SEATS')
  print('3: BOOK TICKET')
  print('4: EXIT')

  choice = int(input('\tEnter option: '))
  if choice==1:
    h1.view_show_list()
  elif choice==2:
    show_id = int(input('\tEnter show id: '))
    h1.view_available_seats(show_id)
  elif choice==3:
    show_id = int(input('\tEnter show id: '))
    row = int(input('\tEnter row: '))
    col = int(input('\tEnter col: '))
    h1.book_seats(show_id, [(row,col)])
  elif choice==4:
    break





