# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1126?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1126
- Title: East Palestine Health Impact Monitoring Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1126
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-06-09T18:19:30Z
- Update date including text: 2025-06-09T18:19:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1126",
    "number": "1126",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000295",
        "district": "14",
        "firstName": "David",
        "fullName": "Rep. Joyce, David P. [R-OH-14]",
        "lastName": "Joyce",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "East Palestine Health Impact Monitoring Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-09T18:19:30Z",
    "updateDateIncludingText": "2025-06-09T18:19:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:02:40Z",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
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
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "OH"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1126ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1126\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Joyce of Ohio (for himself, Ms. Kaptur , Mr. Rulli , and Mrs. Sykes ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require a study on public health impacts as a consequence of the February 3, 2023, train derailment in East Palestine, Ohio.\n#### 1. Short title\nThis Act may be cited as the East Palestine Health Impact Monitoring Act of 2025 .\n#### 2. Study on public health impacts as a consequence of the train derailment in East Palestine, Ohio\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall award a grant, contract, or cooperative agreement to an eligible entity for purposes of conducting a longitudinal study on any human health effects as a consequence of the February 3, 2023, train derailment in East Palestine, Ohio, and subsequent venting and burning of chemicals.\n##### (b) Eligible entity\nTo be eligible for the award under subsection (a), an entity shall be a consortium of public or private institutions of higher education that demonstrates requisite capacity and expertise to carry out the study described in such subsection. The Secretary shall give additional consideration to eligible entities that have established relationships within the affected communities.\n##### (c) Reports\nThe Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives\u2014\n**(1)**\nnot later than 2 years after the date on which an award is made pursuant to subsection (a), a report summarizing the progress of such study, including a description of any challenges related to conducting such study and an anticipated timeline for completion of such study and publication of results; and\n**(2)**\nnot later than 1 year after publication of such results, a report describing such results and any ongoing or planned activities of the Secretary to support or conduct further research and, as appropriate, otherwise address such results.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated such sums as may be necessary for fiscal year 2026, to remain available until September 30, 2030, to carry out this Act.",
      "versionDate": "2025-02-07",
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
            "name": "Accidents",
            "updateDate": "2025-04-24T16:16:13Z"
          },
          {
            "name": "Air quality",
            "updateDate": "2025-04-24T16:16:01Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-24T16:15:55Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-04-24T16:15:43Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-24T16:15:33Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2025-04-24T16:15:48Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-04-24T16:15:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T13:00:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1126",
          "measure-number": "1126",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1126v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>East Palestine Health Impact Monitoring Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to provide a grant to a consortium of institutions of higher education to conduct\u00a0a long-term study on any human health effects from the train derailment (and subsequent venting and burning of chemicals) in East Palestine, Ohio, on February 3, 2023.\u00a0</p>"
        },
        "title": "East Palestine Health Impact Monitoring Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1126.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>East Palestine Health Impact Monitoring Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to provide a grant to a consortium of institutions of higher education to conduct\u00a0a long-term study on any human health effects from the train derailment (and subsequent venting and burning of chemicals) in East Palestine, Ohio, on February 3, 2023.\u00a0</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1126"
    },
    "title": "East Palestine Health Impact Monitoring Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>East Palestine Health Impact Monitoring Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services to provide a grant to a consortium of institutions of higher education to conduct\u00a0a long-term study on any human health effects from the train derailment (and subsequent venting and burning of chemicals) in East Palestine, Ohio, on February 3, 2023.\u00a0</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1126"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1126ih.xml"
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
      "title": "East Palestine Health Impact Monitoring Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "East Palestine Health Impact Monitoring Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study on public health impacts as a consequence of the February 3, 2023, train derailment in East Palestine, Ohio.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:19:45Z"
    }
  ]
}
```
