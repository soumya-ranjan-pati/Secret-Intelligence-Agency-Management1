from django.conf.urls.static import static

from app_cybernatics_protetor import views
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from app_cybernatics_protetor.models import CreateAgent
from cybernatics_protetor import settings
from app_cybernatics_protetor.models import success_stories , Tips, Job_Postings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="home.html"),name='home'),
    #home index stories
    path('stories/',TemplateView.as_view(template_name='Stories.html')),
    path('story1/',TemplateView.as_view(template_name='story1.html')),
    path('story2/', TemplateView.as_view(template_name='story2.html')),
    path('all stories/',views.AllStories),
    #find jobs
    path('find_jobs/',TemplateView.as_view(template_name="findjobs.html")),
    path('viewjobs/',views.ViewJobs),
    path('apply_jobs/',ListView.as_view(template_name="apply_jobs.html",model=Job_Postings)),
    path('applicant/',views.ViewApplicants),
    path('viewclerkjobs/',views.ViewClerkjobs),
    path('applyclerkjobs/',TemplateView.as_view(template_name="apply_clerkjobs.html")),
    path('clerk_applicant/',views.ViewApplicants),
    #tips n suggestions
    path('tips/',TemplateView.as_view(template_name="tips.html")),
    path('suggest/',views.Suggest),
    path('showtips/',ListView.as_view(template_name='showtips.html',model=Tips)),
    path('about/',TemplateView.as_view(template_name="aboutus.html")),
    #admin path #
    path('adminlogin/',TemplateView.as_view(template_name="admin.html")),
    path('welcomeadmin/',views.AdminLogin),
    # admin side index #
    path('sucees/',TemplateView.as_view(template_name="successtories.html")),
    path('delete_success/',ListView.as_view(template_name="delete_stories.html",model=success_stories),name='delete_success'),
    path('<int:story_id>/',views.delete_story,name='delete_story'),
    path('succestories/',views.Success_Stories),

    #job postings#
    path('job/',TemplateView.as_view(template_name="jobposting.html")),
    path('postsaved/',views.PostSaved),
    #viewapplicants
    path('viewapplicants/',views.ShowApplicants),
    #appoin agent
    path('app_agent/',ListView.as_view(template_name="appoint_agent.html",model=CreateAgent)),
    path("assign_agent/",views.showAgent),
    path('savecasedetails/',views.Assign_Agent),
    #agent_manage
    path('agentmanage/',TemplateView.as_view(template_name="agent_manage.html")),
    #create agent
    path('createagent/',TemplateView.as_view(template_name="createagent.html")),
    path('agentregister/',views.AgentRegister),
    #view all agent
    path('viewallagents/',views.ViewAgents),
    #edit agent
    path('editagent/',views.Updateagent),
    path('update<int:pk>/',views.editagent.as_view()),
    #reports
    path('reports_admin/',views.adminreport),
    path('reports/',views.casereport),
    path('reports_defence/',views.defencereport),

    #admin logout
    path('admin_logout/',TemplateView.as_view(template_name="home.html")),
    #agent login
    path('agent_login/',TemplateView.as_view(template_name="agent_login.html")),
    path('agentsign/',views.Agent_Login),
    #case details
    path('case_details/',ListView.as_view(template_name="casedetails.html",model=CreateAgent)),
    path('agentcase/',views.GetDetails),
    #Update Evidences
    path('update_evidence/',views.upDetails),
    path('upevidence<int:pk>/',views.UpEvidence.as_view()),
    #agent_logout/
    path('agent_logout/',TemplateView.as_view(template_name="home.html")),
    #defence of minstry
    path('ministry/',TemplateView.as_view(template_name="defence_login.html")),
    path('welcomedefence/',views.Defence),
    #case creation
    path('case_creation/',TemplateView.as_view(template_name="casecreation.html")),
    path('create_case/',views.Create_Case),
    #defence_logout/
    path('defence_logout/',TemplateView.as_view(template_name="home.html"))



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)