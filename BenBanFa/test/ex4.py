#-*-coding:utf-8-*-
# 100辆汽车
cars = 100;

# 汽车的容量
space_in_a_car = 4.0;

# 司机人数
drivers = 30;

# 乘客人数
passengers = 90;

# 没有开的车数量
cars_not_driven = cars - drivers;

# 开车的数量
cars_driven = drivers;

# 车的总容量
carpool_capacity = cars_driven * space_in_a_car;

# 每辆车的平均乘客人数
average_passengers_per_car = passengers / cars_driven;


# -------------------------


print "There are", cars, "cars available";
print "There are only", drivers, "drivers available";
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
