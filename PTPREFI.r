library(tidyverse)

# Load the dataset
df <- read_csv('Medicaldataset.csv')
setwd("C:/Users/amiohw/OneDrive - STI College Pasay-Edsa/Desktop/code MS")

# Create a histogram for 'Age'
ggplot(df, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = 'skyblue', color = 'black') +
  labs(title = 'Heart Attack Patients Age Distribution',
       x = 'Age',
       y = 'Number of Patients') +
  theme_minimal()

