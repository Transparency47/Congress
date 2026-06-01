# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/153
- Title: To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.
- Congress: 119
- Bill type: HJRES
- Bill number: 153
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-05-22T08:07:53Z
- Update date including text: 2026-05-22T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/153",
    "number": "153",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
    "type": "HJRES",
    "updateDate": "2026-05-22T08:07:53Z",
    "updateDateIncludingText": "2026-05-22T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:01:10Z",
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
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
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
      "sponsorshipDate": "2026-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "WA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "OR"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
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
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres153ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 153\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Ms. Vel\u00e1zquez submitted the following joint resolution; which was referred to the Committee on Foreign Affairs\nJOINT RESOLUTION\nTo direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.\n#### 1. Findings\nCongress makes the following findings:\n**(1)**\nCongress has the sole power to declare war under article I, section 8, clause 11 of the United States Constitution.\n**(2)**\nThe President has a constitutional responsibility to take actions to defend the United States, its territories, its possessions, citizens, service members, and diplomats from attack.\n**(3)**\nCongress has not declared war upon Cuba or upon any person or organization within Cuba, nor enacted a specific statutory authorization for the use of military force within or against Cuba.\n**(4)**\nThe use of force by the United States Armed Forces within or against Cuba, including the use of the United States Coast Guard and other components of the Armed Forces to conduct a blockade or quarantine of Cuba, constitutes the introduction of United States Armed Forces into hostilities within the meaning of section 4(a) of the War Powers Resolution ( 50 U.S.C. 1543(a) ).\n**(5)**\nSection 1013 of the Department of State Authorization Act, Fiscal Years 1984 and 1985 ( 50 U.S.C. 1546a ) provides that any joint resolution or bill requiring the removal of United States Armed Forces from imminent engagement in hostilities without a declaration of war or specific statutory authorization shall be considered in accordance with the expedited procedures under section 601(b) of the International Security and Arms Export Control Act of 1976 ( Public Law 94\u2013329 ).\n#### 2. Removal of United States Armed Forces from hostilities within or against Cuba\n##### (a) Removal\nPursuant to section 1013 of the Department of State Authorization Act, Fiscal Years 1984 and 1985 ( 50 U.S.C. 1546a ), and in accordance with section 601(b) of the International Security Assistance and Arms Export Control Act of 1976 ( Public Law 94\u2013329 ), Congress hereby directs the President to remove the United States Armed Forces from hostilities within or against Cuba, unless explicitly authorized by a declaration of war or a specific authorization for use of military force.\n##### (b) Rule of construction\nNothing in this section may be construed to prevent the United States from defending itself from an armed attack, the threat of an imminent armed attack, or the lawful execution of counternarcotics operations.",
      "versionDate": "2026-03-24",
      "versionType": "IH"
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
        "actionDate": "2026-04-28",
        "text": "The motion to discharge fell when the point of order was well taken."
      },
      "number": "124",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution to direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
      "type": "SJRES"
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
            "name": "Caribbean area",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "Cuba",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2026-05-04T16:00:10Z"
          },
          {
            "name": "War and emergency powers",
            "updateDate": "2026-05-04T16:00:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-03-27T22:04:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-24",
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
          "measure-id": "id119hjres153",
          "measure-number": "153",
          "measure-type": "hjres",
          "orig-publish-date": "2026-03-24",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres153v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2026-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities within or against Cuba\u00a0unless a declaration of war or authorization to use military force for such purpose has been enacted.</p><p>The resolution specifies that it shall not be construed to prevent the United States from defending itself from an armed attack, the threat of an imminent armed attack, or the lawful execution of\u00a0counternarcotics operations.</p>"
        },
        "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres153.xml",
    "summary": {
      "actionDate": "2026-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities within or against Cuba\u00a0unless a declaration of war or authorization to use military force for such purpose has been enacted.</p><p>The resolution specifies that it shall not be construed to prevent the United States from defending itself from an armed attack, the threat of an imminent armed attack, or the lawful execution of\u00a0counternarcotics operations.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hjres153"
    },
    "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress."
  },
  "summaries": [
    {
      "actionDate": "2026-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities within or against Cuba\u00a0unless a declaration of war or authorization to use military force for such purpose has been enacted.</p><p>The resolution specifies that it shall not be construed to prevent the United States from defending itself from an armed attack, the threat of an imminent armed attack, or the lawful execution of\u00a0counternarcotics operations.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hjres153"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres153ih.xml"
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
      "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T17:18:23Z"
    },
    {
      "title": "To direct the removal of United States Armed Forces from hostilities within or against the Republic of Cuba that have not been authorized by Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T08:06:15Z"
    }
  ]
}
```
