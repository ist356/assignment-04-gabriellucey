# Reflection

Student Name:  Gabriel Lucey
Sudent Email:  gplucey@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

During this assignment, I did not have many struggles with pandaslib.py or unibrow.py. The only aspect of this assignment that was a bit difficult for me was incorporating all functions from pandaslib.py into the unibrow Streamlit application. At first, I did not understand why the get_columns_of_type function was needed, but I then realized that the first filter dropdown needed to be only the text columns, not the numerical columns. I learned that setting the numpy type to the desired data type would allow me to filter out any numerical values, so I set the type to "object."

I was also a bit confused at first about what Streamlit functions I should be using to match the UI requirements. At first, I had st.selectbox in place for the column selection; however, after checking the requirements, I realized I needed to use st.multiselect with a default value of all the columns. This made it so that multiple columns could be selected, and each column was automatically displayed once the file was loaded in. I was also unaware that a UI was needed to turn the filter on and off, so I found that using a toggle is a way to turn the filter on and off using an if statement. The if statement makes it so that if the toggle is clicked, all Streamlit functions used to filter the dataframe will be displayed.

I also realized that I must be careful with the indenting when it comes to displaying the dataframe. Originally, the dataframe would only display once the filter was turned on. However, by moving the st.write functions an indent back, the dataframe and description now display both with the filter on and off.

Overall, this assignment was a good refresher for past topics and helped me strengthen my skills using Streamlit applications.