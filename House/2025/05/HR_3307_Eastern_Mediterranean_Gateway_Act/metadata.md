# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3307
- Title: Eastern Mediterranean Gateway Act
- Congress: 119
- Bill type: HR
- Bill number: 3307
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-27T08:06:26Z
- Update date including text: 2026-05-27T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3307",
    "number": "3307",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Eastern Mediterranean Gateway Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:26Z",
    "updateDateIncludingText": "2026-05-27T08:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-05-08T13:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NH"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "RI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "OH"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NE"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3307ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3307\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Schneider (for himself, Mr. Bilirakis , Ms. Titus , Ms. Malliotakis , and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo increase cooperation with countries in the Eastern Mediterranean region in order to strengthen energy security and defense capabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eastern Mediterranean Gateway Act .\n#### 2. Purpose\nThe purpose of this Act is to support the role of Eastern Mediterranean countries as a strategic gateway in the India-Middle East-Europe Economic Corridor (IMEC).\n#### 3. Findings\nCongress finds the following:\n**(1)**\nThe India-Middle East-Europe Economic Corridor (IMEC), launched at the G20 Summit in 2023 with G7 backing, enhances connectivity between Asia, the Middle East, and Europe while serving as a strategic alternative to China\u2019s Belt and Road Initiative.\n**(2)**\nThe Eastern Mediterranean region is of strategic importance to the United States and its allies, as demonstrated by the United States founding role in the 3+1 framework with Greece, Israel, and Cyprus.\n**(3)**\nEnergy projects such as the Great Sea Interconnector, the Gregy Interconnection Project, the Greece-Bulgaria Interconnector, and the LNG terminals in the Eastern Mediterranean play a key role in European energy security and provide critical infrastructure that can serve as the backbone for linking India, the Gulf, and Europe through the Eastern Mediterranean.\n**(4)**\nCyprus, Greece, Egypt, and Israel are key United States partners in promoting stability, security, and economic development in the region.\n**(5)**\nEnhanced defense and security cooperation, as well as educational and cultural exchanges, are essential for strengthening bilateral and multilateral ties.\n**(6)**\nAccording to Presidential Determination 2025\u201303, the furnishing of defense articles and defense services to the Republic of Cyprus will strengthen the security of the United States and promote world peace .\n**(7)**\nThe statement of policy in the Israel Relations Normalization Act of 2022 ( 22 U.S.C. 8601 note), notably that it is the policy of the United States to expand and strengthen the Abraham Accords to encourage other nations to normalize relations with Israel , should guide the Secretary of State and other United States actors in their work to promote integration between India, the Middle East and southeast Europe.\n**(8)**\nIndia has strengthened strategic ties with Greece, Israel, and Cyprus, fostering economic, maritime, and security cooperation that aligns with United States regional priorities.\n**(9)**\nThe success of the India-Middle East-Europe Economic Corridor depends on infrastructure, security, and innovation partnerships rooted in the Eastern Mediterranean region, which serves as the primary connective hub linking the Gulf and Indian subcontinent to Europe.\n#### 4. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe significance of diplomatic initiatives such as the Greece-Cyprus-Israel-US 3+1 format, the East Mediterranean Gas Forum and the Abraham Accords should be recognized and the United States should maintain its leadership role in these diplomatic initiatives;\n**(2)**\nthe United States should continue to actively participate in the initiatives of the East Mediterranean Gas Forum;\n**(3)**\nthe Eastern Mediterranean region is a key gateway that can link three continents and the United States should support energy and transportation infrastructure, connectivity initiatives, defense cooperation, and other forms of integration in and around the region;\n**(4)**\nthe United States recognizes the unique role of Eastern Mediterranean countries as both a distinct subregion and a central connector within the broader IMEC corridor;\n**(5)**\nthe 3+1 diplomatic initiative should resume with a meeting of the Secretary of State with the Ministers of Israel, Greece, and Cyprus; and\n**(6)**\nthe statement of policy in section 203 of the Eastern Mediterranean Security and Energy Partnership Act of 2019 ( 22 U.S.C. 2373 note) should guide the Secretary of State in promoting connectivity between India, the Middle East and Europe, including participation in the trilateral dialogue on energy, maritime security, cyber security and protection of critical infrastructure conducted among Israel, Greece, and Cyprus.\n#### 5. Diplomacy in Eastern Mediterranean region\n##### (a) Strategic dialogues\nThe Secretary of State may institutionalize multilateral strategic dialogues between the United States and IMEC countries, including dedicated formats with Eastern Mediterranean countries, with which the United States has a bilateral strategic dialogue.\n##### (b) Prioritization of the Eastern Mediterranean\nThe Secretary of State shall prioritize the Eastern Mediterranean region in United States foreign policy, focusing on energy security and defense cooperation with countries in such region.\n#### 6. Reports and studies\n##### (a) Report on implementation\nNot later than one year after the date of the enactment of this Act and annually thereafter, the Secretary of Energy, in coordination with the Secretary of State, shall submit to the appropriate congressional committees a report describing the implementation and effect of this Act, including an update on energy projects and defense cooperation that are being carried out pursuant to the authorities of this Act and the amendments made by this Act.\n##### (b) Report on multilateral initiatives\nNot later than one year after the date of the enactment of this Act, the Secretary of State shall provide to the appropriate congressional committees a briefing on each multilateral initiative between the United States and IMEC countries.\n##### (c) Analysis of Cyprus Centre for Land, Open Seas, and Port Security\nNot later than one year after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Homeland Security, shall analyze insights gained from the operation of the Cyprus Centre for Land, Open Seas, and Port Security (in this section referred to as CYCLOPS ) as a potential model for broad-based multilateral cooperation.\n##### (d) Study of program creation and expansion\nNot later than one year after the date of the enactment of this Act, the Secretary of State, in consultation with the Secretary of Energy, shall submit to the appropriate congressional committees a report describing the cost of, steps to, and feasibility of\u2014\n**(1)**\ncreating bilateral programs with Eastern Mediterranean countries modeled on bilateral programs between the United States and Israel, including\u2014\n**(A)**\nthe Binational Agriculture Research and Development Fund;\n**(B)**\nthe United States-Israel Binational Industrial Research and Development Foundation (including projects relating to homeland security and cyber security);\n**(C)**\nthe United States-Israel Binational Science Foundation; and\n**(D)**\nthe United States-Israel Science and Technology Foundation; and\n**(2)**\nexpanding bilateral programs between the United States and Israel, including the programs listed in paragraph (1), to include other Eastern Mediterranean countries and IMEC countries.\n#### 7. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Commerce and the Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources and the Committee on Foreign Relations of the Senate.\n**(2) Eastern Mediterranean country**\nThe term Eastern Mediterranean country means the following:\n**(A)**\nThe Arab Republic of Egypt.\n**(B)**\nThe Hellenic Republic.\n**(C)**\nThe Republic of Cyprus.\n**(D)**\nThe State of Israel.\n**(3) IMEC country**\nThe term IMEC country means the following:\n**(A)**\nThe European Union.\n**(B)**\nThe Federal Republic of Germany.\n**(C)**\nThe French Republic.\n**(D)**\nThe Italian Republic.\n**(E)**\nThe Kingdom of Saudi Arabia.\n**(F)**\nThe Republic of India.\n**(G)**\nThe United Arab Emirates.\n**(H)**\nThe United States.\n**(I)**\nAny other country that the Secretary of State designates as an IMEC country for purposes of this Act.",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-29",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "4443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Eastern Mediterranean Gateway Act",
      "type": "S"
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
        "name": "International Affairs",
        "updateDate": "2025-06-10T14:40:08Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3307ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Eastern Mediterranean Gateway Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eastern Mediterranean Gateway Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase cooperation with countries in the Eastern Mediterranean region in order to strengthen energy security and defense capabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:35Z"
    }
  ]
}
```
