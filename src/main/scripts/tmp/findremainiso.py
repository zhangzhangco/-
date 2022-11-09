import jsonpath
import json
import sys, os, fnmatch
from shutil import copyfile

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
iso114href = {"ISO 23:1993":"/standard/20575.html",
"ISO 25:1994":"/standard/21562.html",
"ISO 26:1993":"/standard/3615.html",
"ISO 28:1976":"/standard/3617.html",
"ISO 69:1998":"/standard/27542.html",
"ISO 70:1981":"/standard/3710.html",
"ISO 71:2014":"/standard/63974.html",
"ISO 74:1976":"/standard/3714.html",
"ISO 162:1985":"/standard/3996.html",
"ISO 359:1983":"/standard/4325.html",
"ISO 466:1976":"/standard/4494.html",
"ISO 486:1988":"/standard/4531.html",
"ISO 490:1993":"/standard/2495.html",
"ISO 491:2002":"/standard/34907.html",
"ISO 1019:1982":"/standard/5489.html",
"ISO 1039:1995":"/standard/23291.html",
"ISO 1188:1984":"/standard/5780.html",
"ISO 1189:1986":"/standard/5782.html",
"ISO 1223:2003":"/standard/31172.html",
"ISO 1700:1988":"/standard/6317.html",
"ISO 1780:1984":"/standard/6413.html",
"ISO 1781:1983":"/standard/6414.html",
"ISO 1785:1983":"/standard/6417.html",
"ISO 1787:1984":"/standard/6420.html",
"ISO 1793:2005":"/standard/36142.html",
"ISO 2404:1986":"/standard/7301.html",
"ISO 2467:2004":"/standard/40001.html",
"ISO 2906:2002":"/standard/30126.html",
"ISO 2907:2002":"/standard/25425.html",
"ISO 2910:2018":"/standard/74446.html",
"ISO 2939:2015":"/standard/52811.html",
"ISO 2969:2015":"/standard/43646.html",
"ISO 3022:1988":"/standard/8105.html",
"ISO 3023:1995":"/standard/23292.html",
"ISO 3024:1983":"/standard/8108.html",
"ISO 3026:1992":"/standard/20537.html",
"ISO 3042:1992":"/standard/8130.html",
"ISO 3042:1992/Cor 1:2004":"/standard/39886.html",
"ISO 3047:1982":"/standard/8154.html",
"ISO 3639:1981":"/standard/9083.html",
"ISO 3641:1976":"/standard/9085.html",
"ISO 3642:1983":"/standard/9086.html",
"ISO 3644:1976":"/standard/9087.html",
"ISO 3645:1984":"/standard/9089.html",
"ISO 3646:1976":"/standard/9090.html",
"ISO 3647:1976":"/standard/9091.html",
"ISO 3653:1978":"/standard/9100.html",
"ISO 3773:1983":"/standard/9294.html",
"ISO 3774:1988":"/standard/9296.html",
"ISO 3820:1978":"/standard/9364.html",
"ISO 4238:1976":"/standard/10038.html",
"ISO 4241:2019":"/standard/74445.html",
"ISO 4242:1980":"/standard/10041.html",
"ISO 4243:1979":"/standard/10042.html",
"ISO 4246:1994":"/standard/10045.html",
"ISO 4834:1997":"/standard/26949.html",
"ISO 5758:2002":"/standard/35512.html",
"ISO 5768:1998":"/standard/30125.html",
"ISO 6025:2000":"/standard/31173.html",
"ISO 6033:1983":"/standard/12229.html",
"ISO 6035:1983":"/standard/12230.html",
"ISO 6036:1996":"/standard/12231.html",
"ISO 6038:1993":"/standard/12233.html",
"ISO 6896:1984":"/standard/13418.html",
"ISO 7343:1993":"/standard/20160.html",
"ISO 7739:2016":"/standard/69743.html",
"ISO 7831:1986":"/standard/14753.html",
"ISO 7832:2014":"/standard/63975.html",
"ISO 8001:1984":"/standard/15000.html",
"ISO 8395:1995":"/standard/15561.html",
"ISO 8400:1985":"/standard/15568.html",
"ISO 8567:2002":"/standard/28294.html",
"ISO 8567:2002/Cor 1:2004":"/standard/39865.html",
"ISO 8590:1994":"/standard/15881.html",
"ISO 8622:1998":"/standard/27543.html",
"ISO 8687:1987":"/standard/16089.html",
"ISO 8758:1992":"/standard/16167.html",
"ISO 9525:1988":"/standard/17258.html",
"ISO 9568:1993":"/standard/17314.html",
"ISO 9642:2020":"/standard/74444.html",
"ISO 10284:1997":"/standard/18326.html",
"ISO 10356:1996":"/standard/18413.html",
"ISO 12222:2017":"/standard/59518.html",
"ISO 12606:1997":"/standard/2459.html",
"ISO 12611:2004":"/standard/39985.html",
"ISO 12612:2016":"/standard/69741.html",
"ISO 17266:2018":"/standard/74447.html",
"ISO 17332:2001":"/standard/32993.html",
"ISO 20859:2005":"/standard/39786.html",
"ISO 21727:2016":"/standard/69744.html",
"ISO 22234:2005":"/standard/40957.html",
"ISO 26428-1:2008":"/standard/50204.html",
"ISO 26428-2:2008":"/standard/50218.html",
"ISO 26428-3:2008":"/standard/50219.html",
"ISO 26428-9:2009":"/standard/52784.html",
"ISO 26428-11:2011":"/standard/57749.html",
"ISO 26428-19:2011":"/standard/57750.html",
"ISO 26429-3:2008":"/standard/50205.html",
"ISO 26429-4:2008":"/standard/50221.html",
"ISO 26429-6:2008":"/standard/50222.html",
"ISO 26429-7:2008":"/standard/50223.html",
"ISO 26429-8:2009":"/standard/52785.html",
"ISO 26429-9:2009":"/standard/52786.html",
"ISO 26429-10:2009":"/standard/52787.html",
"ISO 26430-1:2008":"/standard/50206.html",
"ISO 26430-2:2008":"/standard/50224.html",
"ISO 26430-3:2008":"/standard/50225.html",
"ISO 26430-4:2009":"/standard/52788.html",
"ISO 26430-5:2009":"/standard/52789.html",
"ISO 26430-6:2009":"/standard/52790.html",
"ISO 26430-9:2009":"/standard/52791.html",
"ISO 26431-1:2008":"/standard/50207.html",
"ISO 26432-2:2008":"/standard/50208.html",
"ISO 26433:2009":"/standard/52793.html"}
iso114={"ISO 23:1993":"Cinematography — Camera usage of 35 mm motion-picture film — Specifications",
"ISO 25:1994":"Cinematography — Camera usage of 16 mm motion-picture film — Specifications",
"ISO 26:1993":"Cinematography — Projector usage of 16 mm motion-picture films for direct front projection — Specifications",
"ISO 28:1976":"Cinematography — Camera usage of 8 mm Type R motion-picture film — Specifications",
"ISO 69:1998":"Cinematography — 16 mm motion-picture and magnetic film — Cutting and perforating dimensions",
"ISO 70:1981":"Cinematography — 35 mm negative photographic sound record on 35 mm motion-picture film — Position and maximum width dimensions",
"ISO 71:2014":"Cinematography — 16 mm negative photographic sound record on 16 mm, 35/16 mm and 35/32 mm motion-picture film — Positions and dimensions",
"ISO 74:1976":"Cinematography — Image area produced by camera aperture and maximum projectable image area on 8 mm Type R motion-picture film — Positions and dimensions",
"ISO 162:1985":"Cinematography — Head gaps and sound records for three-, four-, or six-track magnetic sound records on 35 mm and single-track on 17,5 mm motion-picture film containing no picture — Positions and width dimensions",
"ISO 359:1983":"Cinematography — Projectable image area on 16 mm motion-picture prints — Dimensions and location",
"ISO 466:1976":"Cinematography — Image produced by 16 mm motion-picture camera aperture — Position and dimensions",
"ISO 486:1988":"Cinematography — 16 mm motion-picture film perforated 8 mm Type R — Cutting and perforating dimensions",
"ISO 490:1993":"Cinematography — Magnetic stripes and magnetic recording head gaps for sound record on 16 mm motion-picture film perforated along one edge (Type 1) — Positions and width dimensions",
"ISO 491:2002":"Cinematography — 35 mm motion-picture film and magnetic film — Cutting and perforating dimensions",
"ISO 1019:1982":"Cinematography — Spools, daylight loading type for 16 mm motion-picture cameras — Dimensions",
"ISO 1039:1995":"Cinematography — Cores for motion-picture and magnetic film rolls — Dimensions",
"ISO 1188:1984":"Cinematography — Recorded characteristic for magnetic sound on full-coat 16 mm motion-picture film — Specifications",
"ISO 1189:1986":"Cinematography — Recorded characteristic for magnetic sound records on 35 mm motion-picture film excluding striped release prints — Specifications",
"ISO 1223:2003":"Cinematography — Picture areas for motion-picture films for television — Position and dimensions",
"ISO 1700:1988":"Cinematography — 8 mm Type S motion-picture raw stock film — Cutting and perforating dimensions",
"ISO 1780:1984":"Cinematography — Motion-picture camera cartridge, 8 mm Type S Model I — Aperture, camera aperture profile, film position, pressure pad and pressure pad flatness — Dimensions and specifications",
"ISO 1781:1983":"Cinematography — Projector usage of 8 mm Type S motion-picture film for direct front projection",
"ISO 1785:1983":"Cinematography — Printed 8 mm, Type S, image area on 16 mm motion-picture film perforated 8 mm, Type S (1-4) — Position and dimensions",
"ISO 1787:1984":"Cinematography — Camera usage of 8 mm Type S motion-picture film — Specifications",
"ISO 1793:2005":"Cinematography — Reels for 16 mm motion-picture projectors (up to and including 610 m capacity: 38 cm size) — Dimensions",
"ISO 2404:1986":"Cinematography — Six-track magnetic sound records on 70 mm striped release prints — Locations and dimensions",
"ISO 2467:2004":"Cinematography — Image area produced by 65 mm/5 perforation motion-picture camera aperture and maximum projectable image area on 70 mm/5 perforation motion-picture prints — Positions and dimensions",
"ISO 2906:2002":"Cinematography — Image area produced by camera aperture on 35 mm motion-picture film — Position and dimensions",
"ISO 2907:2002":"Cinematography — Maximum projectable image area on 35 mm motion-picture film — Position and dimensions",
"ISO 2910:2018":"Cinematography — Screen luminance and chrominance for the projection of film motion pictures",
"ISO 2939:2015":"Cinematography — Picture image area on 35 mm motion-picture release prints — Position and dimensions and analogue and digital photographic sound to picture record displacement",
"ISO 2969:2015":"Cinematography — B-chain electro-acoustic reponse of motion-picture control rooms and indoor theatres — Specifications and measurements",
"ISO 3022:1988":"Cinematography — 35 mm motion-picture film perforated 16 mm (1-3-0) — Cutting and perforating dimensions",
"ISO 3023:1995":"Cinematography — 65 mm and 70 mm unexposed motion-picture film — Cutting and perforating dimensions",
"ISO 3024:1983":"Cinematography — Motion-picture camera cartridge, 8 mm type S, model 1 — Camera run length, perforation cut-out and end-of-run notch in film — Specifications",
"ISO 3026:1992":"Cinematography — Printed 8 mm Type S image area on 35 mm motion-picture film perforated 8 mm Type S, 2R-4.227 (1664) or 5R-4.234 (1667) — Position and dimensions",
"ISO 3042:1992":"Cinematography — Labelling of containers for raw-stock motion-picture films and magnetic films — Minimum information specifications",
"ISO 3042:1992/Cor 1:2004":"Cinematography — Labelling of containers for raw-stock motion-picture films and magnetic films — Minimum information specifications — Technical Corrigendum 1",
"ISO 3047:1982":"Cinematography — Spool, daylight loading type, for 35 mm motion-picture cameras (capacity 30 m - 100 ft) — Dimensions",
"ISO 3639:1981":"Cinematography — Projection reels/spools 75 to 312 mm diameter for 8 mm Type S motion-picture film — Dimensions and specifications",
"ISO 3641:1976":"Cinematography — Motion-picture camera cartridge, 8 mm Type S Model II — Cartridge fit and take-up core drive — Dimensions and specifications",
"ISO 3642:1983":"Cinematography — Cemented or welded splices on 8 mm Type S motion-picture film for projector use — Dimensions",
"ISO 3644:1976":"Cinematography — Spindles for 8 mm Type R motion-picture cameras and projectors — Dimensions",
"ISO 3645:1984":"Cinematography — Image area produced by 8 mm Type S motion-picture camera aperture and maximum projectable image area — Positions and dimensions",
"ISO 3646:1976":"Cinematography — Motion-picture camera cartridge, 8 mm Type S Model II — Slots, projections and cartridge hole for indicating film speed, colour balance and film identification — Dimensions and positions",
"ISO 3647:1976":"Cinematography — Spindles for 16 mm motion-picture camera spools and projector reels — Dimensions",
"ISO 3653:1978":"Cinematography — Spindles for 8 mm Type S motion-picture projector reels/spools — Dimensions",
"ISO 3773:1983":"Cinematography — Tape splices for 8 mm Type S motion-picture film for projector use — Dimensions",
"ISO 3774:1988":"Cinematography — 35 mm motion-picture film perforated 8 mm Type S (1-3-5-7-0) and (1-0) — Cutting and perforating dimensions",
"ISO 3820:1978":"Cinematography — Sprockets for 8 mm Type S motion-picture film — Dimensions and design",
"ISO 4238:1976":"Cinematography — Optical printing ratios for enlargement and reduction of motion-picture film images — Specifications",
"ISO 4241:2019":"Cinematography — Projection film leader (time-based), trailer and cue marks — Specifications",
"ISO 4242:1980":"Cinematography — Recording head gaps for two sound records on 16 mm magnetic film — Positions and width dimensions",
"ISO 4243:1979":"Cinematography — Picture image area and photographic sound record on 16 mm motion-picture release prints — Positions and dimensions",
"ISO 4246:1994":"Cinematography — Vocabulary",
"ISO 4834:1997":"Cinematography — Magnetic sound test films excluding striped release prints — Basic technical characteristics",
"ISO 5758:2002":"Cinematography — Labelling of containers for motion-picture film and magnetic material — Minimum information for exchange of materials",
"ISO 5768:1998":"Cinematography — Image produced by camera aperture Type W on 16 mm motion-picture film — Position and dimensions",
"ISO 6025:2000":"Cinematography — Analogue photographic sound test films, 35 mm and 16 mm — Specifications",
"ISO 6033:1983":"Cinematography — Projection reel size 7 for 8 mm Type S motion-picture film — Dimensions and specifications",
"ISO 6035:1983":"Cinematography — Viewing conditions for the evaluation of films and slides for television — Colours, luminances and dimensions",
"ISO 6036:1996":"Cinematography — Colour motion-picture prints and slides for television — Density specifications",
"ISO 6038:1993":"Cinematography — Splices for use on 70 mm, 65 mm, 35 mm and 16 mm motion-picture films — Dimensions and locations",
"ISO 6896:1984":"Cinematography — Intermittent sprockets for 35 mm motion-picture projectors — Dimensions",
"ISO 7343:1993":"Cinematography — Two-track photographic sound records on 35 mm motion-picture prints — Positions and width dimensions",
"ISO 7739:2016":"Cinematography — Two-track photographic analogue sound records on 16 mm motion-picture prints — Positions and width dimensions",
"ISO 7831:1986":"Cinematography — A-chain frequency response for reproduction of 35 mm photographic sound — Reproduction characteristics",
"ISO 7832:2014":"Cinematography — Photoelectric output factor of photographic-type audio-level test films — Measurement and calibration",
"ISO 8001:1984":"Cinematography — Underexposed motion-picture film requiring forced development — Designation method",
"ISO 8395:1995":"Cinematography — Test films for the reproduction of 70 mm motion-picture release prints with magnetic stripes — Specifications",
"ISO 8400:1985":"Cinematography — Position of emulsion surface of 16 mm motion-picture prints — Identification",
"ISO 8567:2002":"Cinematography — Maximum permissible area for subtitle on 35 mm and 16 mm motion-picture release prints - Position and dimensions",
"ISO 8567:2002/Cor 1:2004":"Cinematography — Maximum permissible area for subtitle on 35 mm and 16 mm motion-picture release prints - Position and dimensions — Technical Corrigendum 1",
"ISO 8590:1994":"Cinematography — Audio records on 70 mm motion-picture release prints with magnetic stripes — Recorded characteristic",
"ISO 8622:1998":"Cinematography — Magnetic sound records on 70 mm motion-picture release prints with magnetic stripes — A-chain reproduction characteristics",
"ISO 8687:1987":"Cinematography — Signal-to-noise ratio of 8 mm Type S, 16 mm and 35 mm variable-area photographic sound records — Method of measurement",
"ISO 8758:1992":"Cinematography — Photographic control and data records on 16 mm and 35 mm motion-picture film and prints — Dimensions and location",
"ISO 9525:1988":"Cinematography — Recording head gaps for two sound records on 17,5 mm magnetic film — Positions and width dimensions",
"ISO 9568:1993":"Cinematography — Background acoustic noise levels in theatres, review rooms and dubbing rooms",
"ISO 9642:2020":"Cinematography — Time and control code for 24, 25 and 30 frames per second motion-picture film systems — Specifications",
"ISO 10284:1997":"Cinematography — Graphical symbols — Description",
"ISO 10356:1996":"Cinematography — Storage and handling of nitrate-base motion-picture films",
"ISO 12222:2017":"Cinematography — Manufacturer-printed, latent image identification on 16 mm, 35 mm and 65 mm motion-picture film — Specifications and dimensions",
"ISO 12606:1997":"Cinematography — Care and preservation of magnetic audio recordings for motion pictures and television",
"ISO 12611:2004":"Cinematography — Audio head tones for use in international exchange of 35 mm analogue magnetic film masters — Specifications and location",
"ISO 12612:2016":"Cinematography — Interchange of post-production sprocket-based materials",
"ISO 17266:2018":"Cinematography — Multichannel analogue and digital photographic sound and control records on 35 mm motion-picture prints and negatives, and digital sound-control records on 70 mm motion-picture prints and negatives — Position and width dimensions",
"ISO 17332:2001":"Cinematography — Manufacturer-printed latent image identification information for 35 mm motion-picture colour-print film — Specifications",
"ISO 20859:2005":"Cinematography - Spectral response of photographic audio reproducers for analog dye sound tracks on 35 mm film",
"ISO 21727:2016":"Cinematography — Method of measurement of perceived loudness of short duration motion-picture audio material",
"ISO 22234:2005":"Cinematography — Relative and absolute sound pressure levels for motion-picture multi-channel sound systems — Measurement methods and levels applicable to analog photographic film audio, digital photographic film audio and D-cinema audio",
"ISO 26428-1:2008":"Digital cinema (D-cinema) distribution master — Part 1: Image characteristics",
"ISO 26428-2:2008":"Digital cinema (D-cinema) distribution master — Part 2: Audio characteristics",
"ISO 26428-3:2008":"Digital cinema (D-cinema) distribution master — Part 3: Audio channel mapping and channel labeling",
"ISO 26428-9:2009":"Digital cinema (D-cinema) distribution master — Part 9: Image pixel structure level 3 — Serial digital interface signal formatting",
"ISO 26428-11:2011":"Digital cinema (D-cinema) distribution master — Part 11: Additional frame rates",
"ISO 26428-19:2011":"Digital cinema (D-cinema) distribution master — Part 19: Serial digital interface signal formatting for additional frame rates level AFR2 and level AFR4",
"ISO 26429-3:2008":"Digital cinema (D-cinema) packaging — Part 3: Sound and picture track file",
"ISO 26429-4:2008":"Digital cinema (D-cinema) packaging — Part 4: MXF JPEG 2000 application",
"ISO 26429-6:2008":"Digital cinema (D-cinema) packaging — Part 6: MXF track file essence encryption",
"ISO 26429-7:2008":"Digital cinema (D-cinema) packaging — Part 7: Composition playlist",
"ISO 26429-8:2009":"Digital cinema (D-cinema) packaging — Part 8: Packing list",
"ISO 26429-9:2009":"Digital cinema (D-cinema) packaging — Part 9: Asset mapping and file segmentation",
"ISO 26429-10:2009":"Digital cinema (D-cinema) packaging — Part 10: Stereoscopic picture track file",
"ISO 26430-1:2008":"Digital cinema (D-cinema) operations — Part 1: Key delivery message",
"ISO 26430-2:2008":"Digital cinema (D-cinema) operations — Part 2: Digital certificate",
"ISO 26430-3:2008":"Digital cinema (D-cinema) operations — Part 3: Generic extra-theater message format",
"ISO 26430-4:2009":"Digital cinema (D-cinema) operations — Part 4: Log record format specification",
"ISO 26430-5:2009":"Digital cinema (D-cinema) operations — Part 5: Security log event class and constraints",
"ISO 26430-6:2009":"Digital cinema (D-cinema) operations — Part 6: Auditorium security messages for intra-theater communications",
"ISO 26430-9:2009":"Digital cinema (D-cinema) operations — Part 9: Key delivery bundle",
"ISO 26431-1:2008":"Digital cinema (D-cinema) quality — Part 1: Screen luminance level, chromaticity and uniformity",
"ISO 26432-2:2008":"Digital source processing — Part 2: Digital cinema (D-cinema) low frequency effects (LFE) channel audio characteristics",
"ISO 26433:2009":"Digital cinema (D-cinema) — XML data types"}
checkiso = "$..[?(@.group in ['iso-tc36-tc'])]"

docs = "\\src\\main\\data\\documents.json"
# isdcfdocs = "\\src\\main\\data\\isdcf.json"

#从iso114字典中pop已注册的
with open(os.path.abspath('.')+docs, encoding='utf8') as myf:
    mydata = json.load(myf)
    r = jsonpath.jsonpath(mydata, checkiso)
    for o in r:        
        if ( iso114.get(o["docLabel"])):
            iso114.pop(o["docLabel"])

#构造新的对象数组，新建
news = []
for isoid in iso114.keys():
    #加入new
    newone = {}
    newone["docId"]=isoid.replace(":","-").replace("ISO ","iso")
    newone["docLabel"]=isoid
    newone["docTitle"]=iso114[isoid]
    newone["docType"]="国际标准"
    newone["group"]="iso-tc36-tc"
    newone["href"]="https://www.iso.org"+iso114href[isoid]
    newone["publisher"]="ISO"
    newone["status"]={"active":"true"}
    news.append(newone)
print(news)

#   {
#     "docId": "iso26431-1-2008",
#     "docLabel": "ISO 26431-1:2008",
#     "docTitle": "Digital cinema (D-cinema) quality — Part 1: Screen luminance level, chromaticity and uniformity",
#     "docType": "国际标准",
#     "group": "iso-tc36-tc",
#     "href": "https://www.iso.org/standard/50207.html",
#     "keywords": [
#       "DCinema",
#       "质量",
#       "放映",
#       "测量",
#       "图像"
#     ],
#     "publicationDate": "2008-09-01",
#     "publisher": "ISO",
#     "relatedDocs": [
#       "SMPTE.ST431-1.2006"
#     ],
#     "status": {
#       "active": true
#     }
#   },

# for key in range(len(data)):
#     if jsonpath.jsonpath(data, "$["+str(key)+"].href"):
#         file = data[key]['docTitle']
#         # fn = find('*'+file+'*.pdf', '/Users/John/Library/Containers/com.kingsoft.wpsoffice.mac/Data/Library/Application Support/Kingsoft/WPS Cloud Files/userdata/qing/filecache/259626762/标准研究室/标准处文件共享/文献资料/标准电子版归档')
#         fn = find('*'+file+'*.pdf', 'I:\\WPSDrive\\259626762\\WPS网盘\\标准研究室\\标准处文件共享\\文献资料\\标准电子版归档')
#         if len(fn) > 0:
#             srcfile = fn[0]
#             objfilename = data[key]['docLabel'].replace('/', '')+' '+data[key]['docTitle']+'.pdf'
#             objfilename = objfilename.replace(' ', '_')
#             objfile = os.path.abspath('../..')+'\\filmstandards\\'+objfilename

#             copyfile(srcfile,objfile)
#             data[key]['href']='./pdf/'+objfilename
#         # for key, value in data[key].items():
#         #     print(key, value)

# with open(os.path.abspath('.')+docs, 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
# print(json.dumps(data, ensure_ascii=False))
