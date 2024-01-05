from django.contrib import admin

from core.models import Summary, SummaryChunk


class SummaryChunkInline(admin.TabularInline):
    model = SummaryChunk
    readonly_fields = ('chunk_text', 'summary_text',)
    extra = 0


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'summary_text')
    inlines = [SummaryChunkInline,]


admin.site.register(Summary, SummaryAdmin)
