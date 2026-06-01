# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/870
- Title: Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals.
- Congress: 119
- Bill type: HRES
- Bill number: 870
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-03T15:17:59Z
- Update date including text: 2026-04-03T15:17:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-10 - IntroReferral: Submitted in House
- 2025-11-10 - IntroReferral: Submitted in House
- 2025-11-11 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-10: Submitted in House

## Actions

- 2025-11-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-10 - IntroReferral: Submitted in House
- 2025-11-10 - IntroReferral: Submitted in House
- 2025-11-11 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/870",
    "number": "870",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals.",
    "type": "HRES",
    "updateDate": "2026-04-03T15:17:59Z",
    "updateDateIncludingText": "2026-04-03T15:17:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-11",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-11-10T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-11T18:17:38Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres870ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 870\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Espaillat (for himself and Mr. Meeks ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nHonoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals.\n#### 1. Honoring and remembering the victims of American Airlines Flight 587\n##### (a) Honoring and remembering victims\nThe House of Representatives honors and remembers the victims of the crash of American Airlines Flight 587, including\u2014\n**(1)**\nCaptain Edward States, United States;\n**(2)**\nFirst Officer Sten Molin, United States;\n**(3)**\nDeborah Fontakis, United States;\n**(4)**\nBarbara Giannasca, United States;\n**(5)**\nWilmer Gonzalez, United States;\n**(6)**\nJoseph Lopes, United States;\n**(7)**\nMichele Mills, United States;\n**(8)**\nCarol Palm, United States;\n**(9)**\nWilliam Valdespino, United States;\n**(10)**\nManuel Abreu, Dominican Republic;\n**(11)**\nJuana Abreu, United States;\n**(12)**\nCandida Rosa Acosta, United States;\n**(13)**\nOneida Acosta De Araujo, United States;\n**(14)**\nRosa Alcantara, United States;\n**(15)**\nSelene Alcantara, Dominican Republic;\n**(16)**\nDanny Alcantara Taveras, Dominican Republic;\n**(17)**\nHipolito Algarroba, United States;\n**(18)**\nUbencia Algarroba, United States;\n**(19)**\nJosefina Allende, United States;\n**(20)**\nRamon Almanzar, United States;\n**(21)**\nRosa Almanzar, Dominican Republic;\n**(22)**\nJuan Almonte, Dominican Republic;\n**(23)**\nLuz Alvarado, Dominican Republic;\n**(24)**\nRafael Alvarez, United States;\n**(25)**\nMarina Aponte, United States;\n**(26)**\nRegina Arroyo Molina, United States;\n**(27)**\nJovanny Baez, Dominican Republic;\n**(28)**\nNoemi Batista, United States;\n**(29)**\nLialette Batista, United States;\n**(30)**\nTito Bautista, Dominican Republic;\n**(31)**\nBaudilio Bautista, United States;\n**(32)**\nXiomara Betances, Dominican Republic;\n**(33)**\nDennis Blair, United States;\n**(34)**\nJose Bonilla, United States;\n**(35)**\nWilberto Brito, United States;\n**(36)**\nPedro Brito Rodriguez, United States;\n**(37)**\nAngela (Maria) Burdier, Dominican Republic;\n**(38)**\nMartina Burdier De Rodriguez, United States;\n**(39)**\nMaria Burdier Tapia, Dominican Republic;\n**(40)**\nRobert Cabrera, Dominican Republic;\n**(41)**\nConsesora Calaff, United States;\n**(42)**\nRamon Calderon, United States;\n**(43)**\nPetronila Capellan, United States;\n**(44)**\nGenimiz Carty, United States;\n**(45)**\nJuana Castillo, United States;\n**(46)**\nSantana Castillo Fernandez, United States;\n**(47)**\nSobeira Cedeno, United States;\n**(48)**\nAngel Celestino, United States;\n**(49)**\nChristina Charles, United States;\n**(50)**\nDavid (Ching) Chen, Taiwan;\n**(51)**\nVictor Cornelio, Dominican Republic;\n**(52)**\nJuan Coronado, United States;\n**(53)**\nGladys Coronado, United States;\n**(54)**\nDanilo Corporan, Dominican Republic;\n**(55)**\nEduarda Corporan, United States;\n**(56)**\nJanet Corporan (infant);\n**(57)**\nGisela Cuello, United States;\n**(58)**\nIndira Cuevas, United States;\n**(59)**\nFederico de la Asuncion, United States;\n**(60)**\nKarla de la Cruz, United States;\n**(61)**\nClara de la Cruz, United States;\n**(62)**\nLeonardo de la Cruz, United States;\n**(63)**\nLeonte de la Cruz, United States;\n**(64)**\nMarino de la Cruz, Dominican Republic;\n**(65)**\nAngela de la Cruz, Dominican Republic;\n**(66)**\nGlen de la Cruz, United States;\n**(67)**\nMaria de la Cruz, United States;\n**(68)**\nAlexandra de la Cruz, United States;\n**(69)**\nJuan de la Cruz, United States;\n**(70)**\nRafael de la Cruz, United States;\n**(71)**\nAlcibiades de la Cruz, United States;\n**(72)**\nRamona de Leon Corporan, United States;\n**(73)**\nNieves de los Santos, Dominican Republic;\n**(74)**\nGuadalupe del Rosario De Peralta, United States;\n**(75)**\nEustaquio Delarosa, United States;\n**(76)**\nReynida Delgado, Dominican Republic;\n**(77)**\nPatricia Demarchena, Dominican Republic;\n**(78)**\nLorenzo Despradel, United States;\n**(79)**\nRobert Despradel, United States;\n**(80)**\nRoberto Despradel (infant);\n**(81)**\nJulia Diaz;\n**(82)**\nVictor Diaz, United States;\n**(83)**\nFrancisco Diaz, Dominican Republic;\n**(84)**\nLuz Diaz, United States;\n**(85)**\nMaria Diaz, Dominican Republic;\n**(86)**\nAlejandro Diaz, United States;\n**(87)**\nEduvige Diaz Pachano De Bright, Dominican Republic;\n**(88)**\nD Angelo Dilone, United States;\n**(89)**\nJulia Dominguez, United States;\n**(90)**\nAdriano Espino, Dominican Republic;\n**(91)**\nFlorentine Estrella, United States;\n**(92)**\nMigulima Fabre, United States;\n**(93)**\nMarra Filanovsky, United States;\n**(94)**\nIlya Filanovsky, United States;\n**(95)**\nLasar Flores, United States;\n**(96)**\nMariana Flores, United States;\n**(97)**\nLasar (Isaiah) Flores, United States;\n**(98)**\nAnthony (Antonio) Forteza, United States;\n**(99)**\nNalda Galva de Reynoso, Dominican Republic;\n**(100)**\nMilagros Garcia Perez, United States;\n**(101)**\nEduardo George, United States;\n**(102)**\nMilton George, United States;\n**(103)**\nFelix Gervacio, United States;\n**(104)**\nJose Gomez Contrera, United States;\n**(105)**\nPedro Gonzalez, Dominican Republic;\n**(106)**\nCarmen Gonzalez, United States;\n**(107)**\nRegina Gonzalez, United States;\n**(108)**\nSylvie Greleau, Great Britain;\n**(109)**\nAltagracia Guerrero, United States;\n**(110)**\nDariana Guerrero, United States;\n**(111)**\nDiomarys Guerrero, United States;\n**(112)**\nGlenda Guzman, United States;\n**(113)**\nJohnny Guzman, United States;\n**(114)**\nNicolasa Guzman De Mercedes, Dominican Republic;\n**(115)**\nMiguel Guzman, Jr., United States;\n**(116)**\nMarion Hartigan, United States;\n**(117)**\nTeofilo Hernandez, Dominican Republic;\n**(118)**\nJuan Hernandez, Dominican Republic;\n**(119)**\nCarla Hernandez, United States;\n**(120)**\nJoanny Hernandez, United States;\n**(121)**\nJean Heuze, France;\n**(122)**\nYohanly Hidalgo, United States;\n**(123)**\nDario Hidalgo, United States;\n**(124)**\nAlexander Hodge, United States;\n**(125)**\nJoseph Huber, United States;\n**(126)**\nFrances Huber, United States;\n**(127)**\nSarah Huertas, United States;\n**(128)**\nJose Vicente Infante, United States;\n**(129)**\nYamil Jerez, United States;\n**(130)**\nHumberto Jimenez, Dominican Republic;\n**(131)**\nYesica Jimenez, Dominican Republic;\n**(132)**\nJayke Jimenez (infant);\n**(133)**\nRoberto Jimenez Perez, United States;\n**(134)**\nErnestina Jiminian, United States;\n**(135)**\nJose Lafontaine, Dominican Republic;\n**(136)**\nMelvin Landsman, United States;\n**(137)**\nElaine Landsman, United States;\n**(138)**\nLuz Maria Lendof, Dominican Republic;\n**(139)**\nMarcelina Liriano Guerrero, United States;\n**(140)**\nMercedes Lopez, United States;\n**(141)**\nEmily Lopez, United States;\n**(142)**\nArgentina Lopez, United States;\n**(143)**\nRoberto Lopez, Jr., United States;\n**(144)**\nJose Lora, United States;\n**(145)**\nKarl Lora, United States;\n**(146)**\nMercedes Luciano De Veloz, United States;\n**(147)**\nMaricio Made, Dominican Republic;\n**(148)**\nAna Made, Dominican Republic;\n**(149)**\nVictor Marcano, United States;\n**(150)**\nDigna Marte, Dominican Republic;\n**(151)**\nGerman Martinez, Dominican Republic;\n**(152)**\nAurora Martinez, United States;\n**(153)**\nYanelly Martinez, United States;\n**(154)**\nAngel Martinez, United States;\n**(155)**\nSura Martinez, United States;\n**(156)**\nJuan Martinez, Dominican Republic;\n**(157)**\nIbelise Martinez De Goris, Dominican Republic;\n**(158)**\nNieve Mason, Dominican Republic;\n**(159)**\nVirgilia Mateo, United States;\n**(160)**\nNuris Matias, United States;\n**(161)**\nDominga Matias, Dominican Republic;\n**(162)**\nOrlando Mtos Perez, United States;\n**(163)**\nHilda Mayol, United States;\n**(164)**\nCarmen Medina, Dominican Republic;\n**(165)**\nWilfrido Medrano, United States;\n**(166)**\nAshot Melikjanian, United States;\n**(167)**\nGrace Mena, United States;\n**(168)**\nWilton Mendez, United States;\n**(169)**\nDaisy Montalvo, United States;\n**(170)**\nDiane Monte, United States;\n**(171)**\nRemedios Montilla, Dominican Republic;\n**(172)**\nAntonia Morales, United States;\n**(173)**\nLuis Morales, United States;\n**(174)**\nEfrain Mota, United States;\n**(175)**\nLuis Munoz, United States;\n**(176)**\nAlen Noboa, United States;\n**(177)**\nVictoria Nova Rivera, United States;\n**(178)**\nAna Nunez;\n**(179)**\nFatima Nunez, Dominican Republic;\n**(180)**\nAaliya Nunez Reynoso (infant), United States;\n**(181)**\nSiegried Objio, United States;\n**(182)**\nRosanna Ogando, Dominican Republic;\n**(183)**\nRamon Oviedo Germoso, United States;\n**(184)**\nAngel Paradis, United States;\n**(185)**\nCarmen Pena, Dominican Republic;\n**(186)**\nKatherine Pena, United States;\n**(187)**\nMichael Pena, United States;\n**(188)**\nMagnolia Pena Nadir, United States;\n**(189)**\nYelisa Peralta, Dominican Republic;\n**(190)**\nRamon Peralta, Dominican Republic;\n**(191)**\nAugusto Peralta, United States;\n**(192)**\nFernando Perez, United States;\n**(193)**\nCarmen Perez, Dominican Republic;\n**(194)**\nJose Perez, Dominican Republic;\n**(195)**\nMaria Perez Mendez, Dominican Republic;\n**(196)**\nLuis Perreaux, United States;\n**(197)**\nJean Phanord, Haiti;\n**(198)**\nLuis Pichardo, Dominican Republic;\n**(199)**\nRamona Pimentel, Dominican Republic;\n**(200)**\nNurys Polanco, United States;\n**(201)**\nErcilia Polanco, United States;\n**(202)**\nReyna Prospero, United States;\n**(203)**\nJoseph Ramirez, United States;\n**(204)**\nVictor Ramirez, Dominican Republic;\n**(205)**\nJose Ramirez, Dominican Republic;\n**(206)**\nRafael Ravelo, Dominican Republic;\n**(207)**\nEleuteria Reid-Hay, United States;\n**(208)**\nAgapito Reyes, Dominican Republic;\n**(209)**\nRoberto Reyes, United States;\n**(210)**\nNorbeto Rivera, United States;\n**(211)**\nJulio Rodriguez, United States;\n**(212)**\nRuben Rodriguez, United States;\n**(213)**\nJulia Rodriguez, United States;\n**(214)**\nMaria Rodriguez, United States;\n**(215)**\nLucia Rodriguez Almonte, United States;\n**(216)**\nJuana Rojas Javier, Dominican Republic;\n**(217)**\nMercedes Roman, United States;\n**(218)**\nWhilman Rosa, United States;\n**(219)**\nAngel Rosa, United States;\n**(220)**\nJose Rosa Toledo, Dominican Republic;\n**(221)**\nDanilo Rosario Castillo, Dominican Republic;\n**(222)**\nRosa Ruiz, United States;\n**(223)**\nJohanna Sanchez, United States;\n**(224)**\nGilbert Sanchez (infant);\n**(225)**\nFelix Sanchez, United States;\n**(226)**\nLuis Sanchez, United States;\n**(227)**\nJose Sanchez, United States;\n**(228)**\nElvis Sanchez, United States;\n**(229)**\nTimo Santala, United States;\n**(230)**\nIris Magali Santana, Dominican Republic;\n**(231)**\nJose Siri, United States;\n**(232)**\nImelda Solis, United States;\n**(233)**\nDaria Soriano De Batista, Dominican Republic;\n**(234)**\nAsencion Sosa, United States;\n**(235)**\nFranklin Soto, United States;\n**(236)**\nBalbina Soto De Rodriguez, United States;\n**(237)**\nAngela Suazo Perez, United States;\n**(238)**\nLina Tabar, Dominican Republic;\n**(239)**\nMilagros Tabar, Dominican Republic;\n**(240)**\nMaria Tatis, United States;\n**(241)**\nJose Tatis Minaya, Dominican Republic;\n**(242)**\nGuadalupe Taveras, United States;\n**(243)**\nIvelisse Taveras, Dominican Republic;\n**(244)**\nAdaline Tejeda, United States;\n**(245)**\nEvelyn Tolentino, United States;\n**(246)**\nPo Tseng, Taiwan;\n**(247)**\nFeliciano Valera Sierra, United States;\n**(248)**\nMaximo Valerio, Dominican Republic;\n**(249)**\nNorma Valoy, United States;\n**(250)**\nMaria Vargas, United States;\n**(251)**\nIlan Vaserman, Israel;\n**(252)**\nZeneida Vega, Dominican Republic;\n**(253)**\nCarlos Veloz, United States;\n**(254)**\nBraudilio Veloz, United States;\n**(255)**\nGloia Ventin, United States;\n**(256)**\nCristopher Ventin, United States;\n**(257)**\nMaria Del Carmen Ventura, Dominican Republic;\n**(258)**\nNicola Villella, United States;\n**(259)**\nKathleen Williams, United States;\n**(260)**\nCesar Zabala, United States;\n**(261)**\nHelen Concannon of Belle Harbor;\n**(262)**\nThomas Concannon of Belle Harbor;\n**(263)**\nChristopher Lawler of Belle Harbor;\n**(264)**\nKathleen Lawler of Belle Harbor; and\n**(265)**\nFrank Pomponio of Belle Harbor.\n##### (b) Honoring and thanking others\nThe House of Representatives also\u2014\n**(1)**\nhonors and thanks the families, friends, and loved ones of the victims of the crash of American Airlines Flight 587;\n**(2)**\nconveys the most sincere condolences of the citizens of the United States to the families, friends, and communities of the victims; and\n**(3)**\nsolemnly marks the twenty-fourth anniversary of the crash of American Airlines Flight 587 in Rockaway Queens, New York.",
      "versionDate": "2025-11-10",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-19T12:57:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-10",
    "originChamber": "House",
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
          "measure-id": "id119hres870",
          "measure-number": "870",
          "measure-type": "hres",
          "orig-publish-date": "2025-11-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres870v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-11-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors and remembers the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York.</p><p>It also (1) honors and thanks the families, friends, and loved ones of the victims of the crash; (2) conveys the condolences of U.S. citizens to the families, friends, and communities of the victims; and (3) solemnly marks the 24<sup>th </sup>anniversary of the crash.</p>"
        },
        "title": "Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres870.xml",
    "summary": {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors and remembers the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York.</p><p>It also (1) honors and thanks the families, friends, and loved ones of the victims of the crash; (2) conveys the condolences of U.S. citizens to the families, friends, and communities of the victims; and (3) solemnly marks the 24<sup>th </sup>anniversary of the crash.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres870"
    },
    "title": "Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals."
  },
  "summaries": [
    {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors and remembers the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York.</p><p>It also (1) honors and thanks the families, friends, and loved ones of the victims of the crash; (2) conveys the condolences of U.S. citizens to the families, friends, and communities of the victims; and (3) solemnly marks the 24<sup>th </sup>anniversary of the crash.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres870"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres870ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:13Z"
    },
    {
      "title": "Honoring and remembering the victims of the crash of American Airlines Flight 587 in Rockaway Queens, New York, on November 12, 2001, and extending the sincerest condolences of the citizens of the United States to the families and friends of those individuals.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T09:05:22Z"
    }
  ]
}
```
