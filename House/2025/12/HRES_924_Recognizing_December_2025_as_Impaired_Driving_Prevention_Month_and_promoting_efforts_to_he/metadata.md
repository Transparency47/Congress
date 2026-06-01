# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/924?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/924
- Title: Recognizing December 2025 as "Impaired Driving Prevention Month" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving.
- Congress: 119
- Bill type: HRES
- Bill number: 924
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-04-07T14:29:26Z
- Update date including text: 2026-04-07T14:29:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-03 - IntroReferral: Submitted in House
- 2025-12-03 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-03: Submitted in House

## Actions

- 2025-12-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-03 - IntroReferral: Submitted in House
- 2025-12-03 - IntroReferral: Submitted in House
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/924",
    "number": "924",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Recognizing December 2025 as \"Impaired Driving Prevention Month\" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving.",
    "type": "HRES",
    "updateDate": "2026-04-07T14:29:26Z",
    "updateDateIncludingText": "2026-04-07T14:29:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-12-03T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:27:33Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres924ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 924\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Pappas (for himself and Mr. Mann ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nRecognizing December 2025 as Impaired Driving Prevention Month and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving.\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the recognition of Impaired Driving Prevention Month to raise awareness about the dangers of impaired driving;\n**(2)**\nsupports the efforts of the Department of Transportation, State Departments of Transportation, State and local governments, and State and local law enforcement to prevent and stop impaired driving thereby saving lives; and\n**(3)**\nurges people across the United States to take preventable steps against impaired driving such as driving sober and planning ahead for a safe ride home.",
      "versionDate": "2025-12-03",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-05T16:18:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-03",
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
          "measure-id": "id119hres924",
          "measure-number": "924",
          "measure-type": "hres",
          "orig-publish-date": "2025-12-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres924v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-12-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the recognition of Impaired Driving Prevention Month.</p><p>The resolution also supports the efforts of the Department of Transportation, state and local governments, and state and local law enforcement to prevent and stop impaired driving.</p>"
        },
        "title": "Recognizing December 2025 as \"Impaired Driving Prevention Month\" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres924.xml",
    "summary": {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the recognition of Impaired Driving Prevention Month.</p><p>The resolution also supports the efforts of the Department of Transportation, state and local governments, and state and local law enforcement to prevent and stop impaired driving.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres924"
    },
    "title": "Recognizing December 2025 as \"Impaired Driving Prevention Month\" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving."
  },
  "summaries": [
    {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the recognition of Impaired Driving Prevention Month.</p><p>The resolution also supports the efforts of the Department of Transportation, state and local governments, and state and local law enforcement to prevent and stop impaired driving.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres924"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres924ih.xml"
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
      "title": "Recognizing December 2025 as \"Impaired Driving Prevention Month\" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T09:18:41Z"
    },
    {
      "title": "Recognizing December 2025 as \"Impaired Driving Prevention Month\" and promoting efforts to help prevent tragic and preventable crashes, deaths, and injuries caused by impaired driving.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T09:06:05Z"
    }
  ]
}
```
