# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/584
- Title: No Medicaid for Illegal Immigrants Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 584
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2026-04-28T08:06:49Z
- Update date including text: 2026-04-28T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/584",
    "number": "584",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "No Medicaid for Illegal Immigrants Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:49Z",
    "updateDateIncludingText": "2026-04-28T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WI"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NJ"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "OK"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "VA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "ND"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr584ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 584\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to prohibit States from making medical assistance available to certain individuals under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the No Medicaid for Illegal Immigrants Act of 2025 .\n#### 2. Prohibiting States from making medical assistance available to certain individuals under the Medicaid program\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking and at the end;\n**(2)**\nin paragraph (87), by striking the period and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87) the following new paragraph:\n(88) notwithstanding section 1903(v)(4), provide that no medical assistance (other than such assistance for which payment is available pursuant to section 1903(v)(2)) is made available under such plan (or under a waiver of such plan) to an alien who is not lawfully admitted for permanent residence or otherwise permanently residing in the United States under color of law. .",
      "versionDate": "2025-01-21",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-03-03T17:38:23Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2025-03-03T17:38:14Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-03-03T17:38:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-20T19:15:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr584",
          "measure-number": "584",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr584v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Medicaid for Illegal Immigrants Act of 2025</strong></p><p>This bill prohibits state Medicaid programs from covering individuals who are unlawfully present in the United States, except for certain emergency services for which federal payment is authorized under current law.</p>"
        },
        "title": "No Medicaid for Illegal Immigrants Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr584.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Medicaid for Illegal Immigrants Act of 2025</strong></p><p>This bill prohibits state Medicaid programs from covering individuals who are unlawfully present in the United States, except for certain emergency services for which federal payment is authorized under current law.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr584"
    },
    "title": "No Medicaid for Illegal Immigrants Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Medicaid for Illegal Immigrants Act of 2025</strong></p><p>This bill prohibits state Medicaid programs from covering individuals who are unlawfully present in the United States, except for certain emergency services for which federal payment is authorized under current law.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr584"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr584ih.xml"
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
      "title": "No Medicaid for Illegal Immigrants Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Medicaid for Illegal Immigrants Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to prohibit States from making medical assistance available to certain individuals under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:31Z"
    }
  ]
}
```
