# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1281
- Title: RIDE Act
- Congress: 119
- Bill type: S
- Bill number: 1281
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1281",
    "number": "1281",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "RIDE Act",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
        "item": [
          {
            "date": "2025-04-03T17:26:31Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-03T17:26:31Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-14",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NH"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1281is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1281\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Tillis (for himself, Ms. Klobuchar , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a new nonimmigrant visa for mobile entertainment workers.\n#### 1. Short titles\nThis Act may be cited as the Restoring Industry Development in Entertainment Act or the RIDE Act .\n#### 2. Authorization of new P\u20134 nonimmigrant visa\nSection 101(a)(15)(P) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(P) ) is amended\u2014\n**(1)**\nin clause (iii)(II) by striking or at the end; and\n**(2)**\nby striking clause (iv) and inserting the following:\n(iv) is a mobile entertainment worker described in section 214(c)(4)(I) and for which mobile entertainment position the Department of Labor has certified that if\u2014 (I) there are not sufficient workers who are able, willing, and qualified, and who will be available at the time and place needed, to perform the labor or services required; and (II) the employment of the alien in such labor or services will not adversely affect the wages and working conditions of workers in the United States similarly employed; or (v) is the spouse or child of an alien described in clause (i), (ii), (iii), or (iv) and is accompanying, or following to join, such alien. .\n#### 3. Mobile entertainment workers\nSection 214(c)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1184(c)(4) ) is amended by adding at the end the following:\n(I) (i) For purposes of section 101(a)(15)(P)(iv), an alien is a mobile entertainment worker described in this subparagraph if the alien seeks to enter the United States temporarily and solely for the purpose of performing functions that are integral and essential to the operation of a mobile entertainment provider, including\u2014 (I) transporting, assembly, operation, disassembly, and maintenance of mobile entertainment attractions, structures, and equipment, including rides, games, novelties, and food or beverage concessions; and (II) other functions that are common in the mobile entertainment industry and are necessary for the safe and efficient operation of the mobile entertainment provider. (ii) In this subparagraph, the term mobile entertainment provider means\u2014 (I) a carnival or circus that travels around the United States on a temporary or seasonal basis; or (II) a provider of services normally affiliated with a carnival or circus, such as food and game concessions, that travels around the United States on a seasonal or temporary basis to provide services to\u2014 (aa) State, county, and local fairs and festivals; or (bb) support events sponsored by not-for-profit organizations for fundraising. .\n#### 4. Rulemaking\nThe Secretary of Homeland Security and the Secretary of Labor shall each publish in the Federal Register\u2014\n**(1)**\nnot later than 180 days after the date of the enactment of this Act, proposed rules implementing the amendments made by sections 2 and 3; and\n**(2)**\nnot later than 1 year after such date of enactment, final rules implementing the amendments made by sections 2 and 3.",
      "versionDate": "2025-04-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-05-02T14:11:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119s1281",
          "measure-number": "1281",
          "measure-type": "s",
          "orig-publish-date": "2025-04-03",
          "originChamber": "SENATE",
          "update-date": "2026-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1281v00",
            "update-date": "2026-02-20"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Restoring Industry Development in Entertainment Act or the RIDE Act</strong></p><p>This bill makes certain workers with a traveling carnival or circus eligible for P visas (nonimmigrant visas for athletes, artists, and entertainers).</p><p>Such visas shall be available for workers who perform functions that are integral and essential to the carnival or circus, such as transporting and assembling relevant structures and equipment.</p><p>Such visas shall only be available for a position if (1) there are not sufficient U.S. workers available, and (2) employing a non-U.S. national (<em>alien</em> under federal law) will not adversely affect the wages and working conditions of similarly employed U.S. workers.</p>"
        },
        "title": "RIDE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1281.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring Industry Development in Entertainment Act or the RIDE Act</strong></p><p>This bill makes certain workers with a traveling carnival or circus eligible for P visas (nonimmigrant visas for athletes, artists, and entertainers).</p><p>Such visas shall be available for workers who perform functions that are integral and essential to the carnival or circus, such as transporting and assembling relevant structures and equipment.</p><p>Such visas shall only be available for a position if (1) there are not sufficient U.S. workers available, and (2) employing a non-U.S. national (<em>alien</em> under federal law) will not adversely affect the wages and working conditions of similarly employed U.S. workers.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119s1281"
    },
    "title": "RIDE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring Industry Development in Entertainment Act or the RIDE Act</strong></p><p>This bill makes certain workers with a traveling carnival or circus eligible for P visas (nonimmigrant visas for athletes, artists, and entertainers).</p><p>Such visas shall be available for workers who perform functions that are integral and essential to the carnival or circus, such as transporting and assembling relevant structures and equipment.</p><p>Such visas shall only be available for a position if (1) there are not sufficient U.S. workers available, and (2) employing a non-U.S. national (<em>alien</em> under federal law) will not adversely affect the wages and working conditions of similarly employed U.S. workers.</p>",
      "updateDate": "2026-02-20",
      "versionCode": "id119s1281"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1281is.xml"
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
      "title": "RIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Industry Development in Entertainment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a new nonimmigrant visa for mobile entertainment workers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:21Z"
    }
  ]
}
```
