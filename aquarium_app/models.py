from django.db import models


# class Actuator(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Actuator'


# class Cabinet(models.Model):
#     componentid = models.ForeignKey('self', models.DO_NOTHING, db_column='componentID', primary_key=True)  # Field name made lowercase.
#     projectid = models.CharField(db_column='projectID', max_length=5)  # Field name made lowercase.
#     itemno = models.IntegerField(db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     location = models.CharField(max_length=25, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Cabinet'


# class CategorySub(models.Model):
#     category = models.CharField(primary_key=True, max_length=20)
#     subcategory = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'Category_Sub'
#         unique_together = (('category', 'subcategory'),)


class Company(models.Model):
    companyid = models.CharField(db_column='companyID', primary_key=True, max_length=10)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preferredemail = models.CharField(db_column='preferredEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Company'


# class Contacts(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Contacts'


# class Customer(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Customer'


# class Dat(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'DAT_'
class Projects(models.Model):
    projectid = models.CharField(db_column='projectid', primary_key=True, max_length=5)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    estimatedcompdate = models.DateField(db_column='estimatedCompDate', blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=50)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(max_length=50, blank=True, null=True)
    customerid = models.CharField(db_column='customerID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Projects'


class Exhibits(models.Model):
    exhibitID = models.CharField(db_column='exhibitID', primary_key=True, max_length=25)
    exhibitName = models.CharField(db_column='exhibitName', max_length=50)
    description = models.TextField(blank=True, null=True)
    estimatedGal = models.IntegerField(blank=True, null=True)
    desiredTurnover = models.IntegerField(blank=True, null=True)
    systemFlow = models.IntegerField(blank=True, null=True)
    creationDate = models.DateTimeField(db_column='creationDate', blank=True, null=True)
    updateDate = models.DateTimeField(db_column='updateDate', blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
  
	
	

    class Meta:
        managed = False
        db_table = 'Exhibits'

class ProjectExhibits(models.Model):
    exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='projectID', primary_key=True)  # Field name made lowercase.
    newconstruction = models.BooleanField(db_column='newConstruction', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project_Exhibits'
        unique_together = (('projectid', 'exhibitid'),)




# class Otheranalog(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     size = models.CharField(max_length=50, blank=True, null=True)
#     type = models.CharField(max_length=25, blank=True, null=True)
#     location = models.CharField(max_length=25, blank=True, null=True)
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'otherAnalog'



# class Filter(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     diameter = models.CharField(max_length=50, blank=True, null=True)
#     height = models.CharField(max_length=50, blank=True, null=True)
#     material = models.CharField(max_length=25, blank=True, null=True)
#     designflow = models.CharField(db_column='designFlow', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     backwashflow = models.CharField(db_column='backwashFlow', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     orientation = models.CharField(max_length=25, blank=True, null=True)
#     media = models.CharField(max_length=50, blank=True, null=True)
#     location = models.CharField(max_length=25, blank=True, null=True)
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     itemno = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     flow = models.ForeignKey('Flow', models.DO_NOTHING, db_column='flow', blank=True, null=True)
#     flowcontrol = models.BooleanField(db_column='flowControl', blank=True, null=True)  # Field name made lowercase.
#     flowcontrolbyvfd = models.BooleanField(db_column='flowControlByVFD', blank=True, null=True)  # Field name made lowercase.
#     inletactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='inletActuator', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
#     supplypump = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='supplyPump', blank=True, null=True)  # Field name made lowercase.
#     automatedbw = models.BooleanField(db_column='automatedBW', blank=True, null=True)  # Field name made lowercase.
#     dischargeactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='dischargeActuator', blank=True, null=True)  # Field name made lowercase.
#     backwashactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='backwashActuator', blank=True, null=True)  # Field name made lowercase.
#     throttleactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='throttleActuator', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Filter'


# class Flow(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Flow'


# class ItemSubcat(models.Model):
#     itemno = models.ForeignKey('Items', models.DO_NOTHING, db_column='itemNo', primary_key=True)  # Field name made lowercase.
#     category = models.ForeignKey(CategorySub, models.DO_NOTHING, db_column='category')
#     subcategory = models.ForeignKey(CategorySub, models.DO_NOTHING, db_column='subcategory')

#     class Meta:
#         managed = False
#         db_table = 'Item_Subcat'
#         unique_together = (('itemno', 'category', 'subcategory'),)


# class Items(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Items'


# class Level(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Level'


# class Orp(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=50, blank=True, null=True)
#     pipesize = models.DecimalField(db_column='pipeSize', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     instfittingbool = models.BooleanField(db_column='instFittingBOOL', blank=True, null=True)  # Field name made lowercase.
#     instfit_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='instFit_itemNo', blank=True, null=True)  # Field name made lowercase.
#     wettapbool = models.BooleanField(db_column='wetTapBOOL', blank=True, null=True)  # Field name made lowercase.
#     wettap_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='wetTap_itemNo', blank=True, null=True)  # Field name made lowercase.
#     transmitterbool = models.BooleanField(db_column='transmitterBOOL', blank=True, null=True)  # Field name made lowercase.
#     transmitter_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='transmitter_itemNo', blank=True, null=True)  # Field name made lowercase.
#     probebool = models.BooleanField(db_column='probeBOOL', blank=True, null=True)  # Field name made lowercase.
#     probe_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='probe_itemNo', blank=True, null=True)  # Field name made lowercase.
#     localdisplaybool = models.BooleanField(db_column='localDisplayBOOL', blank=True, null=True)  # Field name made lowercase.
#     localdisplay_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='localDisplay_itemNo', blank=True, null=True)  # Field name made lowercase.
#     analoginputpoint = models.CharField(db_column='analogInputPoint', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(max_length=25, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'ORP'


# class Psk(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=50, blank=True, null=True)
#     size = models.CharField(max_length=25, blank=True, null=True)
#     designflow = models.CharField(db_column='designFlow', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(max_length=25, blank=True, null=True)
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     supplypump = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='supplyPump', blank=True, null=True)  # Field name made lowercase.
#     injectpump1 = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='injectPump1', blank=True, null=True)  # Field name made lowercase.
#     injectpump2 = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='injectPump2', blank=True, null=True)  # Field name made lowercase.
#     injectpump3 = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='injectPump3', blank=True, null=True)  # Field name made lowercase.
#     injectpump4 = models.ForeignKey('Pumps', models.DO_NOTHING, db_column='injectPump4', blank=True, null=True)  # Field name made lowercase.
#     flow = models.ForeignKey(Flow, models.DO_NOTHING, db_column='flow', blank=True, null=True)
#     ozonecontrol = models.BooleanField(db_column='ozoneControl', blank=True, null=True)  # Field name made lowercase.
#     orpinput = models.ForeignKey(Orp, models.DO_NOTHING, db_column='ORPInput', blank=True, null=True)  # Field name made lowercase.
#     ozoneactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='ozoneActuator', blank=True, null=True)  # Field name made lowercase.
#     levelcontrol = models.BooleanField(db_column='levelControl', blank=True, null=True)  # Field name made lowercase.
#     levelbyvfd = models.BooleanField(db_column='levelbyVFD', blank=True, null=True)  # Field name made lowercase.
#     levelinput = models.ForeignKey(Level, models.DO_NOTHING, db_column='levelInput', blank=True, null=True)  # Field name made lowercase.
#     inletactuator = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='inletActuator', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
#     flowcontrol = models.BooleanField(db_column='FlowControl', blank=True, null=True)  # Field name made lowercase.
#     ozoneinjection = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'PSK'





# class Pumps(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'Pumps'


# class Temperature(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     pipesize = models.DecimalField(db_column='pipeSize', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     wellbool = models.BooleanField(db_column='wellBOOL', blank=True, null=True)  # Field name made lowercase.
#     instfittingbool = models.BooleanField(db_column='instFittingBOOL', blank=True, null=True)  # Field name made lowercase.
#     instfit_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='instFit_itemNo', blank=True, null=True)  # Field name made lowercase.
#     sensor_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='sensor_itemNo', blank=True, null=True)  # Field name made lowercase.
#     localdisplaybool = models.BooleanField(db_column='localDisplayBOOL', blank=True, null=True)  # Field name made lowercase.
#     localdisplay_itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='localDisplay_itemNo', blank=True, null=True)  # Field name made lowercase.
#     analoginputpoint = models.CharField(db_column='analogInputPoint', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(max_length=25, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Temperature'


# class Vfd(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=50, blank=True, null=True)
#     pump = models.ForeignKey(Pumps, models.DO_NOTHING, db_column='Pump', blank=True, null=True)  # Field name made lowercase.
#     voltage = models.CharField(max_length=25, blank=True, null=True)
#     location = models.CharField(max_length=25, blank=True, null=True)
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     runcommand = models.CharField(db_column='runCommand', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     runningstatus = models.CharField(db_column='runningStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     speedoutpoint = models.CharField(db_column='SpeedOutPoint', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'VFD'


# class Vendor(models.Model):
#     vendorid = models.CharField(db_column='vendorID', primary_key=True, max_length=50)  # Field name made lowercase.
#     vendorname = models.CharField(db_column='vendorName', max_length=50)  # Field name made lowercase.
#     address = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     state = models.CharField(max_length=2, blank=True, null=True)
#     zipcode = models.CharField(db_column='zipCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(max_length=10, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Vendor'


# class Vendoritem(models.Model):
#     vendorid = models.ForeignKey(Vendor, models.DO_NOTHING, db_column='vendorID', primary_key=True)  # Field name made lowercase.
#     itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemNo')  # Field name made lowercase.
#     vendoritemid = models.CharField(db_column='vendorItemID', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
#     leadtime = models.CharField(db_column='leadTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comments = models.CharField(max_length=255, blank=True, null=True)
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'VendorItem'
#         unique_together = (('vendorid', 'itemno'),)


# class Watermotion(models.Model):
#     processid = models.CharField(db_column='processID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     pump1 = models.ForeignKey(Pumps, models.DO_NOTHING, db_column='pump1', blank=True, null=True)
#     pump2 = models.ForeignKey(Pumps, models.DO_NOTHING, db_column='pump2', blank=True, null=True)
#     pump3 = models.ForeignKey(Pumps, models.DO_NOTHING, db_column='pump3', blank=True, null=True)
#     pump4 = models.ForeignKey(Pumps, models.DO_NOTHING, db_column='pump4', blank=True, null=True)
#     actuator1 = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='actuator1', blank=True, null=True)
#     actuator2 = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='actuator2', blank=True, null=True)
#     actuator3 = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='actuator3', blank=True, null=True)
#     actuator4 = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='actuator4', blank=True, null=True)
#     flow1 = models.ForeignKey(Flow, models.DO_NOTHING, db_column='flow1', blank=True, null=True)
#     flow2 = models.ForeignKey(Flow, models.DO_NOTHING, db_column='flow2', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'WaterMotion'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Heatexchanger(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'heatExchanger'



# class Otherdigital(models.Model):
#     componentid = models.CharField(db_column='componentID', primary_key=True, max_length=25)  # Field name made lowercase.
#     exhibitid = models.ForeignKey(Exhibits, models.DO_NOTHING, db_column='exhibitID')  # Field name made lowercase.
#     description = models.CharField(max_length=75, blank=True, null=True)
#     size = models.CharField(max_length=50, blank=True, null=True)
#     type = models.CharField(max_length=25, blank=True, null=True)
#     location = models.CharField(max_length=25, blank=True, null=True)
#     newitem = models.BooleanField(db_column='newItem')  # Field name made lowercase.
#     olddescription = models.CharField(db_column='oldDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     itemno = models.ForeignKey(Items, models.DO_NOTHING, db_column='itemNo', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'otherDigital'


# class Ozonecontactor(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'ozoneContactor'


# class Ozonegenerator(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'ozoneGenerator'


# class Ph(models.Model):

#     class Meta:
#         managed = False
#         db_table = 'pH'


# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=128)
#     principal_id = models.IntegerField()
#     diagram_id = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)