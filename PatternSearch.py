# Tom Czubat

# Import the regular expressions module
import re

# Sample paragraph for searching and replacing
lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

# Find all of the instances of nonalphanumerical characters and store them
# Print out how many times this occurs
results = re.findall("[^a-zA-Z0-9]", lorem_ipsum)
print(len(results))


# Find all of the instances of 'sit-amet' or 'sit:amet' in the Sample
# Store the outcome then output the number of instances
occurences_sit_amet = re.findall(r"sit[-:]amet", lorem_ipsum)
print(len(occurences_sit_amet))


# Replace 'sit:amet' and 'sit-amet' with 'sit amet' using the sub funciton
# Assign the outcome to 'replace_results'
replace_results = re.sub(r"sit[-:]amet", "sit amet", lorem_ipsum)

# Find all the the occurence of 'sit amet'
# Print out the number of occurences 
occurences_sit_amet = re.findall("sit amet", replace_results)
print(len(occurences_sit_amet))