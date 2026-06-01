# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2288
- Title: Common Sense Air Regulations Act
- Congress: 119
- Bill type: HR
- Bill number: 2288
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-06-27T21:00:36Z
- Update date including text: 2025-06-27T21:00:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2288",
    "number": "2288",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Common Sense Air Regulations Act",
    "type": "HR",
    "updateDate": "2025-06-27T21:00:36Z",
    "updateDateIncludingText": "2025-06-27T21:00:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:01:10Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-26",
      "state": "VA"
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
      "sponsorshipDate": "2025-04-29",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2288ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2288\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Carter of Georgia (for himself, Mr. LaMalfa , Mr. Pfluger , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo nullify the final rule of the Environmental Protection Agency titled Reconsideration of the National Ambient Air Quality Standards for Particulate Matter .\n#### 1. Short title\nThis Act may be cited as the Common Sense Air Regulations Act .\n#### 2. Nullification of final rule relating to Reconsideration of the National Ambient Air Quality Standards for Particulate Matter\nThe final rule of the Environmental Protection Agency titled Reconsideration of the National Ambient Air Quality Standards for Particulate Matter (89 Fed. Reg. 16202 (March 6, 2024)) shall have no force or effect.",
      "versionDate": "2025-03-24",
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
        "name": "Environmental Protection",
        "updateDate": "2025-04-03T16:28:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119hr2288",
          "measure-number": "2288",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-24",
          "originChamber": "HOUSE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2288v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Common Sense Air Regulations Act</strong></p><p>This bill nullifies the Environmental Protection Agency (EPA) final rule titled <em>Reconsideration of the National Ambient Air Quality Standards for Particulate Matter</em> (89 Fed.\u00a0Reg. 16202) and published on March 6, 2024. Among other elements, the rule revised primary (health-based) National Ambient Air Quality Standards (NAAQS) for Particulate Matter under the Clean Air Act. NAAQS are air quality standards set and adjusted by the EPA to protect public health and the environment from certain pollutants.</p>"
        },
        "title": "Common Sense Air Regulations Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2288.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Common Sense Air Regulations Act</strong></p><p>This bill nullifies the Environmental Protection Agency (EPA) final rule titled <em>Reconsideration of the National Ambient Air Quality Standards for Particulate Matter</em> (89 Fed.\u00a0Reg. 16202) and published on March 6, 2024. Among other elements, the rule revised primary (health-based) National Ambient Air Quality Standards (NAAQS) for Particulate Matter under the Clean Air Act. NAAQS are air quality standards set and adjusted by the EPA to protect public health and the environment from certain pollutants.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2288"
    },
    "title": "Common Sense Air Regulations Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Common Sense Air Regulations Act</strong></p><p>This bill nullifies the Environmental Protection Agency (EPA) final rule titled <em>Reconsideration of the National Ambient Air Quality Standards for Particulate Matter</em> (89 Fed.\u00a0Reg. 16202) and published on March 6, 2024. Among other elements, the rule revised primary (health-based) National Ambient Air Quality Standards (NAAQS) for Particulate Matter under the Clean Air Act. NAAQS are air quality standards set and adjusted by the EPA to protect public health and the environment from certain pollutants.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2288"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2288ih.xml"
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
      "title": "Common Sense Air Regulations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Common Sense Air Regulations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify the final rule of the Environmental Protection Agency titled \"Reconsideration of the National Ambient Air Quality Standards for Particulate Matter\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:23Z"
    }
  ]
}
```
