# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1045
- Title: Aviation Funding Stability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1045
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-10T11:03:22Z
- Update date including text: 2026-03-10T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1045",
    "number": "1045",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Aviation Funding Stability Act of 2025",
    "type": "S",
    "updateDate": "2026-03-10T11:03:22Z",
    "updateDateIncludingText": "2026-03-10T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
            "date": "2025-03-13T18:38:52Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-13T18:38:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1045is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1045\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for funding from the Airport and Airway Trust Fund for all Federal Aviation Administration activities in the event of a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Funding Stability Act of 2025 .\n#### 2. Funding for the Federal Aviation Administration in the event of a lapse in appropriation\n##### (a) In general\nIf, with respect to the Federal Aviation Administration, an appropriation measure for a fiscal year is not enacted before the beginning of such fiscal year or a joint resolution making continuing appropriations is not in effect, amounts in the Airport and Airway Trust Fund not otherwise appropriated shall be available to the Administrator of the Federal Aviation Administration for continuing programs, projects, or activities (including the costs of direct loans and loan guarantees) that were conducted with amounts made available for the Federal Aviation Administration, including for the accounts Federal Aviation Administration\u2014Operations , Federal Aviation Administration\u2014Facilities and Equipment , Federal Aviation Administration\u2014Research, Engineering, and Development , and Federal Aviation Administration\u2014Grants-in-Aid for Airports in the preceding fiscal year\u2014\n**(1)**\nin the corresponding appropriation Act for such preceding fiscal year; or\n**(2)**\nif the corresponding appropriation bill for such preceding fiscal year did not become law, then in a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (b) Rate for operations\nAppropriations and funds made available, and authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be at a rate for operations not greater than\u2014\n**(1)**\nthe rate for operations provided for in the regular appropriation Act providing for such program, project, or activity for the preceding fiscal year; or\n**(2)**\nin the absence of such an Act, the rate for operations provided for such program, project, or activity pursuant to a joint resolution making continuing appropriations for such preceding fiscal year.\n##### (c) Availability\nAppropriations and funds made available, and authority granted, for any fiscal year pursuant to this section for a program, project, or activity shall be available for the period beginning with the first day of a lapse in appropriations and ending with the date on which the applicable regular appropriation bill for such fiscal year becomes law (whether or not such law provides for such program, project, or activity) or a joint resolution making continuing appropriations becomes law, as the case may be.\n##### (d) Terms and conditions\nAn appropriation or funds made available, or authority granted, for a program, project, or activity for any fiscal year pursuant to this section shall be subject to the terms and conditions imposed with respect to the appropriation made or funds made available for the preceding fiscal year, or authority granted for such program, project, or activity under current law.\n##### (e) End of fiscal year\nIf this section is in effect at the end of a fiscal year, funding levels shall continue as provided in this section for the next fiscal year.\n##### (f) Expenditures and obligations\nExpenditures and obligations made for a program, project, or activity for any fiscal year pursuant to this section shall be charged to the applicable appropriation, fund, or authorization whenever a regular appropriation bill or a joint resolution making continuing appropriations until the end of a fiscal year providing for such program, project, or activity for such period becomes law.\n##### (g) Expenditure authority\nSection 9502(d)(1)(A) of the Internal Revenue Code of 1986 is amended by striking the semicolon at the end and inserting or the Aviation Funding Stability Act of 2025 ; .\n##### (h) Termination\nThis section shall not apply to a program, project, or activity during any portion of a fiscal year if any other provision of law (other than an authorization of appropriations)\u2014\n**(1)**\nmakes an appropriation, makes funds available, or grants authority for such program, project, or activity to continue for such period; or\n**(2)**\nspecifically provides that no appropriation shall be made, no funds shall be made available, or no authority shall be granted for such program, project, or activity to continue for such period.",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-19",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "5451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Aviation Funding Stability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-19",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "5455",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Aviation Funding Stability Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-05-12T18:40:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1045",
          "measure-number": "1045",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1045v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Aviation Funding Stability Act of 2025</strong><strong></strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities for which funds were provided in the preceding fiscal year.</p>"
        },
        "title": "Aviation Funding Stability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1045.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Aviation Funding Stability Act of 2025</strong><strong></strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities for which funds were provided in the preceding fiscal year.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119s1045"
    },
    "title": "Aviation Funding Stability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Aviation Funding Stability Act of 2025</strong><strong></strong></p><p>This bill provides continuing appropriations to the Federal Aviation Administration (FAA) if (1) an appropriations bill for the FAA has not been enacted before a fiscal year begins, or (2) a joint resolution making continuing appropriations for the FAA is not in effect.</p><p>Specifically, the bill provides appropriations from the Airport and Airway Trust Fund at the rate of operations that was provided for the prior fiscal year to continue programs, projects, and activities for which funds were provided in the preceding fiscal year.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119s1045"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1045is.xml"
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
      "title": "Aviation Funding Stability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Aviation Funding Stability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for funding from the Airport and Airway Trust Fund for all Federal Aviation Administration activities in the event of a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:24Z"
    }
  ]
}
```
