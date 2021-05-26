from django.shortcuts import render
from pages.models import Item
from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    d = Item.objects.get(namemach='Testing One')
    if request.method == 'POST':
        if 'reset' in request.POST:
            d2 = Item.objects.get(namemach='Testing One')
            d2.coke = 10
            d2.pepsi = 10
            d2.soda = 10
            d2.one = 5
            d2.five = 5
            d2.ten = 5
            d2.twentyfive = 5
            d2.save()
            messages.success(request,'Reset!')
            return redirect(request.path_info)

        if 'calculate' in request.POST:
            qc = request.POST['quantityc']
            qp = request.POST['quantityp']
            qs = request.POST['quantitys']
            num_one = request.POST['numone']
            num_ten = request.POST['numten']
            num_five = request.POST['numfive']
            num_twen = request.POST['numtwen']
            d3 = Item.objects.get(namemach='Testing One')
            if int(qc)>int(d3.coke) or int(qp)>int(d3.pepsi) or int(qs)>int(d3.soda):
                messages.error(request,'Not sufficient quantity present !')
                return redirect(request.path_info)

            elif int(qc)*25 + int(qp)*32 + int(qs)*47 >  1*int(num_one) + 10*int(num_ten) + 5*int(num_five) + 25*int(num_twen):
                messages.error(request,'You paid less amount !')
                return redirect(request.path_info)

            elif int(qc)*25 + int(qp)*32 + int(qs)*47 ==  1*int(num_one) + 10*int(num_ten) + 5*int(num_five) + 25*int(num_twen):
                d2 = Item.objects.get(namemach='Testing One')
                tempcoke = int(d2.coke)-int(qc)
                d2.coke = tempcoke
                temppepsi = int(d2.pepsi)-int(qp)
                d2.pepsi = temppepsi
                tempsoda = int(d2.soda)-int(qs)
                d2.soda = tempsoda

                tempone = int(d2.one)+int(num_one)
                d2.one = tempone
                tempten = int(d2.ten)+int(num_ten)
                d2.ten = tempten
                tempfive = int(d2.five)+int(num_five)
                d2.five = tempfive
                temptwen = int(d2.twentyfive)+int(num_twen)
                d2.twentyfive = temptwen
                d2.save()
                messages.success(request,'Enjoy, and yes you paid the exact amount !')
                return redirect(request.path_info)

            elif int(qc)*25 + int(qp)*32 + int(qs)*47 <  1*int(num_one) + 10*int(num_ten) + 5*int(num_five) + 25*int(num_twen):
                difference = 1*int(num_one) + 10*int(num_ten) + 5*int(num_five) + 25*int(num_twen) - int(qc)*25 - int(qp)*32 - int(qs)*47
                d2 = Item.objects.get(namemach='Testing One')
                tempcoke = int(d2.coke)-int(qc)
                d2.coke = tempcoke
                temppepsi = int(d2.pepsi)-int(qp)
                d2.pepsi = temppepsi
                tempsoda = int(d2.soda)-int(qs)
                d2.soda = tempsoda

                tempone = int(d2.one)+int(num_one)
                d2.one = tempone
                tempten = int(d2.ten)+int(num_ten)
                d2.ten = tempten
                tempfive = int(d2.five)+int(num_five)
                d2.five = tempfive
                temptwen = int(d2.twentyfive)+int(num_twen)
                d2.twentyfive = temptwen
                d2.save()

                coins=[1,5,10,25]
                i=len(coins)-1
                change_return = 1*int(num_one) + 10*int(num_ten) + 5*int(num_five) + 25*int(num_twen) - int(qc)*25 - int(qp)*32 - int(qs)*47
                note_count={
                    25:0,
                    10:0,
                    5:0,
                    1:0
                }
                j = 1
                while i>=0 and change_return >0:
                    if coins[i]<=change_return:
                        if(j==1):
                            if(d2.twentyfive>0):
                                change_return -=coins[i];
                                note_count[coins[i]]=note_count[coins[i]]+1;
                            else:
                                d2.coke = tempcoke+int(qc)
                                d2.pepsi = temppepsi+int(qp)
                                d2.soda = tempsoda+int(qs)
                                d2.one = tempone-int(num_one)
                                d2.ten = tempten-int(num_ten)
                                d2.five = tempfive-int(num_five)
                                d2.twentyfive = temptwen-int(num_twen)
                                d2.save()
                                messages.error(request,'Not sufficient balance !')
                                return redirect(request.path_info)
                        if(j==2):
                            if(d2.ten>0):
                                change_return -=coins[i];
                                note_count[coins[i]]=note_count[coins[i]]+1;
                            else:
                                d2.coke = tempcoke+int(qc)
                                d2.pepsi = temppepsi+int(qp)
                                d2.soda = tempsoda+int(qs)
                                d2.one = tempone-int(num_one)
                                d2.ten = tempten-int(num_ten)
                                d2.five = tempfive-int(num_five)
                                d2.twentyfive = temptwen-int(num_twen)
                                d2.save()
                                messages.error(request,'Not sufficient balance !')
                                return redirect(request.path_info)
                        if(j==3):
                            if(d2.five>0):
                                change_return -=coins[i];
                                note_count[coins[i]]=note_count[coins[i]]+1;
                            else:
                                d2.coke = tempcoke+int(qc)
                                d2.pepsi = temppepsi+int(qp)
                                d2.soda = tempsoda+int(qs)
                                d2.one = tempone-int(num_one)
                                d2.ten = tempten-int(num_ten)
                                d2.five = tempfive-int(num_five)
                                d2.twentyfive = temptwen-int(num_twen)
                                d2.save()
                                messages.error(request,'Not sufficient balance !')
                                return redirect(request.path_info)
                        if(j==4):
                            if(d2.one>0):
                                change_return -=coins[i];
                                note_count[coins[i]]=note_count[coins[i]]+1;
                            else:
                                d2.coke = tempcoke+int(qc)
                                d2.pepsi = temppepsi+int(qp)
                                d2.soda = tempsoda+int(qs)
                                d2.one = tempone-int(num_one)
                                d2.ten = tempten-int(num_ten)
                                d2.five = tempfive-int(num_five)
                                d2.twentyfive = temptwen-int(num_twen)
                                d2.save()
                                messages.error(request,'Not sufficient balance !')
                                return redirect(request.path_info)
                    else:
                        i-=1
                        j+=1
                print(note_count)

                i = 1
                for note,count in note_count.items():
                    if i==1:
                        d2.twentyfive-=count
                    elif i==2:
                        d2.ten-=count
                    elif i==3:
                        d2.five-=count
                    else:
                        d2.one-=count
                    i+=1
                d2.save()
                messages.success(request,'Enjoy, here is your change !')
                return redirect(request.path_info)

    context = {
        'data':d,
    }
    return render(request,'pages/index.html',context)

def untitled(request):
    return render(request,'pages/untitled.html')
