#db design

'''Driving down the road, you see some random people waiting for someone 
to pick them up and ask them to do some paid work.
 There has got to be a better way. You decide to write an app to assist with this problem. 
You as a user would log into the app with some informal work you need to
have done. Eg. Painting, tiling, building etc. You make an offer for
the amount you will pay for the work and the date you require the worker for.
An informal worker will be assigned to you (by a third party) that has the needed skill 
you need and is available on the selected date. The phones GPS picks up your location and 
assigns the closest qualified worker to do your work. Once the work is complete, the amount is 
subtracted from your credit card and you are asked to rate and comment the worker. The worker 
would get a FNB cashback number or a code to receive the payment at Checkers or Pick ‘n Pay. Design 
a database for the solution. User profiles, jobs, workers etc. You do not need to consider API calls. 
You would like to keep stats on the workers, amount paid, work done.'''

class BankDetails:
    which_bank: str#list of banks
    account_number:int
    #other required fields

class User:
    first_name: str
    last_name:str
    email: str
    cell: str
    slug:str
    payment_details: BankDetails
    account_type:int#company,user,worker

#third party
class Company:
    user: User
    company_name:str
    workers: int
    requests_completed: int
    is_active: False|True

class TypeOfWork:
    name: str
    id:int

class Skills:
    name: str
    description: str

class VerificationDetails:
    id_document: str#img
    id:int
    ##add more fields is required

#profile of worked
class Worker:
    user: User
    company:Company
    bio: str
    years_of_ex: str
    title_occupation:str
    skills: Skills#manytomany field
    price: int|float
    profile_image: str#img
    some_of_your_work: str#img
    some_of_your_work_1: str#img
    some_of_your_work_2: str#img
    verification_details:VerificationDetails#id
    valid_account: False#base VerificationDetails
    slug:str
    is_active:False

class Request:
    type_of_work: TypeOfWork
    description: str
    price: int
    id:int
    date:str
    location:str
    worked: Worker | None

class Review:
    worker: Worker
    stars:int
    review: str