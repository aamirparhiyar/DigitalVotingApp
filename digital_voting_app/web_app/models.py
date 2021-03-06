from django.db import models

class Voter(models.Model):

    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]
    name = models.CharField(max_length = 200)
    email_id = models.CharField(max_length = 345)
    password = models.CharField(max_length = 60)
    aadhar_num = models.CharField(max_length=12, primary_key = True)
    contact_num = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES)
    age = models.IntegerField()
    father_name = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    permanent_address_line_1 = models.CharField(max_length = 500)
    permanent_address_line_2 = models.CharField(max_length = 500, default = '')
    # photograph_image_link = models.URLField(default = '')
    # signature_image_link = models.URLField(default = '')
    #aadhar_doc_link = models.CharField(max_length = 300)
    #occupation = models.CharField(max_length = 100)
    #date_of_birth = models.DateTimeField("Date of Birth")
    #city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200, default = '')
    constituency = models.CharField(max_length = 200, default = 'CONSTITUENCY')
    image = models.ImageField(upload_to = 'profile_images/', default = "default.jpg")

    def __str__(self):
        return self.name + " WHO IS FROM " + self.constituency

    def with_aadhar_num(str):
        return Voter.objects.get(aadhar_num = str)

    def present_voter(aadhar_number):
        hash = {}
        voter = Voter.objects.get(aadhar_num = aadhar_number)
        print(voter)
        hash['name'] = voter.name
        hash['emailId'] = voter.email_id
        hash['aadharNum'] = voter.aadhar_num
        hash['contactNum'] = voter.contact_num
        hash['gender'] = voter.gender
        hash['age'] = voter.age
        hash['fatherName'] = voter.father_name
        hash['motherName'] = voter.mother_name
        #hash['dateOfBirth'] = voter.date_of_birth
        hash['constituency'] = voter.constituency
        return hash