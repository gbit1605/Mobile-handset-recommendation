from flask import jsonify, request
from flask import Flask, render_template
from amazon import send

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_node_ui():
    return render_template('amazon_phones.html')

@app.route('/process', methods=['POST'])

def process():
    name = request.form['name1']
    #dist=request.form['dist']
    
    value=send(name)
    
    name1="Recommendation 1: "+str(value[0][0])+"  "+"Distance: "+str(value[0][2])
    name2="Recommendation 2: "+str(value[1][0])+"  "+"Distance: "+str(value[1][2])
    name3="Recommendation 3: "+str(value[2][0])+"  "+"Distance: "+str(value[2][2])
    name4="Recommendation 4: "+str(value[3][0])+"  "+"Distance: "+str(value[3][2])
    name5="Recommendation 5: "+str(value[4][0])+"  "+"Distance: "+str(value[4][2])
    
    return jsonify({'name1': name1, 'name2': name2, 'name3': name3, 'name4': name4, 'name5': name5})
    #return jsonify({'error' : 'Missing data!'})

if __name__=='__main__':    
    app.run(host='127.0.0.1', port=5000)
    
'''
            <li> Amazon Renewed </li>
            <li> 4D </li>
            <li> Adoniz </li>
            <li> AGARO </li>
            <li> AT and T </li>
            <li> Aeidess </li>
            <li> Alfa </li>
            <li> Amazon Brand - Solimo </li>
            <li> AmazonBasics </li>
            <li> Amegon </li>
            <li> Amkette </li>
            <li> Amzer </li>
            <li> Anker </li>
            <li> Anselmo Global </li>
            <li> Ant Audio </li>
            <li> AOW ATTRACTIVE OFFER WORLD </li>
            <li> Aqua </li>
            <li> Artis </li>
            <li> B.R Telecome </li>
            <li> Beetel </li> 
            <li> Blackbear </li>
            <li> Bainsh </li>
            <li> BAINSH </li>
            <li> Baseus </li>
            <li> Belkin </li>
            <li> BestTalk </li>
            <li> Bhulli </li>
            <li> Binatone </li>
            <li> BlackBerry </li>
            <li> Blaupunkt </li>
            <li> Bliss </li>
            <li> Boat </li>
            <li> Bose </li>
            <li> Boult Audio </li>
            <li> BOUNCEBACK </li>
            <li> Bracevor </li>
            <li> Buddy </li>
            <li> CAT </li>
            <li> CELLBELL </li>
            <li> COOL BUDDYZZ </li>
            <li> captcha </li>
            <li> CUBETEK </li>
            <li> Campro </li>
            <li> Canon </li>
            <li> CEDO </li>
            <li> Celkon </li>
            <li> CHILLI </li>
            <li> CIRCLE </li>
            <li> Classico </li>
            <li> Coolpad </li>
            <li> Corsair </li>
            <li> Cosmic Byte </li>
            <li> D3D </li>
            <li> DMG </li>
            <li> DOMO </li>
            <li> DEBOCK </li>
            <li> Dell </li>
            <li> DESIGNERZ HUB </li>
            <li> Die Hard </li>
            <li> Digitek </li>
            <li> DokFin </li>
            <li> EDNA </li>
            <li> Elv </li>
            <li> ENEM </li>
            <li> ENEM </li>
            <li> Eaanu </li>
            <li> elove </li>
            <li> Enviro Chip </li>
            <li> Equinox </li>
            <li> Unknown </li>
            <li> FREESOLO </li>
            <li> Fashionury </li>
            <li> Febelo </li>
            <li> FiiO </li>
            <li> FIRST MART - A BRAND WORTH REMEMBERING </li>
            <li> Flybot </li>
            <li> FORME </li>
            <li> FORTIFY </li>
            <li> Fotopro </li>
            <li> FYUGO </li>
            <li> G'Five </li>
            <li> GADGETS WRAP </li>
            <li> GIGASMART </li>
            <li> GLOVER </li>
            <li> Gadget365 </li>
            <li> Garmin </li>
            <li> Gear </li>
            <li> Geeky </li>
            <li> Gigaset </li>
            <li> Gionee </li>
            <li> GIZGA essentials </li>
            <li> Golden Sand </li>
            <li> Grandstream </li>
            <li> GreenBerry </li>
            <li> HAMSA </li>
            <li> HOMTOM </li>
            <li> HP </li>
            <li> HTC </li>
            <li> HUMBLE </li>
            <li> Haau </li>
            <li> Generic </li>
            <li> Hikvision </li>
            <li> Honor </li>
            <li> Huawei </li>
            <li> Anonymous </li>
            <li> HyperX </li>
            <li> IKALL </li>
            <li> INDeSHOP </li>	
            <li> Intex </li>
            <li> InFocus </li>
            <li> Ionix </li>
            <li> JBL </li>
            <li> JSTBY LABEL </li>
            <li> Jabra </li>
            <li> Jicson </li>
            <li> Jivi </li>
            <li> KAPILTRADERS </li>
            <li> KE SWADHIN </li>
            <li> KECHAODA </li>
            <li> Karbonn </li>
            <li> Kingston </li>
            <li> koveru </li>
            <li> KrishnaMart </li>
            <li> LEXTAR </li>
            <li> LG </li>
            <li> LYF </li>
            <li> Lava </li>
            <li> Leaf </li>
            <li> Lenovo </li>
            <li> Lewano </li>
            <li> Logitech </li>
            <li> MD ORIGINAL </li>
            <li> Mi </li>
            <li> MM Brand </li>
            <li> MOBICLONICS </li>
            <li> Manya Impex </li>
            <li> marklif </li>
            <li> Marshall </li>
            <li> Mcart </li>
            <li> Meya Happy </li>
            <li> Micromax </li>
            <li> Microsoft </li>
            <li> Mivi </li>
            <li> mobicell </li>
            <li> MOBIFUSE </li>
            <li> Mobiistar </li>
            <li> Mobistone </li>
            <li> mobistyle </li>
            <li> Molife </li>
            <li> MoohMaya </li>
            <li> Moto </li>
            <li> Motorola </li>
            <li> Muphone </li>
            <li> Muzili </li>
            <li> NAVSWA </li>
            <li> NK choudhary </li>
            <li> NOYMI </li>
            <li> Nuvo </li>
            <li> Nik case </li>
            <li> Nillkin </li>                              
            <li> Noise </li>
            <li> Nokia </li>
            <li> Nu Republic </li>
            <li> Oppo </li>
            <li> ORC </li>
            <li> OSVETA </li>
            <li> OnePlus </li>
            <li> Orientel </li>
            <li> PES </li>
            <li> PICKNGRAB </li>
            <li> Panasonic </li>
            <li> PaxMore </li>
            <li> Peace </li>
            <li> Philips </li>
            <li> Photron </li>
            <li> Pirum </li>
            <li> Polycom </li>
            <li> PopSockets </li>
            <li> Portronics </li>
            <li> Poya </li>
            <li> Premsons </li>
            <li> Prime Retail </li>
            <li> PrintVisa </li>
            <li> Quantum </li>
            <li> QuantumZERO </li>
            <li> REALCASE </li>
            <li> REALIKE </li>
            <li> RIVOXX </li>
            <li> Rnaux </li>
            <li> RPM Euro Games </li>
            <li> realme </li>
            <li> Redgear </li>
            <li> Redmi </li>
            <li> Rhythm and Blues </li>
            <li> RidivishN </li>
            <li> Rock </li>
            <li> Romeo</li>
            <li> ROVKING </li>
            <li> SAFESEED </li>
            <li> SAIELLIN </li>
            <li> SBA999 </li>
            <li> SENIOR WORLD </li>
            <li> SHINETEL </li>
            <li> SPAZY CASE </li>
            <li> SUPCASE </li>
            <li> Samsung </li>
            <li> SanDisk </li>
            <li> Scotch-Brite </li>
            <li> Sennheiser </li>
            <li> Shivansh </li>
            <li> Shoponclick </li>
            <li> Sirius </li>
            <li> Skullcandy </li>
            <li> SmartLike </li>
            <li> Smartron </li>
            <li> Sonics </li>
            <li> Sony </li>
            <li> Sound Boss </li>
            <li> stealkart </li>
            <li> STRAUSS </li>
            <li> Strontium </li>
            <li> Stuffcool </li>
            <li> Surya </li>
            <li> Swipe </li>
            <li> SYSKA </li>
            <li> TECHPOOL </li>
            <li> Tenda </li>
            <li> TP-Link </li>
            <li> Targus </li>
            <li> TecKraft </li>
            <li> Tecno </li>
            <li> Tewtross </li>
            <li> The Logo Man </li>
            <li> TheGiftKart </li>
            <li> Thinkzy </li>
            <li> Tip 'n' Top </li>
            <li> tizum </li>
            <li> Toykart </li>
            <li> Trifty </li>
            <li> Ultimate </li>
            <li> UBON </li>
            <li> Uni4 </li>
            <li> Bulfyss </li>
            <li> Urban Armor Gear </li>
            
<div id="name1_alert" class="alert1" role="alert" style="display:none;"></div>
			<div id="name2_alert" class="alert1" role="alert" style="display:none;"></div>
			<div id="name3_alert" class="alert1" role="alert" style="display:none;"></div>
			<div id="name4_alert" class="alert1" role="alert" style="display:none;"></div>
			<div id="name5_alert" class="alert1" role="alert" style="display:none;"></div>
            
'''