
import tags

def setupTranslations():

    t = [ tags.tagTranslation( "NAME", None, "rename-key", "name", None), \

#          00 is supposed to be nation, but in the files it's state
#          tags.tagTranslation( "LSAD", "00", "new-kv", "boundary", "administrative"), \
#          tags.tagTranslation( "LSAD", "00", "new-kv", "admin_level", "2"), \
#          tags.tagTranslation( "LSAD", "00", "new-kv", "place", "country"), \

          # should be 01, is 00
          tags.tagTranslation( "LSAD", "00", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "00", "new-kv", "admin_level", "4"), \
          tags.tagTranslation( "LSAD", "00", "new-kv", "place", "state"), \

          # 03 is "City and Borough" in Alaska
          tags.tagTranslation( "LSAD", "03", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "03", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "03", "new-kv", "place", "city"), \

          # 05 is "Census Area" in Alaska
          tags.tagTranslation( "LSAD", "05", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "05", "new-kv", "admin_level", "6"), \

          # 06 is County in 48 states
          tags.tagTranslation( "LSAD", "06", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "06", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "06", "new-kv", "place", "county"), \

          # 07 is District in Amerian Samoa (county equiv)
          tags.tagTranslation( "LSAD", "07", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "07", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "07", "new-kv", "place", "district"), \

          # 08 is Independent City in MD, MO, and VA
          tags.tagTranslation( "LSAD", "08", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "08", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "08", "new-kv", "place", "city"), \

          # 09 is Independent City in NV
          tags.tagTranslation( "LSAD", "09", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "09", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "09", "new-kv", "place", "city"), \

          # 10 is Island, county equiv in Virgin Islands
          tags.tagTranslation( "LSAD", "10", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "10", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "10", "new-kv", "place", "island"), \

          # 11 is Island, county equiv in American Samoa
          tags.tagTranslation( "LSAD", "11", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "11", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "11", "new-kv", "place", "island"), \

          # 13 is Municipality,  county equiv in Alaska and Northern Mariana Islands
          tags.tagTranslation( "LSAD", "12", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "12", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "12", "new-kv", "place", "municipality"), \

          # 13 is Municipio, county equiv in Puerto Rico
          tags.tagTranslation( "LSAD", "13", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "13", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "13", "new-kv", "place", "municipio"), \

          # 14 county equiv in DC and Guam
          tags.tagTranslation( "LSAD", "14", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "14", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "14", "new-kv", "place", "county"), \

          # 15 Parish,  county equiv in LA
          tags.tagTranslation( "LSAD", "15", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "15", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "15", "new-kv", "place", "parish"), \

          # 19 reservation in Maine, NY, broken down as a county subdivision
          tags.tagTranslation( "LSAD", "19", "new-kv", "boundary", "aboriginal_lands"), \
          tags.tagTranslation( "LSAD", "19", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "19", "new-kv", "place", "reservation"), \

          # 20 barrio in Puerto Rico
          tags.tagTranslation( "LSAD", "20", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "20", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "20", "new-kv", "place", "barrio"), \

          # 21 borough county subdivision in PA, NJ, "special" in NYC
          tags.tagTranslation( "LSAD", "21", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "21", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "21", "new-kv", "place", "borough"), \

          # 22 Census County Division (CCD), statistical
          tags.tagTranslation( "LSAD", "22", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "22", "new-kv", "admin_level", "7"), \

          # 23 census subarea, statistical, alaska
          tags.tagTranslation( "LSAD", "23", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "23", "new-kv", "admin_level", "7"), \

          # 24 subdistrict, US VI
          tags.tagTranslation( "LSAD", "24", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "24", "new-kv", "admin_level", "7"), \

          # 25 City, 20 states, DC
          tags.tagTranslation( "LSAD", "25", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "25", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "25", "new-kv", "place", "city"), \

          # 26 county, American Samoa
          tags.tagTranslation( "LSAD", "26", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "26", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "26", "new-kv", "place", "county"), \

          # 27 district, PA, VA, WV, Guam & Marianas
          tags.tagTranslation( "LSAD", "27", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "27", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "27", "new-kv", "place", "district"), \

          # 28 district, LA, MD, MI, VA, WV, Marianas
          tags.tagTranslation( "LSAD", "28", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "28", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "28", "new-kv", "place", "district"), \

          # 29 precinct, IL, NB
          tags.tagTranslation( "LSAD", "29", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "29", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "29", "new-kv", "place", "precinct"), \

          # 30 precinct, IL, NB
          tags.tagTranslation( "LSAD", "30", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "30", "new-kv", "admin_level", "10"), \
          tags.tagTranslation( "LSAD", "30", "new-kv", "place", "precinct"), \

          # 31 gore Maine, Vermont
          tags.tagTranslation( "LSAD", "31", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "31", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "31", "new-kv", "place", "gore"), \

          # 32 grant NH, VT
          tags.tagTranslation( "LSAD", "32", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "32", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "32", "new-kv", "place", "grant"), \

          # 33 independent city, MD, MO, VA
          tags.tagTranslation( "LSAD", "33", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "33", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "33", "new-kv", "place", "city"), \

          # 34 independent city, NV
          tags.tagTranslation( "LSAD", "34", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "34", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "34", "new-kv", "place", "city"), \

          # 35 island American Samoa
          tags.tagTranslation( "LSAD", "35", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "35", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "35", "new-kv", "place", "island"), \

          # 36 location, New Hampshire
          tags.tagTranslation( "LSAD", "36", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "36", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "36", "new-kv", "place", "location"), \

          # 38 county subdivision Arlington County VA
          tags.tagTranslation( "LSAD", "37", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "37", "new-kv", "admin_level", "7"), \

          # 39 plantation, Maine
          tags.tagTranslation( "LSAD", "39", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "39", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "39", "new-kv", "place", "plantation"), \

          # 40 undefined legal county subdivsion, water, 14 states, PR & US VI
          tags.tagTranslation( "LSAD", "40", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "40", "new-kv", "admin_level", "7"), \

          # 41 barrio-pueblo
          tags.tagTranslation( "LSAD", "41", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "41", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "41", "new-kv", "place", "barrio-pueblo"), \

          # 42 purchase NY
          tags.tagTranslation( "LSAD", "42", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "42", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "42", "new-kv", "place", "purchase"), \

          # 43 town 8 states, + NJ, NC, PA, SD
          tags.tagTranslation( "LSAD", "43", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "43", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "43", "new-kv", "place", "town"), \

          # 44 township 16 states
          tags.tagTranslation( "LSAD", "44", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "44", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "44", "new-kv", "place", "township"), \

          # 45 township KS, MN, NB, NC
          tags.tagTranslation( "LSAD", "45", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "45", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "45", "new-kv", "place", "township"), \

          # 46 UT - statistical, 10 states
          tags.tagTranslation( "LSAD", "46", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "46", "new-kv", "admin_level", "7"), \

          # 47 village NJ, OH, SD, WI
          tags.tagTranslation( "LSAD", "47", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "47", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "47", "new-kv", "place", "village"), \

          # 49 charter township, MI
          tags.tagTranslation( "LSAD", "49", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "49", "new-kv", "admin_level", "7"), \
          tags.tagTranslation( "LSAD", "49", "new-kv", "place", "township"), \

          # 51 subbarrio, Puerto Rico
          tags.tagTranslation( "LSAD", "51", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "51", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "51", "new-kv", "place", "subbarrio"), \

          # 53 city and borough, Alaska (place value is a guess)
          tags.tagTranslation( "LSAD", "53", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "53", "new-kv", "admin_level", "6"), \
          tags.tagTranslation( "LSAD", "53", "new-kv", "place", "city"), \

          # 54 municipality, Alaska
          tags.tagTranslation( "LSAD", "54", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "54", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "54", "new-kv", "place", "municipality"), \

          # 55 comunidad, Puerto Rico, statistical admin level a guess
          tags.tagTranslation( "LSAD", "55", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "55", "new-kv", "admin_level", "8"), \

          # 56 borough, CT, NJ, PA (guess at admin level)
          tags.tagTranslation( "LSAD", "56", "new-kv", "boundary", "administrative"), \
          tags.tagTranslation( "LSAD", "56", "new-kv", "admin_level", "7"), \
           tags.tagTranslation( "LSAD", "56", "new-kv", "place", "borough"), \

          # 57 CDP - statistical boundary for hamlets, etc
          tags.tagTranslation( "LSAD", "57", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "57", "new-kv", "place", "cdp"), \
          tags.tagTranslation( "LSAD", "57", "new-kv", "admin_level", "8"), \

          # 58 city - 49 states, DC
          tags.tagTranslation( "LSAD", "58", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "58", "new-kv", "place", "city"), \
          tags.tagTranslation( "LSAD", "58", "new-kv", "admin_level", "8"), \

          # 59 incorporated place, KY, MT, NV, TN, quasi-legal, CT, GA, IN, MT, TN
          tags.tagTranslation( "LSAD", "59", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "59", "new-kv", "admin_level", "8"), \

          # 60 town - 30 states, US VI
          tags.tagTranslation( "LSAD", "60", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "60", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "60", "new-kv", "place", "town"), \

          # 61 village - 20 states, American Samoa
          tags.tagTranslation( "LSAD", "61", "new-kv", "boundary", "admin"), \
          tags.tagTranslation( "LSAD", "61", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "61", "new-kv", "place", "village"), \

          # 62 zona urbana - statistical place Puerto Rico
          tags.tagTranslation( "LSAD", "62", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "62", "new-kv", "admin_level", "8"), \

          # 65 consolidated city - CT, GA, IN (admin level 6 or 8?)
          tags.tagTranslation( "LSAD", "65", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "65", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "65", "new-kv", "place", "city"), \

          # 66 consolidated city - GA, MT, TN (admin level 6 or 8?)
          tags.tagTranslation( "LSAD", "66", "new-kv", "boundary", "statistical"), \
          tags.tagTranslation( "LSAD", "66", "new-kv", "admin_level", "8"), \
          tags.tagTranslation( "LSAD", "66", "new-kv", "place", "city"), \


          tags.tagTranslation( "LSAD", None, "rename-key", "tiger:LSAD", None), \


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
