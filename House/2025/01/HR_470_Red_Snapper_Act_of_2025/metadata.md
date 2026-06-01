# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/470
- Title: Red Snapper Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 470
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-05T22:03:02Z
- Update date including text: 2025-12-05T22:03:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/470",
    "number": "470",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "R000609",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. Rutherford, John H. [R-FL-5]",
        "lastName": "Rutherford",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Red Snapper Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:03:02Z",
    "updateDateIncludingText": "2025-12-05T22:03:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MS"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 470\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Rutherford (for himself, Mr. Soto , Mr. Bean of Florida , Mr. Carter of Georgia , Ms. Mace , Mr. Webster of Florida , Mr. Bilirakis , Mr. Donalds , Mr. Scott Franklin of Florida , Ms. Salazar , Mr. Dunn of Florida , Ms. Lee of Florida , Mr. Mast , Mr. Gimenez , Mr. Fry , Mr. Austin Scott of Georgia , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide that the Secretary of Commerce shall not issue an interim or final rule or Secretarial Amendment that includes an area or bottom closure in the South Atlantic for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region until the South Atlantic Great Red Snapper Count study is complete and the data related to that study is integrated into the stock assessment.\n#### 1. Short title\nThis Act may be cited as the Red Snapper Act of 2025 .\n#### 2. Conditions for rules and Secretarial Amendments related to certain area closures\n##### (a) Findings\nCongress finds the following:\n**(1)**\nFishing is a major economic driver in the South Atlantic. In Florida alone, recreational anglers provide $14,000,000,000 in economic output and support 119,000 jobs.\n**(2)**\nRed snapper is a highly prized and sought after reef fish by both recreational and commercial fishermen.\n**(3)**\nThe 6-day recreational red snapper season in 2018 added $13,000,000 to the gross domestic product of the South Atlantic region.\n**(4)**\nSince 2010, fishery managers have successfully been working to rebuild the red snapper stock in the South Atlantic. There is currently record high abundance and strong recruitment within the stock.\n**(5)**\nThis record abundance has led to increased out-of-season encounters and discards which is driving red snapper mortality.\n**(6)**\nDespite these increased discards, it is the overriding opinion of the South Atlantic Fishery Management Council\u2019s Snapper Grouper Advisory Panel that based on members\u2019 collective on-the-water experience, the red snapper fishery is recovered.\n**(7)**\nHowever, options for future consideration to reduce out-of-season encounters and red snapper mortalities include shorter seasons and broad area closures for the snapper-grouper fishery in the South Atlantic.\n**(8)**\nThe State of Florida is concerned with the economic implications of area closures for the South Atlantic snapper-grouper recreational fishery.\n**(9)**\n$8,700,000 has been invested in independent survey data over the last 3 fiscal years, including $3,300,000 for the South Atlantic Great Red Snapper Count to estimate the number of red snapper (Lutjanus campechanus) in the South Atlantic waters from North Carolina to Florida.\n**(10)**\nThe National Marine Fisheries Service should incorporate data from this survey into the National Marine Fisheries Service stock assessments as expeditiously as possible to better inform fishery management decisions.\n##### (b) Condition on issuance of certain rule or Secretarial Amendment\nThe Secretary of Commerce shall not issue an interim or final rule or a Secretarial Amendment that includes an area or bottom closure in the South Atlantic for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region until\u2014\n**(1)**\nthe South Atlantic Great Red Snapper Count study is complete; and\n**(2)**\nthe data related to that study is integrated into the first South Atlantic red snapper Southeast Data, Assessment and Review stock assessment that is carried out after the date of the enactment of this section.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "111",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Red Snapper Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Atlantic Coast (U.S.)",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Atlantic Ocean",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Gulf of Mexico",
            "updateDate": "2025-02-24T21:00:38Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-02-24T21:00:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-19T14:32:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr470",
          "measure-number": "470",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr470v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Red Snapper Act of 2025</strong></p><p>This bill prohibits the National Oceanic and Atmospheric Administration (NOAA) from restricting certain fishing activities in the South Atlantic until data from the South Atlantic Great Red Snapper Count study is integrated into the next South Atlantic red snapper Southeast\u00a0Data, Assessment, and Review (SEDAR) stock assessment.\u00a0</p><p>The bill provides that NOAA may not issue an interim rule,\u00a0final rule, or Secretarial Amendment\u00a0establishing an area closure or a bottom fishing closure for specified species\u00a0until (1) the study is complete; and (2) the study data is integrated into the first South Atlantic red snapper SEDAR stock assessment\u00a0that is carried out after the bill's enactment.\u00a0The limitation applies to fishing for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region, including red snapper, grouper, and porgy.</p><p>(Closures generally\u00a0restrict\u00a0recreational and commercial fishing to prevent overfishing and for other conservation purposes.)</p>"
        },
        "title": "Red Snapper Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr470.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Red Snapper Act of 2025</strong></p><p>This bill prohibits the National Oceanic and Atmospheric Administration (NOAA) from restricting certain fishing activities in the South Atlantic until data from the South Atlantic Great Red Snapper Count study is integrated into the next South Atlantic red snapper Southeast\u00a0Data, Assessment, and Review (SEDAR) stock assessment.\u00a0</p><p>The bill provides that NOAA may not issue an interim rule,\u00a0final rule, or Secretarial Amendment\u00a0establishing an area closure or a bottom fishing closure for specified species\u00a0until (1) the study is complete; and (2) the study data is integrated into the first South Atlantic red snapper SEDAR stock assessment\u00a0that is carried out after the bill's enactment.\u00a0The limitation applies to fishing for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region, including red snapper, grouper, and porgy.</p><p>(Closures generally\u00a0restrict\u00a0recreational and commercial fishing to prevent overfishing and for other conservation purposes.)</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr470"
    },
    "title": "Red Snapper Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Red Snapper Act of 2025</strong></p><p>This bill prohibits the National Oceanic and Atmospheric Administration (NOAA) from restricting certain fishing activities in the South Atlantic until data from the South Atlantic Great Red Snapper Count study is integrated into the next South Atlantic red snapper Southeast\u00a0Data, Assessment, and Review (SEDAR) stock assessment.\u00a0</p><p>The bill provides that NOAA may not issue an interim rule,\u00a0final rule, or Secretarial Amendment\u00a0establishing an area closure or a bottom fishing closure for specified species\u00a0until (1) the study is complete; and (2) the study data is integrated into the first South Atlantic red snapper SEDAR stock assessment\u00a0that is carried out after the bill's enactment.\u00a0The limitation applies to fishing for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region, including red snapper, grouper, and porgy.</p><p>(Closures generally\u00a0restrict\u00a0recreational and commercial fishing to prevent overfishing and for other conservation purposes.)</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr470"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr470ih.xml"
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
      "title": "Red Snapper Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Red Snapper Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the Secretary of Commerce shall not issue an interim or final rule or Secretarial Amendment that includes an area or bottom closure in the South Atlantic for species managed under the Fishery Management Plan for the Snapper-Grouper Fishery of the South Atlantic Region until the South Atlantic Great Red Snapper Count study is complete and the data related to that study is integrated into the stock assessment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T10:48:16Z"
    }
  ]
}
```
