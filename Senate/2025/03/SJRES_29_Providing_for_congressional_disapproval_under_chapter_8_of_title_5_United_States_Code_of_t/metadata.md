# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/29?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/29
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Air Plan Approval; Ohio; Withdrawal of Technical Amendment".
- Congress: 119
- Bill type: SJRES
- Bill number: 29
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2025-12-05T21:30:10Z
- Update date including text: 2025-12-05T21:30:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/29",
    "number": "29",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\".",
    "type": "SJRES",
    "updateDate": "2025-12-05T21:30:10Z",
    "updateDateIncludingText": "2025-12-05T21:30:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-03",
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
        "item": {
          "date": "2025-03-03T20:55:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres29is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 29\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Husted (for himself and Mr. Moreno ) introduced the following joint resolution; which was read twice and referred to the Committee on Environment and Public Works\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Air Plan Approval; Ohio; Withdrawal of Technical Amendment .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Air Plan Approval; Ohio; Withdrawal of Technical Amendment (90 Fed. Reg. 6811 (January 21, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2025-03-03",
      "versionType": "IS"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "66",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\".",
      "type": "HJRES"
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
        "updateDate": "2025-03-07T15:03:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119sjres29",
          "measure-number": "29",
          "measure-type": "sjres",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres29v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Air Plan Approval; Ohio; Withdrawal of Technical Amendment</em> (90 Fed. Reg. 6811) and published on January 21, 2025. Among other elements, the rule reversed a final rule from November 2020 that removed the Air Nuisance Rule (ANR) from the Ohio State Implementation Plan (SIP). The EPA determined its original action to remove the ANR was in error, and this rule reinstates the ANR. (Under the Clean Air Act, states must submit SIPs to comply with the National Ambient Air Quality Standards. This ANR was included in Ohio\u2019s SIP.)</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres29.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Air Plan Approval; Ohio; Withdrawal of Technical Amendment</em> (90 Fed. Reg. 6811) and published on January 21, 2025. Among other elements, the rule reversed a final rule from November 2020 that removed the Air Nuisance Rule (ANR) from the Ohio State Implementation Plan (SIP). The EPA determined its original action to remove the ANR was in error, and this rule reinstates the ANR. (Under the Clean Air Act, states must submit SIPs to comply with the National Ambient Air Quality Standards. This ANR was included in Ohio\u2019s SIP.)</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119sjres29"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Air Plan Approval; Ohio; Withdrawal of Technical Amendment</em> (90 Fed. Reg. 6811) and published on January 21, 2025. Among other elements, the rule reversed a final rule from November 2020 that removed the Air Nuisance Rule (ANR) from the Ohio State Implementation Plan (SIP). The EPA determined its original action to remove the ANR was in error, and this rule reinstates the ANR. (Under the Clean Air Act, states must submit SIPs to comply with the National Ambient Air Quality Standards. This ANR was included in Ohio\u2019s SIP.)</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119sjres29"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres29is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:58Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Air Plan Approval; Ohio; Withdrawal of Technical Amendment\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T11:56:20Z"
    }
  ]
}
```
