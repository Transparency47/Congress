# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/79?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/79
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act".
- Congress: 119
- Bill type: HJRES
- Bill number: 79
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-12-06T06:27:23Z
- Update date including text: 2025-12-06T06:27:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H1328-1329)
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H1328-1329)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/79",
    "number": "79",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "F000482",
        "district": "",
        "firstName": "Julie",
        "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
        "lastName": "Fedorchak",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\".",
    "type": "HJRES",
    "updateDate": "2025-12-06T06:27:23Z",
    "updateDateIncludingText": "2025-12-06T06:27:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1328-1329)",
      "type": "IntroReferral"
    },
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
          "date": "2025-03-24T16:03:45Z",
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
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres79ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 79\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Ms. Fedorchak (for herself, Mr. Balderson , and Mr. Allen ) submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act .\nThat Congress disapproves the final rule submitted by the Environmental Protection Agency relating to Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act (89 Fed. Reg. 73293 (September 10, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-03-24",
      "versionType": "IH"
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
        "actionDate": "2025-06-20",
        "text": "Became Public Law No: 119-20."
      },
      "number": "31",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\".",
      "type": "SJRES"
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
        "updateDate": "2025-03-26T12:44:49Z"
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
          "measure-id": "id119hjres79",
          "measure-number": "79",
          "measure-type": "hjres",
          "orig-publish-date": "2025-03-24",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres79v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency final rule titled <em>Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act</em> (89 Fed. Reg. 73293) and published on September 10, 2024. Among other elements, the rule requires sources of persistent and bioaccumulative hazardous air pollutants to continue to comply with certain major source emission standards under the Clean Air Act even if the sources reclassify as area sources.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres79.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency final rule titled <em>Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act</em> (89 Fed. Reg. 73293) and published on September 10, 2024. Among other elements, the rule requires sources of persistent and bioaccumulative hazardous air pollutants to continue to comply with certain major source emission standards under the Clean Air Act even if the sources reclassify as area sources.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hjres79"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency final rule titled <em>Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act</em> (89 Fed. Reg. 73293) and published on September 10, 2024. Among other elements, the rule requires sources of persistent and bioaccumulative hazardous air pollutants to continue to comply with certain major source emission standards under the Clean Air Act even if the sources reclassify as area sources.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hjres79"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres79ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T08:18:26Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Review of Final Rule Reclassification of Major Sources as Area Sources Under Section 112 of the Clean Air Act\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T08:05:41Z"
    }
  ]
}
```
