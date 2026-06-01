# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/51?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/51
- Title: To direct the removal of United States Armed Forces from hostilities that have not been authorized by Congress.
- Congress: 119
- Bill type: HCONRES
- Bill number: 51
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-01-08T09:06:52Z
- Update date including text: 2026-01-08T09:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House
- Latest action: 2025-09-23: Submitted in House

## Actions

- 2025-09-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/51",
    "number": "51",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "O000173",
        "district": "5",
        "firstName": "Ilhan",
        "fullName": "Rep. Omar, Ilhan [D-MN-5]",
        "lastName": "Omar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "To direct the removal of United States Armed Forces from hostilities that have not been authorized by Congress.",
    "type": "HCONRES",
    "updateDate": "2026-01-08T09:06:52Z",
    "updateDateIncludingText": "2026-01-08T09:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:01:30Z",
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
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "IL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "AZ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MI"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "OR"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "WI"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "DC"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "FL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OR"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres51ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 51\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Ms. Omar (for herself, Mr. Casar , and Mr. Garc\u00eda of Illinois ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nTo direct the removal of United States Armed Forces from hostilities that have not been authorized by Congress.\n#### 1. Findings\nCongress makes the following findings:\n**(1)**\nCongress has the sole power to declare war under article I, section 8, clause 11 of the United States Constitution.\n**(2)**\nSection 2(c) of the War Powers Resolution ( 50 U.S.C. 1541(c) ) states that the constitutional powers of the President as Commander-in-Chief to introduce United States Armed Forces into hostilities, or into situations where imminent involvement in hostilities is clearly indicated by the circumstances, are exercised only pursuant to (1) a declaration of war, (2) specific statutory authorization, or (3) a national emergency created by attack upon the United States, its territories or possessions, or its armed forces. .\n**(3)**\nCongress has not declared war upon, nor enacted a specific statutory authorization for use of military force against, the Bolivarian Republic of Venezuela, nor any transnational criminal organizations designated as Foreign Terrorist Organizations or Specially Designated Global Terrorists since February 20, 2025.\n**(4)**\nThe designation of a group, entity, or individual as a Foreign Terrorist Organization or Specially Designated Global Terrorist provides no legal authority for the President to direct the use of military force against members of designated organizations or any foreign state.\n**(5)**\nNeither the 2001 Authorization for Use of Military Force ( Public Law 107\u201340 ; 50 U.S.C. 1541 note) against the perpetrators of the 9/11 attack nor the Authorization for Use of Military Force Against Iraq Resolution of 2002 ( Public Law 107\u2013243 ; 50 U.S.C. 1541 note) provides any statutory authority for the President to direct the use of military force against Venezuela or any transnational criminal organizations designated as Foreign Terrorist Organizations or Specially Designated Global Terrorists since February 20, 2025.\n**(6)**\nRegarding Venezuelan jets flying near U.S. warships dispatched to the South Caribbean Sea, President Trump on September 5, 2025, stated that such planes were going to be in trouble, and if a flyover reoccurs, he told a U.S. general, You have a choice of doing anything you want, including, should such planes put us in a dangerous situation, they will be shot down, indicating the introduction of U.S. forces into imminent hostilities.\n**(7)**\nNo armed attack on the United States by Venezuela or any transnational criminal organizations designated as Foreign Terrorist Organizations or Special Designated Global Terrorist since February 20th, 2025 has occurred, the trafficking of illegal drugs does not itself constitute such an armed attack or threat of an imminent armed attack.\n**(8)**\nThe strike on the vessel in the Southern Caribbean on September 2, 2025, the subsequent strikes in September 2025, and the positioning of U.S. warships and aircraft in the Caribbean and President Trump\u2019s statements on the use of force without prior statutory authorization, fall within the meaning of section 4(a)(1) of the War Powers Resolution ( 50 U.S.C. 1543(a)(1) ), constituting either hostilities or a situation where imminent involvement in hostilities is clearly indicated by the circumstances into which United States Armed Forces have been introduced.\n**(9)**\nSection 5(c) of the War Powers Resolution ( 50 U.S.C. 1544(c) ) states that at any time that United States Armed Forces are engaged in hostilities outside the territory of the United States, its possessions and territories without a declaration of war or specific statutory authorization, such forces shall be removed by the President if the Congress so directs. .\n**(10)**\nIn its report to Congress on the strike dated September 4, 2025, pursuant to section 4(a) of the War Powers Resolution ( 50 U.S.C. 1543(a) ), President Trump stated, It is not possible at this time to know the full scope and duration of military operations that will be necessary. United States forces remain postured to carry out further military operations. .\n**(11)**\nThe question of whether United States forces should be engaged in hostilities against Venezuela or any transnational criminal organizations designated as Foreign Terrorist Organizations or Specially Designated Global Terrorists since February 20, 2025, should be answered following a full briefing to Congress and the American public of the issues at stake, a public debate in Congress, and a congressional vote as contemplated by the Constitution.\n#### 2. Termination of the use of United States forces for hostilities\n##### (a) Termination\nPursuant to section 5(c) of the War Powers Resolution ( 50 U.S.C. 1544(c) ), Congress hereby directs the President to terminate the use of United States Armed Forces for hostilities against the following:\n**(1)**\nThe Bolivarian Republic of Venezuela or any part of its government or military.\n**(2)**\nAny transnational criminal organizations designated as Foreign Terrorist Organizations or Specially Designated Global Terrorists since February 20, 2025.\nUnless explicitly authorized by a declaration of war or specific authorization for use of military force after the date of the adoption of this concurrent resolution.\n##### (b) Rule of construction\nNothing in this section shall be construed to prevent the United States from repelling sudden attacks or engaging in self-defense consistent with the legal requirements outlined in section 2(c) of the War Powers Resolution ( 50 U.S.C. 1541(c) ). The trafficking of illegal drugs does not itself constitute such an armed attack or threat of an imminent armed attack under section 2(c)(3) of the War Powers Resolution ( 50 U.S.C. 1541(c)(3) ).",
      "versionDate": "2025-09-23",
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
        "name": "International Affairs",
        "updateDate": "2025-09-24T15:18:53Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres51ih.xml"
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
      "title": "To direct the removal of United States Armed Forces from hostilities that have not been authorized by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T08:18:18Z"
    },
    {
      "title": "To direct the removal of United States Armed Forces from hostilities that have not been authorized by Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T08:05:31Z"
    }
  ]
}
```
