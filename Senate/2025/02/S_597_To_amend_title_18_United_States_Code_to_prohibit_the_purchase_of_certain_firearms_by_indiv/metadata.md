# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/597?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/597
- Title: Age 21 Act
- Congress: 119
- Bill type: S
- Bill number: 597
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-23T18:04:27Z
- Update date including text: 2026-03-23T18:04:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/597",
    "number": "597",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Age 21 Act",
    "type": "S",
    "updateDate": "2026-03-23T18:04:27Z",
    "updateDateIncludingText": "2026-03-23T18:04:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-13T20:27:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "VA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-13",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s597is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 597\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Padilla (for himself, Mr. Blumenthal , Mr. Booker , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mrs. Gillibrand , Ms. Hirono , Mr. Kaine , Ms. Klobuchar , Mr. Murphy , Mrs. Murray , Mr. Reed , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Warren , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit the purchase of certain firearms by individuals under 21 years of age, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Age 21 Act .\n#### 2. Prohibition on purchase of certain firearms by individuals under 21 years of age\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting after paragraph (30) the following:\n(31) The term semiautomatic pistol means any repeating firearm, other than a shotgun or rifle, that\u2014 (A) utilizes a portion of the energy of a firing cartridge to extract the fired cartridge case and chamber the next round; and (B) requires a separate pull of the trigger to fire each cartridge. ; and\n**(2)**\nby adding at the end the following:\n(38) The term semiautomatic shotgun means any repeating shotgun that\u2014 (A) utilizes a portion of the energy of a firing shell to extract the fired shell casing and chamber the next round; and (B) requires a separate pull of the trigger to fire each cartridge. (39) The term semiautomatic assault weapon means any of the following, regardless of country of manufacture or caliber of ammunition accepted: (A) A semiautomatic rifle that has the capacity to accept a detachable ammunition feeding device and any one of the following: (i) A pistol grip. (ii) A forward grip. (iii) A folding, telescoping, or detachable stock, or a stock that is otherwise foldable or adjustable in a manner that operates to reduce the length, size, or any other dimension, or otherwise enhances the concealability, of the weapon. (iv) A functional grenade launcher. (v) A barrel shroud. (vi) A threaded barrel. (B) A semiautomatic rifle that has a fixed ammunition feeding device with the capacity to accept more than 10 rounds, except for an attached tubular device designed to accept, and capable of operating only with, .22 caliber rimfire ammunition. (C) Any part, combination of parts, component, device, attachment, or accessory that is designed or functions to accelerate the rate of fire of a semiautomatic rifle but not convert the semiautomatic rifle into a machinegun. (D) A semiautomatic pistol that has the capacity to accept a detachable ammunition feeding device and any one of the following: (i) A threaded barrel. (ii) A second pistol grip. (iii) A barrel shroud. (iv) The capacity to accept a detachable ammunition feeding device at some location outside of the pistol grip. (v) A semiautomatic version of an automatic firearm. (vi) A manufactured weight of 50 ounces or more when unloaded. (vii) A stabilizing brace or similar component. (E) A semiautomatic pistol with a fixed ammunition feeding device that has the capacity to accept more than 10 rounds. (F) A semiautomatic shotgun that has any one of the following: (i) A folding, telescoping, or detachable stock. (ii) A pistol grip. (iii) A fixed ammunition feeding device with the capacity to accept more than 5 rounds. (iv) The ability to accept a detachable ammunition feeding device. (v) A forward grip. (vi) A functional grenade launcher. (G) Any shotgun with a revolving cylinder. (H) All of the following rifles, copies, duplicates, variants, or altered facsimiles with the capability of any such weapon thereof: (i) All AK types, including the following: (I) AK, AK47, AK47S, AK\u201374, AKM, AKS, ARM, MAK90, MISR, NHM90, NHM91, Rock River Arms LAR\u201347, SA85, SA93, Vector Arms AK\u201347, VEPR, WASR\u201310, and WUM. (II) IZHMASH Saiga AK. (III) MAADI AK47 and ARM. (IV) Norinco 56S, 56S2, 84S, and 86S. (V) Poly Technologies AK47 and AKS. (ii) All AR types, including the following: (I) AR\u201310. (II) AR\u201315. (III) Alexander Arms Overmatch Plus 16. (IV) Armalite M15 22LR Carbine. (V) Armalite M15\u2013T. (VI) Barrett REC7. (VII) Beretta AR\u201370. (VIII) Black Rain Ordnance Recon Scout. (IX) Bushmaster ACR. (X) Bushmaster Carbon 15. (XI) Bushmaster MOE series. (XII) Bushmaster XM15. (XIII) Chiappa Firearms MFour rifles. (XIV) Colt Match Target rifles. (XV) CORE Rifle Systems CORE15 rifles. (XVI) Daniel Defense M4A1 rifles. (XVII) Devil Dog Arms 15 Series rifles. (XVIII) Diamondback DB15 rifles. (XIX) DoubleStar AR rifles. (XX) DPMS Tactical rifles. (XXI) DSA Inc. ZM\u20134 Carbine. (XXII) Heckler & Koch MR556. (XXIII) High Standard HSA\u201315 rifles. (XXIV) Jesse James Nomad AR\u201315 rifle. (XXV) Knight\u2019s Armament SR\u201315. (XXVI) Lancer L15 rifles. (XXVII) MGI Hydra Series rifles. (XXVIII) Mossberg MMR Tactical rifles. (XXIX) Noreen Firearms BN 36 rifle. (XXX) Olympic Arms. (XXXI) POF USA P415. (XXXII) Precision Firearms AR rifles. (XXXIII) Remington R\u201315 rifles. (XXXIV) Rhino Arms AR rifles. (XXXV) Rock River Arms LAR\u201315. (XXXVI) Sig Sauer SIG516 rifles and MCX rifles. (XXXVII) SKS with a detachable ammunition feeding device. (XXXVIII) Smith & Wesson M&P15 rifles. (XXXIX) Stag Arms AR rifles. (XL) Sturm, Ruger & Co. SR556 and AR\u2013556 rifles. (XLI) Uselton Arms Air-Lite M\u20134 rifles. (XLII) Windham Weaponry AR rifles. (XLIII) WMD Guns Big Beast. (XLIV) Yankee Hill Machine Company, Inc. YHM\u201315 rifles. (iii) Barrett M107A1. (iv) Barrett M82A1. (v) Beretta CX4 Storm. (vi) Calico Liberty Series. (vii) CETME Sporter. (viii) Daewoo K\u20131, K\u20132, Max 1, Max 2, AR 100, and AR 110C. (ix) Fabrique Nationale/FN Herstal FAL, LAR, 22 FNC, 308 Match, L1A1 Sporter, PS90, SCAR, and FS2000. (x) Feather Industries AT\u20139. (xi) Galil Model AR and Model ARM. (xii) Hi-Point Carbine. (xiii) HK\u201391, HK\u201393, HK\u201394, HK\u2013PSG\u20131, and HK USC. (xiv) IWI TAVOR, Galil ACE rifle. (xv) Kel-Tec Sub-2000, SU\u201316, and RFB. (xvi) SIG AMT, SIG PE\u201357, Sig Sauer SG 550, Sig Sauer SG 551, and SIG MCX. (xvii) Springfield Armory SAR\u201348. (xviii) Steyr AUG. (xix) Sturm, Ruger & Co. Mini-14 Tactical Rifle M\u201314/20CF. (xx) All Thompson rifles, including the following: (I) Thompson M1SB. (II) Thompson T1100D. (III) Thompson T150D. (IV) Thompson T1B. (V) Thompson T1B100D. (VI) Thompson T1B50D. (VII) Thompson T1BSB. (VIII) Thompson T1\u2013C. (IX) Thompson T1D. (X) Thompson T1SB. (XI) Thompson T5. (XII) Thompson T5100D. (XIII) Thompson TM1. (XIV) Thompson TM1C. (xxi) UMAREX UZI rifle. (xxii) UZI Mini Carbine, UZI Model A Carbine, and UZI Model B Carbine. (xxiii) Valmet M62S, M71S, and M78. (xxiv) Vector Arms UZI Type. (xxv) Weaver Arms Nighthawk. (xxvi) Wilkinson Arms Linda Carbine. (I) All of the following pistols, copies, duplicates, variants, or altered facsimiles with the capability of any such weapon thereof: (i) All AK\u201347 types, including the following: (I) Centurion 39 AK pistol. (II) CZ Scorpion pistol. (III) Draco AK\u201347 pistol. (IV) HCR AK\u201347 pistol. (V) IO Inc. Hellpup AK\u201347 pistol. (VI) Krinkov pistol. (VII) Mini Draco AK\u201347 pistol. (VIII) PAP M92 pistol. (IX) Yugo Krebs Krink pistol. (ii) All AR\u201315 types, including the following: (I) American Spirit AR\u201315 pistol. (II) Bushmaster Carbon 15 pistol. (III) Chiappa Firearms M4 Pistol GEN II. (IV) CORE Rifle Systems CORE15 Roscoe pistol. (V) Daniel Defense MK18 pistol. (VI) DoubleStar Corporation AR pistol. (VII) DPMS AR\u201315 pistol. (VIII) Jesse James Nomad AR\u201315 pistol. (IX) Olympic Arms AR\u201315 pistol. (X) Osprey Armament MK\u201318 pistol. (XI) POF USA AR pistols. (XII) Rock River Arms LAR 15 pistol. (XIII) Uselton Arms Air-Lite M\u20134 pistol. (iii) Calico Liberty pistols. (iv) DSA SA58 PKP FAL pistol. (v) Encom MP\u20139 and MP\u201345. (vi) Heckler & Koch model SP\u201389 pistol. (vii) Intratec AB\u201310, TEC\u201322 Scorpion, TEC\u20139, and TEC\u2013DC9. (viii) IWI Galil Ace pistol, UZI PRO pistol. (ix) Kel-Tec PLR 16 pistol. (x) The following MAC types: (I) MAC\u201310. (II) MAC\u201311. (III) Masterpiece Arms MPA A930 Mini Pistol, MPA460 Pistol, MPA Tactical Pistol, and MPA Mini Tactical Pistol. (IV) Military Armament Corp. Ingram M\u201311. (V) Velocity Arms VMAC. (xi) Sig Sauer P556 pistol. (xii) Sites Spectre. (xiii) All Thompson types, including the following: (I) Thompson TA510D. (II) Thompson TA5. (xiv) All UZI types, including Micro-UZI. (J) All of the following shotguns, copies, duplicates, variants, or altered facsimiles with the capability of any such weapon thereof: (i) DERYA Anakon MC\u20131980, Anakon SD12. (ii) Doruk Lethal shotguns. (iii) Franchi LAW\u201312 and SPAS 12. (iv) All IZHMASH Saiga 12 types, including the following: (I) IZHMASH Saiga 12. (II) IZHMASH Saiga 12S. (III) IZHMASH Saiga 12S EXP\u201301. (IV) IZHMASH Saiga 12K. (V) IZHMASH Saiga 12K\u2013030. (VI) IZHMASH Saiga 12K\u2013040 Taktika. (v) Streetsweeper. (vi) Striker 12. (K) All belt-fed semiautomatic firearms, including TNW M2HB and FN M2495. (L) Any combination of parts from which a firearm described in subparagraphs (A) through (K) can be assembled. (M) The frame or receiver of a rifle or shotgun described in subparagraph (A), (B), (C), (F), (G), (H), (J), or (K). (40) The term large capacity ammunition feeding device \u2014 (A) means a magazine, belt, drum, feed strip, or similar device, including any such device joined or coupled with another in any manner, that has an overall capacity of, or that can be readily restored, changed, or converted to accept, more than 10 rounds of ammunition; and (B) does not include an attached tubular device designed to accept, and capable of operating only with, .22 caliber rimfire ammunition. (41) The term barrel shroud \u2014 (A) means a shroud that is attached to, or partially or completely encircles, the barrel of a firearm so that the shroud protects the user of the firearm from heat generated by the barrel; and (B) does not include\u2014 (i) a slide that partially or completely encloses the barrel; or (ii) an extension of the stock along the bottom of the barrel which does not encircle or substantially encircle the barrel. (42) The term detachable ammunition feeding device means an ammunition feeding device that can be removed from a firearm without disassembly of the firearm action. (43) The term fixed ammunition feeding device means an ammunition feeding device that is permanently fixed to the firearm in such a manner that it cannot be removed without disassembly of the firearm. (44) The term folding, telescoping, or detachable stock means a stock that folds, telescopes, detaches or otherwise operates to reduce the length, size, or any other dimension, or otherwise enhances the concealability, of a firearm. (45) The term forward grip means a grip located forward of the trigger that functions as a pistol grip. (46) The term grenade launcher means an attachment for use on a firearm that is designed to propel a grenade or other similar destructive device. (47) The term pistol grip means a grip, a thumbhole stock or Thordsen-type grip or stock, or any other characteristic that can function as a grip. (48) The term threaded barrel means a feature or characteristic that is designed in such a manner to allow for the attachment of a device such as a firearm silencer or a flash suppressor. (49) The term belt-fed semiautomatic firearm means any repeating firearm that\u2014 (A) utilizes a portion of the energy of a firing cartridge to extract the fired cartridge case and chamber the next round; (B) requires a separate pull of the trigger to fire each cartridge; and (C) has the capacity to accept a belt ammunition feeding device. .\n##### (b) Prohibition\nChapter 44 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 922\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nby inserting (A) after (1) ; and\n**(II)**\nby inserting or after the semicolon; and\n**(ii)**\nby adding at the end the following:\n(B) any large capacity ammunition feeding device to any individual who the licensee knows or has reasonable cause to believe is less than 21 years of age; ;\n**(B)**\nin subsection (c)(1), by inserting a large capacity ammunition feeding device or before any firearm other than ; and\n**(C)**\nin subsection (x)\u2014\n**(i)**\nin paragraph (1), by striking a juvenile\u2014 and all that follows through handgun. and inserting the following:\nless than 21 years of age\u2014 (A) a handgun; (B) a semiautomatic assault weapon; (C) a large capacity ammunition feeding device; or (D) ammunition that is suitable for use only in a handgun or semiautomatic assault weapon. ;\n**(ii)**\nin paragraph (2), by striking a juvenile and all that follows through handgun. and inserting the following:\nless than 21 years of age to knowingly possess\u2014 (A) a handgun; (B) a semiautomatic assault weapon; (C) a large capacity ammunition feeding device; or (D) ammunition that is suitable for use only in a handgun or semiautomatic assault weapon. ;\n**(iii)**\nby striking paragraphs (3), (4), and (5) and inserting the following:\n(3) This subsection does not apply to\u2014 (A) a temporary transfer of a covered firearm or covered ammunition to a person who is less than 21 years of age or to the possession or use of a covered firearm or covered ammunition by a person who is less than 21 years of age if\u2014 (i) the covered firearm or covered ammunition is possessed and used by the person in the course of employment, in the course of ranching or farming related to activities at the residence of the person (or on property used for ranching or farming at which the person, with the permission of the property owner or lessee, is performing activities related to the operation of the farm or ranch), target practice, hunting, or a course of instruction in the safe and lawful use of a covered firearm; (ii) the covered firearm or covered ammunition is possessed and used by the person with the prior written consent of the person's parent or guardian who is not prohibited by Federal, State, or local law from possessing a firearm, except\u2014 (I) during transportation by the person of an unloaded covered firearm in a locked container directly from the place of transfer to a place at which an activity described in clause (i) is to take place and transportation by the person of that covered firearm, unloaded and in a locked container, directly from the place at which such an activity took place to the transferor; or (II) with respect to ranching or farming activities as described in clause (i), a person who is less than 21 years of age may possess and use a covered firearm or covered ammunition with the prior written approval of the person's parent or legal guardian and at the direction of an adult who is not prohibited by Federal, State or local law from possessing a firearm; (iii) the person has the prior written consent in the person's possession at all times when a covered firearm or covered ammunition is in the possession of the person; and (iv) the covered firearm or covered ammunition is possessed and used by the person in accordance with State and local law; (B) a person who is less than 21 years of age who is a member of the Armed Forces of the United States or the National Guard who possesses or is armed with a covered firearm or covered ammunition in the line of duty; (C) a transfer by inheritance of title (but not possession) of a covered firearm or covered ammunition to a person who is less than 21 years of age; or (D) the possession of a covered firearm or covered ammunition by a person who is less than 21 years of age taken in defense of the person or other individuals against an intruder into the residence of the person or a residence in which the person is an invited guest. (4) A covered firearm or covered ammunition, the possession of which is transferred to a person who is less than 21 years of age in circumstances in which the transferor is not in violation of this subsection shall not be subject to permanent confiscation by the Government if its possession by the person who is less than 21 years of age subsequently becomes unlawful because of the conduct of the person who is less than 21 years of age, but shall be returned to the lawful owner when such covered firearm or covered ammunition is no longer required by the Government for the purposes of investigation or prosecution. (5) For purposes of this subsection\u2014 (A) the term covered ammunition means ammunition that is suitable for use only in a handgun or a semiautomatic assault weapon; and (B) the term covered firearm means\u2014 (i) a handgun; (ii) a semiautomatic assault weapon; or (iii) a large capacity ammunition feeding device. ; and\n**(iv)**\nin paragraph (6)\u2014\n**(I)**\nin subparagraph (A), by striking a juvenile defendant's parent or legal guardian and inserting the parent or legal guardian of a defendant who is less than 21 years of age ; and\n**(II)**\nin subparagraph (C), by striking a juvenile defendant and inserting a defendant who is less than 21 years of age ; and\n**(2)**\nin section 924(a)(6)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking juvenile each place the term appears and inserting person who is less than 21 years of age ; and\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nin the matter preceding subclause (I), by striking juvenile and inserting person who is less than 21 years of age ;\n**(II)**\nin subclause (I)\u2014\n**(aa)**\nby striking juvenile and inserting person who is less than 21 years of age ; and\n**(bb)**\nby striking handgun or ammunition and inserting covered firearm or covered ammunition ; and\n**(III)**\nin subclause (II), by striking juvenile has and inserting person who is less than 21 years of age has ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking juvenile each place the term appears and inserting person who is less than 21 years of age ; and\n**(ii)**\nby striking handgun or ammunition each place the term appears and inserting covered firearm or covered ammunition .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-07-08T12:45:01Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-08T12:45:01Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-07-08T12:45:01Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-07-08T12:45:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-17T17:36:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s597",
          "measure-number": "597",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2026-03-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s597v00",
            "update-date": "2026-03-23"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Age 21 Act</b></p> <p>This bill raises the minimum age to purchase a large capacity ammunition feeding device or semiautomatic assault weapon from 18 to 21 years of age.</p>"
        },
        "title": "Age 21 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s597.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Age 21 Act</b></p> <p>This bill raises the minimum age to purchase a large capacity ammunition feeding device or semiautomatic assault weapon from 18 to 21 years of age.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s597"
    },
    "title": "Age 21 Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Age 21 Act</b></p> <p>This bill raises the minimum age to purchase a large capacity ammunition feeding device or semiautomatic assault weapon from 18 to 21 years of age.</p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s597"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s597is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Age 21 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Age 21 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit the purchase of certain firearms by individuals under 21 years of age, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:30Z"
    }
  ]
}
```
