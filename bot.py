from pyrogram import Client, filters, enums
from pyromod import listen
import random, asyncio

API_ID = 8186557
API_HASH = "efd77b34c69c164ce158037ff5a0d117"
app = Client("ElNqYbx", api_id=API_ID, api_hash=API_HASH, session_string="AQCYjk9Z9l4AJlP41Q8vKbUtDVfPzacwEJCLMEg2-qNEJWnTrxAbUmHH0fJx6btBCFfs7YIo6viUUUDMfcvH8GsZ5gcYJeMvZe0s_SsJI65EXMaquF8O9Y2OMrOZd9Doc8sUunuqxNAlldCdhN5VYxuuU5vmwa8fOhLrAVvCrgfFdke7JhTpwUFq7-W0ChiGcYpstu4G5NzAqxPfjnVU1-jTLJQl1RnJr9_bEvfdJzhBNNCTh_XXSIfQCqGeTsSEy737pL29yLeiU6QilnXVV1SYVY0OpodVygGyu5fGUT9CsVZZ_mPhPgTJOeifXB-JNVVmAMdyUhIsDAiRVvSQVXAAAAAW_0MWEA")
msg = {}
lists = {}
list = {}
users = []
xx = {}
async def send(chat_id, tim):
  while not await asyncio.sleep(tim):
   if not xx[chat_id]:
     break
   if len(list[chat_id]) == 0:
     for x in lists[chat_id]:
         list[chat_id].append(x)
   print(len(list[chat_id]))
   print(list[chat_id])
   m = random.choice(list[chat_id])
   list[chat_id].remove(m)
   async for dialog in app.get_dialogs():
     if not dialog.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
       continue
     try:
          await app.forward_messages(dialog.chat.id, 1167237579, m)
     except Exception as a:
        print(a)

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

@app.on_message(filters.command("ذيع خاص", ""))
async def brodcats(client, message):
   if not message.from_user.id == 1167237579: return
   if not message.reply_to_message: return await message.reply_text("قم بالرد علي الرسالة التي تريد اذاعتها")
   text = message.reply_to_message.text
   d = 0
   f = 0
   async for dialog in client.get_dialogs():
       if enums.ChatType.PRIVATE == dialog.chat.type:
         try:
           await client.send_message(dialog.chat.id, text)
           d += 1
         except Exception as a:
           print(a)
           f += 1
   await message.reply_text(f"تم الاذاعه الي {d} \nوفشل في {f}")

@app.on_message(filters.command("الغاء التكرار", ""))
async def stoploop(client, message):
   if not message.from_user.id == 1167237579: return
   chat_id = message.from_user.id
   if not xx.get(chat_id): return await message.reply_text("لم يتم تفعيل التكرار")
   xx[chat_id] = None
   await message.reply_text("تم الغاء تفعيل التكرار .")
@app.on_message(filters.command("تعين التكرار", ""))
async def setloops(client, message):
   if not message.from_user.id == 1167237579: return
   tim = await client.ask(message.chat.id, "عايز الرساله تتكرر كل كام ثانيه", filters.user(message.from_user.id))
   tim = int(tim.text)
   chat_id = message.from_user.id
   list[chat_id] = []
   lists[chat_id] = []
   ask = await client.ask(message.chat.id, "كم رساله تريد تعينها", filters.user(message.from_user.id))
   lop = int(ask.text) - 1
   ask1 = await client.ask(message.chat.id, "أرسل الرساله الاولي ", filters.user(message.from_user.id))
   list[chat_id].append(ask1.id)
   lists[chat_id].append(ask1.id)
   for x in range(lop):
       askk = await client.ask(message.chat.id, "ارسل الرساله التاليه", filters.user(message.from_user.id))
       list[chat_id].append(askk.id)
       lists[chat_id].append(askk.id)
       await askk.reply_text("تم حفظ الرساله بنجاح ")
   xx[chat_id] = True
   await message.reply_text("**تم تعين التكرار**")
   await asyncio.create_task(send(chat_id, tim))

print("Running 😃")
app.run()