# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2968?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2968
- Title: Business over Ballots Act
- Congress: 119
- Bill type: HR
- Bill number: 2968
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-10-22T08:05:35Z
- Update date including text: 2025-10-22T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-17 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-30 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-17 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-30 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2968",
    "number": "2968",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Business over Ballots Act",
    "type": "HR",
    "updateDate": "2025-10-22T08:05:35Z",
    "updateDateIncludingText": "2025-10-22T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
        "item": [
          {
            "date": "2025-04-30T17:30:52Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-17T13:31:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-17T13:31:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MO"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MP"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "KS"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "WI"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "GA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MT"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "MN"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2968ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2968\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Williams of Texas (for himself, Mr. Alford , Ms. King-Hinds , Ms. Van Duyne , Mr. Schmidt , Mr. Meuser , Mr. Ellzey , Mr. Wied , Mr. Jack , Mr. Downing , Mr. Bresnahan , Mr. Patronis , and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Small Business , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the authority of the Small Business Administration to facilitate access to voter registration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Business over Ballots Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Small Business Administration should focus on aiding and assisting small business concerns;\n**(2)**\nfacilitating access to voter registration is beyond the scope of the mission of the Administration and the authority of the Administration under Federal law; and\n**(3)**\nany Executive order issued by the President may not conflict with this Act or otherwise compel the Administrator of the Small Business Administration to facilitate access to voter registration.\n#### 3. Limitations on facilitation of access to voter registration by the Small Business Administration\n##### (a) Prohibition\nThe Administrator of the Small Business Administration may not take any action to facilitate access to voter registration other than actions authorized by Federal law.\n##### (b) Terms of contracts\nOn or after the date of the enactment of this Act, any contract or other agreement entered into by the Administrator to provide assistance to a person shall include a term stating that such person may not use such assistance to facilitate access to voter registration.\n##### (c) Existing recipients\nA recipient of assistance from the Administrator may not use such assistance to facilitate access to voter registration unless explicitly authorized by the terms of such assistance.\n##### (d) Covered entities\nThe Administrator may not use, act through, or otherwise make a request of a covered entity to engage in activities to facilitate access to voter registration unless the Administrator is so authorized by Congress.\n##### (e) Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Small Business Administration.\n**(2) Covered entity**\nThe term covered entity \u2014\n**(A)**\nmeans an entity, State government, or unit of local government that receives funding or other assistance from the Administrator under a contract, cooperative agreement, memorandum of understanding, or other agreement to carry out a program administered by the Administrator; and\n**(B)**\ndoes not include a person that receives a loan or loan guarantee under section 7 of the Small Business Act ( 15 U.S.C. 636 ).",
      "versionDate": "2025-04-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-20T18:27:08Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-05-20T18:25:54Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-05-20T18:26:25Z"
          },
          {
            "name": "Small Business Administration",
            "updateDate": "2025-05-20T18:26:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-16T13:01:54Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2968ih.xml"
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
      "title": "Business over Ballots Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Business over Ballots Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the authority of the Small Business Administration to facilitate access to voter registration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:33:29Z"
    }
  ]
}
```
