from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path

amazon ="https://aax-eu.amazon.in/x/c/QkH3Ya8MQZZYpuk_M4i6yUgAAAF61tx1jAMAAAH2AUhrm9Y/https://www.amazon.in/gp/aw/d/B089MS8XQ3/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=49410e438f4a311e868408c9bfa3b8e6&hsa_cr_id=8170570950902&ref_=sbx_be_s_sparkle_mcd_asin_2_img&pd_rd_w=QrJFQ&pf_rd_p=088a4896-4e55-4a9c-9e96-fdb109ea7578&pd_rd_wg=LSWP1&pf_rd_r=43KNSM0MQ4VN886JWG1T&pd_rd_r=61dc1b0e-b00a-40f7-a760-18bdf5ff0bd4"
flipkart ="https://www.flipkart.com/redmi-9-power-blazing-blue-64-gb/p/itm9533b02ba34ef?pid=MOBFYZ7HHGJUATYD&lid=LSTMOBFYZ7HHGJUATYDFYZRIS&marketplace=FLIPKART&q=redmi+9+power&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=eabf717c-81d7-44f9-bb21-907620b59a9b.MOBFYZ7HHGJUATYD.SEARCH&ppt=hp&ppn=homepage&ssid=ytomjle9z40000001627102440230&qH=636f38d734b1a1de"
paytm = "https://paytmmall.com/samsung-galaxy-m32-4-gb-64-gb-light-blue-CMPLXMOBSAMSUNG-GALAAPNI993020EE7CEEBE-pdp?product_id=338849830&sid=cfdb4189-2d4c-4978-bfc0-00ef8995ef4d&src=consumer_search&svc=-1&cid=66781&tracker=organic%7C66781%7Cgalaxy%20m32%7Cgrid%7CSearch_experimentName%3Ddemographics_location%23NA_gender%23NA%7C%7C12%7Cdemographics_location%23NA_gender%23NA&get_review_id=338849832&site_id=2&child_site_id=6"
wd = webdriver.Chrome(r'C:\Users\rahulmyakal\OneDrive\Documents\bestenlist\project\chromedriver.exe')
print ("Best Enlist Python BootCamp Project\n")
print("\n Price Comparision Between Amazon, Flipkart and Paytm")

print ("Connecting to Amazon")
wd.get(amazon)
pr_name = wd.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[1]')
product = pr_name.text
f_price = wd.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[10]/div[1]/div/table/tbody/tr[2]')
amazon_price = f_price.text
print (" ---> Successfully retrieved the price from Amazon \n")

print("Connecting to Flipkart")
wd.get(flipkart)
f_price = wd.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
flipkart_price = f_price.text
print (" ---> Successfully retrieved the price from flipkart \n")

print("Connecting to Paytm")
wd.get(paytm)
f_price = wd.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/span[1]')
paytm_price = f_price.text
print (" ---> Successfully retrieved the price from Paytm\n")

# Final display
print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!!-!-!-!-!-!-!-!-!-!-!-!-!-!-!!-!-!-!-!-! Getting All Information !-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
print({product})
print("Price available at Amazon is: "+amazon_price)
print("Price available at Flipkart is: "+flipkart_price)
print("Price available at Paytm is: "+paytm_price)

print("\n Project Completed ")


