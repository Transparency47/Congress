# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/676
- Title: A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.
- Congress: 119
- Bill type: SRES
- Bill number: 676
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-22T19:45:21Z
- Update date including text: 2026-05-23T06:48:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1825)
- 2026-04-16 - IntroReferral: Submitted in Senate
- 2026-05-21 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)
- 2026-05-21 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)
- 2026-05-21 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-05-21 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- Latest action: 2026-04-16: Submitted in Senate

## Actions

- 2026-04-16 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1825)
- 2026-04-16 - IntroReferral: Submitted in Senate
- 2026-05-21 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)
- 2026-05-21 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)
- 2026-05-21 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-05-21 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/676",
    "number": "676",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
    "type": "SRES",
    "updateDate": "2026-05-22T19:45:21Z",
    "updateDateIncludingText": "2026-05-23T06:48:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2452)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1825)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
            "date": "2026-05-21T18:40:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-16T17:05:57Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres676is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 676\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Fetterman (for himself and Mr. McCormick ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nRESOLUTION\nRecognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.\nThat the Senate\u2014\n**(1)**\nsupports the recognition of National Mushroom Day;\n**(2)**\nhonors the Commonwealth of Pennsylvania for its unparalleled contributions to the national mushroom industry; and\n**(3)**\nrecognizes the role mushrooms play in a healthy diet that is rich in whole foods.",
      "versionDate": "2026-04-16",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres676ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 676\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Fetterman (for himself and Mr. McCormick ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nMay 21, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.\nThat the Senate\u2014\n**(1)**\nsupports the recognition of National Mushroom Day;\n**(2)**\nhonors the Commonwealth of Pennsylvania for its unparalleled contributions to the national mushroom industry; and\n**(3)**\nrecognizes the role mushrooms play in a healthy diet that is rich in whole foods.",
      "versionDate": "2026-05-21",
      "versionType": "ATS"
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
        "actionDate": "2026-04-16",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "1184",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
      "type": "HRES"
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-24T14:46:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-16",
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
          "measure-id": "id119sres676",
          "measure-number": "676",
          "measure-type": "sres",
          "orig-publish-date": "2026-04-16",
          "originChamber": "SENATE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres676v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2026-04-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>"
        },
        "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres676.xml",
    "summary": {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119sres676"
    },
    "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets."
  },
  "summaries": [
    {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119sres676"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres676is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres676ats.xml"
        }
      ],
      "type": "ATS"
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
      "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:27Z"
    },
    {
      "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:15:21Z"
    }
  ]
}
```
