from django.shortcuts import render
from django.http import HttpResponse
from web_app.models import Voter

def index(request):
    #return HttpResponse("<h1>HELLO</h1>")
    MONTH_NAMES = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    MONTH_DIGIT_LIST = ['', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    STATE_NAMES = ['', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam','Bihar', 'Chattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
    DATE_LIST = list(range(1,32))
    DATE_DIGIT_LIST = ['', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    YEAR_LIST = list(range(2019, 1940, -1))
    TEST_LIST = [
    ["A", "B"],
    ["C", "D"]
    ]
    CONSTITUENCY_LIST = {"Andhra Pradesh": ['Araku', 'Srikakulam', 'Vizianagaram', 'Visakhapatnam', 'Anakapalli', 'Kakinada', 'Amalapuram', 'Rajahmundry', 'Narasapuram', 'Eluru', 'Machilipatnam', 'Vijayawada', 'Guntur', 'Narasaraopet', 'Bapatla', 'Ongole', 'Nandyal', 'Kurnool', 'Anantapur', 'Hindupur', 'Kadapa', 'Nellore', 'Tirupati', 'Rajampet', 'Chittoor'],
    "Arunachal Pradesh": ['Arunachal West', 'Arunachal East'],
    "Assam": ['Karimganj', 'Silchar', 'Autonomous District', 'Dhubri', 'Kokrajhar', 'Barpeta', 'Gauhati', 'Mangaldoi', 'Tezpur', 'Nowgong', 'Kaliabor', 'Jorhat', 'Dibrugarh', 'Lakhimpur'],
    "Bihar": ['Valmiki Nagar', 'Paschim Champaran', 'Purvi Champaran', 'Sheohar', 'Sitamarhi', 'Madhubani', 'Jhanjharpur', 'Supaul', 'Araria', 'Kishanganj', 'Katihar', 'Purnia', 'Madhepura', 'Darbhanga', 'Muzaffarpur', 'Vaishali', 'Gopalganj', 'Siwan', 'Maharajganj', 'Saran', 'Hajipur', 'Ujiarpur', 'Samastipur', 'Begusarai', 'Khagaria', 'Bhagalpur', 'Banka', 'Munger', 'Nalanda', 'Patna Sahib', 'Pataliputra', 'Arrah', 'Buxar', 'Sasaram', 'Karakat', 'Jahanabad', 'Aurangabad', 'Gaya', 'Nawada', 'Jamui'],
    "Chattisgarh": ['Sarguja', 'Raigarh', 'Janjgir', 'Korba', 'Bilaspur', 'Rajnandgaon', 'Durg', 'Raipur', 'Mahasamund', 'Bastar', 'Kanker'], 
    "Goa": ['North Goa', 'South Goa'], 
    "Gujarat": ['Kachchh', 'Banaskantha', 'Patan', 'Mahesana', 'Sabarkantha', 'Gandhinagar', 'Ahmedabad East', 'Ahmedabad West', 'Surendranagar', 'Rajkot', 'Porbandar', 'Jamnagar', 'Junagadh', 'Amreli', 'Bhavnagar', 'Anand', 'Kheda', 'Panchmahal', 'Dahod', 'Vadodara', 'Chhota Udaipur', 'Bharuch', 'Bardoli', 'Surat', 'Navsari', 'Valsad'], 
    "Haryana": ['Ambala', 'Kurukshetra', 'Sirsa', 'Hissar', 'Karnal', 'Sonipat', 'Rohtak', 'Bhiwani–Mahendragarh', 'Gurgaon', 'Faridabad'],
    "Himachal Pradesh": ['Kangra', 'Mandi', 'Hamirpur', 'Shimla'],
    "Jammu & Kashmir": ['Baramulla', 'Srinagar', 'Anantnag', 'Ladakh', 'Udhampur', 'Jammu'], 
    "Jharkhand": ['Rajmahal', 'Dumka', 'Godda', 'Chatra', 'Kodarma', 'Giridih', 'Dhanbad', 'Ranchi', 'Jamshedpur', 'Singhbhum', 'Khunti', 'Lohardaga', 'Palamau', 'Hazaribagh'], 
    "Karnataka": ['Chikkodi', 'Belagavi', 'Bagalkot', 'Bijapur', 'Kalaburagi', 'Raichur', 'Bidar', 'Koppal', 'Bellary', 'Haveri', 'Dharwad', 'Uttara Kannada', 'Davanagere', 'Shimoga', 'Udupi Chikmagalur', 'Hassan', 'Dakshina Kannada', 'Chitradurga', 'Tumkur', 'Mandya', 'Mysore', 'Chamarajanagar', 'Bangalore Rural', 'Bangalore North', 'Bangalore Central', 'Bangalore South', 'Chikballapur', 'Kolar'], 
    "Kerala": ['Kasaragod', 'Kannur', 'Vatakara', 'Wayanad', 'Kozhikode', 'Malappuram', 'Ponnani', 'Palakkad', 'Alathur', 'Thrissur', 'Chalakudy', 'Ernakulam', 'Idukki', 'Kottayam', 'Alappuzha', 'Mavelikara', 'Pathanamthitta', 'Kollam', 'Attingal', 'Thiruvananthapuram'], 
    "Madhya Pradesh": ['Morena', 'Bhind', 'Gwalior', 'Guna', 'Sagar', 'Tikamgarh', 'Damoh', 'Khajuraho', 'Satna', 'Rewa', 'Sidhi', 'Shahdol', 'Jabalpur', 'Mandla', 'Balaghat', 'Chhindwara', 'Hoshangabad', 'Vidisha', 'Bhopal', 'Rajgarh', 'Dewas', 'Ujjain', 'Mandsaur', 'Ratlam', 'Dhar', 'Indore', 'Khargone', 'Khandwa', 'Betul'],
    "Maharashtra": ['Nandurbar', 'Dhule', 'Jalgaon', 'Raver', 'Buldhana', 'Akola', 'Amravati', 'Wardha', 'Ramtek', 'Nagpur', 'Bhandara–Gondiya', 'Gadchiroli–Chimur', 'Chandrapur', 'Yavatmal–Washim', 'Hingoli', 'Nanded', 'Parbhani', 'Jalna', 'Aurangabad', 'Dindori', 'Nashik', 'Palghar', 'Bhiwandi', 'Kalyan', 'Thane', 'Mumbai North', 'Mumbai North West', 'Mumbai North East', 'Mumbai North Central', 'Mumbai South Central', 'Mumbai South', 'Raigad', 'Maval', 'Pune', 'Baramati', 'Shirur', 'Ahmednagar', 'Shirdi', 'Beed', 'Osmanabad', 'Latur', 'Solapur', 'Madha', 'Sangli', 'Satara', 'Ratnagiri–Sindhudurg', 'Kolhapur', 'Hatkanangle'], 
    "Manipur": ['Inner Manipur', 'Outer Manipur'], 
    "Meghalaya": ['Shillong', 'Tura'],
    "Mizoram": ['Mizoram'],
    "Nagaland": ['Nagaland'], 
    "Odisha": ['Bargarh', 'Sundargarh', 'Sambalpur', 'Keonjhar', 'Mayurbhanj', 'Balasore', 'Bhadrak', 'Jajpur', 'Dhenkanal', 'Bolangir', 'Kalahandi', 'Nabarangpur', 'Kandhamal', 'Cuttack', 'Kendrapara', 'Jagatsinghpur', 'Puri', 'Bhubaneswar', 'Aska', 'Berhampur', 'Koraput'],
    "Punjab": ['Gurdaspur', 'Amritsar', 'Khadoor Sahib', 'Jalandhar', 'Hoshiarpur', 'Anandpur Sahib', 'Ludhiana', 'Fatehgarh Sahib', 'Faridkot', 'Firozpur', 'Bathinda', 'Sangrur', 'Patiala'],
    "Rajasthan": ['Ganganagar', 'Bikaner', 'Churu', 'Jhunjhunu', 'Sikar', 'Jaipur Rural', 'Jaipur', 'Alwar', 'Bharatpur', 'Karauli–Dholpur', 'Dausa', 'Tonk–Sawai Madhopur', 'Ajmer', 'Nagaur', 'Pali', 'Jodhpur', 'Barmer', 'Jalore', 'Udaipur', 'Banswara', 'Chittorgarh', 'Rajsamand', 'Bhilwara', 'Kota', 'Jhalawar–Baran'],
    "Sikkim": ['Sikkim'],
    "Tamil Nadu": ['Thiruvallur', 'Chennai North', 'Chennai South', 'Chennai Central', 'Sriperumbudur', 'Kancheepuram', 'Arakkonam', 'Vellore', 'Krishnagiri', 'Dharmapuri', 'Tiruvannamalai', 'Arani', 'Villupuram', 'Kallakurichi', 'Salem', 'Namakkal', 'Erode', 'Tiruppur', 'Nilgiris', 'Coimbatore', 'Pollachi', 'Dindigul', 'Karur', 'Tiruchirappalli', 'Perambalur', 'Cuddalore', 'Chidambaram', 'Mayiladuturai', 'Nagapattinam', 'Thanjavur', 'Sivaganga', 'Madurai', 'Theni', 'Virudhunagar', 'Ramanathapuram', 'Thoothukudi', 'Tenkasi', 'Tirunelveli', 'Kanyakumari'],
    "Telangana": ['Adilabad', 'Peddapalle', 'Karimnagar', 'Nizamabad', 'Zahirabad', 'Medak', 'Malkajgiri', 'Secunderabad', 'Hyderabad', 'Chevella', 'Mahbubnagar', 'Nagarkurnool', 'Nalgonda', 'Bhongir', 'Warangal', 'Mahabubabad', 'Khammam'],
    "Tripura": ['Tripura West', 'Tripura East'],
    "Uttar Pradesh": ['Saharanpur', 'Kairana', 'Muzaffarnagar', 'Bijnor', 'Nagina', 'Moradabad', 'Rampur', 'Sambhal', 'Amroha', 'Meerut', 'Baghpat', 'Ghaziabad', 'Gautam Buddha Nagar', 'Bulandshahr', 'Aligarh', 'Hathras', 'Mathura', 'Agra', 'Fatehpur Sikri', 'Firozabad', 'Mainpuri', 'Etah', 'Badaun', 'Aonla', 'Bareilly', 'Pilibhit', 'Shahjahanpur', 'Kheri', 'Dhaurahra', 'Sitapur', 'Hardoi', 'Misrikh', 'Unnao', 'Mohanlalganj', 'Lucknow', 'Rae Bareli', 'Amethi', 'Sultanpur', 'Pratapgarh', 'Farrukhabad', 'Etawah', 'Kannauj', 'Kanpur Urban', 'Akbarpur', 'Jalaun', 'Jhansi', 'Hamirpur', 'Banda', 'Fatehpur', 'Kaushambi', 'Phulpur', 'Allahabad', 'Barabanki', 'Faizabad', 'Ambedkar Nagar', 'Bahraich', 'Kaiserganj', 'Shrawasti', 'Gonda', 'Domariyaganj', 'Basti', 'Sant Kabir Nagar', 'Maharajganj', 'Gorakhpur', 'Kushi Nagar', 'Deoria', 'Bansgaon', 'Lalganj', 'Azamgarh', 'Ghosi', 'Salempur', 'Ballia', 'Jaunpur', 'Machhlishahr', 'Ghazipur', 'Chandauli', 'Varanasi', 'Bhadohi', 'Mirzapur', 'Robertsganj'], 
    "Uttarakhand": ['Tehri Garhwal', 'Garhwal', 'Almora', 'Nainital–Udhamsingh Nagar', 'Haridwar'],
    "West Bengal": ['Cooch Behar', 'Alipurduars', 'Jalpaiguri', 'Darjeeling', 'Raiganj', 'Balurghat', 'Maldaha Uttar', 'Maldaha Dakshin', 'Jangipur', 'Baharampur', 'Murshidabad', 'Krishnanagar', 'Ranaghat', 'Bangaon', 'Barrackpur', 'Dum Dum', 'Barasat', 'Basirhat', 'Jaynagar', 'Mathurapur', 'Diamond Harbour', 'Jadavpur', 'Kolkata Dakshin', 'Kolkata Uttar', 'Howrah', 'Uluberia', 'Srerampur', 'Hooghly', 'Arambag', 'Tamluk', 'Kanthi', 'Ghatal', 'Jhargram', 'Medinipur', 'Purulia', 'Bankura', 'Bishnupur', 'Bardhaman Purba', 'Bardhaman–Durgapur', 'Asansol', 'Bolpur', 'Birbhum']
    }


    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         #return redirect('home')
    # else:
    #     form = DocumentForm()
    return render(request, 'web_app/vote.html', {"months": MONTH_DIGIT_LIST, "states": STATE_NAMES, "dates": DATE_DIGIT_LIST, "years": YEAR_LIST, "cons_list": CONSTITUENCY_LIST, "test_list": TEST_LIST})

def create_voter(request):
    voter_birthdate = request.POST['voter_birth_year'] + '-' + request.POST['voter_birth_month'] + '-' + request.POST['voter_birth_date']
    print("voter_birthdate = " + voter_birthdate)
    voter = Voter(name = request.POST['voter_name'], 
    age = request.POST['voter_age'],
    gender = request.POST['voter_gender'],
    email_id = request.POST['voter_email'],
    password = request.POST['voter_password'],
    aadhar_num = request.POST['voter_aadhar_num'],
    contact_num = request.POST['voter_contact'],
    father_name = request.POST['voter_father_name'],
    mother_name = request.POST['voter_mother_name'],
    permanent_address_line_1 = request.POST['voter_address_line_1'],
    permanent_address_line_2 = request.POST['voter_address_line_2'],
    date_of_birth = voter_birthdate,
    state = request.POST['voter_state'],
    constituency = request.POST['voter_const'])
    a=Voter(name = "Ashutosh",age=21, gender = "M", email_id = "ashutosh", password = "password", aadhar_num = "927752953828", contact_num = "9057322110", father_name = "Naveen Rahi", mother_name = "Poonam Rahi", permanent_address_line_1 = "hbefe", permanent_address_line_2 = "vdyFEF", date_of_birth = "1997-08-03", state = "Rajasthan", constituency = "Kota")
    voter.save()
    return HttpResponse("<h1>DETAILS SAVED SUCCESSFULLY!!</h1>")

