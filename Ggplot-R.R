plot(1,7)
plot(1:10, type="l")

#line plot
line1 <- c(1,2,3,4,5,10)
line2 <- c(2,5,7,8,9,10)
plot(line1, type = "l", col = "blue")
lines(line2, type = "l", col = "red")

# scatter plot
x <- c(2,3,6,7,7,8,9,2,4,9)
y <- c(3,5,6,7,3,4,9,7,5,8)
plot(x,y)

# pie chat
x <- c(20,30,40,60)
my_labels <- c("mango", "berries", "sugar", "oranges")
colors <- c("blue", "red", "orange","black")
pie(x, label = my_labels, main="fruits", col = colors )

# barplot
x <- c("A", "B", "C", "D")
y <- c(2,4,6,8)
barplot(y, names.arg = x, density = 10) # density puts lines

# Ggplot2 in R

install.packages("ggplot2")
library(ggplot2)
# ggplot(data, aes(x_axis, y_axis)) = geometry
# scatter plot
df = mtcars
#df
ggplot(data = mtcars, aes(x=mpg, y=hp))+ geom_point()

# customise plot
ggplot(data = mtcars, aes(x=mpg, y=hp)) +
  geom_point() + 
  labs(title = "Scatter Plotof MPG Vs HP", 
       x="Miles per Gallon",
       y= "Horsepower")+
  theme_minimal()

# bar plot
df = mtcars
ggplot(data=df, aes(x= factor(cyl))) + geom_bar()

# box plot
df = mtcars
ggplot(data=df, aes(x= factor(cyl), y = mpg)) + geom_boxplot()