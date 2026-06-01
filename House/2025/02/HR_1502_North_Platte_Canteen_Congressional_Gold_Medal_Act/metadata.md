# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1502
- Title: North Platte Canteen Congressional Gold Medal Act
- Congress: 119
- Bill type: HR
- Bill number: 1502
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-05-27T08:06:02Z
- Update date including text: 2026-05-27T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1502",
    "number": "1502",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "North Platte Canteen Congressional Gold Medal Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:02Z",
    "updateDateIncludingText": "2026-05-27T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:31:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NE"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NE"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "KS"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "KS"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "IA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "IL"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "MO"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
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
      "sponsorshipDate": "2026-05-21",
      "state": "CT"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "PA"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "OH"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "AL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "IL"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "OR"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "CO"
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
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "IL"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1502ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1502\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Smith of Nebraska (for himself, Mr. Bacon , and Mr. Flood ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo award a Congressional Gold Medal, collectively, to the individuals and communities who volunteered or donated items to the North Platte Canteen in North Platte, Nebraska, during World War II from December 25, 1941, to April 1, 1946.\n#### 1. Short title\nThis Act may be cited as the North Platte Canteen Congressional Gold Medal Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nHome-front volunteerism was integral to the victory of the United States during World War II. Numerous exemplars of patriotism emerged throughout the Midwest, galvanizing the rural United States and the rest of the country supporting the war effort.\n**(2)**\nThe North Platte Canteen in North Platte, Nebraska, was one of the largest volunteer efforts of World War II.\n**(3)**\nCanteen services boosted morale in the United States by providing free, wholesome entertainment to troops traveling across the country. Approximately 120 community-based canteens operated in the United States during World War II.\n**(4)**\nThe North Platte Canteen greeted and served food to approximately 6,000,000 U.S. troops traveling across the United States from December 25, 1941, to April 1, 1946.\n**(5)**\nOn December 17, 1941, the residents of North Platte, Nebraska, received information that a train of Nebraska National Guardsmen would be traveling through North Platte en route to the West Coast of the United States. Although the train carried members of the Kansas National Guard, residents of the community welcomed the men from Kansas with food and other items as an appreciation for their service.\n**(6)**\nOn December 18, 1941, Rae Wilson, of North Platte, proposed to her community the idea of establishing the North Platte Canteen so that residents could greet U.S. troops en route to serving the United States in the European Theater or the Pacific Theater.\n**(7)**\n55,000 individuals, the majority of whom were women, from 125 communities in Nebraska, Colorado, and Kansas donated food and volunteered at the North Platte Canteen for approximately 5 years.\n**(8)**\nThe North Platte Canteen provided hospitality to as many as 24 troop trains per day. During a 1-month period, the Canteen\u2019s volunteers served over 40,000 homemade cookies, 30,000 hard-boiled eggs, 6,500 doughnuts, 4,000 loaves of bread, 3,000 pounds of meat, 450 pounds of cheese, 60 quarts of peanut butter, 1,350 pounds of coffee, 1,000 quarts of cream, 750 dozen rolls, and 600 birthday cakes.\n**(9)**\nThe North Platte Canteen principally operated at the Union Pacific Railroad station in North Platte, Nebraska, with volunteers from local communities, organizations, churches, schools, and other groups, and without Federal assistance.\n**(10)**\n$137,000 in cash contributions supported the North Platte Canteen\u2019s operations for almost 5 years. The funds were raised through benefit dances, scrap-metal drives, school victory clubs, donation cans in local businesses, and from the relatives of troops who traveled through the North Platte area.\n**(11)**\nIn December 1943, the North Platte Canteen was honored by the United States Army with the presentation of the Meritorious Wartime Service Award by the Secretary of War.\n**(12)**\nIn 2004, the 108th Congress passed a resolution recognizing the heroic efforts of those who made enormous sacrifices to make the North Platte Canteen a success during World War II.\n#### 3. Congressional gold medal\n##### (a) Presentation authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the presentation, on behalf of Congress, of a gold medal of appropriate design to the individuals and communities who volunteered or donated items to the North Platte Canteen in North Platte, Nebraska, during World War II.\n##### (b) Design and striking\nFor purposes of the presentation described in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions to be determined by the Secretary.\n##### (c) Lincoln County Historical Museum\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the Lincoln County Historical Museum in North Platte, Nebraska, where it will be available for display as appropriate and available for research.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs of the medals, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nMedals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "645",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "North Platte Canteen Congressional Gold Medal Act",
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
            "name": "Congressional tributes",
            "updateDate": "2025-07-10T14:37:49Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-07-10T14:37:49Z"
          },
          {
            "name": "Nebraska",
            "updateDate": "2025-07-10T14:37:49Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-07-10T14:37:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T20:29:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1502",
          "measure-number": "1502",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1502v00",
            "update-date": "2025-08-08"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>North Platte Canteen Congressional Gold Medal Act</strong></p><p>This bill provides for the award of a Congressional Gold Medal to recognize the individuals and communities that provided financial and other support for the North Platte Canteen in North Platte, Nebraska, during World War II.</p>"
        },
        "title": "North Platte Canteen Congressional Gold Medal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1502.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>North Platte Canteen Congressional Gold Medal Act</strong></p><p>This bill provides for the award of a Congressional Gold Medal to recognize the individuals and communities that provided financial and other support for the North Platte Canteen in North Platte, Nebraska, during World War II.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119hr1502"
    },
    "title": "North Platte Canteen Congressional Gold Medal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>North Platte Canteen Congressional Gold Medal Act</strong></p><p>This bill provides for the award of a Congressional Gold Medal to recognize the individuals and communities that provided financial and other support for the North Platte Canteen in North Platte, Nebraska, during World War II.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119hr1502"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1502ih.xml"
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
      "title": "North Platte Canteen Congressional Gold Medal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "North Platte Canteen Congressional Gold Medal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional Gold Medal, collectively, to the individuals and communities who volunteered or donated items to the North Platte Canteen in North Platte, Nebraska, during World War II from December 25, 1941, to April 1, 1946.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T05:18:31Z"
    }
  ]
}
```
