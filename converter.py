import requests

all_currencies_unfiltered = """ AED	United Arab Emirates Dirham
AFN	Afghan Afghani
ALL	Albanian Lek
AMD	Armenian Dram
ANG	Netherlands Antillean Guilder
AOA	Angolan Kwanza
ARS	Argentine Peso
AUD	Australian Dollar
AWG	Aruban Florin
AZN	Azerbaijani Manat
BAM	Bosnia-Herzegovina Convertible Mark
BBD	Barbadian Dollar
BDT	Bangladeshi Taka
BGN	Bulgarian Lev
BHD	Bahraini Dinar
BIF	Burundian Franc
BMD	Bermudan Dollar
BND	Brunei Dollar
BOB	Bolivian Boliviano
BRL	Brazilian Real
BSD	Bahamian Dollar
BTC	Bitcoin
BTN	Bhutanese Ngultrum
BWP	Botswanan Pula
BYR	Belarusian Ruble
BZD	Belize Dollar
CAD	Canadian Dollar
CDF	Congolese Franc
CHF	Swiss Franc
CLF	Chilean Unit of Account (UF)
CLP	Chilean Peso
CNY	Chinese Yuan
COP	Colombian Peso
CRC	Costa Rican Colón
CUC	Cuban Convertible Peso
CUP	Cuban Peso
CVE	Cape Verdean Escudo
CZK	Czech Republic Koruna
DJF	Djiboutian Franc
DKK	Danish Krone
DOP	Dominican Peso
DZD	Algerian Dinar
EGP	Egyptian Pound
ERN	Eritrean Nakfa
ETB	Ethiopian Birr
EUR	Euro
FJD	Fijian Dollar
FKP	Falkland Islands Pound
GBP	British Pound Sterling
GEL	Georgian Lari
GGP	Guernsey Pound
GHS	Ghanaian Cedi
GIP	Gibraltar Pound
GMD	Gambian Dalasi
GNF	Guinean Franc
GTQ	Guatemalan Quetzal
GYD	Guyanaese Dollar
HKD	Hong Kong Dollar
HNL	Honduran Lempira
HRK	Croatian Kuna
HTG	Haitian Gourde
HUF	Hungarian Forint
IDR	Indonesian Rupiah
ILS	Israeli New Sheqel
IMP	Manx pound
INR	Indian Rupee
IQD	Iraqi Dinar
IRR	Iranian Rial
ISK	Icelandic Króna
JEP	Jersey Pound
JMD	Jamaican Dollar
JOD	Jordanian Dinar
JPY	Japanese Yen
KES	Kenyan Shilling
KGS	Kyrgystani Som
KHR	Cambodian Riel
KMF	Comorian Franc
KPW	North Korean Won
KRW	South Korean Won
KWD	Kuwaiti Dinar
KYD	Cayman Islands Dollar
KZT	Kazakhstani Tenge
LAK	Laotian Kip
LBP	Lebanese Pound
LKR	Sri Lankan Rupee
LRD	Liberian Dollar
LSL	Lesotho Loti
LTL	Lithuanian Litas
LVL	Latvian Lats
LYD	Libyan Dinar
MAD	Moroccan Dirham
MDL	Moldovan Leu
MGA	Malagasy Ariary
MKD	Macedonian Denar
MMK	Myanma Kyat
MNT	Mongolian Tugrik
MOP	Macanese Pataca
MRO	Mauritanian Ouguiya
MUR	Mauritian Rupee
MVR	Maldivian Rufiyaa
MWK	Malawian Kwacha
MXN	Mexican Peso
MYR	Malaysian Ringgit
MZN	Mozambican Metical
NAD	Namibian Dollar
NGN	Nigerian Naira
NIO	Nicaraguan Córdoba
NOK	Norwegian Krone
NPR	Nepalese Rupee
NZD	New Zealand Dollar
OMR	Omani Rial
PAB	Panamanian Balboa
PEN	Peruvian Nuevo Sol
PGK	Papua New Guinean Kina
PHP	Philippine Peso
PKR	Pakistani Rupee
PLN	Polish Zloty
PYG	Paraguayan Guarani
QAR	Qatari Rial
RON	Romanian Leu
RSD	Serbian Dinar
RUB	Russian Ruble
RWF	Rwandan Franc
SAR	Saudi Riyal
SBD	Solomon Islands Dollar
SCR	Seychellois Rupee
SDG	Sudanese Pound
SEK	Swedish Krona
SGD	Singapore Dollar
SHP	Saint Helena Pound
SLL	Sierra Leonean Leone
SOS	Somali Shilling
SRD	Surinamese Dollar
STD	São Tomé and Príncipe Dobra
SVC	Salvadoran Colón
SYP	Syrian Pound
SZL	Swazi Lilangeni
THB	Thai Baht
TJS	Tajikistani Somoni
TMT	Turkmenistani Manat
TND	Tunisian Dinar
TOP	Tongan Paʻanga
TRY	Turkish Lira
TTD	Trinidad and Tobago Dollar
TWD	New Taiwan Dollar
TZS	Tanzanian Shilling
UAH	Ukrainian Hryvnia
UGX	Ugandan Shilling
USD	United States Dollar
UYU	Uruguayan Peso
UZS	Uzbekistan Som
VEF	Venezuelan Bolívar Fuerte
VND	Vietnamese Dong
VUV	Vanuatu Vatu
WST	Samoan Tala
XAF	CFA Franc BEAC
XAG	Silver (troy ounce)
XAU	Gold (troy ounce)
XCD	East Caribbean Dollar
XDR	Special Drawing Rights
XOF	CFA Franc BCEAO
XPF	CFP Franc
YER	Yemeni Rial
ZAR	South African Rand
ZMK	Zambian Kwacha (pre-2013)
ZMW	Zambian Kwacha
ZWL	Zimbabwean Dollar"""





class Converter():
    

    def __init__(self):

        self.all_curr = self.get_curr(all_currencies_unfiltered)

    def get_curr(self, curr):
        """Read and return all words in dictionary."""

        messy_currency_list = curr.split()
        all_curr = [c.strip() for c in messy_currency_list if c.isupper() and len(c) == 3]
        # dict_file.close()
        return all_curr
    def check_valid_currency(self, curr):
        curr = curr.upper()
        if curr in self.all_curr:
            return True
        return False
    def getData(self, base, other, amount):
        # Set API endpoint and required parameters
        endpoint = 'convert'
        access_key = '5eb1d7778541779ef8eef603af8eb38a'  
        params = {
            'access_key': access_key,
            'from': base,
            'to': other,
            'amount': amount
        }

        # Initialize and send GET request
        response = requests.get(f'http://api.exchangerate.host/{endpoint}', params=params)

        # If the response was successful, decode the JSON data
        if response.ok:
            result = response.json()
            conversion_result = result.get('result')
            
        else:
            conversion_result = -1

        return conversion_result
    
    def process_conversion(self, base, other, amount):
        if (not base or not other or not amount):
            message = 'Please enter all inputs'
            return ['err' , message]
        
        if ((not self.check_valid_currency(base)) or not self.check_valid_currency(other)):
            message = 'One of your requested currencies are not supported'
            return ['err', message]


            
        try:
            float(amount)
            amount = float(amount)
            if amount < 0:
                message = 'The amount is not valid'
                return ['err', message]
        except ValueError:
            message = 'The amount is not valid'
            return ['err', message]
        
        result = self.getData(base = base, other = other, amount = amount)

        return ['ok', result]




    





    
