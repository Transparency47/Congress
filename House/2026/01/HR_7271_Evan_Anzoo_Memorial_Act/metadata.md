# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7271?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7271
- Title: Evan Anzoo Memorial Act
- Congress: 119
- Bill type: HR
- Bill number: 7271
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-04-28T08:06:02Z
- Update date including text: 2026-04-28T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7271",
    "number": "7271",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000344",
        "district": "32",
        "firstName": "Brad",
        "fullName": "Rep. Sherman, Brad [D-CA-32]",
        "lastName": "Sherman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Evan Anzoo Memorial Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:02Z",
    "updateDateIncludingText": "2026-04-28T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:33:45Z",
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
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "DE"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "WA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NV"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AZ"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "RI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7271ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7271\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Sherman (for himself, Mr. Meeks , Ms. Kamlager-Dove , Ms. Dean of Pennsylvania , Mr. Castro of Texas , Mr. Schneider , Ms. Jacobs , Mr. Costa , Ms. McBride , Mrs. Cherfilus-McCormick , Mr. Olszewski , Mr. Keating , Mr. Jackson of Illinois , Ms. Jayapal , Ms. Titus , Mr. Latimer , Mr. Lieu , Mr. Stanton , Ms. Johnson of Texas , Mr. Mfume , Mr. Bera , Mr. Moskowitz , and Mr. Amo ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Comptroller General to submit a report on the effects of the United States Agency for International Development stop work order, the discontinuation of USAID services, and the shuttering of USAID, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Evan Anzoo Memorial Act .\n#### 2. Report\n##### (a) Final report\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate, and make available on a public website, a report on the following:\n**(1)**\nAn estimate of the number of deaths in 2025 due to the United States Agency for International Development (USAID) stop work order, discontinuation of USAID services, and shuttering of USAID.\n**(2)**\nAn estimate of the number of anticipated future deaths over 5 years from the initial USAID stop work order, the discontinuation of USAID services, and shuttering of USAID due to the lack of access to services that USAID previously provided.\n**(3)**\nA determination whether any of the following individuals died as a result of the initial USAID stop work order, the discontinuation of USAID services, or the shuttering of USAID:\n**(A)**\nEvan Anzoo, 5, South Sudan, died after losing access to USAID-provided HIV/AIDs treatment.\n**(B)**\nPe Kau Lau, 71, Thailand, died after losing access to USAID-provided oxygen supply.\n**(C)**\nJibia Tusifu, 10, Democratic Republic of Congo, died after losing access to USAID-provided malaria treatments.\n**(D)**\nDaniella Kalenga, 8, Uganda, died after losing access to USAID-provided malaria treatments.\n**(E)**\nSuza Kenyaba, 5, Democratic Republic of Congo, died after losing access to USAID-provided malaria treatments.\n**(F)**\nPeter Donde, 10, South Sudan, died after losing access to USAID-provided HIV/AIDs treatment.\n**(G)**\nAchol Deng, 8, South Sudan, died after losing access to USAID-provided HIV/AIDs treatment.\n**(H)**\nGilbert Kayombo, 7, Democratic Republic of Congo, died after losing access to USAID-provided HIV/AIDs treatment.\n**(I)**\nMartha Juan, 25, South Sudan, died after losing access to USAID-provided antiretroviral drugs.\n**(J)**\nViola Kiden, 28, South Sudan, died after losing access to USAID-provided antiretroviral drugs.\n**(4)**\nA list of the names of any other known individuals determined to have died as a result of initial USAID stop work order, the discontinuation of USAID services, or the shuttering of USAID.\n##### (b) Interim update\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General of the United States shall update the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate on the findings, as of the date of such update, of the Comptroller General with respect to the matters described in paragraphs (1) through (4) of subsection (a).",
      "versionDate": "2026-01-27",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-09T19:29:54Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7271ih.xml"
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
      "title": "Evan Anzoo Memorial Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Evan Anzoo Memorial Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General to submit a report on the effects of the United States Agency for International Development stop work order, the discontinuation of USAID services, and the shuttering of USAID, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:29Z"
    }
  ]
}
```
