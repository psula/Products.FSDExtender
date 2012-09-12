from Products.Archetypes.atapi import *
from Products.FacultyStaffDirectory.interfaces.person import IPerson
from Products.FSDExtender.interfaces import IFSDExtenderLayer
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from zope.component import adapts
from zope.interface import implements

# you must subclass all field types you are going to use as ExtensionFields

class _LinesExtensionField(ExtensionField, LinesField): pass
class _FileExtensionField(ExtensionField, FileField): pass
class _StringExtensionField(ExtensionField, StringField): pass

class FSDExtender(object):
    adapts(IPerson)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    # bind this extender to the browser layer we created
    layer = IFSDExtenderLayer

    # specify the additional fields you want to add
    fields = [
        _LinesExtensionField(
            "Officehours",
            schemata = "Contact Information",
            widget = LinesWidget(
                label=u"Office Hours",
                description=u"Enter Your Office Hours",
            ),
        ),
        
        _FileExtensionField(
            "MyCV",
            schemata = "Professional Information",
            widget = FileWidget(
                label=u"Curriculum Vitae",
                description=u"Upload your Curriculum Vitae.  Vitae must in Microsoft Word or Adobe PDF format.",
            ),
        ),
		_StringExtensionField('CVurl',
                required=False,
                searchable=False,
                validators= ('isURL'),
                schemata="Professional Information",
                widget=StringWidget(
                    label=u"CV URL",
                    visible = {'view':'visible','edit':'visible'},
					description=u"If your CV resides on a personal or other external website, enter the URL here.",
                )
        ),
         _StringExtensionField('facebookURL',
                required=False,
                searchable=False,
                validators= ('isURL'),
                schemata="Contact Information",
                widget=StringWidget(
                    label=u"Facebook URL",
                    visible = {'view':'visible','edit':'visible'},
                )
        ),
        _StringExtensionField('linkedInURL',
                required=False,
                searchable=False,
                validators= ('isURL'),
                schemata="Contact Information",
                widget=StringWidget(
                    label=u"LinkedIn URL",
                    visible = {'view':'visible','edit':'visible'},
                )
        ),
        _StringExtensionField('twitterURL',
                required=False,
                searchable=False,
                validators= ('isURL'),
                schemata="Contact Information",
                widget=StringWidget(
                    label=u"Twitter URL",
                    visible = {'view':'visible','edit':'visible'},
                )
        ),
		_LinesExtensionField(
            "Dissertation",
			required=False,
			searchable=False,
            schemata = "Professional Information",
            widget = LinesWidget(
                label=u"Dissertation",
                
            ),
        ),
		_StringExtensionField('chairPersons',
	                required=False,
	                searchable=False,
	                schemata="Professional Information",
	                widget=StringWidget(
	                    label=u"Dissertation Chair",
	                    visible = {'view':'visible','edit':'visible'},
	                )
	        ),
		_StringExtensionField('researchInterests',
		                required=False,
		                searchable=False,
		                schemata="Professional Information",
		                widget=StringWidget(
		                    label=u"Research Interests",
		                    visible = {'view':'visible','edit':'visible'},
		                )
		        ),

    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
        
    def fiddle(object, schema):
             
        for hideme in ['User Settings', 'categorization', 'dates', 'ownership', 'settings']:
            for fieldName in schema.getSchemataFields(hideme):
                fieldName.widget.visible={'edit':'invisible','view':'invisible'}
			    
        return schema

        
   