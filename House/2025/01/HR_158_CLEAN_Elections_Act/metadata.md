# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/158
- Title: CLEAN Elections Act
- Congress: 119
- Bill type: HR
- Bill number: 158
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-17T09:06:09Z
- Update date including text: 2025-12-17T09:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/158",
    "number": "158",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "CLEAN Elections Act",
    "type": "HR",
    "updateDate": "2025-12-17T09:06:09Z",
    "updateDateIncludingText": "2025-12-17T09:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:27:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "VA"
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
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr158ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 158\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the use of independent nonpartisan commissions to carry out congressional redistricting.\n#### 1. Short title\nThis Act may be cited as the Citizen Legislature Anti-Corruption Reform of Elections Act or the CLEAN Elections Act .\n#### 2. Requiring use of independent nonpartisan commissions to carry out redistricting\n##### (a) Requirement\n**(1) Congressional redistricting**\nEach State shall conduct Congressional redistricting (beginning with the redistricting carried out pursuant to the decennial census conducted during 2020) in accordance with a redistricting plan developed by a nonpartisan independent redistricting commission.\n**(2) Redistricting for State legislative districts**\nNotwithstanding any other provision of law, a State may not use any funds provided by the Federal Government directly for election administration purposes unless the State certifies to the Election Assistance Commission that the State conducts redistricting for State legislative districts in the State (beginning with the first such redistricting carried out after the date of the enactment of this Act) in accordance with a redistricting plan developed by a nonpartisan independent redistricting commission.\n##### (b) Nonpartisan independent status\nFor purposes of this section, a commission shall be considered to be a nonpartisan independent commission if\u2014\n**(1)**\nthe number of its members who are affiliated with the political party with the largest percentage of the registered voters in the State who are affiliated with a political party (as determined with respect to the most recent statewide election for Federal office held in the State for which such information is available) is equal to the number of its members who are affiliated with the political party with the second largest percentage of the registered voters in the State who are affiliated with a political party (as so determined); and\n**(2)**\nnone of its members is an elected public official.\n##### (c) State defined\nIn this section, the term State means each of the several States.",
      "versionDate": "2025-01-03",
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
            "name": "Congressional districts and representation",
            "updateDate": "2025-02-19T21:18:50Z"
          },
          {
            "name": "Congressional elections",
            "updateDate": "2025-02-19T21:19:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-19T21:18:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:04:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr158",
          "measure-number": "158",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr158v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Citizen Legislature Anti-Corruption Reform of Elections Act or the CLEAN Elections Act</strong></p><p>This bill establishes requirements for nonpartisan redistricting.</p><p>States must conduct congressional redistricting using a plan developed by a nonpartisan independent redistricting commission, beginning with the 2020 census.</p><p>A state may not use federal funds provided for election administration purposes unless it certifies to the Election Assistance Commission that it conducts redistricting for its state legislative districts using a plan developed by a nonpartisan independent redistricting commission.</p>"
        },
        "title": "CLEAN Elections Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr158.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Citizen Legislature Anti-Corruption Reform of Elections Act or the CLEAN Elections Act</strong></p><p>This bill establishes requirements for nonpartisan redistricting.</p><p>States must conduct congressional redistricting using a plan developed by a nonpartisan independent redistricting commission, beginning with the 2020 census.</p><p>A state may not use federal funds provided for election administration purposes unless it certifies to the Election Assistance Commission that it conducts redistricting for its state legislative districts using a plan developed by a nonpartisan independent redistricting commission.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr158"
    },
    "title": "CLEAN Elections Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Citizen Legislature Anti-Corruption Reform of Elections Act or the CLEAN Elections Act</strong></p><p>This bill establishes requirements for nonpartisan redistricting.</p><p>States must conduct congressional redistricting using a plan developed by a nonpartisan independent redistricting commission, beginning with the 2020 census.</p><p>A state may not use federal funds provided for election administration purposes unless it certifies to the Election Assistance Commission that it conducts redistricting for its state legislative districts using a plan developed by a nonpartisan independent redistricting commission.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr158"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr158ih.xml"
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
      "title": "CLEAN Elections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAN Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Citizen Legislature Anti-Corruption Reform of Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the use of independent nonpartisan commissions to carry out congressional redistricting.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:23Z"
    }
  ]
}
```
