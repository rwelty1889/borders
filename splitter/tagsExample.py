
import tags

def setupTranslations():

    t = [ tags.tagTranslation( "NAME", None, "rename-key", "name", None), \

#          00 is supposed to be nation, but in the files it's state
#          tags.tagTranslation( "LSAD", "00", "new-kv", "boundary", "administrative"), \
#          tags.tagTranslation( "LSAD", "00", "new-kv", "admin_level", "2"), \
#          tags.tagTranslation( "LSAD", "00", "new-kv", "place", "country"), \
#          tags.tagTranslation( "LSAD", "00", "delete-kv", None, None), \

          # should be 01, is 00
          tags.tagTranslation( "LSAD", "00", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "00", "new-kv", "admin_level", "4"), \
          tags.tagTranslation( "LSAD", "00", "new-kv", "place", "state"), \
          tags.tagTranslation( "LSAD", "00", "delete-kv", None, None), \

          # 03 is "City and Borough" in Alaska
          tags.tagTranslation( "LSAD", "03", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "03", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "03", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "03", "delete-kv", None, None), \

          # 05 is "Census Area" in Alaska
          tags.tagTranslation( "LSAD", "05", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "05", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "05", "delete-kv", None, None), \

          # 06 is County in 48 states
          tags.tagTranslation( "LSAD", "06", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "06", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "06", "new-kv", "place", "county"), \
          tags.tagTranslation( "LSAD", "06", "delete-kv", None, None), \

          # 07 is District in Amerian Samoa (county equiv)
          tags.tagTranslation( "LSAD", "07", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "07", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "07", "new-kv", "place", "district"), \
          tags.tagTranslation( "LSAD", "07", "delete-kv", None, None), \

          # 08 is Independent City in MD, MO, and VA
          tags.tagTranslation( "LSAD", "08", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "08", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "08", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "08", "delete-kv", None, None), \

          # 09 is Independent City in NV
          tags.tagTranslation( "LSAD", "09", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "09", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "09", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "09", "delete-kv", None, None), \

          # 10 is Island, county equiv in Virgin Islands
          tags.tagTranslation( "LSAD", "10", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "10", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "10", "new-kv", "place", "island"), \
          tags.tagTranslation( "LSAD", "10", "delete-kv", None, None), \

          # 11 is Island, county equiv in American Samoa
          tags.tagTranslation( "LSAD", "11", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "11", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "11", "new-kv", "place", "island"), \
          tags.tagTranslation( "LSAD", "11", "delete-kv", None, None), \

          # 13 is Municipality,  county equiv in Alaska and Northern Mariana Islands
          tags.tagTranslation( "LSAD", "12", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "12", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "12", "new-kv", "place", "municipality"), \
          tags.tagTranslation( "LSAD", "12", "delete-kv", None, None), \

          # 13 is Municipio, county equiv in Puerto Rico
          tags.tagTranslation( "LSAD", "13", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "13", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "13", "new-kv", "place", "municipio"), \
          tags.tagTranslation( "LSAD", "13", "delete-kv", None, None), \

          # 14 county equiv in DC and Guam
          tags.tagTranslation( "LSAD", "14", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "14", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "14", "new-kv", "place", "county"), \
          tags.tagTranslation( "LSAD", "14", "delete-kv", None, None), \

          # 15 Parish,  county equiv in LA
          tags.tagTranslation( "LSAD", "15", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "15", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "15", "new-kv", "place", "parish"), \
          tags.tagTranslation( "LSAD", "15", "delete-kv", None, None), \

          # 19 reservation in Maine, NY, broken down as a county subdivision
          tags.tagTranslation( "LSAD", "19", "new-kv", "boundary", "aboriginal_lands"), \
          tags.tagTranslation( "LSAD", "19", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "19", "new-kv", "place", "reservation"), \
          tags.tagTranslation( "LSAD", "19", "delete-kv", None, None), \

          # 20 barrio in Puerto Rico
          tags.tagTranslation( "LSAD", "20", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "20", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "20", "new-kv", "place", "barrio"), \
          tags.tagTranslation( "LSAD", "20", "delete-kv", None, None), \

          # 21 borough county subdivision in PA, NJ, "special" in NYC
          tags.tagTranslation( "LSAD", "21", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "21", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "21", "new-kv", "place", "borough"), \
          tags.tagTranslation( "LSAD", "21", "delete-kv", None, None), \

          # 22 Census County Division (CCD), statistical
          tags.tagTranslation( "LSAD", "22", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "22", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "22", "delete-kv", None, None), \

          # 23 census subarea, statistical, alaska
          tags.tagTranslation( "LSAD", "23", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "23", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "23", "delete-kv", None, None), \

          # 24 subdistrict, US VI
          tags.tagTranslation( "LSAD", "24", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "24", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "24", "delete-kv", None, None), \

          # 25 City, 20 states, DC
          tags.tagTranslation( "LSAD", "25", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "25", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "25", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "25", "delete-kv", None, None), \

          # 26 county, American Samoa
          tags.tagTranslation( "LSAD", "26", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "26", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "26", "new-kv", "place", "county"), \
          tags.tagTranslation( "LSAD", "26", "delete-kv", None, None), \

          # 27 district, PA, VA, WV, Guam & Marianas
          tags.tagTranslation( "LSAD", "27", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "27", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "27", "new-kv", "place", "district"), \
          tags.tagTranslation( "LSAD", "27", "delete-kv", None, None), \

          # 28 district, LA, MD, MI, VA, WV, Marianas
          tags.tagTranslation( "LSAD", "28", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "28", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "28", "new-kv", "place", "district"), \
          tags.tagTranslation( "LSAD", "28", "delete-kv", None, None), \

          # 29 precinct, IL, NB
          tags.tagTranslation( "LSAD", "29", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "29", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "29", "new-kv", "place", "precinct"), \
          tags.tagTranslation( "LSAD", "29", "delete-kv", None, None), \

          # 30 precinct, IL, NB
          tags.tagTranslation( "LSAD", "30", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "30", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "30", "new-kv", "place", "precinct"), \
          tags.tagTranslation( "LSAD", "30", "delete-kv", None, None), \

          # 31 gore Maine, Vermont
          tags.tagTranslation( "LSAD", "31", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "31", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "31", "new-kv", "place", "gore"), \
          tags.tagTranslation( "LSAD", "31", "delete-kv", None, None), \

          # 32 grant NH, VT
          tags.tagTranslation( "LSAD", "32", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "32", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "32", "new-kv", "place", "grant"), \
          tags.tagTranslation( "LSAD", "32", "delete-kv", None, None), \

          # 33 independent city, MD, MO, VA
          tags.tagTranslation( "LSAD", "33", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "33", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "33", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "33", "delete-kv", None, None), \

          # 34 independent city, NV
          tags.tagTranslation( "LSAD", "34", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "34", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "34", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "34", "delete-kv", None, None), \

          # 35 island American Samoa
          tags.tagTranslation( "LSAD", "35", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "35", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "35", "new-kv", "place", "island"), \
          tags.tagTranslation( "LSAD", "35", "delete-kv", None, None), \

          # 36 location, New Hampshire
          tags.tagTranslation( "LSAD", "36", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "36", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "36", "new-kv", "place", "location"), \
          tags.tagTranslation( "LSAD", "36", "delete-kv", None, None), \

          # 38 county subdivision Arlington County VA
          tags.tagTranslation( "LSAD", "37", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "37", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "37", "delete-kv", None, None), \

          # 39 plantation, Maine
          tags.tagTranslation( "LSAD", "39", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "39", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "39", "new-kv", "place", "plantation"), \
          tags.tagTranslation( "LSAD", "39", "delete-kv", None, None), \

          # 40 undefined legal county subdivsion, water, 14 states, PR & US VI
          tags.tagTranslation( "LSAD", "40", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "40", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "40", "delete-kv", None, None), \

          # 41 barrio-pueblo
          tags.tagTranslation( "LSAD", "41", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "41", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "41", "new-kv", "place", "barrio-pueblo"), \
          tags.tagTranslation( "LSAD", "41", "delete-kv", None, None), \

          # 42 purchase NY
          tags.tagTranslation( "LSAD", "42", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "42", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "42", "new-kv", "place", "purchase"), \
          tags.tagTranslation( "LSAD", "42", "delete-kv", None, None), \

          # 43 town 8 states, + NJ, NC, PA, SD
          tags.tagTranslation( "LSAD", "43", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "43", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "43", "new-kv", "place", "town"), \
          tags.tagTranslation( "LSAD", "43", "delete-kv", None, None), \

          # 44 township 16 states
          tags.tagTranslation( "LSAD", "44", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "44", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "44", "new-kv", "place", "township"), \
          tags.tagTranslation( "LSAD", "44", "delete-kv", None, None), \

          # 45 township KS, MN, NB, NC
          tags.tagTranslation( "LSAD", "45", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "45", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "45", "new-kv", "place", "township"), \
          tags.tagTranslation( "LSAD", "45", "delete-kv", None, None), \

          # 46 UT - statistical, 10 states
          tags.tagTranslation( "LSAD", "46", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "46", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "46", "delete-kv", None, None), \

          # 47 village NJ, OH, SD, WI
          tags.tagTranslation( "LSAD", "47", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "47", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "47", "new-kv", "place", "village"), \
          tags.tagTranslation( "LSAD", "47", "delete-kv", None, None), \

          # 49 charter township, MI
          tags.tagTranslation( "LSAD", "49", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "49", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "49", "new-kv", "place", "township"), \
          tags.tagTranslation( "LSAD", "49", "delete-kv", None, None), \

          # 51 subbarrio, Puerto Rico
          tags.tagTranslation( "LSAD", "51", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "51", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "51", "new-kv", "place", "subbarrio"), \
          tags.tagTranslation( "LSAD", "51", "delete-kv", None, None), \

          # 53 city and borough, Alaska (place value is a guess)
          tags.tagTranslation( "LSAD", "53", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "53", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "53", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "53", "delete-kv", None, None), \

          # 54 municipality, Alaska
          tags.tagTranslation( "LSAD", "54", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "54", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "54", "new-kv", "place", "municipality"), \
          tags.tagTranslation( "LSAD", "54", "delete-kv", None, None), \

          # 55 comunidad, Puerto Rico, statistical admin level a guess
          tags.tagTranslation( "LSAD", "55", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "55", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "55", "delete-kv", None, None), \

          # 56 borough, CT, NJ, PA (guess at admin level)
          tags.tagTranslation( "LSAD", "56", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "56", "new-kv", "admin_level", "7"), \
           tags.tagTranslation( "LSAD", "56", "new-kv", "place", "borough"), \
          tags.tagTranslation( "LSAD", "56", "delete-kv", None, None), \

          # 57 CDP - statistical boundary for hamlets, etc
          tags.tagTranslation( "LSAD", "57", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "57", "new-kv", "place", "cdp"), \
          tags.tagTranslation( "LSAD", "57", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "57", "delete-kv", None, None), \

          # 58 city - 49 states, DC
          tags.tagTranslation( "LSAD", "58", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "58", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "58", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "58", "delete-kv", None, None), \

          # 59 incorporated place, KY, MT, NV, TN, quasi-legal, CT, GA, IN, MT, TN
          tags.tagTranslation( "LSAD", "59", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "59", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "59", "delete-kv", None, None), \

          # 60 town - 30 states, US VI
          tags.tagTranslation( "LSAD", "60", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "60", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "60", "new-kv", "place", "town"), \
          tags.tagTranslation( "LSAD", "60", "delete-kv", None, None), \

          # 61 village - 20 states, American Samoa
          tags.tagTranslation( "LSAD", "61", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "61", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "61", "new-kv", "place", "village"), \
          tags.tagTranslation( "LSAD", "61", "delete-kv", None, None), \

          # 62 zona urbana - statistical place Puerto Rico
          tags.tagTranslation( "LSAD", "62", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "62", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "62", "delete-kv", None, None), \

          # 65 consolidated city - CT, GA, IN (admin level 6 or 8?)
          tags.tagTranslation( "LSAD", "65", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "65", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "65", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "65", "delete-kv", None, None), \

          # 66 consolidated city - GA, MT, TN (admin level 6 or 8?)
          tags.tagTranslation( "LSAD", "66", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "66", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "66", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "66", "delete-kv", None, None), \

          tags.tagTranslation( "AWATER", None, "delete-kv", None, None), \
#          tags.tagTranslation( "AWATER", None, "rename-key", "tiger:AWATER", None)
          tags.tagTranslation( "ALAND", None, "delete-kv", None, None), \
          tags.tagTranslation( "PCICBSA", None, "delete-kv", None, None), \
          tags.tagTranslation( "PCINECTA", None, "delete-kv", None, None), \
          tags.tagTranslation( "INTPTLAT", None, "delete-kv", None, None), \
          tags.tagTranslation( "INTPTLON", None, "delete-kv", None, None), \
          tags.tagTranslation( "PLACENS", None, "delete-kv", None, None), \
          tags.tagTranslation( "PLACEFP", None, "delete-kv", None, None), \
          tags.tagTranslation( "CLASSFP", None, "delete-kv", None, None), \
          tags.tagTranslation( "GEOID", None, "delete-kv", None, None), \
          tags.tagTranslation( "FUNCSTAT", None, "delete-kv", None, None), \
          tags.tagTranslation( "MTFCC", None, "delete-kv", None, None), \
          tags.tagTranslation( "NAMELSAD", None, "delete-kv", None, None), \
          tags.tagTranslation( "STATEFP", None, "rename-key", "tiger:STATEFP", None)

          ]

    return t
