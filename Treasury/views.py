from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .forms import *
from django.contrib import messages
import weasyprint
from django.template.loader import render_to_string
from .models import *


class TreasuryList(LoginRequiredMixin, ListView):
    login_url = '/auth/login/'
    model = Treasury
    paginate_by = 12
    template_name = 'Treasury/treasury_list.html'
    
    def get_queryset(self):
        qureyset = self.model.objects.filter(deleted=False).order_by('-id')
        return qureyset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['title'] = 'قائمة الخزائن'
        context['icons'] = '<i class="fas fa-shapes"></i>'
        context['page'] = 'active'
        context['count'] = self.model.objects.filter(deleted=False).count()
        return context


class TreasuryTrachList(LoginRequiredMixin, ListView):
    login_url = '/auth/login'
    model = Treasury
    paginate_by = 12
    template_name = 'Treasury/treasury_list.html'
    
    def get_queryset(self):
        queyset = self.model.objects.filter(deleted=True).order_by('-id')
        return queyset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'trach'
        context['count'] = self.model.objects.filter(deleted=True).count()
        return context


class TreasuryCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = Treasury
    form_class = TreasuryForm
    template_name = 'forms/treasury_form.html'
    success_url = reverse_lazy('Treasury:TreasuryList')

   
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافة خزينة جديد'
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:TreasuryCreate')
        return context
    
    def post(self, request):
        if request.method == 'POST':
            form =self.form_class(request.POST or None)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.treasury_user = request.user
                myform.save()
                return redirect(self.get_success_url()) 

    def get_success_url(self):
        messages.success(self.request, "تم اضافة خزينة جديدة", extra_tags="success")

        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
    

class TreasuryUpdate(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = Treasury
    form_class = TreasuryForm
    template_name = 'forms/treasury_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تعديل الخزنة: ' + str(self.object)
        context['message'] = 'update'
        context['action_url'] = reverse_lazy('Treasury:TreasuryUpdate', kwargs={'pk': self.object.id})
        return context
    
    def get_success_url(self):
        messages.success(self.request,  "تم تعديل الخزنة " + str(self.object) + " بنجاح ", extra_tags="success")
        if self.request.POST.get('url'):
            return self.request.POST.get('url')
        else:
            return self.success_url
                

class TreasuryDelete(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = Treasury
    form_class = TreasuryDeleteForm
    template_name = 'forms/treasury_form.html'
    

    def get_success_url(self):
        return reverse('Treasury:TreasuryList')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'نقل الخزنة الي سلة المهملات: ' + str(self.object)
        context['message'] = 'delete'
        context['action_url'] = reverse_lazy('Treasury:TreasuryDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, " تم نقل الخزنة " + str(self.object) + ' الي سلة المهملات بنجاح ' , extra_tags="success")
        myform = Treasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 1
        myform.save()
        return redirect(self.get_success_url())        


class TreasuryRestore(LoginRequiredMixin ,UpdateView):
    login_url = '/auth/login/'
    model = Treasury
    form_class = TreasuryDeleteForm
    template_name = 'forms/treasury_form.html'
    

    def get_success_url(self):
        return reverse('Treasury:TreasuryList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'استرجاع الخزنة: ' + str(self.object)
        context['message'] = 'restore'
        context['action_url'] = reverse_lazy('Treasury:TreasuryRestore', kwargs={'pk': self.object.id})
        return context

    def form_valid(self):
        messages.success(self.request, " تم ارجاع الخزنة " + str(self.object) + ' الي القائمة بنجاح ' , extra_tags="success")
        myform = Treasury.objects.get(id=self.kwargs['pk'])
        myform.deleted = 0
        myform.save()
        return redirect(self.get_success_url())
    

class TreasurySuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = Treasury
    form_class = TreasuryDeleteForm
    template_name = 'forms/form_template.html'

    def get_success_url(self):
        return reverse('Treasury:TreasuryTrachList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف الخزنة : ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Treasury:TreasurySuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, "تم حذف الخزنة " + str(self.object) + " نهائيا بنجاح ", extra_tags="success")
        my_form = Treasury.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())


class TreasuryDetails(LoginRequiredMixin, DetailView):
    login_url = '/auth/login/'
    model = Treasury
    template_name = 'Treasury/treasury_details.html'
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'list'
        context['treasury'] = self.object
        context['form'] = TreasuryOperationForm
        context['treasury_operation_obj'] = TreasuryOperation.objects.filter(treasury=self.object).order_by('-operation_date')
        return context



class OperationInCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = TreasuryOperation
    form_class = TreasuryOperationForm
    template_name = 'forms/treasury_operation_form.html'
   
    
    def get_success_url(self):
        messages.success(self.request, "تم اضافة الرصيد بنجاح", extra_tags="success")
        return reverse_lazy('Treasury:TreasuryDetails', kwargs={'pk': self.request.POST.get('treasury_pk')})
          
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'اضافة رصيد جديد'
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:OperationInCreate',  kwargs={'pk': self.kwargs['pk']})
        return context
    
    def form_valid(self, form):
        
        form.save()
        obj = form.save(commit=False)
        myform = TreasuryOperation.objects.get(id=obj.id)
        myform.operation_user = self.request.user
        myform.treasury_id =  self.request.POST.get('treasury_pk')
        myform.operation_type = 1
        myform.save()

        operation_object = TreasuryOperation.objects.get(id=obj.id)
        new_operation_value = operation_object.operation_value

        myform2= Treasury.objects.get(id=self.request.POST.get('treasury_pk'))
        old_balance = myform2.treasury_balance
        new_balance = float(new_operation_value) + float(old_balance)
        myform2.treasury_balance = new_balance
        myform2.save()
        
        return redirect(self.get_success_url())


class OperationOutCreate(LoginRequiredMixin, CreateView):
    login_url = '/auth/login/'
    model = TreasuryOperation
    form_class = TreasuryOperationForm
    template_name = 'forms/treasury_operation_form.html'
   
    
    def get_success_url(self):
        messages.success(self.request, "تم سحب من الرصيد بنجاح", extra_tags="success")
        return reverse_lazy('Treasury:TreasuryDetails', kwargs={'pk': self.request.POST.get('treasury_pk')})
          
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'عملية سحب رصيد جديدة'
        context['message'] = 'add'
        context['action_url'] = reverse_lazy('Treasury:OperationOutCreate',  kwargs={'pk': self.kwargs['pk']})
        return context
    
    def form_valid(self, form):
        form.save()
        obj = form.save(commit=False)
        myform = TreasuryOperation.objects.get(id=obj.id)
        myform.operation_user = self.request.user
        myform.treasury_id =  self.request.POST.get('treasury_pk')
        myform.operation_type = 2
        myform.save()

        operation_object = TreasuryOperation.objects.get(id=obj.id)
        new_operation_value = operation_object.operation_value

        myform2= Treasury.objects.get(id=self.request.POST.get('treasury_pk'))
        old_balance = myform2.treasury_balance
        new_balance =  float(old_balance) - float(new_operation_value)
        myform2.treasury_balance = new_balance
        myform2.save()
        
        return redirect(self.get_success_url())
    

class OperationSuperDelete(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/'
    model = TreasuryOperation
    form_class = TreasuryOperationDeleteForm
    template_name = 'forms/treasury_operation_form.html'


    def get_success_url(self):
        return reverse_lazy('Treasury:TreasuryDetails', kwargs={'pk': self.object.treasury.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف العملية : ' + str(self.object)
        context['message'] = 'super_delete'
        context['action_url'] = reverse_lazy('Treasury:OperationSuperDelete', kwargs={'pk': self.object.id})
        return context

    def form_valid(self, form):
        messages.success(self.request, "تم حذف العملية بنجاح", extra_tags="success")
        my_form = TreasuryOperation.objects.get(id=self.kwargs['pk'])
        my_form.delete()
        return redirect(self.get_success_url())
