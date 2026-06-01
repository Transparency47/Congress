# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/552?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/552
- Title: Veterans Collaboration Act
- Congress: 119
- Bill type: HR
- Bill number: 552
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-08-16T08:05:34Z
- Update date including text: 2025-08-16T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/552",
    "number": "552",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Veterans Collaboration Act",
    "type": "HR",
    "updateDate": "2025-08-16T08:05:34Z",
    "updateDateIncludingText": "2025-08-16T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:38:44Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr552ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 552\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Wittman introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a pilot program to promote and encourage collaboration between the Department of Veterans Affairs and nonprofit organizations and institutions of higher learning that provide administrative assistance to veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans Collaboration Act .\n#### 2. Department of Veterans Affairs pilot program on encouragement of partnerships between veterans service organizations and law schools providing pro bono services to veterans\n##### (a) In general\nThe Secretary of Veterans Affairs shall carry out a two-year pilot program to promote and encourage partnerships between the Department of Veterans Affairs and nonprofit organizations and institutions of higher learning. In carrying out the pilot program, the Secretary shall encourage partnerships between\u2014\n**(1)**\nveterans service organizations that provide personnel with appropriate credentials to assist veterans in filing claims and appeals with the Department for disability compensation and to address other legal needs of veterans; and\n**(2)**\nlaw schools that provide pro bono legal assistance and legal services to veterans.\n##### (b) Metrics\nThe Secretary shall establish guidelines to determine which organizations and institutions are best positioned to serve veterans and seek to encourage such organizations and institutions to participate in the pilot program.\n##### (c) Location\nThe Secretary shall carry out the pilot program in States with the highest veteran populations, as determined by the Secretary.\n##### (d) Use of social media\nIn carrying out the pilot program, the Secretary shall use social media to promote the partnerships carried out under the pilot program and to notify veterans of such partnerships.\n##### (e) Reports\nNot later than 30 days after the last day of each fiscal quarter until the termination of the pilot program, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on the pilot program. Each such report shall include, for the fiscal quarter covered by the report, a description of the use of social media under subsection (d) and the number of veterans who received assistance from law schools through the program.",
      "versionDate": "2025-01-16",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-10T15:26:16Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-10T15:26:09Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-10T15:26:28Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-03-10T15:26:24Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-03-10T15:26:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:33:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr552",
          "measure-number": "552",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr552v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Collaboration Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a two-year pilot program to promote and encourage partnerships between the VA and nonprofit organizations and institutions of higher learning. Specifically, the VA must encourage partnerships between (1) veterans service organizations that provide credentialed personnel to assist veterans with legal needs, and (2) law schools that provide pro bono legal assistance and legal services to veterans.</p>"
        },
        "title": "Veterans Collaboration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr552.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Collaboration Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a two-year pilot program to promote and encourage partnerships between the VA and nonprofit organizations and institutions of higher learning. Specifically, the VA must encourage partnerships between (1) veterans service organizations that provide credentialed personnel to assist veterans with legal needs, and (2) law schools that provide pro bono legal assistance and legal services to veterans.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr552"
    },
    "title": "Veterans Collaboration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Collaboration Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement a two-year pilot program to promote and encourage partnerships between the VA and nonprofit organizations and institutions of higher learning. Specifically, the VA must encourage partnerships between (1) veterans service organizations that provide credentialed personnel to assist veterans with legal needs, and (2) law schools that provide pro bono legal assistance and legal services to veterans.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr552"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr552ih.xml"
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
      "title": "Veterans Collaboration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Collaboration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to carry out a pilot program to promote and encourage collaboration between the Department of Veterans Affairs and nonprofit organizations and institutions of higher learning that provide administrative assistance to veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:22Z"
    }
  ]
}
```
