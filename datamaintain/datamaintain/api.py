# import searchform
import fxapi
import logging

from django.db import transaction
from django.conf.urls.i18n import i18n_patterns
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext, string_concat
from django.contrib.auth.models import User

from models import *
# from commerce.models import *
# from control.models import *
# from commerce.views import *
# from commerce import logic
# from commerce.templatetags.fxcommerce import format_price
# from fixido.search_sites import SearchView
# # from leads.searchform import ActorCampaignEmailStatisticsFilter
# # from leads.searchform import ActorSearchFilter, LeadSearchFilter
# # from leads.searchform import CategorySearchFilter, SearchFilter
# # from leads.searchform import RecentLeadsFilter, RecentSearchFilter
# # from leads.searchform import TradeSearchFilter, TransactionSearchFilter
# 
# from tracking.utils import get_ip_address
# from tracking.utils import update_recently_view_lead, update_recent_search

#LeadCategoryAPI = fxapi.RestView.create('categories', LeadCategory, actions=['list'])
AbsentListAPI = fxapi.RestView.create('absentlist', AbsentList, actions=['list'])
print "absentlistview", AbsentListAPI
#LeadProvidedAPI = fxapi.RestView.create('leads_provided', ActorProvidedLead, actions=['list'])
#LeadBoughtAPI = fxapi.RestView.create('leads_bought', ActorBoughtLead, actions=['list'])
#TransactionAPI = fxapi.RestView.create('transactions', Trade , actions=['list'],model_list_fields=['transaction_id', 'lead_id', 'price'])
logger = logging.getLogger("myapplog")

class AbsentList_RestAPI(fxapi.RestView):
    name = 'absentlist'
    model = Student_Admission
    actions = ['list']
    # model_list_fields = ['date','absent_regno', 'absent_name',]
    # query_fields = ['date','absent_regno', 'absent_name',]
    # model_list_fields = ['date','absent','staff']
    query_fields = ['regno','dob']
    @classmethod
    def get_details(cls):
      print "get_details"
      absentlist = AbsentList.objects.get(regno=regno,dob=dob)
      print absentlist
    @classmethod
    def action_list(cls, request, limit=None, pk=None, action='list'):
        
        result = super(AbsentList_RestAPI, cls).action_list(request, limit, pk, action)
        
        print "result", result

        regno=request.REQUEST['regno']
        print regno
        dob=request.REQUEST['dob']
        print dob
        
        find_student=Student_Admission.objects.get(reg_no=regno)
        print "find_student", find_student.id
        
        find_detail= Create_Attendance_List.objects.filter(student__id=find_student.id)
        for find_details in find_detail:
            print find_details.date
        
#         find_student=Student_Admission.objects.get(dob=dob)
#         print "find_student", find_student
        
#         find_detail= Create_Attendance_List.objects.filter(student__id=find_student_admission)
#         print find_detail
        
#         find_list=Create_Attendance_List_.objects.filter(student__id=find_detail.id)
#         print find_list.date
        
        
        
        absentlists =AbsentList.objects.filter(date=date)
        if absentlists:
          
          result['data'] = absentlists

        else:  
          result['data'] = "No Results found"
           

# class AbsentList_RestAPI(fxapi.RestView):
#     name = 'absentlist'
#     model = AbsentList
#     actions = ['list']
#     # model_list_fields = ['date','absent_regno', 'absent_name',]
#     # query_fields = ['date','absent_regno', 'absent_name',]
#     # model_list_fields = ['date','absent','staff']
#     query_fields = ['date','absent','staff']
#     @classmethod
#     def get_details(cls):
#       print "get_details"
#       absentlist = AbsentList.objects.get(date=date)
#       print absentlist
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
#         
#         result = super(AbsentList_RestAPI, cls).action_list(request, limit, pk, action)
#         
#         print "result", result
# 
#         date=request.REQUEST['date']
#         print date
#         
#         
#         
#         absentlists =AbsentList.objects.filter(date=date)
#         if absentlists:
#           
#           result['data'] = absentlists
# 
#         else:  
#           result['data'] = "No Results found"
        # _date=AbsentList.objects.get(pk=1)
        # print _date
        
        

#         absentlists = []
#         _absentlists = result['data']
#         print "Data", _absentlists

# #         if pk:
# #           print "enter pk"
#         # absentlist = {}
#         # _absentlist = result['data']
#         # print "data1", _absentlist
#         # for field in cls.get_model_list_fields(pk):
#         #     if hasattr(_absentlist, field):
#         #       absentlist[field] = getattr(_absentlist, field)
#         # _absentlist = [absentlist]
#         # print _absentlist

#         # for field in cls.get_model_list_fields():
#         #     if hasattr(_absentlist, field):
#         #       absentlist[field] = getattr(_absentlist, field)
#         # _absentlist = [absentlist]
#         # print _absentlist

#         if _absentlists:
#           print "testing"  
#           _user = User.objects.get(pk=int(_absentlists[0]['staff']))
#           print "user1", _user
        
#         for absentlist in _absentlists:
#           print "absentlist", absentlist['absent']
#           _absentlist = AbsentList_Details.objects.get(pk=int(absentlist['absent']))
          
    
#           _absentlist_get =  Rest.action_list(request, pk=_absentlist.pk, action='get')
          
#           absentlist.update(_absentlist_get['data'])
# #     #       lead['price'] = CurrencyExchangeRate.Convert(
# #     #         lead['price'], lead['price_currency'], _actor.currency)[0]
# #     #       lead['price'] = format_price(lead['price'], _actor.currency)
# #     #       lead['price_currency'] = _actor.currency
          
#           del absentlist['absent']
#           absentlists.append(absentlist)

#         absentlists = sorted(absentlists, key=lambda k: k['id'], reverse=True)
#         result['data'] = absentlists[0] if pk else absentlists

        return result
        

# class Rest(fxapi.RestView):
#   name = 'absentlist'
#   model = AbsentList
# 
# #   safe_fields = ['consumer', 'id']
# #   exclude_fields = ['active', 'status']
# #   filter_by_user = 'seller'
# 
#   model_list_fields = ['date','absent_regno', 'absent_name',]
#   
# #   model_edit_fields = list(set(model_list_fields) - set([
# #       'consumer', 'id', 'keywords', 
# #     ])) + ['consumer_id']
# 
# #   extra_edit_fields = [
# #       'keywords',
# #       'address_street',
# #       'address_postal_code',
# #       'address_city',
# #       'address_region',
# #       'address_country',
# # 
# #       'consumer_first_name',
# #       'consumer_last_name',
# #       'consumer_email',
# #       'consumer_phone_number',
# #       'consumer_preferred_method',
# #       'PaymentMode',
# #       'company_name',
# #       'reference',
# #       'accept_campaign',
# #       'reinquire',
# #       'au_minimum_price',
# #       'au_minutes_to_auction_start',
# #       #'companyaddress_postal_code'
# #   ]
# #   extra_list_fields = extra_edit_fields
# 
# 
#   @classmethod
#   def action_list(cls, request, limit=None, pk=None, action='list', 
#     is_buyer=False):
# 
#     result = super(Rest, cls).action_list(request, limit, pk, action, 
#       is_buyer=is_buyer)
# 
#     if not result['status'] or not result['data']:
#       return result
#     try:
#         leads = []
#         _leads = result['data']
#     
#         if pk:
#           lead = {}
#           _lead = result['data']
#           for field in cls.get_model_list_fields(pk):
#             if hasattr(_lead, field):
#               lead[field] = getattr(_lead, field)
#           _leads = [lead]
#     
#         for lead in _leads:
#           if lead['consumer']:
#             _pk = lead['consumer'] if isinstance(lead['consumer'], (int, long)) else lead['consumer'].pk
#             consumer = Consumer.objects.get(pk=_pk)
#             lead['consumer'] = None
#             lead['consumer_id'] = consumer.pk
#     
#             prefix = 'consumer_'
#             for field in cls.extra_list_fields:
#               if field.startswith(prefix):
#                 lead[field] = getattr(consumer, field.replace(prefix,''))
#     
#             if consumer.address:
#               address = consumer.address
#     
#               prefix = 'address_'
#               for field in cls.extra_list_fields:
#                 if field.startswith(prefix):
#                   lead[field] = getattr(address, field.replace(prefix,''))
#             
#             if consumer.company:
#               company = consumer.company
#               companyaddress = company.address
#               
#               prefix = 'companyaddress_'
#               for field in cls.extra_list_fields:
#                 if field.startswith(prefix):
#                   lead[field] = getattr(companyaddress, field.replace(prefix,''))
#     
#               prefix = 'company_'
#               for field in cls.extra_list_fields:
#                 if field.startswith(prefix):
#                   lead[field] = getattr(company, field.replace(prefix,''))
#             
#             # if consumer.company.address:
#             #   companyaddress = consumer.company.address
#     
#             #   prefix = 'companyaddress_'
#             #   for field in cls.extra_list_fields:
#             #     if field.startswith(prefix):
#             #       lead[field] = getattr(companyaddress, field.replace(prefix,''))      
#              
#           #if lead['keywords']:
#           _lead = Lead.objects.get(pk=lead['id'])
#           
#           update_recently_view_lead(_lead, request, 'API')
#           
#           keywords = [kw.name for kw in _lead.keywords.all()]
#           lead['keywords'] = ','.join(keywords)
#           lead['Total'] = _lead.sale + _lead.pre_sold
#           lead['available'] = lead['sale'] - lead['sold']
#           lead['phone_verified'] = _lead.phone_verified
#           lead['email_verified'] = _lead.email_verified
#           lead['reinquire'] = _lead.reinquire
#           lead['consumer'] = lead.get('consumer_first_name', '')
#           lead['consumer_lastname'] = lead.get('consumer_last_name', '')
#           lead['consumer_phno'] = lead.get('consumer_phone_number', '')
#           leads.append(lead)
#         
#         leads = sorted(leads, key=lambda k: k['id'],reverse=True)
#         result['data'] = leads[0] if pk else leads
#     except Exception as e:
#         logger.error("Unknown error in API for" + str(request.user))
#         result['status'] = False
#         result['data'] = None
#         result['error'] = e.message or e.messages
#     
#     return result
# 
#   @classmethod
#   @transaction.commit_on_success
#   def action_update(cls, request, pk=None):
#     sid = transaction.savepoint() 
#     result = super(Rest, cls).action_update(request, pk)
#     if not result['status'] or not result['data']:
#           return result
#     try:
#         lead = result['data']
#         lead = Lead.objects.get(pk=lead)
#         consumerid = lead.consumer_id
#         ActorProvidedLead.objects.get_or_create(actor=lead.seller, lead=lead)
#         
#     
#         fields = [f for f in cls.extra_edit_fields if f.startswith('consumer_') and f != 'consumer_id']
#         if fields:
#           consumer = Consumer()
#           if 'consumer_id' in request.POST and request.POST['consumer_id']:
#             consumer = Consumer.objects.get(pk=request.POST['consumer_id'])
#           
#           if consumerid  != None:
#               consumer = Consumer.objects.get(pk=consumerid )
#              
#           for field in fields:
#             if field in request.POST and request.POST[field]:
#               setattr(consumer, field.replace('consumer_', ''), request.POST[field])
#     
#           afields = [f for f in cls.extra_edit_fields if f.startswith('address_')]
#           if afields:
#             address = consumer.address if consumer.address else ConsumerAddress()
#     
#             for field in afields:
#               if field in request.POST and request.POST[field]:
#                 setattr(address, field.replace('address_', ''), request.POST[field])
#             address.save()
#           
#           cfields = [f for f in cls.extra_edit_fields if f.startswith('companyaddress_')]
#           
#           # if cfields:
#           #   companyaddress = consumer.company.address if consumer.company.address else CompanyAddress()
#           
#           #   for field in cfields:
#           #     if field in request.POST and request.POST[field]:
#           #       setattr(companyaddress, field.replace('companyaddress_', ''), request.POST[field])
#           #   companyaddress.save() 
#           
#           bfields = [f for f in cls.extra_edit_fields if f.startswith('company_')]
#           
#           if bfields or cfields:
#             company = consumer.company if consumer.company else ConsumerCompany()
#             companyaddress = company.address if company.address else CompanyAddress()
#             for field in cfields:
#               if field in request.POST and request.POST[field]:
#                 setattr(companyaddress, field.replace('companyaddress_', ''), request.POST[field])
#             companyaddress.save() 
#             
#             for field in bfields:
#               if field in request.POST and request.POST[field]:
#                 setattr(company, field.replace('company_', ''), request.POST[field])
#             company.address = companyaddress    
#             company.save()
#     
#             consumer.company = company 
#             consumer.address = address
#     
#           consumer.save()
#           lead.consumer = consumer
#           
#           accept_campaign = request.POST.get('accept_campaign', '1')
#           
#           if accept_campaign == '0' or accept_campaign.lower() == 'false':
#             lead.reinquire = False
#           elif accept_campaign == '1' or accept_campaign.lower() == 'true':
#             lead.reinquire = True
#           
#           reinquire_lead =  request.POST.get('reinquire', '0')  
#           if reinquire_lead == '0' or reinquire_lead.lower() == 'false':
#             lead.reinquire = False
#           elif reinquire_lead == '1' or reinquire_lead.lower() == 'true':
#             lead.reinquire = True  
#             
#                
#           lead.save()
#           
#           set_auction = str(request.POST.get('set_auction', '0'))
#           if set_auction == 'on' or set_auction == '1':
#             aufields = [f for f in cls.extra_edit_fields if f.startswith('au_')]
#             if aufields:
#               if hasattr(lead, 'auction'):
#                 auction = lead.auction 
#               else:
#                 auction = Auction()
#                 auction.lead = lead
#       
#               for field in aufields:
#                 if field in request.POST and request.POST[field]:
#                   setattr(auction, field.replace('au_', ''), int(request.POST[field]))
#               auction.save()
# 
#         if 'keywords' in request.POST:
#           keywords = request.POST['keywords'].split(',')
#           saved_keywords = []
#     
#           for keyword in keywords:
#             if keyword:
#               keyword = keyword.strip()
#               kw, created = LeadKeyword.objects.get_or_create(name=keyword)
#               saved_keywords.append(kw)
#     
#           if saved_keywords:
#             lead.keywords = saved_keywords
#             lead.save()
#         transaction.savepoint_commit(sid)
#     
#     except Exception as e:
#         transaction.savepoint_rollback(sid)
# 
#         result['status'] = False
#         result['data'] = None
#         result['error'] = e.message or e.messages
#         
#     return result
# 
#   @classmethod
#   def action_delete(cls, request, pk):
#     list_result = super(Rest, cls).action_list(request, pk=pk, action='delete')
# 
#     if list_result['status'] and list_result['data']:
#       
#       list_result['data'].status = 'inactive'
#       list_result['data'].active = False
#       list_result['data'].save()
# 
#       list_result['data'] = list_result['data'].pk
# 
#     return list_result
# 
# 
#   @classmethod
#   def action_buy(cls, request, pk):
#     
#     access, user = cls.validate(request, 'get')
#     result = ""
#     buy_result = {}
#     list_result = super(Rest, cls).action_list(request, pk=pk, action='buy')
#     actor = Actor.objects.get(pk=user)
#     lead_id = request.POST.get('pk')
#     lead = Lead.objects.get(pk=int(lead_id))
#     leadRequired = request.POST.get('sale')
# 
#     update_recently_view_lead(lead, request, 'API')
#     error, order, transaction = logic.checkout_using_account(
#       actor, 'api', lead, request=request)
# 
#     if error:
#       if isinstance(error, logic.LeadUnavailableError):
#         result += "Lead is unavailable. Leads remaining:" + \
#           str(error.value) +'. '
# 
#       if isinstance(error, logic.InvalidLeadError):
#         result += "This lead was inactive or deleted. "
# 
#       if isinstance(error, logic.InvalidQuantityError):
#         result += "You provided invalid quantity. "
# 
#       if isinstance(error, logic.LeadAlreadyBoughtError):
#         result += "This lead already bought by you. "
# 
#       if isinstance(error, logic.SellerCantBeBuyerError):
#         result += "Can't buy the same lead you provided. "
# 
#       if isinstance(error, logic.LowAccountBalanceError):
#         result += "Not enough balance on your account. You need:" + \
#           "%.2f %s. " % error.value
# 
#       if isinstance(error, logic.UnidentifiedCheckoutError):
#         logging.error("Unknown error in API", error)
#         result += "Unknown error. Please contact support."
# 
#       buy_result ['status'] = 'false'
#       buy_result ['data'] = ''
#       buy_result['error'] = result
# 
#       return buy_result
# 
#     buy_result ['status'] = 'true'
#     buy_result ['data'] = 'Order sucessfully'
#     buy_result['error'] = ''
#     return buy_result


# class Search(fxapi.RestView):
#   name = 'search'
#   model = Lead
#   actions = ['list', 'get']
# 
#   searchview = SearchView(form_class=LeadSearchFilter, results_per_page=5)
# 
#   query_fields = ['q', 'page', 'result_per_page', 'budget_start', 'budget_end',
#     'deal_start', 'deal_end', 'price_start', 'price_end', 'locations',
#     'keywords', 'category']
# 
#   list_fields = ['id','title', 'description', 'price', 'price_currency','sale',
#     'deal_starts', 'deal_ends', 'category_id', 'language', 'generation_method',
#     'generation_date', 'keywords', 'created', 'ranking', 'sold', 'pre_sold',]
# 
#   detail_fields = list_fields + [
#       'keywords',
#       'address_postal_code',
#       'address_city',
#       'address_region',
#       'address_country',
# 
#       'consumer_first_name',
#       'consumer_last_name',
#       'consumer_email',
#       'consumer_phone_number',
#       #'consumer_company'
#   ]
# 
#   @classmethod
#   def action_list(cls, request):
#     output = {'status':False, 'data':[], 'error':[]}
#     access, user = cls.validate(request, 'list')
# 
#     if not access:
#       output['error'].append("You don't have access to it")
#       return output
# 
#     #form = searchform.LeadSearchFilter(request.GET)
# 
#     cls.searchview.request = request
#     cls.searchview.form = cls.searchview.build_form()
#     cls.searchview.query = cls.searchview.get_query()
#     cls.searchview.results = cls.searchview.get_results()
#     #results = form.build_page()
#     (paginator, page) = cls.searchview.build_page()
# 
#     context = {
#         'query': cls.searchview.query,
#         #'form': self.form,
#         'leads': [],
#         'current_page': page.number,
#         'total_result': page.paginator.count,
#         #'paginator': paginator,
#         #'suggestion': None,
#     }
#     
#     for result in page.object_list:
#       try:
#         update_recently_view_lead(result.object, request, 'API')
#         update_recent_search(request.GET.get('q'), request, 'API')
#         context['leads'].append(cls._get_model(result.object, user))
#       except Exception as e:
#         output['error'].append(result.object.id)
#         print 'Error parsing', result.object.id, e
# 
#     output['data'] = context
#     output['status'] = True
#     return output
# 
#   @classmethod
#   def _get_model(cls, lead, user, pk=None):
#     brought = ActorBoughtLead.objects.filter(actor=user, lead=lead).exists()
# 
#     val = {}
#     for prob in cls.list_fields:
#         if(prob =='keywords'):            
#             keywords = [kw.name for kw in lead.keywords.all()]
#             val['keywords'] = ','.join(keywords)  
#             val[prob] = val['keywords'] 
#         
#         if(prob!='keywords'):
#             if hasattr(lead, prob):
# 
#                 val[prob] = getattr(lead, prob)
#     
#     if pk != None:
#         consumer = lead.consumer
#         prefix = 'consumer_'
#         for field in cls.detail_fields:
#             if(field == "address_city") and (field=="address_postal_code") and (field=="address_country"):
#                 val[field] = getattr(consumer, field.replace(prefix,''))
#     
#         if consumer.address:
#             address = consumer.address
#     
#             prefix = 'address_'
#             for field in cls.detail_fields:
#               if field.startswith(prefix):
#                 val[field] = getattr(address, field.replace(prefix,''))
#             
#     #ended(taskid:400)
#     
#     if brought and lead.consumer:
#       consumer = lead.consumer  
#        
#       val['consumer_id'] = consumer.pk
#        
#       prefix = 'consumer_'
#       for field in cls.detail_fields:
#         if field.startswith(prefix):
#           val[field] = getattr(consumer, field.replace(prefix,''))
# 
#       if consumer.address:
#         address = consumer.address
# 
#         prefix = 'address_'
#         for field in cls.detail_fields:
#           if field.startswith(prefix):
#             val[field] = getattr(address, field.replace(prefix,''))
#              
#     if(pk!=None):
#         val['available'] = val['sale']-val['sold']
#  
#     val['total'] = val['pre_sold'] + val['sale']
#     val['seller_name'] = lead.seller.company.name
#     val['available'] = val['sale']-val['sold']
#     val['phone_verified'] = lead.phone_verified
#     val['email_verified'] = lead.email_verified
#     val['reinquire'] = lead.reinquire
#     val['price'] = float(lead.price_as(user.currency))
#     val['price_currency'] = user.currency
#     
#     del val['sold']
#     del val['pre_sold']
#     del val['sale']
#     return val
# 
#   @classmethod
#   def action_get(cls, request, pk):
#     output = {'status':False, 'data':None, 'error':[]}
#     access, user = cls.validate(request, 'get')
#     
#     if not access:
#       output['error'].append("You don't have access to it")
#       return output
# 
#     lead = cls.model.objects.get(pk=pk)
#     if not lead.isactive():
#       raise lead.DoesNotExist("Lead matching query does not exist.")
#     lead.viewed()
#     
#     try:
#       update_recent_search(lead.title, request, 'API')
#     except:
#       import traceback
#       traceback.print_exc()
#     output['data'] = cls._get_model(lead, user,pk)    
#     output['status'] = True
#     return output
# 
# 
#     # result = ""
#     # buy_result = {}
#    
#     # actor = Actor.objects.get(pk=pk)
#     # lead_id = request.POST.get('pk')
#     # lead = Lead.objects.get(pk=int(lead_id))
#     # leadsboughts = ActorBoughtLead.objects.filter(actor=int(request.user.id), lead = lead )
#     # providedlead = ActorProvidedLead.objects.filter(actor=int(request.user.id), lead = lead)
#     # leadRequired = request.POST.get('sale')
#     # leadSale = lead.sale
#     # leadSold = lead.sold
#     # leadstatus = lead.status
#     # leadAvailable = leadSale-leadSold
#     # lead_deleted = lead.active
#     
#     # buy_result ['status']='true'
#     # buy_result ['data'] ="Order sucessfully"
#     # buy_result['error'] = ''   
#  
#     # return buy_result
# 
# 
# class Transactions(fxapi.RestView):
#  
#     name = 'transactions'
#     model = Transaction
#     actions = ['list']
#     
#     safe_fields = []
#     exclude_fields = []
#     filter_by_user = 'actor'
#     query_fields = [
#         'date_from', 'date_to', 'page', 'transaction_type',
#         'result_per_page', 'transaction_id', 
#     ]
#     
#     list_fields = [
#         'id', 'transaction_type', 'actor_key', 'created',
#         'transaction_date', 'reference', 'order_id', 'transaction_id',
#     ]
#     
#     extra_edit_fields = [
#         'transaction_type',
#     ]
#     extra_list_fields = extra_edit_fields
#     
#     searchview = SearchView(form_class=TransactionSearchFilter,
#       results_per_page=5) 
#     
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
#       
#       output = {'status':False, 'data':[], 'error':[]}
#       access, user = cls.validate(request, 'list')   
#     
#       if not access:
#         output['error'].append("You don't have access to it")
#         return output
#       
#       result = super(Transactions, cls).action_list(request, pk)
#       _transactions = result['data']
#       transaction_list = []
#       for transaction in _transactions:
#         transaction_list.append(int(transaction['actor_id']))
#         
#       date_from = request.GET.get('date_from', '')
#       date_to   = request.GET.get('date_to', '')
#       if date_from == "" or date_to == "" :
#         transaction_obj = cls.model.objects.filter(
#           actor__in = transaction_list).order_by('-transaction_date')
#       else:
#         transaction_obj =  cls.model.objects.filter(
#           transaction_date__range = [date_from, date_to],
#           actor__in = transaction_list).order_by('-transaction_date')
#       
#       if request.GET.get('transaction_type'):
#         transaction_obj = transaction_obj.filter(
#           transaction_type=request.GET['transaction_type'])
# 
#       cls.searchview.request = request
#       cls.searchview.form = cls.searchview.build_form()
#       cls.searchview.query = cls.searchview.get_query()
#       cls.searchview.results = transaction_obj
#       #cls.searchview.results = cls.searchview.get_results()
#       #results = form.build_page()
#       (paginator, page) = cls.searchview.build_page()
#     
#       context = {
#         'Transactions': [],
#         'current_page': page.number,
#         'total_result': page.paginator.count
#       }  
#      
#       for result in page.object_list:
#       
#         try:      
#           context['Transactions'].append(cls._get_model(result, user))
#           context['Transactions'] = sorted(context['Transactions'], 
#             key=lambda k: k['transaction_date'], reverse=True)
#         except Exception as e:
#           output['error'].append(result.object.id)
#           print 'Error parsing', result.object.id, e
#           
#       output['data'] = context
#       output['status'] = True
#       
#       return output
#     
#     @classmethod
#     def _get_model(cls, stats, user):
#     
#       val = {}   
#       
#       for prob in cls.list_fields: 
#         if (prob == "actor_key"):
#           actorObj = Actor.objects.get(pk=user)
#           val['actor_key'] = actorObj.actor_key
#         if hasattr(stats, prob):    
#           val[prob] = getattr(stats, prob)      
#           
#       return val
#  
# 
# class Trades(fxapi.RestView):
#  
#   name = 'trades'
#   model = Trade
#   actions = ['list','get']
# 
#   safe_fields = []
#   exclude_fields = []
#   filter_by_user = 'seller'
#   query_fields = ['date_from','date_to','lead_id','page','result_per_page']    
#   
#   list_fields = ['transaction_id', 'lead_id', 'quantity', 'price',
#     'price_currency', 'commission_currency', 'seller_sales_currency',
#     'seller_sales_total', 'seller_sales_transaction_id', 'commission_total',
#     'commission_percentage', 'transaction_date', 
#   ]
#   
#   searchview = SearchView(form_class= TradeSearchFilter,results_per_page=5)
# 
#   @classmethod
#   def action_list(cls, request, limit=None, pk=None, action='list'):
#         
#     output = {'status':False, 'data':[], 'error':[]}
#     access, user = cls.validate(request, 'list')   
# 
#     if not access:
#       output['error'].append("You don't have access to it")
#       return output
#     
#     result = super(Trades, cls).action_list(request, pk)
#     _trades = result['data']
#     trade_list = []
#     for trade in _trades:
#       trade_list.append(int(trade['id']))
#       
#     date_from = request.GET.get('date_from', '')
#     date_to   = request.GET.get('date_to', '')
#     if date_from == "" or date_to == "" :
#       trade_obj = cls.model.objects.filter(
#         pk__in = trade_list).order_by('-transaction_date')
#     else:
#       trade_obj =  cls.model.objects.filter(
#         created_date__range = [date_from, date_to], 
#         pk__in = trade_list).order_by('-transaction_date')
#     
#     if request.GET['lead_id']:
#       trade_obj = trade_obj.filter(lead_id=request.GET['lead_id'])
# 
#     cls.searchview.request = request
#     cls.searchview.form = cls.searchview.build_form()
#     cls.searchview.query = cls.searchview.get_query()
#     cls.searchview.results = trade_obj
#     #cls.searchview.results = cls.searchview.get_results()
#     #results = form.build_page()
#     (paginator, page) = cls.searchview.build_page()
# 
#     context = {
#       'trades': [],
#       'current_page': page.number,
#       'total_result': page.paginator.count,
#     }
# 
#     for result in page.object_list:
#     
#       try:
#         _trade = cls._get_model(result, user)
#         
#         _trade['price'] = CurrencyExchangeRate.Convert(
#           _trade['price'], _trade['price_currency'], user.currency)[0]
#         _trade['price'] = format_price(_trade['price'], user.currency)
# 
#         _trade['seller_sales_total'] = CurrencyExchangeRate.Convert(
#           _trade['seller_sales_total'], _trade['seller_sales_currency'], 
#           user.currency)[0]
#         _trade['seller_sales_total'] = format_price(
#           _trade['seller_sales_total'], user.currency)
# 
#         _trade['commission_total'] = CurrencyExchangeRate.Convert(
#           _trade['commission_total'], _trade['commission_currency'], 
#           user.currency)[0]
#         _trade['commission_total'] = format_price(
#           _trade['commission_total'], user.currency)
# 
#         _trade['price_currency'] = user.currency
#         del _trade['seller_sales_currency']
#         del _trade['commission_currency']
#         
#         context['trades'].append(_trade)
#       except Exception as e:
#         output['error'].append(result.object.id)
#         print 'Error parsing', result.object.id, e
# 
#     context['trades'] = sorted(context['trades'], 
#       key=lambda k: k['transaction_date'], reverse=True)
#     output['data'] = context
#     output['status'] = True
#     
#     return output
# 
#   @classmethod
#   def _get_model(cls, trade, user):
#   
#     val = {}   
#     
#     for prob in cls.list_fields:       
#       if hasattr(trade, prob):          
#         val[prob] = getattr(trade, prob)
#       
#       if prob == "lead_id":
#         lId = val['lead_id']            
#         leadinfo = Lead.objects.get(id = lId)    
#         val['title'] = leadinfo.title
#             
#     return val


# class Users(fxapi.RestView):
#  
#   name = 'users'
#   model = User
#   actions = ['list']
# 
# #   safe_fields = []
# #   exclude_fields = []
# #   filter_by_user = ''
#   
#   query_fields = ['date_from','date_to','result_per_page']  
# #   model_list_fields = ['email','id']
#   
# #   list_fields = ['email','user_ptr_id','actor_key','updated_on']
#      
#   searchview = SearchView(form_class=ActorSearchFilter, results_per_page=100000)
# 
#   @classmethod
#   def action_list(cls, request, limit=None, pk=None, action='list'):
#         
#     output = {'status':False, 'data':[], 'error':[]}
#     access, user = cls.validate(request, 'list')   
# 
#     if not access:
#       output['error'].append("You don't have access to it")
#       return output
#     
#     result = super(Actors, cls).action_list(request, pk)
#     date_from = request.GET.get('date_from', '')
#     date_to   = request.GET.get('date_to', '')
#     if date_from == "" or date_to == "" :
#       actor_obj = cls.model.objects.all().order_by('-user_ptr')
#     else:
#       actor_obj = cls.model.objects.filter(
#         updated_on__range=[date_from, date_to]).order_by('-user_ptr')
#       #actor_obj =  cls.model.objects.all()
#     cls.searchview.request = request
#     cls.searchview.form = cls.searchview.build_form()
#     cls.searchview.query = cls.searchview.get_query()
#     cls.searchview.results = actor_obj
#     #cls.searchview.results = cls.searchview.get_results()
#     #results = form.build_page()
#     (paginator, page) = cls.searchview.build_page()
# 
#     context = {
#         'actors': [],
#         'total_result': page.paginator.count,
#     }
# 
#     #result = super(Actors, cls).action_list(request, pk)
#     for result in page.object_list:
#     
#       try:      
#         context['actors'].append(cls._get_model(result, user))
#         context['actors'] = sorted(context['actors'], 
#           key=lambda k: k['user_ptr_id'], reverse=True)
#         
#       except Exception as e:
#         output['error'].append(result.object.id)
#         print 'Error parsing', result.object.id, e
# 
#     output['data'] = context
#     output['status'] = True
#     return output
# 
#   @classmethod
#   def _get_model(cls, actor, user):
#   
#     val = {}   
#     
#     for prob in cls.list_fields:
#       if hasattr(actor, prob):
#         val[prob] = getattr(actor, prob)
#     return val


# class ActorCampaignEmailStatistics(fxapi.RestView):
#  
#   name = 'ActorCampaignEmailStatistics'
#   model = ActorCampaignEmailStatistics
#   actions = ['list']
# 
#   safe_fields = []
#   exclude_fields = []
#   query_fields = ['date_from','date_to','page','result_per_page']    
#   
#   list_fields = ['id','LeadId','leadbuyer','created','emailcampaignurl']
#   
#   searchview = SearchView(form_class=ActorCampaignEmailStatisticsFilter, 
#     results_per_page=5)
# 
#   @classmethod
#   def action_list(cls, request, limit=None, pk=None, action='list'):
# 
#     output = {'status':False, 'data':[], 'error':[]}
#     access, user = cls.validate(request, 'list')
# 
#     if not access:
#       output['error'].append("You don't have access to it")
#       return output
# 
#     cls.searchview.request = request
#     cls.searchview.form = cls.searchview.build_form()
#     cls.searchview.query = cls.searchview.get_query()
#     cls.searchview.results = cls.searchview.get_results()
#     #results = form.build_page()
#     (paginator, page) = cls.searchview.build_page()
# 
#     context = {
#         'ActorCampaignEmailStatistics': [],
#         'current_page': page.number,
#         'total_result': page.paginator.count
#     }  
#    
#     result = super(ActorCampaignEmailStatistics, cls).action_list(request, pk)
#  
#     for result in page.object_list:
#     
#       try:
#         context['ActorCampaignEmailStatistics'].append(cls._get_model(result.object, user))
#         
#       except Exception as e:
#         output['error'].append(result.object.id)
#         print 'Error parsing', result.object.id, e
# 
#     output['data'] = context
#     output['status'] = True
#     
#     return output
# 
#   @classmethod
#   def _get_model(cls, stats, user):
#   
#     val = {}
#     
#     for prob in cls.list_fields:
#       if hasattr(stats, prob):
#         val[prob] = getattr(stats, prob)
#     
#     return val
# 
# 
# class LeadCategoryAPI(fxapi.RestView):
#  
#     name = 'categories'
#     model = LeadCategory
#     actions = ['list']
#     safe_fields = []
#     exclude_fields = []
#     query_fields = ['language','page','result_per_page']
#     
#     list_fields = ['name','category_number']
#    
#     searchview = SearchView(form_class=CategorySearchFilter, results_per_page=5)
#   
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
#     
#       output = {'status':False, 'data':[], 'error':[]}
#       access, user = cls.validate(request, 'list')
#       
#       if not access:
#         output['error'].append("You don't have access to it")
#         return output
#         
#       category_obj = cls.model.objects.all()
#       
#       cls.searchview.request = request
#       cls.searchview.form = cls.searchview.build_form()
#       cls.searchview.query = cls.searchview.get_query()
#       cls.searchview.results = category_obj
#       #cls.searchview.results = cls.searchview.get_results()
#       #results = form.build_page()
#       (paginator, page) = cls.searchview.build_page()
#       
#       context = {
#         'Categories': [],
#         'current_page': page.number,
#         'total_result': page.paginator.count
#       }  
#       language = request.GET.get('language', 'en')
#       result = super(LeadCategoryAPI, cls).action_list(request, pk)
#       
#       for result in page.object_list:
#       
#         try:
#           context['Categories'].append(cls._get_model(result, user ,language))
#           
#         except Exception as e:
#           output['error'].append(result.object.id)
#           print 'Error parsing', result.object.id, e
#       
#       output['data'] = context
#       output['status'] = True
#       
#       return output
#     
#     @classmethod
#     def _get_model(cls, stats, user,language):
#     
#       val = {}
#       
#       for prob in cls.list_fields:
#         if hasattr(stats, prob):
#           val[prob] = getattr(stats, prob)
#         
#         translation.activate(language)
#       
#       valtrans = {}
#       for v in val:
#         if v == 'name':
#           valtrans['name'] = translation.ugettext(val['name'])
#         valtrans['category'] = val['category_number']
#     
#       return valtrans
# 
# 
# class LeadFilterAPI(fxapi.RestView):
#  
#     name = 'filters'
#     model = LeadFilter
#     actions = ['list']
#     safe_fields = []
#     exclude_fields = []
#     filter_by_user = 'actor'
#     query_fields = ['page','result_per_page']
#     
#     list_fields = [
#       'id', 'name', 'description', 'status', 'search', 'count',
#       'clat', 'clon', 'cad', 'created', 'crad', 'leadcount','actor',
#     ]
#    
#     searchview = SearchView(form_class=SearchFilter, results_per_page=5)
# 
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
#     
#       output = {'status':False, 'data':[], 'error':[]}
#       access, user = cls.validate(request, 'list')
#       
#       if not access:
#         output['error'].append("You don't have access to it")
#         return output
#         
#       result = super(LeadFilterAPI, cls).action_list(request, pk)
#       _leads = result['data']
#       actor_list = []
# 
#       for lead in _leads:
#         actor_list.append(lead['actor_id'])
#       actor_list = set(actor_list)
#       leadfilter_obj =  cls.model.objects.filter(
#         actor__in=actor_list).exclude(status="inactive")
# 
#       cls.searchview.request = request
#       cls.searchview.form = cls.searchview.build_form()
#       cls.searchview.query = cls.searchview.get_query()
#       cls.searchview.results = leadfilter_obj
#       #cls.searchview.results = cls.searchview.get_results()
#       #results = form.build_page()
#       (paginator, page) = cls.searchview.build_page()
#       
#       context = {
#           'filters': [],
#           'current_page': page.number,
#           'total_result': page.paginator.count
#       }  
#       language = request.GET.get('language', 'en')
#       
#       for result in page.object_list:
#       
#         try:
#           context['filters'].append(cls._get_model(result, user))
#           context['filters'] = sorted(context['filters'],
#             key=lambda k: k['id'], reverse=True)
#         except Exception as e:
#           output['error'].append(result.object.id)
#           print 'Error parsing', result.object.id, e
# 
#       output['data'] = context
#       output['status'] = True
#       
#       return output
#     
#     @classmethod
#     def _get_model(cls, stats, user):
#     
#       val = {}
#       
#       for prob in cls.list_fields:
#         if hasattr(stats, prob):
#           if not prob == 'actor' :
#             val[prob] = getattr(stats, prob)
#           
#       return val
#  
# class RecentLeadsAPI(fxapi.RestView):
#  
#     name = 'recentleads'
#     model = RecentlyviewLeads
#     actions = ['list']
#     safe_fields = []
#     exclude_fields = []
#     filter_by_user = 'user_id'
#     query_fields = ['page','result_per_page','date_from','date_to']
# 
#     list_fields = ['id','created']
#    
#     searchview = SearchView(form_class=RecentLeadsFilter, results_per_page=5)
# 
#   
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
# 
#       output = {'status':False, 'data':[], 'error':[]}
#       access, user = cls.validate(request, 'list')
#       
#       if not access:
#         output['error'].append("You don't have access to it")
#         return output
#       
#       result = super(RecentLeadsAPI, cls).action_list(request, pk)
#       _recentleads = result['data']
#       recentleads_list = []
#       for recentlead in _recentleads:
#         recentleads_list.append(int(recentlead['id']))
#         
#       #recentlead_obj = cls.model.objects.filter(pk__in = recentleads_list)
#       date_from = request.GET.get('date_from', '')
#       date_to   = request.GET.get('date_to', '')
#       if date_from == "" or date_to == "" :
#         recentlead_obj = cls.model.objects.filter(
#           pk__in=recentleads_list).order_by('-id')
#       else:
#         recentlead_obj =  cls.model.objects.filter(
#           created__range=[date_from, date_to], 
#           pk__in=recentleads_list).order_by('-id')
#       
#       cls.searchview.request = request
#       cls.searchview.form = cls.searchview.build_form()
#       cls.searchview.query = cls.searchview.get_query()
#       cls.searchview.results = recentlead_obj
#       #cls.searchview.results = cls.searchview.get_results()
#       #results = form.build_page()
#       (paginator, page) = cls.searchview.build_page()
#       
#       context = {
#         'recentlead': [],
#         'current_page': page.number,
#         'total_result': page.paginator.count
#       }
#       
#       for result in page.object_list:
#       
#         try:
#           context['recentlead'].append(cls._get_model(result, user))
#           context['recentlead'] = sorted(context['recentlead'],
#             key=lambda k: k['id'], reverse=True)
#         except Exception as e:
#           output['error'].append(result.object.id)
#           print 'Error parsing', result.object.id, e
#       
#       output['data'] = context
#       output['status'] = True
#       return output
#     
#     @classmethod
#     def _get_model(cls, stats, user):
#       from collections import OrderedDict
#       val = OrderedDict()  
#       
#       for prob in cls.list_fields:
#           if hasattr(stats, prob):
#             val[prob] = getattr(stats, prob)
#           
#           if prob == "id":
#             lId = val['id']
#             leadinfo = RecentlyviewLeads.objects.get(id = lId)
#             val['lead_id'] = leadinfo.lead.id
#             val['lead_title'] = leadinfo.lead.title
#             val['created'] = leadinfo.lead.created
#             #val['status'] = leadinfo.lead.status
#             #val['active'] = leadinfo.lead.active
#             #val['price'] = leadinfo.lead.price
#             #val['price_currency'] = leadinfo.lead.price_currency
#             #val['available'] = leadinfo.lead.sale
#       
#       return val
#      
#   
# class RecentSearchAPI(fxapi.RestView):
#  
#     name = 'recentsearch'
#     model = RecentlySearch
#     actions = ['list']
#     safe_fields = []
#     exclude_fields = []
#     filter_by_user = 'user'
#     query_fields = ['page', 'result_per_page', 'date_from', 'date_to']
#     
#     list_fields = ['id', 'activity_view', 'created']
#        
#     searchview = SearchView(form_class=RecentSearchFilter, results_per_page=5)
#   
#     @classmethod
#     def action_list(cls, request, limit=None, pk=None, action='list'):
#             
#       output = {'status':False, 'data':[], 'error':[]}
#       access, user = cls.validate(request, 'list')
#       
#       if not access:
#         output['error'].append("You don't have access to it")
#         return output
#       
#       result = super(RecentSearchAPI, cls).action_list(request, pk)
#       _recentsearches = result['data']
#       recentsearch_list = []
#       for recentsearch in _recentsearches:
#         recentsearch_list.append(int(recentsearch['id']))
#         
#       date_from = request.GET.get('date_from', '')
#       date_to   = request.GET.get('date_to', '')
#       if date_from == "" or date_to == "" :
#         recentsearch_obj = cls.model.objects.filter(
#           pk__in=recentsearch_list).order_by('-id')
#       else:
#         recentsearch_obj = cls.model.objects.filter(
#           created__range=[date_from, date_to],
#           pk__in=recentsearch_list).order_by('-id')
#       
#       cls.searchview.request = request
#       cls.searchview.form = cls.searchview.build_form()
#       cls.searchview.query = cls.searchview.get_query()
#       cls.searchview.results = recentsearch_obj
#       #cls.searchview.results = cls.searchview.get_results()
#       #results = form.build_page()
#       (paginator, page) = cls.searchview.build_page()
#       
#       context = {
#           'recentsearch': [],
#           'current_page': page.number,
#           'total_result': page.paginator.count
#       }  
#       
#       
#       for result in page.object_list:
#         try:
#           context['recentsearch'].append(cls._get_model(result, user))
#           context['recentsearch'] = sorted(context['recentsearch'],
#             key=lambda k: k['id'], reverse=True)
#         except Exception as e:
#           output['error'].append(result.object.id)
#           print 'Error parsing', result.object.id, e
#       
#       output['data'] = context
#       output['status'] = True
#       
#       return output
#     
#     @classmethod
#     def _get_model(cls, stats, user):
#     
#       val = {}   
#       for prob in cls.list_fields:
#         if hasattr(stats, prob):
#           val[prob] = getattr(stats, prob)
#       
#       val['search'] = val['activity_view']
#       del val['activity_view']
#       return val
