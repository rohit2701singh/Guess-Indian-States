import turtle
import pandas

INDIAN_STATES = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
                 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
                 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Jammu and Kashmir', 'Ladakh']

screen = turtle.Screen()
screen.title("Indian State Game")
screen.setup(700, 825)  # hit and trial method
screen.bgpic("india_map_new.gif")
x_cor_list = []
y_cor_list = []


def get_mouse_click_coordinate(x, y):
    coordinates = (x, y)
    print(coordinates)

    x_cor_list.append(coordinates[0])
    y_cor_list.append(coordinates[1])


turtle.onscreenclick(get_mouse_click_coordinate)
turtle.mainloop()

print(f"x_cor: {x_cor_list}")
print(f"y_cor:{y_cor_list}")

x_coordinates = x_cor_list
y_coordinates = y_cor_list

state_dict = {
    "states": INDIAN_STATES,
    "x": x_coordinates,
    "y": y_coordinates,
}

data = pandas.DataFrame(state_dict)
data.to_csv("indian_states_coordinates.csv")


# save it so that you don't have to find the solution again.

# x_cor_list: [-76.0, 268.0, 237.0, 86.0, -7.0, -206.0, -261.0, -137.0, -121.0, 61.0, -155.0, -155.0, -98.0, -173.0, 270.0,
#         211.0, 247.0, 285.0, 58.0, -159.0, -207.0, 137.0, -99.0, -83.0, 217.0, -53.0, -82.0, 121.0]
# y_cor_list: [-167.0, 182.0, 138.0, 113.0, 8.0, -163.0, 33.0, 189.0, 272.0, 53.0, -155.0, -273.0, 29.0, -72.0, 93.0, 109.0,
#          55.0, 133.0, -23.0, 236.0, 133.0, 157.0, -269.0, -101.0, 63.0, 140.0, 222.0, 44.0]
