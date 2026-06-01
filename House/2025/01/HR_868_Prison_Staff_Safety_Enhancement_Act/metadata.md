# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/868
- Title: Prison Staff Safety Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 868
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-04-16T08:06:50Z
- Update date including text: 2026-04-16T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/868",
    "number": "868",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Prison Staff Safety Enhancement Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:50Z",
    "updateDateIncludingText": "2026-04-16T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:01:20Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "AL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "IA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NE"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr868ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 868\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Lee of Florida introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo address sexual harassment and sexual assault of Bureau of Prisons staff in prisons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prison Staff Safety Enhancement Act .\n#### 2. Addressing sexual harassment and sexual assault of Bureau of Prisons staff\n##### (a) Definitions\nIn this section:\n**(1) Correctional officer**\nThe term correctional officer has the meaning given the term in section 4051 of title 18, United States Code.\n**(2) Inspector General**\nThe term Inspector General means the Inspector General of the Department of Justice.\n**(3) Incarcerated individual**\nThe term incarcerated individual has the meaning given the term prisoner in section 4051 of title 18, United States Code.\n**(4) Sexual assault**\nThe term sexual assault means an act described in subsection (b), (c), or (d) of section 920 of title 10, United States Code.\n**(5) Sexual harassment**\nThe term sexual harassment means unwelcome sexual advances, requests for sexual favors, or other verbal or physical conduct of a sexual nature that explicitly or implicitly affect an individual\u2019s employment, unreasonably interfere with an individual\u2019s work performance, or create an intimidating, hostile, or offensive work environment.\n##### (b) Review and analysis\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Inspector General shall carry out a comprehensive statistical review and analysis of the incidence and effects of sexual harassment and sexual assault perpetrated by incarcerated individuals against a correctional officer or other employee of the Bureau of Prisons.\n**(2) Analysis**\nThe review and analysis required under paragraph (1) shall include an analysis of punishments for sexual harassment and sexual assault as of the date of enactment of this Act in facilities controlled by the Bureau of Prisons, including data on the use of such punishments during the 5-year period preceding the date of enactment of this Act.\n##### (c) Report\nNot later than 180 days after completing the review and analysis under subsection (b)(1), the Inspector General shall submit to the Attorney General and to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that summarizes the findings of the review and analysis.\n##### (d) Rulemaking\nNot later than 1 year after receiving the report under subsection (c), the Attorney General shall promulgate a rule adopting national standards for prevention, reduction, and punishment of sexual harassment and sexual assault perpetrated by an incarcerated individual against a correctional officer or other employee of the Bureau of Prisons.",
      "versionDate": "2025-01-31",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-07T13:37:26Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-04-07T13:37:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-04T17:24:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr868",
          "measure-number": "868",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr868v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill requires the Department of Justice to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the Bureau of Prisons.</p>"
        },
        "title": "Prison Staff Safety Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr868.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill requires the Department of Justice to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the Bureau of Prisons.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr868"
    },
    "title": "Prison Staff Safety Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill requires the Department of Justice to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the Bureau of Prisons.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119hr868"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr868ih.xml"
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
      "title": "Prison Staff Safety Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prison Staff Safety Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address sexual harassment and sexual assault of Bureau of Prisons staff in prisons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:30Z"
    }
  ]
}
```
