import string 
from selenium import webdriver
from time import sleep
import json
import traceback
from selenium.webdriver.firefox.options import Options
import re
options = Options()
options.headless = True
import googlemaps
import requests
import webbrowser

profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.stylesheet', 2)
profile.set_preference('permissions.default.image', False)
profile.set_preference("javascript.enabled", True)
gmaps_key=googlemaps.Client(key = "----------")
n=1
count=1
browser = webdriver.Firefox(options=options, executable_path='/home/poulami/Downloads/geckodriver')
url='------'
browser.get(url)
sleep(5)
num=0
attr_num=2
page_number=1
while(page_number!=6299):
	sleep(2)
	
	# params = {
 #                'action': 'display_filtered_archives_of_trd_topics',
 #                'filtered_type': 'Property',
 #                'number_of_click_page': '1',
 #            }
	# req = requests.post('https://therealdeal.com/new-research/wp-admin/admin-ajax.php', data = params)
	with open('Nanotechnology.html', 'wb') as fd:
		for chunk in req.iter_content(chunk_size=500000000):
			fd.write(chunk)
		#s=webbrowser.open_new_tab('Nanotechnology.html')
		#print(s)

	for count in range(1,26):
		num_next=0
		data=browser.find_elements_by_class_name('database-items')
		data1=data[num].text
		data2=data1.split('\n')
		#print(data2)
		count_number=len(data2)-1
		# name=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[1]/span[2]/a')
		# title=name[num].text
		# print(title)
		# if(title==''):
		# 	print('x')
		for i in range(0,count_number):
			try:
				if 'BUILDING NAME ' in data2[i]:
					x=data2[i].split('BUILDING NAME ')
					i+=1
					title=x[i]
					building=title
					#print(title)
				i+=1
			except:
				print (traceback.format_exc())
		try:
			if 'Avenue' in title or 'Street' in title :
				street_name=title
			else:
				street_name=""

			if 'nd' in title or 'st' in title or 'th' in title or 'ND' in title or 'ST' in title or 'TH' in title:
				st=re.findall(r"(\d+)[th|nd|st|ND|ST|TH]", title)
				street_number=st[0]
			else:
				street_number=""
		except:
			print (traceback.format_exc())
		for i in range(0,count_number):
			if 'ADDRESS ' in data2[i]:
				a=data2[i].split('ADDRESS ')
				#print(a)
				i+=1
				address=a[1]
				#print(address)
			i+=1
		
		if title=="":
			title=address
			building=address
		for i in range(0,count_number):
			if 'NEIGHBORHOOD ' in data2[i]:
				a=data2[i].split('NEIGHBORHOOD ')
				#print(a)
				i+=1
				neighbourhood=a[1]
				#print(address)
			i+=1
		try:
			floor_count=""
			for i in range(0,count_number):
				if 'FLOORS ' in data2[i]:
					fl=data2[i].split('FLOORS ')
					#print(a)
					i+=1
					floor_count=fl[1]
					#print(floor_count)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			lease_start_date=""
			for i in range(0,count_number):
				if 'FILE DOB PLANS ' in data2[i]:
					ld=data2[i].split('FILE DOB PLANS ')
					#print(a)
					i+=1
					lease_start_date=ld[1]
					#print(lease_start_date)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			lease_end_date=""
			for i in range(0,count_number):
				if 'LIST/LAUNCH SALES ' in data2[i]:
					led=data2[i].split('LIST/LAUNCH SALES ')
					#print(a)
					i+=1
					lease_end_date=led[1]
					#print(lease_end_date)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			architect=""
			for i in range(0,count_number):
				if 'ARCHITECT ' in data2[i]:
					atect=data2[i].split('ARCHITECT ')
					#print(a)
					i+=1
					architect=atect[1]
					#print(architect)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			year_built=""
			for i in range(0,count_number):
				if 'YEAR BUILT ' in data2[i]:
					yb=data2[i].split('YEAR BUILT ')
					#print(a)
					i+=1
					year_built=yb[1]
					#print(year_built)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			presented_by=""
			for i in range(0,count_number):
				if 'SALES/MARKETING ' in data2[i]:
					pb=data2[i].split('SALES/MARKETING ')
					#print(a)
					i+=1
					presented_by=pb[1]
					#print(presented_by)
				i+=1
		except:
			print (traceback.format_exc())

		

		try:
			if 'BOROUGH ' in data2[3]:
				a=data2[3].split('BOROUGH ')
				#print(a)
				#i+=1
				borough=a[1]
			else:
				borough=""
				#print(borough)
		except:
			print (traceback.format_exc())
		# try:
		# 	presented_by=""
		# 	for i in range(0,count_number):
		# 		if 'OWNER ' in data2[i]:
		# 			a=data2[i].split('OWNER ')
		# 			#print(a)
		# 			i+=1
		# 			owner=a[1]
		# 			#print(presented_by)
		# 		i+=1
		# except:
		# 	owner=""
		# 	print (traceback.format_exc())

		try:
			if 'OWNER ' in data2[4]:
				a=data2[4].split('OWNER ')
					#print(a)
					#i+=1
				owner=a[1]
				#print(owner)
		except:
			owner=""
			print (traceback.format_exc())

		

		image_link=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[1]/div/a/img')
		property_images=image_link[num].get_attribute("src")
		
		link=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[2]/ul/li[1]/span[2]/a')
		l=link[num].get_attribute("href")
		browser1 = webdriver.Firefox(options=options, executable_path = '/home/poulami/Downloads/geckodriver')
		browser1.get(l)
		information=browser1.find_elements_by_class_name('contacts')
		information_dict=information[num_next].text
		#print(type(information_dict))
		try:
			geocode_result=gmaps_key.geocode(information_dict)
			lat=geocode_result[0]["geometry"]["location"]["lat"]
			lon=geocode_result[0]["geometry"]["location"]["lng"]
		except:
			print(traceback.format_exc())
		# try:
		# 	pincode = re.search([0-9][0-9][0-9][0-9][0-9],information_dict)
		# 	print(pincode)
		# 	# pincode_dict=pincode.group(0)
		# except:
		# 	print(traceback.format_exc())
		description=browser1.find_elements_by_class_name('sub_info')
		description_dict=description[0].text
		full_info=browser1.find_elements_by_class_name('content')
		full_info_dict=full_info[num_next].text
		full_info_dict1=full_info_dict.split('\n')
		#print(full_info_dict1)
		count_number_next=len(full_info_dict1)-1
		print(count_number_next)
		try:
			area=""
			for i in range(0,count_number_next):
				if 'SQUARE FEET ' in full_info_dict1[i]:
					# print('hi')
					sf=full_info_dict1[i]
					# print(sf)
					ar=sf.split('SQUARE FEET ')
					i+=1
					area=ar[1]
					#print(area)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			price=""
			for i in range(0,count_number_next):
				if 'PRICE' in full_info_dict1[i] and 'PRICE PER FOOT' not in full_info_dict1[i]:
					# print('hi')
					p=full_info_dict1[i]
					# print(sf)
					pr=p.split('PRICE ')
					i+=1
					price=pr[1]
					#print(area)
				i+=1
		except:
			print (traceback.format_exc())
		
		try:
			total_units=""
			for i in range(0,count_number_next):
				if 'TOTAL UNITS ' in full_info_dict1[i]:
					# print('hi')
					tu=full_info_dict1[i]
					# print(sf)
					tus=tu.split('TOTAL UNITS ')
					i+=1
					total_units=tus[1]
					#print(area)
				i+=1
		except:
			print (traceback.format_exc())

		try:
			ag_initial_price=""
			for i in range(0,count_number_next):
				if 'AG INITIAL PRICE ' in full_info_dict1[i]:
					# print('hi')
					ag=full_info_dict1[i]
					# print(sf)
					agp=ag.split('AG INITIAL PRICE ')
					i+=1
					ag_initial_price=agp[1]
					#print(area)
				i+=1
		except:
			print (traceback.format_exc())
		try:
			pincode=""
			
			for i in range(0,count_number_next):
				if 'NY ' in full_info_dict1[i]:
					# print('hi')
					pi=full_info_dict1[i]
					# print(pi)
					pic=pi.split('NY ')
					# cit=pi.split(', NY')
					#print(cit)
					i+=1
					pincode=pic[1]
					# city=cit[0]
					# print(pincode)
					if not(len(pincode)==5 and pincode.isdigit()):
						pincode=""

				i+=1
		except:
			print (traceback.format_exc())

		
		city="New York"
		contact=""
		country="USA"
		currency="$"
		landmark=""
		is_premium=""
		former_tenant=""
		lease_term=""
		property_sub_type="Vacant"
		property_type="Property"
		space=""
		unit=""
		vacancy_type=""
		status=""
		market_value=""
		industry_name=""
		opening_hours=""
		is_popup_shop= False
		key_money=""
		neighbours=""
		area_plan=""
		street_footfall=""
		status=""
		area_unit="Square Feet"
		dict={"latitude":lat,"longitude":lon,"street_number":street_number,"street_name":street_name,"city":city,"pincode":pincode,"total_units":total_units,"ag_initial_price":ag_initial_price,"price":price,"area":area,"presented_by":presented_by,"contact":contact,"year_built":year_built,"architect":architect,"lease_end_date":lease_end_date,"lease_start_date":lease_start_date,"floor_count":floor_count,"owner":owner,"borough":borough,"neighbourhood":neighbourhood,"address":address,"area_unit":area_unit,"status":status,"street_footfall":street_footfall,"country":country,"title":title,"building":building,"property_images":[property_images],"description":description_dict,"currency":currency,"landmark":landmark,"is_premium":is_premium,"former_tenant":former_tenant,"lease_term":lease_term,"property_sub_type":property_sub_type,"property_type":property_type,"space":space,"unit":unit,"vacancy_type":vacancy_type,"status":status,"market_value":market_value,"industry_name":industry_name,"opening_hours":opening_hours,"is_popup_shop":is_popup_shop,"key_money":key_money,"neighbours":neighbours,"area_plan":area_plan}
		print(dict)
		with open('/media/poulami/Storage/Old_System/work_scraping/Web.json', 'a') as file:
			file.write(json.dumps(dict))
		
		image_link=browser.find_elements_by_xpath('//*[@id="sort_topics"]/div[" + str(attr_num) + "]/div/div/div[1]/div/a/img')
		property_images=image_link[num].get_attribute("src")
		num+=1
		print(num)
		# print(property_images)
		attr_num+=1
		if(attr_num==26):
			attr_num=2
		if(num==25):
			num=0

		page_number+=1
		#print(page_number)
	browser.find_element_by_id("next_achive_button").click()
	