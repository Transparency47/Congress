# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5618?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5618
- Title: Housing PLUS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5618
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-12-15T20:11:18Z
- Update date including text: 2025-12-15T20:11:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5618",
    "number": "5618",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Housing PLUS Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-15T20:11:18Z",
    "updateDateIncludingText": "2025-12-15T20:11:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NE"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5618ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5618\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Barr (for himself, Mr. Flood , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo allow amounts made available for the Continuum of Care program of the Secretary of Housing and Urban Development.\n#### 1. Short title\nThis Act may be cited as the Housing Promotes Livelihood and Ultimate Success Act of 2025 or the Housing PLUS Act of 2025 .\n#### 2. Availability of Continuum of Care funds for grantees requiring wraparound services or applying preconditions\nSubtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ) is amended by adding at the end the following new section:\n436. Availability of funds for grantees requiring wraparound services or applying preconditions (a) Availability Notwithstanding any other provision of law, the Secretary may not, in making amounts available under this subtitle, prohibit, limit, or restrict the award or amount of grants made with such amounts to or for eligible entities, project sponsors, or recipients\u2014 (1) that require the provision of supportive services, such as counseling, job training, or addiction treatment, for individuals served by a program, project, or activity assisted with such amounts; (2) that require, as a condition for occupancy in a project, or assistance from a program, project, or activity, assisted with such amounts that individuals meet certain prerequisites, such as sobriety or lack of drug use; or (3) faith-based organizations. (b) Set aside Notwithstanding any other provision of law, in making available amounts under this subtitle for each fiscal year, the Secretary shall ensure that not less than 50 percent of such amounts shall be used by eligible entities, project sponsors, and recipients that provide or offer access to wraparound services. (c) Accountability Not later than 180 days after the completion of each fiscal year, the Secretary shall submit, to the House Committee on Financial Services of the House of Representatives and Committee on Banking, Housing and Urban Affairs of the Senate, for such fiscal year\u2014 (1) a written certification that the amounts made available for carrying out this subtitle were made available in compliance with subsections (a) and (b) of this section; and (2) a report specifying how the Notices of Funding Opportunity for such fiscal year for amounts made available for carrying out this subtitle evidence such compliance. .",
      "versionDate": "2025-09-30",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-12-15T20:11:18Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5618ih.xml"
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
      "title": "Housing PLUS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T04:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing PLUS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T04:08:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Promotes Livelihood and Ultimate Success Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T04:08:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow amounts made available for the Continuum of Care program of the Secretary of Housing and Urban Development.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-08T04:03:12Z"
    }
  ]
}
```
