from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from vote_analysis_data .models import Analysis_vote
from django.contrib import messages

import matplotlib
matplotlib.use('Agg')  # Django ke liye important

import matplotlib.pyplot as plt
from io import BytesIO



def vote_graph(request):

    # ✅ Sirf 1 Player ka data nikalna
  
    count=Analysis_vote.objects.filter(team_name="RCB",player_name="Andre Russel").count()
    count1=Analysis_vote.objects.filter(team_name="KKR",player_name="Andre Russel").count()
    count2=Analysis_vote.objects.filter(team_name="SRH",player_name="Andre Russel").count()
    count3=Analysis_vote.objects.filter(team_name="LSG",player_name="Andre Russel").count()
    count4=Analysis_vote.objects.filter(team_name="MI",player_name="Andre Russel").count()
    count5=Analysis_vote.objects.filter(team_name="DD",player_name="Andre Russel").count()
    count6=Analysis_vote.objects.filter(team_name="RR",player_name="Andre Russel").count()
    count7=Analysis_vote.objects.filter(team_name="CSK",player_name="Andre Russel").count()
    count8=Analysis_vote.objects.filter(team_name="GT",player_name="Andre Russel").count()
    count9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Andre Russel").count()
    
    li_rusell=[count,count1,count2,count3,count4,count5,count6,count7,count8,count9]

    
   # li_rusell = [5,4,1,0,2,3,3,7,0,4]
    teams=['RCB','KKR','SRH','LSG','MI','DD','RR','CSK','GT','KXIP']
#
    #for v in player_votes:
    colors=['red','purple','orange','aquamarine','blue','red','pink','yellow','purple','red']
##
    #  teams.append(v.team_name)


    # ✅ Graph Banana
    plt.figure(figsize=(8,6))
    plt.bar(teams,li_rusell,color=colors,label="Team_Votes")
    plt.legend()
    plt.title("Andre Rusell Vote",color="black",fontsize=15)
    plt.xlabel("Teams")
    plt.ylabel("Votes")

    # ✅ Image Response Banana
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    
    return HttpResponse(buffer.getvalue(),content_type="image/png")
    print(player_votes)


def vote_graph1(request):
    
    count=Analysis_vote.objects.filter(team_name="RCB",player_name="Ravi Bishnoi").count()
    count1=Analysis_vote.objects.filter(team_name="KKR",player_name="Ravi Bishnoi").count()
    count2=Analysis_vote.objects.filter(team_name="SRH",player_name="Ravi Bishnoi").count()
    count3=Analysis_vote.objects.filter(team_name="LSG",player_name="Ravi Bishnoi").count()
    count4=Analysis_vote.objects.filter(team_name="MI",player_name="Ravi Bishnoi").count()
    count5=Analysis_vote.objects.filter(team_name="DD",player_name="Ravi Bishnoi").count()
    count6=Analysis_vote.objects.filter(team_name="RR",player_name="Ravi Bishnoi").count()
    count7=Analysis_vote.objects.filter(team_name="CSK",player_name="Ravi Bishnoi").count()
    count8=Analysis_vote.objects.filter(team_name="GT",player_name="Ravi Bishnoi").count()
    count9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Ravi Bishnoi").count()
    
    li_Bishnoi=[count,count1,count2,count3,count4,count5,count6,count7,count8,count9]

    teams=['RCB','KKR','SRH','LSG','MI','DD','RR','CSK','GT','KXIP']
#
    #for v in player_votes:
    colors=['red','purple','orange','aquamarine','blue','red','pink','yellow','purple','red']
##
    plt.figure(figsize=(6,4))
    plt.bar(teams,li_Bishnoi,color=colors,label="Team_Votes")
    plt.legend()
    plt.title("Ravi Bishnoi Vote",color="black",fontsize=15)
    plt.xlabel("Teams")
    plt.ylabel("Votes")

    # ✅ Image Response Banana
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(),content_type="image/png")


def vote_graph2(request):
    
    count=Analysis_vote.objects.filter(team_name="RCB",player_name="Liam Livingstone").count()
    count1=Analysis_vote.objects.filter(team_name="KKR",player_name="Liam Livingstone").count()
    count2=Analysis_vote.objects.filter(team_name="SRH",player_name="Liam Livingstone").count()
    count3=Analysis_vote.objects.filter(team_name="LSG",player_name="Liam Livingstone").count()
    count4=Analysis_vote.objects.filter(team_name="MI",player_name="Liam Livingstone").count()
    count5=Analysis_vote.objects.filter(team_name="DD",player_name="Liam Livingstone").count()
    count6=Analysis_vote.objects.filter(team_name="RR",player_name="Liam Livingstone").count()
    count7=Analysis_vote.objects.filter(team_name="CSK",player_name="Liam Livingstone").count()
    count8=Analysis_vote.objects.filter(team_name="GT",player_name="Liam Livingstone").count()
    count9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Liam Livingstone").count()
    
    li_stone=[count,count1,count2,count3,count4,count5,count6,count7,count8,count9]

    teams=['RCB','KKR','SRH','LSG','MI','DD','RR','CSK','GT','KXIP']
#
    
    colors=['red','purple','orange','aquamarine','blue','red','pink','yellow','purple','red']

    plt.figure(figsize=(6,4))
    plt.bar(teams,li_stone,color=colors,label="Team_Votes")
    plt.legend()
    plt.title("Liam livingstone Vote",color="black",fontsize=15)
    plt.xlabel("Teams")
    plt.ylabel("Votes")

    # ✅ Image Response Banana
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(),content_type="image/png")



























def Anal_data(request):
    if request.method=='POST':
        player_name=request.POST['player_name']
        team_name=request.POST['team_name']
        db=Analysis_vote(player_name=player_name,team_name=team_name)
        db.save()


        #template=loader.get_template('auction_login_page.html')
        #return HttpResponse(template.render())
        messages.success(request,"vote Succsessfully Done")
       
        


        return redirect('Anal_data')
    return render(request,'auction_login_page.html')


# Create your views here.
def show_results(request):
    db=Analysis_vote.objects.all().values()
    template=loader.get_template('show_result.html')

    context={
        'mydata':db
    }
    return HttpResponse(template.render(context,request))

def vote_count(request):
    
    count=Analysis_vote.objects.filter(team_name="RCB",player_name="Andre Russel").count()
    count1=Analysis_vote.objects.filter(team_name="KKR",player_name="Andre Russel").count()
    count2=Analysis_vote.objects.filter(team_name="SRH",player_name="Andre Russel").count()
    count3=Analysis_vote.objects.filter(team_name="LSG",player_name="Andre Russel").count()
    count4=Analysis_vote.objects.filter(team_name="MI",player_name="Andre Russel").count()
    count5=Analysis_vote.objects.filter(team_name="DD",player_name="Andre Russel").count()
    count6=Analysis_vote.objects.filter(team_name="RR",player_name="Andre Russel").count()
    count7=Analysis_vote.objects.filter(team_name="CSK",player_name="Andre Russel").count()
    count8=Analysis_vote.objects.filter(team_name="GT",player_name="Andre Russel").count()
    count9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Andre Russel").count()
    
    li_rusell=[count,count1,count2,count3,count4,count5,count6,count7,count8,count9]


 
    rcount=Analysis_vote.objects.filter(team_name="RCB",player_name="Ravi Bishnoi").count()
    rcount1=Analysis_vote.objects.filter(team_name="KKR",player_name="Ravi Bishnoi").count()
    rcount2=Analysis_vote.objects.filter(team_name="SRH",player_name="Ravi Bishnoi").count()
    rcount3=Analysis_vote.objects.filter(team_name="LSG",player_name="Ravi Bishnoi").count()
    rcount4=Analysis_vote.objects.filter(team_name="MI",player_name="Ravi Bishnoi").count()
    rcount5=Analysis_vote.objects.filter(team_name="DD",player_name="Ravi Bishnoi").count()
    rcount6=Analysis_vote.objects.filter(team_name="RR",player_name="Ravi Bishnoi").count()
    rcount7=Analysis_vote.objects.filter(team_name="CSK",player_name="Ravi Bishnoi").count()
    rcount8=Analysis_vote.objects.filter(team_name="GT",player_name="Ravi Bishnoi").count()
    rcount9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Ravi Bishnoi").count()
    
    li_bishnoi=[rcount,rcount1,rcount2,rcount3,rcount4,rcount5,rcount6,rcount7,rcount8,rcount9]


    lcount=Analysis_vote.objects.filter(team_name="RCB",player_name="Liam Livingstone").count()
    lcount1=Analysis_vote.objects.filter(team_name="KKR",player_name="Liam Livingstone").count()
    lcount2=Analysis_vote.objects.filter(team_name="SRH",player_name="Liam Livingstone").count()
    lcount3=Analysis_vote.objects.filter(team_name="LSG",player_name="Liam Livingstone").count()
    lcount4=Analysis_vote.objects.filter(team_name="MI",player_name="Liam Livingstone").count()
    lcount5=Analysis_vote.objects.filter(team_name="DD",player_name="Liam Livingstone").count()
    lcount6=Analysis_vote.objects.filter(team_name="RR",player_name="Liam Livingstone").count()
    lcount7=Analysis_vote.objects.filter(team_name="CSK",player_name="Liam Livingstone").count()
    lcount8=Analysis_vote.objects.filter(team_name="GT",player_name="Liam Livingstone").count()
    lcount9=Analysis_vote.objects.filter(team_name="KXIP",player_name="Liam Livingstone").count()
    
    li_stone=[lcount,lcount1,lcount2,lcount3,lcount4,lcount5,lcount6,lcount7,lcount8,lcount9]






    template=loader.get_template('final_result_winner.html')
    context={
        'myvote':li_rusell,
        'myvote1':li_bishnoi,
        'myvote2':li_stone,
       
    }
    return HttpResponse(template.render(context,request))
   
            

