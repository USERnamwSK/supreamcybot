from os import system
system("pip install windows-curses")
system("pip install websocket-client==0.57.0")
system("pip install fancy_text")
system("pip install secmail")
system("pip install bs4")
system("pip install google_images_search")
system("pip install pillow")
system("pip install BotAmino")
system("pip install flask")
from keep_alive import keep_alive

keep_alive()
import BotAmino
import sys
from random import uniform, choice, randint
import copy
from zipfile import ZipFile
import zipfile
import os
import aminofix
from google_images_search import GoogleImagesSearch
import youtube_dl, os, urllib.request, subprocess, webbrowser
import curses
import numpy as np
import pyjokes
import unicodedata
from time import sleep
from gtts import gTTS, lang
from fancy_text import fancy
from google_trans_new import google_translator
from constant import LANGUAGES, DEFAULT_SERVICE_URLS
from json import dumps, load
from threading import Thread
import threading
from random import choice, randint
import time
import urllib
from datetime import datetime
from youtube_dl import YoutubeDL
from BotAmino import *
import random
from PIL import Image, ImageFont, ImageDraw
import string
import pytz
import shutil
import requests
from pymongo import MongoClient
import urllib.parse
from multiprocessing.pool import ThreadPool





#useriku = "b3c859d0-983d-4a10-a6d1-eb11eebbf2e3"

mongo = MongoClient("mongodb://alexa:aman@cluster0-shard-00-00.3nela.mongodb.net:27017,cluster0-shard-00-01.3nela.mongodb.net:27017,cluster0-shard-00-02.3nela.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ngo3g6-shard-0&authSource=admin&retryWrites=true&w=majority")

# 79964099 anime mangas scan
# 93307693 univers perdu
# 79964099 on es la public
# 59002602 majeur
#Animes & RP: 144781697


#client = BotAmino(sid="AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICIzOTg5NTg1Zi00ODE1LTRmYjItYTMxZC01NDBlMzQ4OTk4YmYiLCAiNSI6IDE2NzU0Mjk0OTcsICI0IjogIjM3LjE2Ny4xODEuMTcyIiwgIjYiOiAxMDB91pwBjegoFuJ2MoZcDEwN1TL6VRw")
client = BotAmino("nilal34244@labebx.com","Soridu94")



comid = 93307693

path_utilities = 'utilities'
path_amino = f'{path_utilities}/amino_list'
path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"
path_download = "news"
client.bio = f"Createur du bot : soso"
client.prefix = "!"
client.activity = True




def generateUUID():
    return str(uuid4())


def print_exception(exc):
    print(repr(exc))

def get_wallet_amount(data):
    return client.get_wallet_info().totalCoins

def admins(data):
    return data.authorId in admn


adm = ["a92d7072-c06d-45d3-bf5f-b8bf3846e552"]

admn = ["a92d7072-c06d-45d3-bf5f-b8bf3846e552"]


def nope(data):
    return False


def is_black(data):
    if data.authorId in data.subClient.favorite_users:
        data.subClient.send_message(data.chatId, message="Tu es interdit d'utilisé le bot ", replyTo=data.messageId)


def is_it_me(data):
    return data.authorId in ('a92d7072-c06d-45d3-bf5f-b8bf3846e552')


def is_staff(data):
    return data.authorId in ("a92d7072-c06d-45d3-bf5f-b8bf3846e552") or data.subClient.is_in_staff(data.authorId)


def extra(uid: str):
    event = uuid4()
    data = {
        "reward": {"ad_unit_id": "255884441431980_807351306285288", "credentials_type": "publisher",
                   "custom_json": {"hashed_user_id": f"{uid}"}, "demand_type": "sdk_bidding", "event_id": f"{event}",
                   "network": "facebook", "placement_tag": "default", "reward_name": "Amino Coin",
                   "reward_valid": "true", "reward_value": 2, "shared_id": "dc042f0c-0c80-4dfd-9fde-87a5979d0d2f",
                   "version_id": "1569147951493", "waterfall_id": "dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app": {"bundle_id": "com.narvii.amino.master", "current_orientation": "portrait",
                "release_version": "3.4.33567",
                "user_agent": "Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},
        "date_created": 1620295485, "session_id": "49374c2c-1aa3-4094-b603-1cf2720dca67",
        "device_user": {"country": "US", "device": {"architecture": "aarch64",
                                                    "carrier": {"country_code": 602, "name": "Vodafone",
                                                                "network_code": 0}, "is_phone": "true",
                                                    "model": "GT-S5360", "model_type": "Samsung",
                                                    "operating_system": "android", "operating_system_version": "29",
                                                    "screen_size": {"height": 2260, "resolution": 2.55, "width": 1080}},
                        "do_not_track": "false", "idfa": "7495ec00-0490-4d53-8b9a-b5cc31ba885b", "ip_address": "",
                        "locale": "en", "timezone": {"location": "Asia\/Seoul", "offset": "GMT+09:00"},
                        "volume_enabled": "true"}
    }

    headers = {
        "cookies": "__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization": "Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }
    requests.post("https://ads.tapdaq.com/v4/analytics/reward", json=data, headers=headers)


def telecharger(url):
    music = None
    if ("=" in url and "/" in url and " " not in url) or ("/" in url and " " not in url):
        if "=" in url and "/" in url:
            music = url.rsplit("=", 1)[-1]
        elif "/" in url:
            music = url.rsplit("/")[-1]

        if music in os.listdir(path_download):
            return music

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'extract-audio': True,
            'outtmpl': f"{path_download}/{music}.webm",
        }

        with YoutubeDL(ydl_opts) as ydl:
            video_length = ydl.extract_info(url, download=True).get('duration')
            ydl.cache.remove()

        url = music + ".mp3"

        return url, video_length
    return False, False


def decoupe(musical, temps):
    size = 170
    with open(musical, "rb") as fichier:
        nombre_ligne = len(fichier.readlines())

    if temps < 180 or temps > 540:
        return False

    decoupage = int(size * nombre_ligne / temps)

    t = 0
    file_list = []
    for a in range(0, nombre_ligne, decoupage):
        b = a + decoupage
        if b >= nombre_ligne:
            b = nombre_ligne

        with open(musical, "rb") as fichier:
            lignes = fichier.readlines()[a:b]

        with open(musical.replace(".mp3", "PART" + str(t) + ".mp3"), "wb") as mus:
            for ligne in lignes:
                mus.write(ligne)

        file_list.append(musical.replace(".mp3", "PART" + str(t) + ".mp3"))
        t += 1
    return file_list


lis = ['Tape dans le fond je suis pas ta mère', 'suce ton pere', '- Non.', 'Je ne sais pas, réfléchis par toi-même',
           '- Oui.',
           'Difficile de répondre, en effet.', 'Répétez la question.', 'Êtes-vous sûr de vouloir le savoir ? ',
           'Lilalilalou', 'Poupipoupipou', 'Zoubizoubizou', 'Ma viiie', 'tabarnak',
           ' Je ne sais pas. ', 'Je refléchis', ' tg ', "ptdrrr t ki ?", 'T’es archi moche plus que ma merde', 'Tu pu',
           'T’es aussi belle qu’une fleur', 'Tu sens tellement bon que je veut te croquer', 'ratio',
           'Je ne suis pas du même avis.', 'nikoumouk', ','',T’es pire que sourcils au barreaux de shit ftg', 'bouge',
           'Nique ton père', 'Va manger ta merde', 'Va te faire enculer ça te donneras des couleurs',
           'J’te saute comme les tours jumelles', 'oui mon soumis', 'oui maitre', 'tais toi femme']

gayles = ['🏳‍🌈 Vous êtes gay/lesbienne à: 0%', '🏳‍🌈 Vous êtes gay/lesbienne à: 0.5%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 1%', '🏳‍🌈 Vous êtes gay/lesbienne à: 2.56%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 3%', '🏳‍🌈 Vous êtes gay/lesbienne à: 5%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 13.45%', '🏳‍🌈 Vous êtes gay/lesbienne à: 23.75%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 35.93%', '🏳‍🌈 Vous êtes gay/lesbienne à: 41.99%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 49%', '🏳‍🌈 Vous êtes gay/lesbienne à: 69.34%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 79.33%', '🏳‍🌈 Vous êtes gay/lesbienne à: 95.55%',
              '🏳‍🌈 Vous êtes gay/lesbienne à: 100%', 'Vous êtes hétéro.', 'Vous êtes hétéro.', 'Vous êtes hétéro.']

roulette = ['1ac.png', '1000ac.png', '500ac.png', 'ban.png']

@client.command("chat")
def chat(data):
    bid="162843&key=uyk4IpiAS3SSjWXF"
    apikey="uyk4IpiAS3SSjWXF"
    id="162843"
    if data.message:
        message=data.message
        r = requests.get(url=f"http://api.brainshop.ai/get?bid={bid}&key={apikey}&uid={id}&msg={message}")
        ans=r.json()['cnt']
        data.subClient.send_message(data.chatId,message=ans,replyTo=data.messageId)
    else:
        data.subClient.send_message(data.chatId,message="Say something!!",replyTo=data.messageId)

@client.command("visitor")
def visitorList(data):
    phone = data.subClient.get_user_visitors(data.authorId).visitors
    data.subClient.send_message(message=f"aa : {phone}",chatId=data.chatId)




@client.command("ult")
def spam(data):
    chats = data.subClient.get_chat_threads(size=100)
    chat_id = data.chatId
    message = "test"
    message_type = 0
    threads_count = 100

    def spam_process():
        thread_pool = ThreadPool(threads_count)
        while True:
            try:
                thread_pool.apply_async(data.subClient.send_message, [chat_id, message, message_type])
            except:
                return

    pool = ThreadPool(threads_count)
    pool.apply(spam_process)


@client.on_member_join_chat()
def Bienvenue(data):
    lists = []
    z = open("cids.txt", "a")
    t = open('cids.txt', 'r')
    # lists=[]
    for m in t.read().splitlines():
        temp = m
        if temp not in lists:
            lists.append(int(temp))
    if data.comId not in lists:
        tlt = data.subClient.get_chat_thread(data.chatId).title
        img3 = open(".tvs.png", "rb")
        vip = data.subClient.get_user_info(data.authorId).influencerInfo
        plus = data.subClient.get_user_info(data.authorId).accountMembershipStatus
        following = data.subClient.get_user_info(data.authorId).followingCount
        followers = data.subClient.get_user_info(data.authorId).followersCount
        lvll = data.subClient.get_user_info(data.authorId).level
        frm = data.subClient.get_user_info(data.authorId).avatarFrame
        aiv = data.subClient.get_user_info(data.authorId).avatarFrameId
        rolee = data.subClient.get_user_info(data.authorId).role
        #	img2=open(".wel.png","rb")
        x = data.subClient.get_user_info(data.authorId).icon
        response = requests.get(f"{x}")
        file = open("res.png", "wb")
        file.write(response.content)
        file.close()
        img = Image.open("res.png")

        height, width = img.size
        lum_img = Image.new('L', [height, width], 0)
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0, 0), (height, width)], 0, 360, fill=255)
        img_arr = np.array(img)
        lum_img_arr = np.array(lum_img)
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        (Image.fromarray(final_img_arr)).save("res.png")
        bgg = Image.open("btt.png").resize((800, 300))
        bg = Image.open("res.png").resize((800, 800))
        if frm != None and aiv != "04f6fbf2-85a3-45c0-bdae-cd02057617e7":
            E = (frm["resourceUrl"])
            rq = requests.get(E)
            zip = open("frmes.zip", "wb")
            zip.write(rq.content)
            zipi = ZipFile("frmes.zip", "r")
            zipi.extractall("fame")
            pt = os.listdir('fame')
            # if "frame.webp" in pt:
            #					web=Image.open("fame/frame.webp")
            #					web.save("fame/frame.png")
            # pty="fame"
            isdir = open("fame/frame.png", "rb")
            # isdir = os.path.isdir(pty)
            if isdir == True or aiv != "04f6fbf2-85a3-45c0-bdae-cd02057617e7" or aiv != None:
                fg = Image.open("fame/frame.png").resize((860, 860))
                # fg=Image.open("pinoc.png").resize((860,860))
                bg.paste(fg, (-25, -25), fg)
                bg.save("new.png")
                fhg = "new.png"
        elif plus == 1 and frm == None:
            fg = Image.open("aplus.png").resize((1100, 1100))
            bg.paste(fg, (-170, -170), fg)
            bg.save("aps.png")
            fhg = "aps.png"
        else:
            fhg = "res.png"

        j = Image.open(fhg).resize((230, 230))
        k = Image.open("vip.png").resize((60, 60))
        l = Image.open("plus.png").resize((80, 80))
        if rolee == 100 or rolee == 102:
            bdg = Image.open("leader.png").resize((150, 60))
        elif rolee == 101:
            bdg = Image.open("curator.png").resize((150, 60))
        else:
            bdg = Image.open("member.png").resize((150, 60))
        lv = Image.open(f"level/{lvll}.png").resize((90, 90))
        bgg.paste(j, (30, 30), j)
        if vip != None:
            bgg.paste(k, (560, 53), k)
        bgg.paste(lv, (660, 35), lv)
        if plus == 1:
            bgg.paste(l, (480, 45), l)
        bgg.paste(bdg, (280, 50), bdg)
        draw = ImageDraw.Draw(bgg)
        bgg.save("ne.png")
        ftf = open("ne.png", "rb")
        msg = f"""[BC]━━━━┅━━━┅━━━━
[BC]Bienvenue dans {tlt}
[C]1.Avant tout soso supremacy ! ꒰😌꒱
[C]2.Suivez les règles et les directives du chat de groupe.
[C]3.Respectez l'hôte et le cohôte et les membres.
[C]4.Amuser vous bien.😁
[BC]━━━━┅━━━┅━━━━"""
        data.subClient.full_embed("aminoapps.com/p/5w2u19", ftf, msg, data.chatId)


cons = mongo["coinss"]
coi = cons["coinsss"]
ttt = open('claim.txt', 'r')
claims = []
for m in ttt.read().splitlines():
    temp = m
    if temp not in claims:
        claims.append(int(temp))

@client.on_member_leave_chat()
def aurevoir(data):
    data.subClient.send_message(message="Ah bientot...")



@client.command("123456789")
def coins(data):
    current=datetime.now()
    dat=current.day
    wall=int(data.subClient.get_wallet_amount())
    user=data.authorId
    if data.comId in claims:
            lvl=data.subClient.get_user_info(user).level
            blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
            if lvl==5 or lvl>=5:
                if len(blg)!=0:
                    if wall>=50:
                        for bid in blg:
                            data.subClient.send_coins(coins=50,blogId=bid)
                            data.subClient.send_message(data.chatId,message=f"""[C]<$@{data.author}$>Gg a toi tu as gagner 50 ac
""",mentionUserIds=[data.authorId])
                    else:
                        data.subClient.send_message(data.chatId,message="je n'ai plus d'ac",replyTo=data.messageId)
                else:
                    data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> Fait un post si tu veux que sa fonctionne",mentionUserIds=[data.authorId],replyTo=data.messageId)
            else:
                data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> Tu dois etre minimum lvl 5.",replyTo=data.messageId, mentionUserIds=[data.authorId])
    else:
                lvl=data.subClient.get_user_info(user).level
                blg=data.subClient.get_user_blogs(userId=user,size=1).blogId
                if lvl==5 or lvl>=5:
                    if len(blg)!=0:
                        if wall>=50:
                            for bid in blg:
                                data.subClient.send_coins(coins=50,blogId=bid)
                                data.subClient.send_message(data.chatId,message=f"""[c]<$@{data.author}$>Gg a toi tu as gagner 50 ac
""",mentionUserIds=[data.authorId])
                        else:
                            data.subClient.send_message(data.chatId,message="je n'ai plus d'ac",replyTo=data.messageId)
                    else:
                        data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> Fait un post si tu veux que sa fonctionne",mentionUserIds=[data.authorId],replyTo=data.messageId)
                else:
                        data.subClient.send_message(data.chatId,message=f"<$@{data.author}$> Tu dois etre minimum lvl 5.",replyTo=data.messageId, mentionUserIds=[data.authorId])



@client.command()
def voc(data):
    client.start_vc(comId=data.comId, chatId=data.chatId)
    data.subClient.send_message(message="me voilaa !",chatId=data.chatId)


@client.command()
def fin(data):
    client.end_vc(comId=data.comId, chatId=data.chatId)
    data.subClient.send_message(message="Je m'eclipse !",chatId=data.chatId)


@client.command("ship")
def ship(data):
    couple = data.message + " null null "
    people = couple.split(" ")
    percentage = uniform(0, 100)
    quote = ' '
    if percentage <= 10:
        quote = 'certainement pas.'
    elif 10 <= percentage <= 25:
        quote = 'Euh...'
    elif 25 <= percentage <= 50:
        quote = 'peut etre un jour?'
    elif 50 <= percentage <= 75:
        quote = 'Mon couple ❤'
    elif 75 <= percentage <= 100:
        quote = 'Top couple❤❤❤'
    data.subClient.send_message(chatId=data.chatId, message=f"{people[0]} x {people[1]} a {percentage:.2f}% "
                                                            f"de chance de marché.")
    data.subClient.send_message(chatId=data.chatId, message=quote)
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("joinall")
def joinall(data):
    print(type(data))
    data.subClient.send_message(chatId=data.chatId, message="J'ai rejoint tous les chats...")
    data.subClient.join_all_chat()

    


@client.command()
def fond(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
        filename = image.split("/")[-1]
        urllib.request.urlretrieve(image, filename)
        with open(filename, 'rb') as fp:
            data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")



@client.command()
def titre(args):
    if client.check(args, 'staff', id_=client.botId):
        try:
            title, color = args.message.split("color=")
            color = color if color.startswith("#") else f'#{color}'
        except Exception:
            title = args.message
            color = None

        mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
        if mention:
            args.authorId = mention
            args.author = args.subClient.get_user_info(args.authorId).nickname

        if args.subClient.add_title(args.authorId, title, color):
            args.subClient.send_message(args.chatId, f"{args.author} Vous avez reçu votre titre.")


@client.command("profile")
def profile(data):
    profilchange = data.subClient.get_user_info(client.get_wallet_info().totalCoins).modifiedTime
    repa = data.subClient.get_user_info(data.authorId).reputation
    lvl = data.subClient.get_user_info(data.authorId).level
    crttime = data.subClient.get_user_info(data.authorId).createdTime
    followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
    profilchange = data.subClient.get_user_info(client.get_wallet_info().totalCoins).modifiedTime
    commentz = data.subClient.get_user_info(data.authorId).commentsCount
    posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
    followed = data.subClient.get_user_info(data.authorId).followingCount
    sysrole = data.subClient.get_user_info(data.authorId).role
    data.subClient.send_message(data.chatId, message=f"""
[C]Pseudo : {data.author}

[C]ID Amino : {data.authorId}

[C]Date d'entrée dans la communauté : {crttime}

[C]Dernière mise à jour du profil : {profilchange}

[C]Réputation : {repa}

[C]Level : {lvl}

[C]Total de posts : {posts}

[C]Nombre de commentaires sur le mur du profil : {commentz}

[C]Nombre d'abos : {followed}

[C]Nombre d'abonnés : {followers}

[C]Numéro de compte dans le système {sysrole}
""")


@client.command("@", condition=is_staff)
def everyone(args):
    mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId).userId]
    # test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId).userId])
    args.subClient.send_message(chatId=args.chatId, message=f"@everyone {args.message}", mentionUserIds=mention)


@client.command()
def pv(data):
    data.subClient.start_chat(data.authorId, message=f"[i]yo {data.author}\nLuffy ici...Comment tu va !")
    data.subClient.send_message(data.chatId, message=f"<$@{data.author}$> regarde tes pv", replyTo=data.messageId,
                                mentionUserIds=[data.authorId])




@client.command("msg")
def msg(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId, asStaff=True, reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10 and not (client.check(args, 'staff')):
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value,
                                        mentionUserIds=ment)
            tz = pytz.timezone('Asia/Kolkata')
            now = datetime.now(tz)
            current_time = now.strftime("%H:%M:%S")
            kt = args.subClient.get_chat_thread(args.chatId).membersCanInvite
            if kt != None:
                op = client.get_from_id(objectId=args.chatId, objectType="12", comId=args.comId).json
                chatlink = op["extensions"]["linkInfo"]["shareURLShortCode"]
            else:
                chatlink = "Private Chat"
            # chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
            val = args.subClient.get_chat_thread(args.chatId).title
            chats = args.subClient.favorite_chats
            if val == None:
                val = "Private Chat"
            for id, in zip(chats):
                args.subClient.send_message(chatId=id, message=f"""[c]{args.author} used hidden message in {val}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

{args.message}

[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁

Chat : {chatlink}
Time : {current_time}""", embedTitle=f"{args.author}", embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",
                                            embedContent=f"chat: {val}")


def clears(d, md):
    try:
        d.subClient.delete_message(chatId=d.chatId, messageId=md, asStaff=True, reason="Clear")
    except:
        pass


@client.command("suicide")
def ban(data):
    con = data.author
    soso = data.authorId
    supremacy = data.chatId
    data.subClient.send_message(message=f"Gg {con} il ne te reste plus que  5sec a vivre ",chatId=supremacy)
    time.sleep(5)
    data.subClient.ban(userId=soso, reason="fuis")



@client.command("help")
def help(args):
    img = open(".pro.png", "rb")
    ias = ("help.png")
    im = open(".pr.png", "rb")
    yimg = open("youimage.png", "rb")
    Image.open(ias).resize((863, 400)).save("nsus.png")
    ff = open("nsus.png", "rb")
    msg = f"""[Cub]les Commandes du bot :\n\n[C]◈.!bot — Commande general du bot.\n[C]◈. !membre — liste des commande membre.\n[C]◈. !fun — commande pour le fun.\n[C]◈. !modo — commande staff.\n[C]◈. !admin — commande admin."""
    args.subClient.full_embed("aminoapps.com/p/5w2u19", ff, msg, args.chatId)
    client.show_online(args.comId)


@client.command()
def comid(data):
    n = data.message
    fok = client.get_from_code(n)
    id = client.get_from_code(n).objectId
    cid = fok.path[1:fok.path.index("/")]
    data.subClient.send_message(chatId=data.chatId, message=f"Id de la commu = {cid}")



@client.command()
def admnlist(data):
    msg = """[c]Bot Admin
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
http://aminoapps.com/u/SoribaBlackStar
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
"""
    data.subClient.send_message(data.chatId, message=msg)


@client.command(condition=is_it_me)
def send(args):
    coins = args.subClient.get_wallet_amount()
    if coins >= 1:
        amt = 0
        while coins > 200:
            args.subClient.pay(200, chatId=args.chatId)
            coins -= 200
            amt += 200
        args.subClient.pay(int(coins), chatId=args.chatId)
        args.subClient.send_message(args.chatId, f"envoie de {coins + amt} ac...")
    else:
        args.subClient.send_message(args.chatId, "j'ai plus d'ac!")


@client.command()
def name(data):
    data.subClient.edit_profile(nickname=data.message)
    data.subClient.send_message(chatId=data.chatId, message=f"mon nouveau nom est {data.message}")


@client.command()
def pvp(data):
    import time
    msg = data.message + " null null "
    msg = msg.split(" ")
    try:
        rounds = int(msg[0])
    except (TypeError, ValueError):
        rounds = 5
        msg[2] = msg[1]
        msg[1] = msg[0]
        msg[0] = 5

    if msg[1] == '' or msg[1] == ' ' or msg[1] == 'null':
        msg[1] = data.author
    if msg[2] == '' or msg[1] == ' ' or msg[2] == 'null':
        msg[2] = data.author
    if msg[1] == msg[2]:
        msg[2] = f'Inverser_{msg[1]}'

    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[icu]{data.author} a commencé un PVP."
                                                                    f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                    f'\n[ci]Que le meilleur gagne !')
            break
        except:
            print(f"Erreur... Nouvelle tentative dans 5 secondes.")
            time.sleep(5)
    win1 = 0
    win2 = 0
    round = 0
    for tpvp in range(0, rounds):
        round = round + 1
        punch = randint(0, 1)
        if punch == 0:
            win1 = win1 + 1
            agress = msg[1]
            defens = msg[2]
        else:
            win2 = win2 + 1
            agress = msg[2]
            defens = msg[1]
        time.sleep(4)
        while True:
            try:
                data.subClient.send_message(chatId=data.chatId, message=f"[cu]Tours {round}"
                                                                        f"\n[ci]{msg[1]} ⚔ {msg[2]}"
                                                                        f"\n[ic] {agress} detruis {defens}!")
                break
            except:
                print(f"Erreur... Nouvelle tentative dans 5 secondes")
                time.sleep(5)
    while True:
        try:
            if win1 > win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} a gagné!"
                                                                        f"\n[ciu][{win1} x {win2}]")
            elif win1 < win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} a gagné!"
                                                                        f"\n[cic][{win1}x{win2}]")
            elif win1 == win2:
                data.subClient.send_message(chatId=data.chatId, message=f"[iC]Lien.")
            break
        except:
            print(f"Erreur... Nouvelle tentative dans 5 secondes.")
            time.sleep(5)


@client.command(condition=admins)
def aadmin(data):
    adm.append("{data.message}")
    data.subClient.send_message(data.chatId, message="ajouté a la liste des admin")


@client.command("level")
def rank(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    if "aminoapps.com" in data.message:
        user = (client.get_from_code(data.message.split(' ')[0]).objectId)
    elif mention != None:
        for x in mention:
            user = x
    else:
        user = data.authorId

    if data.chatId:
        tlt = data.subClient.get_chat_thread(data.chatId).title
        img3 = open(".tvs.png", "rb")
        vip = data.subClient.get_user_info(user).influencerInfo
        plus = data.subClient.get_user_info(user).accountMembershipStatus
        following = data.subClient.get_user_info(user).followingCount
        repa = data.subClient.get_user_info(user).reputation
        lvll = data.subClient.get_user_info(user).level
        frm = data.subClient.get_user_info(user).avatarFrame
        rolee = data.subClient.get_user_info(user).role
        #	img2=open(".wel.png","rb")
        x = data.subClient.get_user_info(user).icon
        response = requests.get(f"{x}")
        file = open(".sampl9e.png", "wb")
        file.write(response.content)
        file.close()
        img = Image.open(".sampl9e.png")
        if frm != None:
            E = (frm["resourceUrl"])
            rq = requests.get(E)
            zip = open("frmes.zip", "wb")
            zip.write(rq.content)
            zipi = ZipFile("frmes.zip", "r")
            zipi.extractall("fame")
            pt = os.listdir('fame')
            if "frame.webp" in pt:
                web = Image.open("fame/frame.webp")
                web.save("fame/frame.png")
        height, width = img.size
        lum_img = Image.new('L', [height, width], 0)
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0, 0), (height, width)], 0, 360, fill=255)
        img_arr = np.array(img)
        lum_img_arr = np.array(lum_img)
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        (Image.fromarray(final_img_arr)).save("res.png")
        bgg = Image.open("bt.png").resize((800, 300))
        bg = Image.open("res.png").resize((800, 800))
        pty = "fame"
        isdir = os.path.isdir(pty)
        if isdir == True:
            fg = Image.open("fame/frame.png").resize((860, 860))
            bg.paste(fg, (-25, -25), fg)
            bg.save("new.png")
            fhg = "new.png"
        else:
            fhg = "res.png"

        j = Image.open(fhg).resize((230, 230))
        k = Image.open("vip.png").resize((60, 60))
        l = Image.open("plus.png").resize((80, 80))
        if rolee == 100 or rolee == 102:
            bdg = Image.open("leader.png").resize((150, 60))
        elif rolee == 101:
            bdg = Image.open("curator.png").resize((150, 60))
        else:
            bdg = Image.open("member.png").resize((150, 60))
        lv = Image.open(f"level/{lvll}.png").resize((90, 90))
        bgg.paste(j, (30, 30), j)
        if vip != None:
            bgg.paste(k, (560, 53), k)
        bgg.paste(lv, (660, 35), lv)
        if plus == 1:
            bgg.paste(l, (480, 45), l)
        bgg.paste(bdg, (280, 50), bdg)
        title_fot = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
        title_font = ImageFont.truetype('BebasNeue-Regular.ttf', 40)
        title_fon = ImageFont.truetype('BebasNeue-Regular.ttf', 35)
        title_fn = ImageFont.truetype('BebasNeue-Regular.ttf', 45)
        draw = ImageDraw.Draw(bgg)
        draw.text((300, 150), f"{data.author}", (255, 255, 255), font=title_fot)
        draw.text((300, 220), "REPUTATION :", (255, 0, 0), font=title_font)
        # draw.text((540,220), "followers :", (255,0,0), font=title_font)
        draw.text((465, 215), f"{repa}", (255, 255, 255), font=title_fn)
        #	draw.text((705,215), f"{followers}", (255,255,255), font=title_fn)
        bgg.save("ne.png")
        ftf = open("ne.png", "rb")
        msg = f"""[C]{data.author}"""
        data.subClient.full_embed("aminoapps.com/p/5w2u19", ftf, msg, data.chatId)
    pag = "fame"
    shutil.rmtree(pag)


@client.command("cohote")
def mentionco(args):
    if client.check(args, 'staff', 'admin'):
        if args.message and client.check(args, 'admin'):
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_thread(args.chatId).json['extensions']['coHost']]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_thread(args.chatId).json['extensions']['coHost']])
        # print(test)

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"<$@Cohosts{test}$>", mentionUserIds=mention)


@client.command("bot")
def bot(args):
    img = open(".pro.png", "rb")
    ias = ("help.png")
    im = open(".pr.png", "rb")
    yimg = open("youimage.png", "rb")
    Image.open(ias).resize((863, 400)).save("nsus.png")
    ff = open("nsus.png", "rb")
    msg = f"""[Cub]les Commandes general du bot :\n\n[C]◈.!msg .\n[C]◈. !vc .\n[C]◈. !voc .\n[C]◈. !fin .\n[C]◈. !ship.\n[C]◈. !pvp .\n[C]◈. !rank .\n[C]◈. !titre.\n[C]◈. !fond .\n[C]◈. !infoprofile .\n[C]◈. !play .\n[C]◈. !an.\n[C]◈. !infos ."""
    args.subClient.full_embed("aminoapps.com/p/5w2u19", ff, msg, args.chatId)
    #client.show_online(data.comId)


@client.command("fun")
def fun(args):
    img = open(".pro.png", "rb")
    ias = ("help.png")
    im = open(".pr.png", "rb")
    yimg = open("youimage.png", "rb")
    Image.open(ias).resize((863, 400)).save("nsus.png")
    ff = open("nsus.png", "rb")
    msg = f"""[Cub]les Commandes fun du bot :\n\n[C]◈.!os .\n[C]◈. !code ."""
    args.subClient.full_embed("aminoapps.com/p/5w2u19", ff, msg, args.chatId)


@client.command("modo", condition=is_staff)
def modo(args):
    img = open(".pro.png", "rb")
    ias = ("help.png")
    im = open(".pr.png", "rb")
    yimg = open("youimage.png", "rb")
    Image.open(ias).resize((863, 400)).save("nsus.png")
    ff = open("nsus.png", "rb")
    msg = f"""[Cub]les Commandes staff du bot :\n\n[C]◈.!sup .\n[C]◈. !joinall .\n[C]◈. !@ .\n[C]◈. !cohote .\n[C]◈. !add.\n[C]◈. !rem .\n[C]◈. !banl ."""
    args.subClient.full_embed("aminoapps.com/p/5w2u19", ff, msg, args.chatId)


@client.command("admin", condition=is_it_me)
def admin(args, ):
    img = open(".pro.png", "rb")
    ias = ("help.png")
    im = open(".pr.png", "rb")
    yimg = open("youimage.png", "rb")
    Image.open(ias).resize((863, 400)).save("nsus.png")
    ff = open("nsus.png", "rb")
    msg = f"""[Cub]les Commandes general du bot :\n\n[C]◈.!joinamino .\n[C]◈. !send .\n[C]◈. !name .\n[C]◈. !block .\n[C]◈. !unblock ."""
    args.subClient.full_embed("aminoapps.com/p/5w2u19", ff, msg, args.chatId)
    #client.show_online(data.comId)



@client.command("google")
def searchuser(data):
    msg = data.message.split(" ")
    code1 = msg[0]
    code2 = msg[1]
    user = (client.get_from_code(code1).objectId)
    cd = (client.get_from_code(code2))
    cid = cd.path[1:cd.path.index("/")]
    try:
        ui = client.get_from_id(objectType=0, objectId=user, comId=cid).json
        lin = ui["extensions"]["linkInfo"]["shareURLShortCode"]
        data.subClient.send_message(data.chatId, message=f"""[cu]Mugiwara  a un profil d'utilisateur

Link : {lin}

""", embedTitle="lien du profil", embedLink=f"{lin}", embedContent="Cliquez ici pour atteindre l'utilisateur")
    except:
        data.subClient.send_message(data.chatId, message="utilisateur non disponible sur cette commu",
                                    replyTo=data.messageId)
        pass


@client.command("add")
def add_banned_word(args):
    if client.check(args, 'staff', 'admin'):
        if not args.message or args.message in args.subClient.banned_words:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.add_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} ajouté dans la ban list des mots")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M:%S")
        kt = args.subClient.get_chat_thread(args.chatId).membersCanInvite

        # chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        if kt != None:
            op = client.get_from_id(objectId=args.chatId, objectType="12", comId=args.comId).json
            chatlink = op["extensions"]["linkInfo"]["shareURLShortCode"]
        else:
            chatlink = "Private Chat"
        val = args.subClient.get_chat_thread(args.chatId).title
        chats = args.subClient.favorite_chats
        if val == None:
            val = "Private Chat"
        for id, in zip(chats):
            args.subClient.send_message(chatId=id, message=f"""[c]{args.author} ajouté dans la ban list des mots

[c]{args.message}

Chat : {chatlink}
Time : {current_time}""", embedTitle=f"{args.author}", embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",
                                        embedContent=f"chat: {val}")


@client.command("rem")
def remove_banned_word(args):
    if client.check(args, 'staff', 'admin'):
        if not args.message:
            return
        try:
            ar = args.message.lower().strip().split()
        except Exception:
            ar = [ar.lower().strip()]
        args.subClient.remove_banned_words(ar)
        args.subClient.send_message(args.chatId, f"{args.message} supprimé de la ban list des mot")
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M:%S")
        kt = args.subClient.get_chat_thread(args.chatId).membersCanInvite

        # chatlink=f"ndc://x{args.comId}/chat-thread/{args.chatId}"
        if kt != None:
            op = client.get_from_id(objectId=args.chatId, objectType="12", comId=args.comId).json
            chatlink = op["extensions"]["linkInfo"]["shareURLShortCode"]
        else:
            chatlink = "Private Chat"
        val = args.subClient.get_chat_thread(args.chatId).title
        chats = args.subClient.favorite_chats
        if val == None:
            val = "Private Chat"
        for id, in zip(chats):
            args.subClient.send_message(chatId=id, message=f"""[c]{args.author} supprimé de la ban list des mots

[c]{args.message}

Chat : {chatlink}
Time : {current_time}""", embedTitle=f"{args.author}", embedLink=f"ndc://x{args.comId}/user-profile/{args.authorId}",
                                        embedContent=f"chat: {val}")


@client.command("banl")
def banned_word_list(args):
    val = ""
    if args.subClient.banned_words:
        for elem in args.subClient.banned_words:
            val += "◈" + elem + "\n"
    else:
        val = "vide"
    try:
        args.subClient.send_message(args.chatId, message=f"""
[c]Banned Words
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙
{val}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
    except Exception:
        args.subClient.send_message(args.chatId, message="limite de mot atteint")
        pass


@client.command("block")
def block(args):
    if client.check(args, 'staff', 'admin'):
        mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
        for user in mention:
            if not client.is_it_admin(user):
                args.subClient.add_favorite_users(str(user))
                h = args.subClient.get_user_info(userId=str(user)).nickname
                args.subClient.client.block(userId=str(user))
                args.subClient.block(userId=str(user))
                args.subClient.send_message(args.chatId, f"<$@{h}$> est interdit d'utilisé le bot!",
                                            mentionUserIds=[str(user)])
            else:
                args.subClient.send_message(args.chatId, message="tu ne peux blocker un admin", replyTo=args.messageId)
    else:
        args.subClient.send_message(args.chatId, message="commande modo", messageId=args.messageId)


@client.command("deblock", condition=is_black)
def unblock(args):
    if client.check(args, 'staff', 'admin'):
        mention = args.subClient.get_message_info(chatId=args.chatId, messageId=args.messageId).mentionUserIds
        for user in mention:
            if not client.is_it_admin(user):
                h = args.subClient.get_user_info(userId=str(user)).nickname
                args.subClient.client.unblock(userId=str(user))
                args.subClient.remove_favorite_users(str(user))
                args.subClient.unblock(userId=str(user))
                args.subClient.send_message(args.chatId, f"<$@{h}$> est autoriser a utiliser le bot!",
                                            mentionUserIds=[str(user)])
    else:
        args.subClient.send_message(args.chatId, message="commande modo", messageId=args.messageId)

    # else:
    #	args.subClient.send_message(args.chatId,message="Mod Command",messageId=args.messageId)


@client.command(condition=is_staff)
def hack(data):
    it = randint(500, 2000)
    ist = randint(50, 630)
    iss = randint(10, 40)
    o = randint(1, 9)
    v = randint(23, 98)
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for user in mention:
        repa = data.subClient.get_user_info(userId=str(user)).reputation
        h = data.subClient.get_user_info(userId=str(user)).nickname
        lvl = data.subClient.get_user_info(userId=str(user)).level
        crttime = data.subClient.get_user_info(userId=str(user)).createdTime
        followers = data.subClient.get_user_achievements(userId=str(user)).numberOfFollowersCount
        profilchange = data.subClient.get_user_info(userId=str(user)).modifiedTime
        commentz = data.subClient.get_user_info(userId=str(user)).commentsCount
        posts = data.subClient.get_user_achievements(userId=str(user)).numberOfPostsCreated
        followed = data.subClient.get_user_info(userId=str(user)).followingCount
        # data.subClient.send_message(data.chatId,message="Are you sure(Y/N)")
        # time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"Chargement commencé {h}'s profile....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Récupération de l'adresse IP de l'appareil........")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"{h}'s ip adress : 192.158.{o}.{v}")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"""
{h}'s profile chargé.

Pseudo: {h}
id: {str(user)}
Compte créé: {crttime}
Dernier changement: {profilchange}
Réputations: {repa}
Niveau du compte: {lvl}
Nombre de posts créé: {posts}
Nombre de commentaires sur le mur du profil : {commentz}
Nombre d'abos : {followed}
Nombre d'abonnés : {followers}""")
        data.subClient.send_message(data.chatId, message="Chargement des fichiers système.....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"{it} chats trouvés à partir de {h}'s comptes")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message=f"""
{h}'s System Information...

{it} fichiers trouvés
{ist} images trouvés
{iss} Vidéo chargés""")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Tous les fichiers téléchargés sur le serveur")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Vérification de tous les fichiers.....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="Connexion du serveur au serveur Darkweb....")
        time.sleep(7)
        data.subClient.send_message(data.chatId, message="""struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize){

	struct group_info *group_info;
	int nblocks;
	int i;


	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
	/* Make sure we always allocate at least one indirect block pointer */
	nblocks = nblocks ? : 1;
	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
	if (!group_info)
		return NULL;
	group_info->ngroups = gidsetsize;
	group_info->nblocks = nblocks;
	atomic_set(&group_info->usage, 1);""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="""	if (gidsetsize <= NGROUPS_SMALL)
		group_info->blocks[0] = group_info->small_block;
	else {
		for (i = 0; i < nblocks; i++) {
			gid_t *b;
			b = (void *)__get_free_page(GFP_USER);
			if (!b)
				goto out_undo_partial_alloc;
			group_info->blocks[i] = b;
		}
	}
	return group_info;


out_undo_partial_alloc:

	while (--i >= 0) {
		free_page((unsigned long)group_info->blocks[i]);
	}
	kfree(group_info);
	return NULL;
}



EXPORT_SYMBOL(groups_alloc);
""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="""void groups_free(struct group_info *group_info)

{

	if (group_info->blocks[0] != group_info->small_block) {
		int i;
		for (i = 0; i < group_info->nblocks|""")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message="Connecté au Dark Web")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"Piraté avec succès {h}'s appareil")
        time.sleep(5)
        data.subClient.send_message(data.chatId, message=f"{h}'s les données de l'appareil téléchargées sur Darkweb..")
        data.subClient.send_message(data.chatId, message=f"<$@{h}$> votre appareil est piraté",
                                    mentionUserIds=[str(user)])


@client.command("acc")
def accept(args):
    if client.check(args, 'staff', 'admin'):
        if args.subClient.accept_role(args.chatId):
            args.subClient.send_message(args.chatId, "role accepter")
            return
        val = args.subClient.get_notices(start=0, size=25)
        for elem in val:
            print(elem["title"])
        ans = None
        res = None

        for elem in val:
            if 'devenir' in elem['title'] or "hotehost" in elem['title']:
                res = elem['noticeId']
            if res:
                ans = args.subClient.accept_role(res)
            if ans:
                args.subClient.send_message(args.chatId, f"Accepté", replyTo=args.messageId)
                return
        else:
            args.subClient.send_message(args.chatId, "leader ou cura a accepter")


@client.command("info")
def info(data):
    data.subclient.send_message(message="[ci]Hé là je suis un bot cree par soso lui meme je peux accueillir les nouveaux je peux faire toute sorte de chose et surtout soso supremacy")

@client.command("online")
def online(data):
    online = ""
    online2 = data.subclient.get_online_users(start=0, size=1000)
    for uid in online2.profile.nickname:
        online = online + uid + "\n"
    data.subclient.send_message(message="voici la liste des personne connecter :"
                                        f"{online}")

@client.on_message()
def on_message(data):
    if data.message.startswith("quoi"):
        data.subClient.send_message(data.chatId, message="feur")
    if data.message.startswith("oui"):
        data.subClient.send_message(data.chatId, message="stiti")
    if data.message.startswith("non"):
        data.subClient.send_message(data.chatId, message="bril")
    if data.message.startswith("ouai"):
        data.subClient.send_message(data.chatId, message="stern")
    if data.message.startswith("?"):
        user = data.author
        data.subClient.send_message(message=f"{user}" + " " + str(random.choice(lis)), chatId=data.chatId)
    if data.message.startswith("ok"):
        data.subClient.send_message(message="sur glace !", chatId=data.chatId)
    #if data.message.startswith("pd"):
        #data.subClient.kick(userId="b3c859d0-983d-4a10-a6d1-eb11eebbf2e3" ,chatId=data.chatId ,allowRejoin=True)
   # if data.message.startswith("tg"):
        #data.subClient.kick(userId="b3c859d0-983d-4a10-a6d1-eb11eebbf2e3" ,chatId=data.chatId ,allowRejoin=True)
   # if data.message.startswith("Tg"):
        #data.subClient.kick(userId="b3c859d0-983d-4a10-a6d1-eb11eebbf2e3" ,chatId=data.chatId ,allowRejoin=True)


@client.command("bou")
def bou(soso):
    soso.subClient.send_message(message="")



@client.command("an")
def ah(data):
    data.subClient.delete_message(messageId=data.messageId, chatId=data.chatId, asStaff=True, reason="sup")
    data.subClient.send_message(message=(f"Annonce de, {data.author} :\n\n{data.message}"), chatId=data.chatId,messageType=68)

@client.command("sup")
def sup(data):
    for msgId in data.subClient.get_chat_messages(chatId=data.chatId, size=50).messageId:
        data.subClient.delete_message(reason="sup", chatId=data.chatId, messageId=msgId, asStaff=True)


@client.command("os")
def os(data):
    user = data.author
    data.subClient.send_message(message=f"{user}" +""+ str(random.choice(gayles)), chatId=data.chatId)



@client.command("x100")
def x100(data):
    comid = data.comId
    chats = data.subClient.get_chat_threads(size=100)
    chat_id = data.chatId
    threads_count = 100

    def spam_process():
        thread_pool = ThreadPool(threads_count)
        while True:
            try:
                thread_pool.apply_async(client.start_vc, [chat_id,comid])
                thread_pool.apply_async(client.end_vc, [chat_id,comid])
            except:
                return

    pool = ThreadPool(threads_count)
    pool.apply(spam_process)




@client.command("roue")
def roue(data):
    data.subClient.send_message(message="Lancement du jeu de la roulette russe...", chatId=data.chatId)
    time.sleep(3)
    with open("debut.png", 'rb') as file:
        data.subClient.send_message(chatId=data.chatId, file=file, fileType="image")
    data.subClient.send_message(message="Roulette Russe Lancer !", chatId=data.chatId)
    time.sleep(2)
    data.subClient.send_message(message="Les regles sont simple si tu tombes les ac,tu aura le nombre que tu aura gagner sinon dans le cas ban tu sera automatiquement banni ! ", chatId=data.chatId)
    time.sleep(5)
    data.subClient.send_message(message="Je pense t'avoir laisser assez de temps pour lire les regles alors commençons !", chatId=data.chatId)
    time.sleep(3)
    data.subClient.send_message(message="sa tourne...", chatId=data.chatId )
    time.sleep(3)
    data.subClient.send_message(message="sa tourne...", chatId=data.chatId)
    data.subClient.send_message(chatId=data.chatId, file=(random.choice(roulette)), fileType="image")
    data.subClient.send_message(message="Merci pour ta participation !", chatId=data.chatId)

def maintenance():
    print("launch maintenance")
    i = 0
    while i < 7200:
        i += 10
        time.sleep(10)
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])


# Thread(target=maintenance).start()
# activate this if your bot stop working by moments

client.launch(True)
print("Bot Lancer")

def socketRoot():
    j = 0
    while True:
        if j >= 300:
            print("Updating socket.......")
            client.close()
            client.run_amino_socket()
            print("Socket updated")
            j = 0
        j = j + 1
        time.sleep(1)


socketRoot()


