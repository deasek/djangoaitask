from django.db import models
from openai import OpenAI

from ai.settings import DEFAULT_COMPLETION_MAX_TOKENS
from core.helpers import make_chunks
from .base import BaseModel


class ApiException(Exception):
    ...


class Summary(BaseModel):
    input_text = models.TextField()  # extracted text
    summary_text = models.TextField(null=True, blank=True)  # generated summary text

    @classmethod
    def _summarize_input_text(cls, input_text, completion_max_tokens=DEFAULT_COMPLETION_MAX_TOKENS):
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize in one sentence"
                },
                {
                    "role": "user",
                    "content": input_text
                }
            ],
            temperature=0.7,
            max_tokens=completion_max_tokens,
            top_p=1
        )
        return response.choices[0].message.content

    @classmethod
    def parse_input_file(cls, input_file):
        raw_text = input_file.read().decode('utf-8')
        summary = Summary.objects.create(input_text=raw_text)
        paragraphs = raw_text.split('\n\n')  # Just for plain text
        chunks = make_chunks(paragraphs, 2) # number of paragraphs we want to include in chunk
        summary_chunks_objects = []
        for chunk in chunks:
            chunk_text = '\n\n'.join(chunk)
            summarized_text = Summary._summarize_input_text(chunk_text)
            chunk = SummaryChunk.objects.create(summary=summary, chunk_text=chunk_text, summary_text=summarized_text)
            summary_chunks_objects.append(chunk)

        # Let's summarize all outputs
        all_summaries = '\n\n'.join([chunk.summary_text for chunk in summary_chunks_objects])
        general_summary = Summary._summarize_input_text(all_summaries)
        summary.summary_text = general_summary
        summary.save()
        return summary

    class Meta:
        verbose_name = "Summary"
        verbose_name_plural = "Summaries"


class SummaryChunk(BaseModel):
    summary = models.ForeignKey(Summary, related_name='chunks', on_delete=models.CASCADE)
    chunk_text = models.TextField()
    summary_text = models.TextField(null=True, blank=True)  # generated summary text
