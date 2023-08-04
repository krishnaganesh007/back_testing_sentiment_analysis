## Youtube video scraping
from youtube_transcript_api import YouTubeTranscriptApi

# some provided subclasses, each outputs a different string format.
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
from youtube_transcript_api.formatters import SRTFormatter

# Provide the video ID to get the transcripts
transcript = YouTubeTranscriptApi.get_transcript("S7r_ipKQjkA&t")
formatter = JSONFormatter()
formatter.format_transcript(transcript)

transcript[0].fetch()

transcription = YouTubeTranscriptApi.list_transcripts("S7r_ipKQjkA&t")
check.video_id

transcription._translation_languages
transcription._generated_transcripts

NqrrjdLz

transcript = YouTubeTranscriptApi.get_transcript("47vUqkkVYbI")


check

