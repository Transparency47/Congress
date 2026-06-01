# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2108?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2108
- Title: VARIANCE Act
- Congress: 119
- Bill type: S
- Bill number: 2108
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2025-08-26T12:34:02Z
- Update date including text: 2025-08-26T12:34:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2108",
    "number": "2108",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "VARIANCE Act",
    "type": "S",
    "updateDate": "2025-08-26T12:34:02Z",
    "updateDateIncludingText": "2025-08-26T12:34:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
          "date": "2025-06-18T16:30:21Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2108is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2108\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Ricketts (for himself and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to establish an axle weight variance for certain commercial motor vehicles transporting dry bulk goods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Vehicle Axle Redistribution Increases Allow New Capacities for Efficiency Act or the VARIANCE Act .\n#### 2. Axle weight variance for the transportation of dry bulk goods\nSection 127 of title 23, United States Code, is amended by adding at the end the following:\n(z) Axle weight variance for the transportation of dry bulk goods (1) Definition of dry bulk goods In this subsection, the term dry bulk goods means a homogeneous, unmarked, unpackaged, nonliquid cargo being transported in a trailer specifically designed for that purpose. (2) Weight variance Notwithstanding any other provision of this section, except for the maximum gross vehicle weight limitation, a commercial motor vehicle transporting dry bulk goods may not exceed 110 percent of the maximum weight on any axle or axle group described in subsection (a), including any enforcement tolerance. .",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-07-14T14:18:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-18",
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
          "measure-id": "id119s2108",
          "measure-number": "2108",
          "measure-type": "s",
          "orig-publish-date": "2025-06-18",
          "originChamber": "SENATE",
          "update-date": "2025-08-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2108v00",
            "update-date": "2025-08-26"
          },
          "action-date": "2025-06-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Vehicle Axle Redistribution Increases Allow New Capacities for Efficiency Act or the VARIANCE Act</strong></p><p>This bill allows commercial motor vehicles transporting dry bulk goods to operate on the Interstate Highway System with up to 110% of the maximum authorized weight on any axle or axle group.</p>"
        },
        "title": "VARIANCE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2108.xml",
    "summary": {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vehicle Axle Redistribution Increases Allow New Capacities for Efficiency Act or the VARIANCE Act</strong></p><p>This bill allows commercial motor vehicles transporting dry bulk goods to operate on the Interstate Highway System with up to 110% of the maximum authorized weight on any axle or axle group.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119s2108"
    },
    "title": "VARIANCE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Vehicle Axle Redistribution Increases Allow New Capacities for Efficiency Act or the VARIANCE Act</strong></p><p>This bill allows commercial motor vehicles transporting dry bulk goods to operate on the Interstate Highway System with up to 110% of the maximum authorized weight on any axle or axle group.</p>",
      "updateDate": "2025-08-26",
      "versionCode": "id119s2108"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2108is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "VARIANCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VARIANCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Vehicle Axle Redistribution Increases Allow New Capacities for Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to establish an axle weight variance for certain commercial motor vehicles transporting dry bulk goods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:11Z"
    }
  ]
}
```
