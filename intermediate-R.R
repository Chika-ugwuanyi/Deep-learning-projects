# if else
a <- 4
b <- 5
if (a>b){
  print("Ok")
} else if(a==b){
  print("They are equal")
} else{
  print("Not ok")
}

a <- 200
b <- 33
if (b > a) {
  print("b is greater than a")
} else if (a == b) {
  print("a and b are equal")
} else {
  print("a is greater than b")
}  
a <- 200
b <- 33
c <- 500

if (a<b & b>a) {
  print("ok")
}else{
print("ok ok")
}

# loop in R
counter <- 1
while (counter <= 5){
  print("ok")
  counter <- counter + 1
}

counter <- 1
while (counter <= 50){
  paste("counter value is ", counter)
  if (counter == 5){
    break
  }
  counter <- counter + 1
}


counter <- 1
while (counter <= 10){
  paste("counter value is ", counter, "\n")
  if (counter == 5){
    next
  }
  counter <- counter + 1
}

# create functions
myfunc <- function(){
  print("Ok")
}

myfunc()

myfunc <- function(a, b){
  print(a+b)
}
myfunc(4,8)

# default parameters in functs
myfunc <- function(country = "Norway"){
  paste("OI am from ", country)
}

myfunc()

# return in funct
myfuncRet <- function(a,b){
  return(a+b)
}
x = myfuncRet(3,8)
x = x - 5

# Nested functions
Nested_function <- function(x,y){
  print(x)
  print(y)
  a<- x+y
  return(a)
}

Nested_function(Nested_function(4,5), Nested_function(3,6))

# Recursion (works like loops)
tryRecursion <- function(k){
  if (k>0){
    result <- k+ tryRecursion(k - 1)
    print(result)
  } else {
    result = 0
    return(result)
  }
}

tryRecursion(5)

# global variable
text = "Awesome"
my_globa_fun <- function(){
  print("R is ", text)
}

my_globa_fun()

# data structure in R
# vectors of strings and numbers
my_fruit <- c("banana", "mangos", "apples")
my_fruit2 <- c(1,2.3)
my_fruit2
numbers <- 1:10
numbers

# lists
my_list <- list("Ali", 1, "ok")
my_list

# matrix
my_matrix <- matrix(c(1,2,3,4,5,6), nrow=3, ncol=2)
my_matrix

# dataframe
df <- data.frame(
  Training = c("strength", "stamina", "other"),
  Pulse = c(100, 50, 80),
  Duration = c(660,30,45)
)
df
summary(df)

# factor
my_fcator <- factor(c("low", "med", "high", "med", "fun"))
my_fcator

# timeseries
my_timeseries <- ts(c(5, 10, 15, 20), start = 2020, frequency = 4)
my_timeseries

# environment (data structures used to store variables and fncs)
my_env = new.env()
assign("x", 5, envir = my_env)

x_value = get("x", envir = my_env)
print(x_value)

x <- 5
print(x)

# Arrays
# 1-dimension
my_array <- c(1:24)
my_array

# multi-dimentional
mul_dimes <- array(my_array, dim = c(4,3,2)) # create 2 arrays
mul_dimes

mul_dimes2 <- array(my_array, dim = c(4,3,1)) # create 1 array
mul_dimes2

# graphics in R
