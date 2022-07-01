import hashlib
from aiogram import types, Dispatcher
import googlesearch
def finder(text):
    result = googlesearch(text, max_result=10).to_dict()
    return result

async def inline_google_hundler(querry: types.InlineQuery):
    text =querry.query or "echo"
    links = finder(text)
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
        title=f"{link['title']}",
        url=f"https://www.youtube.com/watch?v={link['id']}",
        thumb_url=f"{link['thumbnails']}",
        input_message_content=types.InputMessageContent(
            message_text=f"https://www.youtube.com/watch?v={link['id']}"))
        for link in links]
    await querry.answer(articles,cache_time=60, is_personal=True)