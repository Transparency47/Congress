# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/30?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/30
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020".
- Congress: 119
- Bill type: HJRES
- Bill number: 30
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2026-01-09T05:26:14Z
- Update date including text: 2026-01-09T05:26:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/30",
    "number": "30",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\".",
    "type": "HJRES",
    "updateDate": "2026-01-09T05:26:14Z",
    "updateDateIncludingText": "2026-01-09T05:26:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:02:05Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OH"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres30ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 30\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Dunn of Florida (for himself, Mr. Ogles , Mr. Rulli , and Mr. Messmer ) submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020 .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020 (89 Fed. Reg. 82682 (October 11, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "14",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\".",
      "type": "SJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "38",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\".",
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
        "updateDate": "2025-01-27T17:33:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hjres30",
          "measure-number": "30",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres30v00",
            "update-date": "2025-03-04"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency\u00a0rule titled <em>Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020</em> and published on October 11, 2024. The rule establishes an emission reduction and reclamation program for the management of hydrofluorocarbons, which are greenhouse gases. The rule also establishes alternative Resource Conservation and Recovery Act standards for certain ignitable spent refrigerants being recycled for reuse.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres30.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency\u00a0rule titled <em>Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020</em> and published on October 11, 2024. The rule establishes an emission reduction and reclamation program for the management of hydrofluorocarbons, which are greenhouse gases. The rule also establishes alternative Resource Conservation and Recovery Act standards for certain ignitable spent refrigerants being recycled for reuse.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hjres30"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency\u00a0rule titled <em>Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020</em> and published on October 11, 2024. The rule establishes an emission reduction and reclamation program for the management of hydrofluorocarbons, which are greenhouse gases. The rule also establishes alternative Resource Conservation and Recovery Act standards for certain ignitable spent refrigerants being recycled for reuse.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hjres30"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres30ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-25T09:48:49Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Phasedown of Hydrofluorocarbons: Management of Certain Hydrofluorocarbons and Substitutes Under the American Innovation and Manufacturing Act of 2020\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-25T09:05:23Z"
    }
  ]
}
```
