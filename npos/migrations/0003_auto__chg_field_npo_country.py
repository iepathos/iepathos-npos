# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Npo.country'
        db.alter_column('npos_npo', 'country', self.gf('django.db.models.fields.CharField')(max_length=13))

    def backwards(self, orm):

        # Changing field 'Npo.country'
        db.alter_column('npos_npo', 'country', self.gf('django.db.models.fields.CharField')(max_length=12))

    models = {
        'npos.npo': {
            'Meta': {'object_name': 'Npo'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'ein': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['npos']