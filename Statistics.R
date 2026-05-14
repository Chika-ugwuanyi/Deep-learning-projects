dim(mtcars) # gets the shape of the dataset
# get column names
names(mtcars)
# get row names
rownames(mtcars)
df = mtcars
df

# get min & max value of the rows(mpg)
min(df$mpg)
max(df$mpg)
# get mean, mode and median value
mean(df$mpg)
median(df$mpg)
names(sort(-table(df$mpg)))[1]

# Quantile
quantile(df$wt, c(0.50)) # get data from 50%
quantile(df$wt, c(0.25))
quantile(df$wt, c(0.75))
quantile(df$wt) # give me all the percentile at once
