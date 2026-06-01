# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7053?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7053
- Title: Preemption of Real Property Discrimination Act
- Congress: 119
- Bill type: HR
- Bill number: 7053
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-05-21T08:07:31Z
- Update date including text: 2026-05-21T08:07:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7053",
    "number": "7053",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Preemption of Real Property Discrimination Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:31Z",
    "updateDateIncludingText": "2026-05-21T08:07:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:02:35Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7053ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7053\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Green of Texas (for himself, Ms. Chu , and Ms. Meng ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo preempt State prohibitions on real estate purchases by foreign citizens, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preemption of Real Property Discrimination Act .\n#### 2. Preemption of State prohibitions on real estate purchases by foreign citizens\n##### (a) In general\nAny law of a State, the District of Columbia, or any territory of the United States that prohibits or otherwise restricts the purchase by an individual of real property within such State, District, or territory based on the citizenship of the purchaser is hereby preempted.\n##### (b) Enforcement\nThe Attorney General is authorized to enforce this section.\n##### (c) Private right of action\n**(1) In general**\nIn the case of any State, District, or territory that attempts to enforce a law preempted by subsection (a), an individual harmed by such action may bring a civil action against such State, District, or territory in any Federal court of competent jurisdiction.\n**(2) Injunctive relief**\nIn a civil action brought under paragraph (1) in which a plaintiff prevails, the court may award the plaintiff injunctive relief.",
      "versionDate": "2026-01-14",
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
        "name": "Law",
        "updateDate": "2026-02-10T14:53:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-14",
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
          "measure-id": "id119hr7053",
          "measure-number": "7053",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-14",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7053v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2026-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Preemption of Real Property Discrimination Act </b></p> <p>This bill preempts any state law that prohibits or restricts the purchase of real property by an individual based on the individual's citizenship. </p>"
        },
        "title": "Preemption of Real Property Discrimination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7053.xml",
    "summary": {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Preemption of Real Property Discrimination Act </b></p> <p>This bill preempts any state law that prohibits or restricts the purchase of real property by an individual based on the individual's citizenship. </p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr7053"
    },
    "title": "Preemption of Real Property Discrimination Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Preemption of Real Property Discrimination Act </b></p> <p>This bill preempts any state law that prohibits or restricts the purchase of real property by an individual based on the individual's citizenship. </p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr7053"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7053ih.xml"
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
      "title": "Preemption of Real Property Discrimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preemption of Real Property Discrimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To preempt State prohibitions on real estate purchases by foreign citizens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T06:48:22Z"
    }
  ]
}
```
