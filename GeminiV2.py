import os
import google.generativeai as genai



os.environ["GOOGLE_API_KEY"]
# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
'''
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "categorize the following receipt items into one of these categories and say how much was spent on each category :\"Groceries\", \"Dining\", \"Utilities\", \"Transportation\", \"Healthcare\", \"Personal Care\", \"Clothing and Accessories\", \"Entertainment\", \"Home and Furniture\", \"Education\", \"Travel\",  \"Gifts and Donations\", \"Business Expenses\", \"Insurance\", \"Taxes\", \"Investments\", \"Miscellaneous\"\nWALL-MART-SUPERSTORE\nST# 2323 OP#\nHAND TOWEL\nGATORADE\nT-SHIRT\n(888) 888\n8888\nMANAGER TOD LINGA\n888 WALL STORE ST\nWALL ST CITY, LA 88888\n23432435 TE# 51\nTR# 4354\n075953630184\n2.97 X\n068949055223\n2.00 X\n036231552452\n16.88 X\nPUSH PINS\n088348997350\n1.24 X\nSUBTOTAL\n23.09\nTAX 1\n7.89%\n2.90\nTAX 2\n4.90%\n1.28\nTOTAL\n27.27\nCREDIT TEND\n27.27\nCHANGE DUE\n0.00\nACCOUNT #\nAPPROVAL # 77W166\nREF # 307171075528\n**** ***9999\nTERMINAL #5419885359\n\nITEMS SOLD 4\nTC# 1752 5627 3145 9811 0000\nGet Free Holiday Savings by Cell!\nThank You for Shopping With Us!\n10/17/2020 16:12\n✰✰✰ CUSTOMER COPY ✰✰✰",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here's a breakdown of the receipt items and their categories:\n\n* **Groceries:** \n    * **GATORADE:** $2.00\n* **Personal Care:** \n    * **HAND TOWEL:** $2.97 \n* **Clothing and Accessories:** \n    * **T-SHIRT:** $16.88\n* **Home and Furniture:** \n    * **PUSH PINS:** $1.24 \n\n**Total Spent by Category:**\n\n* **Groceries:** $2.00\n* **Personal Care:** $2.97\n* **Clothing and Accessories:** $16.88\n* **Home and Furniture:** $1.24 \n",
            ],
        },
    ]
)

response = chat_session.send_message("Please provide a breakdown of each item and category based on the above receipt.")

print(response.text)
'''


'''
receipt_text = """
WALL-MART-SUPERSTORE
ST# 2323 OP#
HAND TOWEL
GATORADE
T-SHIRT
(888) 888
8888
MANAGER TOD LINGA
888 WALL STORE ST
WALL ST CITY, LA 88888
23432435 TE# 51
TR# 4354
075953630184
2.97 X
068949055223
2.00 X
036231552452
16.88 X
PUSH PINS
088348997350
1.24 X
SUBTOTAL
23.09
TAX 1
7.89%
2.90
TAX 2
4.90%
1.28
TOTAL
27.27
CREDIT TEND
27.27
CHANGE DUE
0.00
ACCOUNT #
APPROVAL # 77W166
REF # 307171075528
**** ***9999
TERMINAL #5419885359

ITEMS SOLD 4
TC# 1752 5627 3145 9811 0000
Get Free Holiday Savings by Cell!
Thank You for Shopping With Us!
10/17/2020 16:12
✰✰✰ CUSTOMER COPY ✰✰✰
"""
'''
receipt_text = """
TESCO
SHREWSBURY CATTLE MARKET
any questions please visit
www.tesco.com/store-locator
TAPE MEASURE
£2.10
PROTEIN COOKIE
£1.80
PROTEIN COOKIE
£1.80
CONDOMS
£10.00
PROCECCO
£7.00
PROCECCO
£7.00
PROCECCO
£7.00
SAUVIGNON BLNC *
£7.00
SAUVIGNON BLNC *
£7.00
KRONENBOURG
*
£4.60
TAPE MEASURE
£2.10
PROTEIN COOKIE
£1.80
PROTEIN COOKIE
£1.80
CONDOMS
£10.00
SAUVIGNON BLNC *
£7.00
SAUVIGNON BLNC *
£7.00
KRONENBOURG
*
£4.60
TOTAL
£55.30
CASH
£60.00
CHANGE DUE
£4.70
Join Clubcard Today
This visit you could have collected
15 Clubcard points.
Download the Tesco Grocery & Clubcard
app or visit Tesco.com/Clubcard
9740 1041 1710 2112 2589 3617 1533 28
A chance to win a £1000 Tesco gift card
and collect 25 Clubcard points.
Visit www.tescoviews.com t's & C's apply
17/10/22 12:26 5332 171 9171 8936

"""
# Define the prompt, embedding the receipt text as a variable
prompt = f"""Categorize the following receipt items into one of these categories and say how much was spent on each category:
"Groceries", "Dining", "Utilities", "Transportation", "Healthcare", "Personal Care", "Clothing and Accessories", "Entertainment", "Home and Furniture", "Education", "Travel", "Gifts and Donations", "Business Expenses", "Insurance", "Taxes", "Investments", "Miscellaneous"

{receipt_text}
"""

# Send the prompt directly to the model without chat history
#response = model.send_message(prompt)
#response = model.generate(prompt=prompt)

#response = model.generate_text(prompt=prompt)
chat = model.start_chat(history=[])
response = chat.send_message(prompt)
# Print the model's response
print(response.text)

