# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6003
- Title: Justice Involved Veterans Support Act
- Congress: 119
- Bill type: HR
- Bill number: 6003
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-01T21:39:08Z
- Update date including text: 2026-04-01T21:39:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6003",
    "number": "6003",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Justice Involved Veterans Support Act",
    "type": "HR",
    "updateDate": "2026-04-01T21:39:08Z",
    "updateDateIncludingText": "2026-04-01T21:39:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NE"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6003ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6003\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Crow (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General, in consultation with the Secretary of Veterans Affairs, to establish a pilot program to help State prisons and local jails improve the documentation of incarcerated veterans.\n#### 1. Short title\nThis Act may be cited as the Justice Involved Veterans Support Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nApproximately 181,000 veterans are incarcerated in the United States.\n**(2)**\nMore than half of all veterans involved in the criminal justice system suffer from a mental health condition or substance abuse disorder.\n**(3)**\nSuch veterans may be at a greater risk for suicide.\n**(4)**\nVeterans released from incarceration have specialized needs and face different issues relating to reentry into society.\n#### 3. Pilot program to improve documentation of incarcerated veterans\n##### (a) Establishment\nThe Attorney General, in consultation with the Secretary of Veterans Affairs, shall carry out a pilot program to provide grants and technical assistance to State prisons and local jails to improve documentation of whether inmates of such institutions are veterans.\n##### (b) Purpose\nThe purposes of the pilot program are the following:\n**(1)**\nTo assist the Secretary in providing benefits to incarcerated veterans under laws administered by the Secretary.\n**(2)**\nTo assist veterans affairs offices of States in providing benefits to incarcerated veterans under laws administered by such offices.\n**(3)**\nTo increase the number of veterans involved in the criminal justice system whose cases are diverted to veterans treatment courts.\n##### (c) Priority\nIn selecting grant recipients under the pilot program, the Attorney General shall give priority to State prisons and local jails located in\u2014\n**(1)**\nStates that contain the greatest populations of veterans per capita;\n**(2)**\nStates with the highest rates of veterans living in poverty; and\n**(3)**\njurisdictions that contain a veterans treatment court or veterans diversion program.\n##### (d) Definitions\nIn this section, the terms veterans treatment court and veterans diversion program mean a State or local court that is participating in the veterans treatment court program (as defined in section 2991(i)(1) of the Omnibus Crime Control and Safe Streets Act of 1968; 34 U.S.C. 10651(i)(1) ).",
      "versionDate": "2025-11-10",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-19T13:10:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-10",
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
          "measure-id": "id119hr6003",
          "measure-number": "6003",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6003v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-11-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Justice Involved Veterans Support Act</strong></p> <p>This bill directs the Department of Justice, in consultation with the Department of Veterans Affairs, to establish a pilot program to improve documentation of whether inmates of state prisons and local jails are veterans.</p>"
        },
        "title": "Justice Involved Veterans Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6003.xml",
    "summary": {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice Involved Veterans Support Act</strong></p> <p>This bill directs the Department of Justice, in consultation with the Department of Veterans Affairs, to establish a pilot program to improve documentation of whether inmates of state prisons and local jails are veterans.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr6003"
    },
    "title": "Justice Involved Veterans Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice Involved Veterans Support Act</strong></p> <p>This bill directs the Department of Justice, in consultation with the Department of Veterans Affairs, to establish a pilot program to improve documentation of whether inmates of state prisons and local jails are veterans.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr6003"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6003ih.xml"
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
      "title": "Justice Involved Veterans Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice Involved Veterans Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General, in consultation with the Secretary of Veterans Affairs, to establish a pilot program to help State prisons and local jails improve the documentation of incarcerated veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:15Z"
    }
  ]
}
```
