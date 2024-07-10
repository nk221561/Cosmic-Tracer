

def search_constellation_by_name(query):
    
    if query.lower() == 'orion':
        return {
            'name': 'Orion',
            'description': 'Orion is a prominent constellation located on the celestial equator...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\orion.jpg"  
        }
    elif query.lower() == 'aquarius':
        return {
            'name': 'Aquarius',
            'description': 'Aquarius is a constellation of the zodiac, situated between Capricornus and Pisces...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\aquarius.jpg"  
        }
    elif query.lower() == 'ursa major':
        return {
            'name': 'Ursa Major',
            'description': 'Ursa Major is a prominent northern constellation, known for containing the Big Dipper...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\ursa_major.jpg"  
        }
    elif query.lower() == 'leo':
        return {
            'name': 'Leo',
            'description': 'Leo is one of the constellations of the zodiac, lying between Cancer to the west and Virgo to the east...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\leo.jpg"  
        }
    elif query.lower() == 'gemini':
        return {
            'name': 'Gemini',
            'description': 'Gemini is one of the constellations of the zodiac, lying between Taurus to the west and Cancer to the east...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\gemini.jpg"  
        }
    elif query.lower() == 'scorpius':
        return {
            'name': 'Scorpius',
            'description': 'Scorpius is one of the constellations of the zodiac, lying between Libra to the west and Sagittarius to the east...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\scorpio.jpg" 
        }
    elif query.lower() == 'taurus':
        return {
            'name': 'Taurus',
            'description': 'Taurus is one of the constellations of the zodiac, situated immediately north of the celestial equator...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\taurus.jpg"  
        }
    elif query.lower() == 'virgo':
        return {
            'name': 'Virgo',
            'description': 'Virgo is one of the constellations of the zodiac, lying between Leo to the west and Libra to the east...',
            'image_url': "D:\\cosmicTracerBackend\\templates\\virgo.jpg"  
        }
    else:
        return None
