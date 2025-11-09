# # utils/voice_narrator.py
# from elevenlabs import generate, play, save, set_api_key
# from config import ELEVENLABS_API_KEY
# import tempfile

# set_api_key(ELEVENLABS_API_KEY)

# def narrate_text(text, voice="Rachel"):
#     audio = generate(
#         text=text,
#         voice=voice,
#         model="eleven_monolingual_v1"
#     )
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
#         save(audio, f.name)
#         return f.name



# utils/voice_narrator.py
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from config import ELEVENLABS_API_KEY
import tempfile

# Initialize ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def narrate_text(text, voice_id="21m00Tcm4TlvDq8ikWAM"):  # Default "Rachel" voice ID
    # Streamed audio generator (needs to be concatenated)
    audio_stream = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=text,
        output_format="mp3_44100_128"
    )

    # Collect all streamed audio chunks into one bytes object
    audio_bytes = b"".join(audio_stream)

    # Save to a temporary MP3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        f.write(audio_bytes)
        return f.name
