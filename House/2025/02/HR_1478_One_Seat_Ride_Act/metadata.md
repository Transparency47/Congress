# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1478
- Title: One Seat Ride Act
- Congress: 119
- Bill type: HR
- Bill number: 1478
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-04-11T12:28:54Z
- Update date including text: 2025-04-11T12:28:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-21 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-21 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1478",
    "number": "1478",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "One Seat Ride Act",
    "type": "HR",
    "updateDate": "2025-04-11T12:28:54Z",
    "updateDateIncludingText": "2025-04-11T12:28:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:31:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-21T22:22:17Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1478ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1478\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Kean (for himself and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to conduct a study on the costs and benefits of commuter rail passenger transportation involving transfers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Seat Ride Act .\n#### 2. Study on commuter service\n##### (a) In general\nThe Secretary of Transportation shall conduct a study identifying the benefits of commuter rail passenger transportation and major obstacles to providing commuter rail passenger transportation that does not involve a transfer for passengers.\n##### (b) Requirements\nIn conducting the study under subsection (a), the Secretary shall\u2014\n**(1)**\nconsider economic, logistical, and quality of life factors in analyzing the major obstacles to implementing single-seat trips on commuter rail passenger transportation for as many passengers as possible; and\n**(2)**\ninclude in such study an analysis of the costs and benefits with respect to single-seat trips on commuter rail passenger transportation on the New Jersey Transit Raritan Valley line during peak hours and the impact such trips would have on other New Jersey Transit lines.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate a report on the study required under subsection (a).\n##### (d) Commuter rail passenger transportation defined\nIn this section, the term commuter rail passenger transportation has the meaning given such term in section 24102 of title 49, United States Code.",
      "versionDate": "2025-02-21",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-18T14:17:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1478",
          "measure-number": "1478",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-04-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1478v00",
            "update-date": "2025-04-11"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>One Seat Ride Act</strong></p><p>This bill requires the Department of Transportation to conduct a study on the benefits of commuter rail passenger transportation and major obstacles to providing commuter rail passenger transportation that does not involve a transfer for passengers. The study must consider economic, logistical, and quality of life factors. It must also include a cost-benefit analysis of single-seat trips on the New Jersey Transit Raritan Valley line during peak hours and the impact such trips would have on other New Jersey Transit lines.</p>"
        },
        "title": "One Seat Ride Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1478.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Seat Ride Act</strong></p><p>This bill requires the Department of Transportation to conduct a study on the benefits of commuter rail passenger transportation and major obstacles to providing commuter rail passenger transportation that does not involve a transfer for passengers. The study must consider economic, logistical, and quality of life factors. It must also include a cost-benefit analysis of single-seat trips on the New Jersey Transit Raritan Valley line during peak hours and the impact such trips would have on other New Jersey Transit lines.</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hr1478"
    },
    "title": "One Seat Ride Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Seat Ride Act</strong></p><p>This bill requires the Department of Transportation to conduct a study on the benefits of commuter rail passenger transportation and major obstacles to providing commuter rail passenger transportation that does not involve a transfer for passengers. The study must consider economic, logistical, and quality of life factors. It must also include a cost-benefit analysis of single-seat trips on the New Jersey Transit Raritan Valley line during peak hours and the impact such trips would have on other New Jersey Transit lines.</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hr1478"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1478ih.xml"
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
      "title": "One Seat Ride Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Seat Ride Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to conduct a study on the costs and benefits of commuter rail passenger transportation involving transfers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:30Z"
    }
  ]
}
```
