import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def help():
    print('Geri dönüşüm ile ilgili bilgi almak istiyorsan bu komutları kullanın: yardım , oneri , geridönüşümkutuları , doğadakaybolmasüreleri , nerelerezararverirler , kullanımalanları')

@bot.command()
async def yardım(ctx):
    await ctx.send('Doğal Kaynakların Korunması ilk maddemizdir. Geri dönüşüm, hammaddelerin tekrar kullanılmasını sağlar, bu da ormanların, madenlerin ve diğer doğal kaynakların korunmasına yardımcı olur. Enerji tasarrufu çok öenmlidir. İhtiyacımız olmadığı zaman elektiriği kapatmalıyız, dişlerimizi fırçalarken suyu kapatmalıyız. Yeni ürünler üretmek için gereken enerji, geri dönüştürülmüş malzemelerden üretim yapıldığında genellikle daha azdır. Çevre kirliliğini engellememiz lazımdır çünkü küresel ısınma çok büyük bir sorundur.')

@bot.command()
async def oneri(ctx):
    await ctx.send('Geri dönüşüm maddelerini çöpe atmak yerine geri dönüşüm kutularına atmalıyız. Çünkü atmazsak dünyamız çöp yığınına dönüşür.')

@bot.command()
async def geridönüşümkutuları(ctx):
    await ctx.send(' Sarı: Plastik , Yeşil: Cam ,Kırmızı: Metal , Gri: Organik atıklar (bu, bazı yerlerde değişebilir)')

@bot.command()
async def doğadakaybolmasüreleri(ctx):
    await ctx.send('Plastik: 10-1000 yıl. Cam: 1 milyon yıl veya daha fazla. Metal: 50-500 yıl. Organik Atıklar: 1 ay - 3 yıl.')

@bot.command()
async def nerelerezararverirler(ctx):
    await ctx.send('İnsan: Yediğimiz balıklar eğer plastik yerler ise bize zarar verebilirler. Plastik: Deniz ve kara yaşamını tehdit eder, mikroplastikler su kaynaklarını kirletir. Cam: Doğada çok uzun süre kaldığı için araziye zarar verir. Metal: Oksitlenerek toprağa ve suya zararlı maddeler salabilir. Organik Atıklar: Doğru şekilde kompostlanmazsa metan gazı salınımına neden olabilir, ancak genellikle daha az çevresel zarara sahiptir.')

@bot.command()
async def kullanımalanları(ctx):
    await ctx.send('Güneş enerjisi; Tanım güneş panelleri aracılığıyla güneş ışığının elektrik enerjisine dönüştürülmesi ile birçok işimize yarar. Ayrıca doğaya zarar vermezler. Uygulumalar: Evde , tarım işlerinde , su ısıtma sistemlerinde kullanılır.')

