# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/46?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/46
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)".
- Congress: 119
- Bill type: HJRES
- Bill number: 46
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-04-07T22:49:57Z
- Update date including text: 2025-04-07T22:49:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/46",
    "number": "46",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001116",
        "district": "9",
        "firstName": "Andrew",
        "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
        "lastName": "Clyde",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)\".",
    "type": "HJRES",
    "updateDate": "2025-04-07T22:49:57Z",
    "updateDateIncludingText": "2025-04-07T22:49:57Z"
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
          "date": "2025-02-12T15:06:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres46ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 46\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Clyde submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA) .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA) (89 Fed. Reg. 91486 (November 19, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-12",
      "versionType": "IH"
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
        "updateDate": "2025-02-14T13:22:56Z"
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
          "measure-id": "id119hjres46",
          "measure-number": "46",
          "measure-type": "hjres",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres46v00",
            "update-date": "2025-04-07"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency rule relating to <em>Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 91486) and published on November 19, 2024. Among other elements, the rule revised regulations for two of the five persistent, bioaccumulative, and toxic chemicals to address implementation issues and further reduce potential for exposures to such chemicals for humans and the environment (e.g., requiring the use of personal protective equipment during certain activities involving decabromodiphenyl ether).\u00a0</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres46.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency rule relating to <em>Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 91486) and published on November 19, 2024. Among other elements, the rule revised regulations for two of the five persistent, bioaccumulative, and toxic chemicals to address implementation issues and further reduce potential for exposures to such chemicals for humans and the environment (e.g., requiring the use of personal protective equipment during certain activities involving decabromodiphenyl ether).\u00a0</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hjres46"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency rule relating to <em>Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)</em> (89 Fed. Reg. 91486) and published on November 19, 2024. Among other elements, the rule revised regulations for two of the five persistent, bioaccumulative, and toxic chemicals to address implementation issues and further reduce potential for exposures to such chemicals for humans and the environment (e.g., requiring the use of personal protective equipment during certain activities involving decabromodiphenyl ether).\u00a0</p>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hjres46"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres46ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:34Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Decabromodiphenyl Ether and Phenol, Isopropylated Phosphate (3:1); Revision to the Regulation of Persistent, Bioaccumulative, and Toxic Chemicals Under the Toxic Substances Control Act (TSCA)\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:06:24Z"
    }
  ]
}
```
