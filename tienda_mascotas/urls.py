from django.conf.urls import url
from tienda_mascotas.views import index,animal_add, cliente_add, adopcion_add, \
Animal_list, Cliente_list, Adopcion_list, animal_edit, animal_delete, cliente_edit, cliente_delete

urlpatterns = [
   url(r'^$', index, name='index'),
   url(r'^add_ani$', animal_add, name='add_a'),
   url(r'^add_cli$', cliente_add, name='add_c'),
   url(r'^add_adop$', adopcion_add, name='add_adop'),
   url(r'^edit_ani/(?P<id_animal>\d+)/$', animal_edit, name='edt_a'),
   url(r'^delete_ani/(?P<id_animal>\d+)/$', animal_delete, name='del_a'),
   url(r'^edit_cli/(?P<id_cliente>\d+)/$', cliente_edit, name='edt_c'),
   url(r'^delete_cli/(?P<id_cliente>\d+)/$', cliente_delete, name='del_c'),
   url(r'^list_ani$', Animal_list.as_view(), name='list_a'),
   url(r'^list_cli$', Cliente_list.as_view(), name='list_c'),
   url(r'^list_adop$', Adopcion_list.as_view(), name='list_adop'),
]
