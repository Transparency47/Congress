# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1243
- Title: United Nations Voting Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1243
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-12-06T06:42:53Z
- Update date including text: 2025-12-06T06:42:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1243",
    "number": "1243",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "United Nations Voting Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-06T06:42:53Z",
    "updateDateIncludingText": "2025-12-06T06:42:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:05:35Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "AL"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1243ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1243\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Davidson (for himself, Mr. Weber of Texas , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit United States assistance to foreign countries that oppose the position of the United States in the United Nations.\n#### 1. Short title\nThis Act may be cited as the United Nations Voting Accountability Act of 2025 .\n#### 2. Prohibition on assistance to countries that oppose the position of the United States in the United Nations\n##### (a) Prohibition\nUnited States assistance may not be provided to a country that opposed the position of the United States in the United Nations.\n##### (b) Exemption due to change in government\n**(1) In general**\nThe Secretary of State may exempt a country from the prohibition described in subsection (a) if the Secretary determines that since the beginning of the most recent session of the General Assembly\u2014\n**(A)**\nthere has been a fundamental change in the leadership and policies of the government of a country to which the prohibition in such subsection applies; and\n**(B)**\nas a result of such change, the government of such country will no longer oppose the position of the United States in the United Nations.\n**(2) Duration of exemption**\nAn exemption under paragraph (1) shall be effective only until submission of the next report required under section 406 of the Foreign Relations Authorization Act, Fiscal Years 1990 and 1991 ( 22 U.S.C. 2414a ) that is submitted after the Secretary of State makes such an exemption.\n**(3) Notification and discussion**\nThe Secretary of State shall notify Congress with respect to an exemption made under paragraph (1), together with a discussion of the basis for the Secretary\u2019s determination with respect to each such exemption.\n##### (c) Definitions\nAs used in this Act\u2014\n**(1)**\nthe term opposed the position of the United States means, in the case of a country, that the country\u2019s recorded votes in the United Nations General Assembly during the most recent session of the General Assembly and, in the case of a country which is a member of the United Nations Security Council, the country\u2019s recorded votes both in the Security Council and the General Assembly during the most recent session of the General Assembly, were the same as the position of the United States less than 50 percent of the time, using for this purpose a comparison of the recorded vote cast by each member country with the recorded vote cast by the United States, as described in the annual report submitted to Congress pursuant to section 406 of the Foreign Relations Authorization Act, Fiscal Years 1990 and 1991;\n**(2)**\nthe term most recent session of the General Assembly means the most recently completed plenary session of the General Assembly for which a comparison of the vote cast by each member country with the vote cast by the United States is described in the most recent report submitted to Congress pursuant to section 406 of the Foreign Relations Authorization Act, Fiscal Years 1990 and 1991; and\n**(3)**\nthe term United States assistance means assistance under\u2014\n**(A)**\nchapter 4 of part II of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2346 et seq. ; relating to the economic support fund);\n**(B)**\nchapter 5 of part II of such Act ( 22 U.S.C. 2347 et seq. ; relating to international military education and training);\n**(C)**\nthe Foreign Military Financing Program account under section 23 of the Arms Export Control Act ( 22 U.S.C. 2763 ); and\n**(D)**\nany other monetary or physical assistance.\n##### (d) Effective date\nThis Act shall take effect upon the date of the submission to Congress of the report required under section 406 of the Foreign Relations Authorization Act, Fiscal Years 1990 and 1991, that is required to be submitted by March 31, 2026.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-06-25",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2170",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United Nations Voting Accountability Act of 2025",
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
        "updateDate": "2025-05-08T15:31:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1243",
          "measure-number": "1243",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1243v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United Nations Voting Accountability Act of 2025</strong></p><p>This bill prohibits giving assistance, such as various types of economic support or military training, to countries that shared U.S. positions on\u00a0less than 50% of the recorded votes in the most recent United Nations session.</p><p>A country may be exempted from this prohibition if the Department of State determines that the country will no longer oppose U.S. positions due to a fundamental change in the country's leadership and policies.</p>"
        },
        "title": "United Nations Voting Accountability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1243.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United Nations Voting Accountability Act of 2025</strong></p><p>This bill prohibits giving assistance, such as various types of economic support or military training, to countries that shared U.S. positions on\u00a0less than 50% of the recorded votes in the most recent United Nations session.</p><p>A country may be exempted from this prohibition if the Department of State determines that the country will no longer oppose U.S. positions due to a fundamental change in the country's leadership and policies.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr1243"
    },
    "title": "United Nations Voting Accountability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United Nations Voting Accountability Act of 2025</strong></p><p>This bill prohibits giving assistance, such as various types of economic support or military training, to countries that shared U.S. positions on\u00a0less than 50% of the recorded votes in the most recent United Nations session.</p><p>A country may be exempted from this prohibition if the Department of State determines that the country will no longer oppose U.S. positions due to a fundamental change in the country's leadership and policies.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr1243"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1243ih.xml"
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
      "title": "United Nations Voting Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United Nations Voting Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit United States assistance to foreign countries that oppose the position of the United States in the United Nations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:28Z"
    }
  ]
}
```
