
from types import MemberDescriptorType


crews = {
    "REALTA": "Go get a bigger ship",
    "CORVETTE": "Go get a bigger ship",
    "FORTUNATE": "Go get a bigger ship",
    "PHINDRA": "Go get a bigger ship",
    "TURAS": "Go get a bigger ship",
    "JELLYFISH": "Go get a bigger ship",
    "TALLA": "Go get a bigger ship",
    "ENVOY": "Go get a bigger ship",
    "FRANKLIN": "Swarms: Pike (Cap) Moreau Tlaan || Picard (Cap) Beverley Tlaan || 5/10 (Cap) 7/10 8/10",
    "BOTANY-BAY": "Data-mining: Any officer (Cap), Joaquin, Any officer",
    "KHERA": "Go get a bigger ship",
    "VAHKLAS": "Go get a bigger ship",
    "KUMARI": "Go get a bigger ship",
    "NORTHSTAR": "Go get a bigger ship",
    "DVOR": "Latinum mining: Joaquin(Cap), TPring, 1/10",
    "DISCOVERY": "Paul Stamets(Cap) Culber Saru for jumping/summoning",
    "MERIDIAN": "Ariam (Cap) + 2 Synergy",
    "VIDAR": "Probes 29 and smaller ==> 7/10 (Cap), 8/10, 9/10 || Probes 29-32 ==> Pike (Cap) Moreau Tlaan || Probes 33 ==> 5/10 Chen Tlaan",
    "HORIZON": "Mining Crew. Type '!crew mining' for more info",
    "STELLA": "Riker(Cap) Kirk Spock or Kirk (Cap) Spock Khan for Armadas. PMC for farming codes",
    "FRANKLIN-A": "Same as Franklin (!crew Franklin)",
    "SARCOPHAGUS": "Gorkon (Cap) Kerla Khan",
    "SARKOPHAG": "Gorkon (Cap) Kerla Khan",
    "D3": "Gorkon (cap) Kerla Khan || Kirk (Cap) Spock + (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "BORTAS": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "BREL": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "D4": "Lorca (Cap) Tilly Khan || Gorkon Kerla Khan || Worf Kerla Khan. Dailies: !crew dailies",
    "KVORT": "Mining crew. Type '!crew minnig' for more info",
    "MAYFLOWER": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "SALADIN": "Bones (Cap) Kirk Spock || Yuki(Cap) Khan (Marcus/Chavernek/Kang) || Kuron(Cap) Harrison Khan. Dailies: !crew dailies",
    "INTREPID": "Bones (Cap) Kirk Spock || Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "ENTERPRISE": "5/10 (Cap) Kirk Khan || Gorkon(Cap) Kirk Khan || TOS Kirk (Cap) TOS Mccoy TOS Uhura || Yuki(Cap) Khan (Marcus/Chavernek/Kang)",
    "LEGIONARY": "To be done",
    "CENTURION": "Bones (Cap) Kirk Spock || Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "GLADIUS":  "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "AUGUR": "Georgio (Cap) D‘Jaoki Tyler || Kumak (Cap) Nero Livis. Dailies: !crew dailies",
    "ANTARES": "Mining crew. Type '!crew mining' for more info",
    "ISSJELLY": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "KELVIN":"Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "NEWTON": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "ENTERPRISE-A":"5/10 (Cap) Kirk Khan || Gorkon (Cap) Kirk Khan || TOS-Kirk (Cap) TOS-Uhura TOS-Mccoy",
    "VALDORE":"Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "PILUM": "Yuki (Cap) + Marcus/Chavernek/Kang + 1 anti-faction. || Kuron Harrison Kang Dailies: !crew dailies",
    "TRIBUNE": "Georgio (Cap) D'Jaoki Tyler",
    "KTINGA": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "KORINAR": "Yuki(Cap) Khan (Marcus/Chavernek/Kang). Dailies: !crew dailies",
    "HEGHTA": "Gorkon (Cap) Kerla Khan || Lorca (Cap) Tilly Khan || Azebtur (Cap) Gorkon Khan",
    "VORTA": "Basic mining crew. Officers like 10/10 Ston, Tpring, Barot. If you use it as fighter you are probably drunk",
    "DAILIES": "Pike (Cap) Moreau Chen against Explorers/Battleships. Pike Moreau Tlaan against Interceptors. (Pike and Moreau can be switched with Picard and Beverley)"
}

helps = {
    "JOKE": "Returns a random joke",
    "WITZ": "Gibt einen zufälligen Witz",
    "CHUCK": "Wie !witz für chuck norris Witze",
    "DAILY": "Gibt die nächsten Dailies aus. TBD",
    "TAKEOVER": "Gibt Infos über anstehende GÜS aus. // Gives information about upcoming defenses",
    "PIZZA": "PIZAAAAA",
    "MOTIVATE": "Nimmt einen Namen und motiviert // Takes a name and motivates. --> !motivate Karl --> go go go Karl",
    "DISCORD": "Gibt den Link zu unserem Discord aus. // Gives the link to our discord server.",
    "WEATHER": "Nimmt einen Standort und gibt das Wetter zurück. Takes a location and returns the weather. --> !weather London",
    "WETTER": "Nimmt einen Standort und gibt das Wetter zurück. Takes a location and returns the weather. --> !wetter Wien",
    "KACKNOOBS": "KACKNOOBS",
    "CREW": "Nimmt ein Schiff und gibt Vorschläge. Takes a ship and makes suggestions. --> !crew discovery"
}

scaps = {
    "D3": ["Tritanium: 36,3 Mio. || Dilithium: 1,4 Mio. || EP: 51.234 || 4*Teile grau: 105.000 || 4*Teile grün: 7.842 ||", "Gas 4* grau: 27.444 || Gas 4* grün: 1.556 || Gas 4* blau: 244", "Kristall 4* grau: 50.968 || Kristall 4* grün: 2.889 || Kristall 4* blau: 454"],
    "LEGIONARY": ["Tritanium: 52,6 Mio. || Dilithium: 3,45 Mio. || EP: 51.234 || 4*Teile grau: 107.000 || 4*Teile grün: 8.044 ||", "Erz 4* grau: 52.316 || Erz 4* grün: 2.965 || Erz 4* blau: 466", "Kristall 4* grau: 28.171 || Kristall 4* grün: 1.597 || Kristall 4* blau: 251"],
    "MAYFLOWER": ["Tritanium: 30,1 Mio. || Dilithium: 3,73 Mio. || EP: 51.234 || 4*Teile grau: 111.000 || 4*Teile grün: 8.362 ||", "Erz 4* grau: 29.416 || Erz 4* grün: 1.667 || Erz 4* blau: 262", "Gas 4* grau: 54.630 || Gas 4* grün: 3.096 || Gas 4* blau: 486"]
}

shipids = {
    "FRANKLIN": "644714972",
    "BOTANY-BAY": "1087128295",
    "KHERA": "393740394",
    "VAHKLAS": "3033866568",
    "KUMARI": "3005922948",
    "NORTHSTAR": "1029262994",
    "DVOR": "1784814733",
    "DISCOVERY": "1307832955",
    "MERIDIAN": "1878809713",
    "VIDAR": "2529591723",
    "HORIZON": "3046584086",
    "STELLA": "293385368",
    "FRANKLIN-A": "2016654425",
    "SARCOPHAGUS": "593579233",
    "SARKOPHAG": "593579233",
    "D3": "2704762692",
    "BORTAS": "2004925834",
    "BREL": "2441576367",
    "D4": "957865248",
    "KVORT": "2869476908",
    "MAYFLOWER": "1220133742",
    "SALADIN": "3056258007",
    "INTREPID": "1463338054",
    "ENTERPRISE": "2483093372",
    "LEGIONARY": "3554487827",
    "CENTURION": "673187302",
    "GLADIUS":  "2165876444",
    "AUGUR": "3459465041",
    "VALKIS": "1535317053",
    "ANTARES": "108924704",
    "ISSJELLY": "1628890938",
    "PILUM": "2254702328",
    "KTINGA": "1244824002",
    "KORINAR": "3665388873",
    "VALDORE": "1027217748",
    "KELVIN": "711428193",
}

def get_Crews():
    return crews
def get_Helps():
    return helps
def get_Scraps():
    return scaps

def get_Link(t, t1, name):
    id = shipids[name.upper()]
    message = "https://stfc.space/ships/"+id+"?tier="+t+"&scrap_level=45&ci=0&tiers=@:1%26:" + t1+"&c=$description:true&component_stats=1&t_r=1"
    return message
