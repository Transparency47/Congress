# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/69?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/69
- Title: Freedom to Petition the Government Act
- Congress: 119
- Bill type: HR
- Bill number: 69
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-12T21:12:26Z
- Update date including text: 2025-02-12T21:12:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/69",
    "number": "69",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Freedom to Petition the Government Act",
    "type": "HR",
    "updateDate": "2025-02-12T21:12:26Z",
    "updateDateIncludingText": "2025-02-12T21:12:26Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
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
          "date": "2025-01-03T16:09:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr69ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 69\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Ogles , and Mr. Crane ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 29, District of Columbia Official Code, to treat meetings held by nonprofit organizations with officials of the Federal Government which are held in the District of Columbia at locations owned or leased by the Federal Government as activities not constituting doing business in the District of Columbia for purposes of determining whether such organizations are required to register with the District of Columbia.\n#### 1. Short title\nThis Act may be cited as the Freedom to Petition the Government Act .\n#### 2. Treatment of meetings between nonprofit organizations and Federal officials as activities not constituting doing business in District of Columbia\nSection 29\u2013105.05(a), District of Columbia Official Code, is amended\u2014\n**(1)**\nby striking and at the end of paragraph (9);\n**(2)**\nby striking the period at the end of paragraph (10) and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(11) In the case of an entity that is described in section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code, holding a meeting with a Member of Congress or another officer, employee, or representative of the Federal Government at a location owned or leased by the Federal Government. .",
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
            "name": "District of Columbia",
            "updateDate": "2025-02-06T15:17:12Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-06T15:17:07Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-06T15:17:24Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-06T15:17:28Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-02-06T15:17:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-31T18:26:26Z"
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
          "measure-id": "id119hr69",
          "measure-number": "69",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr69v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freedom to Petition the Government Act</strong></p><p>This bill allows outside nonprofit organizations to meet with federal officials in the District of Columbia (DC) on federal property without having to register as businesses in DC. </p><p>Currently, entities that are formed outside of DC, including nonprofit organizations, must generally register with DC before doing business in DC. Under the bill, outside nonprofit organizations may meet with\u00a0federal government officials at federally leased or owned buildings in DC without having to register.</p><p>\u00a0</p>"
        },
        "title": "Freedom to Petition the Government Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr69.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom to Petition the Government Act</strong></p><p>This bill allows outside nonprofit organizations to meet with federal officials in the District of Columbia (DC) on federal property without having to register as businesses in DC. </p><p>Currently, entities that are formed outside of DC, including nonprofit organizations, must generally register with DC before doing business in DC. Under the bill, outside nonprofit organizations may meet with\u00a0federal government officials at federally leased or owned buildings in DC without having to register.</p><p>\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr69"
    },
    "title": "Freedom to Petition the Government Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom to Petition the Government Act</strong></p><p>This bill allows outside nonprofit organizations to meet with federal officials in the District of Columbia (DC) on federal property without having to register as businesses in DC. </p><p>Currently, entities that are formed outside of DC, including nonprofit organizations, must generally register with DC before doing business in DC. Under the bill, outside nonprofit organizations may meet with\u00a0federal government officials at federally leased or owned buildings in DC without having to register.</p><p>\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr69"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr69ih.xml"
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
      "title": "Freedom to Petition the Government Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T12:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom to Petition the Government Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-29T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 29, District of Columbia Official Code, to treat meetings held by nonprofit organizations with officials of the Federal Government which are held in the District of Columbia at locations owned or leased by the Federal Government as activities not constituting doing business in the District of Columbia for purposes of determining whether such organizations are required to register with the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T12:19:01Z"
    }
  ]
}
```
