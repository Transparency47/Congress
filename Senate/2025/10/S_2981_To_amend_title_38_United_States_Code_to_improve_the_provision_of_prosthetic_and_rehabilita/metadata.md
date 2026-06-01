# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2981
- Title: Veterans Prosthetics Advancement and Reform Act
- Congress: 119
- Bill type: S
- Bill number: 2981
- Origin chamber: Senate
- Introduced date: 2025-10-07
- Update date: 2026-05-19T15:20:42Z
- Update date including text: 2026-05-19T15:20:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-07: Introduced in Senate
- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.
- Latest action: 2025-10-07: Introduced in Senate

## Actions

- 2025-10-07 - IntroReferral: Introduced in Senate
- 2025-10-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-07",
    "latestAction": {
      "actionDate": "2025-10-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2981",
    "number": "2981",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Veterans Prosthetics Advancement and Reform Act",
    "type": "S",
    "updateDate": "2026-05-19T15:20:42Z",
    "updateDateIncludingText": "2026-05-19T15:20:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-07",
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
        "item": [
          {
            "date": "2026-03-18T20:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-07T20:30:04Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-07T20:30:04Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2981is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2981\nIN THE SENATE OF THE UNITED STATES\nOctober 7, 2025 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the provision of prosthetic and rehabilitative items and services by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Prosthetics Advancement and Reform Act .\n#### 2. Improvements to Department of Veterans Affairs prosthetic and rehabilitative items and service\n##### (a) In general\nChapter 17 of title 38, United States Code, is amended by inserting after section 1709C the following new section:\n1709D. Prosthetic and rehabilitative items and services formulary (a) In general The Secretary shall establish a list of prosthetic and rehabilitative items and services, which may be referred to as the Prosthetic and Rehabilitative Items and Services Formulary or the Formulary , for purposes of furnishing medical services under section 1701(6)(F) of this title pursuant to section 1710 of this title. (b) Requirements (1) Input In developing the Formulary, the Secretary shall solicit input from veterans and the public. (2) Availability of items The Secretary shall ensure that all items and services included in the Formulary are available at or through all facilities of the Department. (3) Items To be included In developing the Formulary, the Secretary shall rely on the best available evidence to identify which items and services should be included on the Formulary. (c) Publication and communication (1) Publication and update The Secretary shall publish the Formulary on a website of the Department and shall update the Formulary periodically. (2) Communication The Secretary shall communicate to veterans the contents of the Formulary and information about how to appeal decisions regarding the provision of items and services on the Formulary. (d) Contracts The Secretary shall enter into such contracts as the Secretary considers necessary to support the availability of items and services included in the Formulary. (e) Training The Secretary shall ensure the availability of training on the Formulary for clinicians and other staff of the Department. (f) Exceptions (1) In general The Secretary shall establish a process for clinicians of the Department to request, prescribe, and furnish prosthetic and rehabilitative items and services that are not included on the Formulary when medically necessary. (2) Monitoring of non-Formulary items and services The Secretary shall monitor requests, prescriptions, and the furnishing of prosthetic and rehabilitative items and services under paragraph (1)\u2014 (A) to ensure that such items and services are being consistently and appropriately prescribed at all facilities of the Department; and (B) to determine whether such items or services should be added to the Formulary. (g) Consideration In developing the Formulary, the Secretary shall consider how the approach of the Pharmacy Benefits Management Services of the Department for formulary management and medication safety can be adapted to support the efficient and effective administration of the Formulary. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1709C the following new item:\n1709D. Prosthetic and rehabilitative items and services formulary",
      "versionDate": "2025-10-07",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T19:18:38Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2026-04-16T19:18:29Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-16T19:18:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-17T16:32:22Z"
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
      "date": "2025-10-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2981is.xml"
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
      "title": "Veterans Prosthetics Advancement and Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Prosthetics Advancement and Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to improve the provision of prosthetic and rehabilitative items and services by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:03:12Z"
    }
  ]
}
```
