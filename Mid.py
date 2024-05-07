class Star_Cinema:
     Hall_list = []
     def entery_hall(self, hall):
          self.Hall_list.append(hall)

class Hall(Star_Cinema):
     def __init__(self, rows, cols, hall_no) -> None:
          super().__init__()
          self.seats = {}
          self.show_list = []
          self.rows = rows
          self.cols = cols
          self.hall_no = hall_no
          self.entery_hall(self)

     def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        allocation = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = allocation

     def book_seats(self, id, seat_no):
          if id not in self.seats:
               print("Invalid ID")
               return
          for seat in seat_no:
               row, col = seat
               if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print(f'Invalid seat {row} and {col}')
                    continue
               if self.seats[id][row][col] == 1:
                    print(f'Seat is already booked')
               else:
                    print(f"Seat ({row}, {col}) booked successfully")
                    
     def view_show_list(self):
          print('Running shows: ')
          for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

     def view_available_seats(self, show_id):
           if show_id not in self.seats:
               print(f'Invalid seat for show id {show_id}')
               return
           #print(f"Available seats for show {show_id}:")
           for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[show_id][i][j] == 0:
                        print(f"Row: {i} Col: {j}")


SC = Star_Cinema()
H = Hall(10, 10, 5)
VSL = H.view_show_list()
VAS = H.view_available_seats(1)
BS = H.book_seats(1, 9)

run = True
while run:
     print("Welcome to Star Cinema")
     print('1 : View Show List')
     print('2 : View Available Seats')
     print('3 : Book Seat')
     print('0 : Exit')


     ch = int(input("Enter Option:"))
     
     if ch == 0:
          run = False
     elif ch == 1:
          print(VSL)

     elif ch == 2:
          print(VAS)
     
     elif ch == 3:
          print(BS)
          


     # vsl1 = int(input())




     
     

        