# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8637?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8637
- Title: Release Your Taxes Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8637
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T20:01:33Z
- Update date including text: 2026-05-20T20:01:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8637",
    "number": "8637",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Release Your Taxes Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T20:01:33Z",
    "updateDateIncludingText": "2026-05-20T20:01:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8637ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8637\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Stevens introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require incumbent and aspiring Members of Congress to disclose their income tax returns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Release Your Taxes Act of 2026 .\n#### 2. Disclosure of Federal income tax return\n##### (a) Definitions\nIn this section:\n**(1) Appropriate congressional officials**\nThe term appropriate congressional officials means the following:\n**(A)**\nThe Clerk of the House of Representatives.\n**(B)**\nThe Secretary of the Senate.\n**(2) Congressional candidate**\nThe term congressional candidate means a candidate, as such term is defined under section 301 of the Federal Election Campaign Act of 1971, who seeks nomination for election, or election, to the office of Senator or Representative in, or Delegate or Resident Commissioner to, the Congress.\n**(3) Member of Congress**\nThe term Member of Congress means a Senator or Representative in, or a Delegate or Resident Commissioner to, the Congress.\n**(4) Tax return filing**\nThe term tax return filing means any of the following:\n**(A)**\nForm 1040 and Schedule A filed with a return of tax under the Internal Revenue Code of 1986, or the equivalent successor forms or schedules.\n**(B)**\nAn application or request for extension of the due date for return of tax under such Code.\n**(C)**\nThe statement referred to in subsection (d)(3).\n##### (b) Establishment of tax return database\nThe appropriate congressional officials shall\u2014\n**(1)**\nestablish a database containing every tax return filing submitted to the appropriate congressional officials pursuant to this section; and\n**(2)**\nprescribe from time to time such rules necessary to carry out this section.\n##### (c) Publication of database\nThe appropriate congressional officials shall publish\u2014\n**(1)**\nthe database established under subsection (b) on a website available to the general public under the authority of appropriate congressional officials; and\n**(2)**\neach tax return filing received by the appropriate congressional officials through the database within 5 business days after the date on which the appropriate congressional officials received the filing.\n##### (d) Disclosure requirement\n**(1) In general**\nAn individual shall submit to the appropriate congressional officials a tax return filing pertaining to the individual not later than 2 business days after the date of the filing of the tax return filing pursuant to the Internal Revenue Code of 1986 if any of the following apply:\n**(A)**\nThe individual is a Member of Congress or a congressional candidate for any part of the tax year with respect to which the tax return filing pertains.\n**(B)**\nThe individual is a Member of Congress or a congressional candidate for any part of the calendar year in which the individual files the tax return filing.\n**(2) Change in office status after filing**\nAn individual who is not a Member of Congress or a congressional candidate on the date that the individual files a tax return filing pertaining to the individual and becomes a Member of Congress or congressional candidate after such date in the same calendar year shall submit the tax return filing to the appropriate congressional officials not later than 30 days after the individual becomes a Member of Congress or congressional candidate.\n**(3) Absence of tax return**\nAn individual who would be subject to the requirements under paragraph (1) or (2) if the individual were to be required to file a return of tax under the Internal Revenue Code of 1986 with respect to a tax year but is not actually required to file such a return for such tax year shall submit to the appropriate congressional officials a statement explaining that the individual is not required to file the return not later than the due date that would apply for filing the return.\n##### (e) Failure of compliance\nThe appropriate congressional officials\u2014\n**(1)**\nshall include promptly in the website referred to in subsection (c)(1) the name of any individual who does not comply with a requirement under subsection (d) notwithstanding a duty to comply with the requirement; and\n**(2)**\nshall not remove the name of such individual from the website unless and until\u2014\n**(A)**\nthe individual complies with the requirement; or\n**(B)**\nmore than 6 years have elapsed after the date on which the individual is no longer a Member of Congress or a congressional candidate.\n##### (f) Transition provisions\nNot later than 30 days after the date of the enactment of this section, an individual who is a Member of Congress or a congressional candidate on such date shall submit to the appropriate congressional officials any tax return filing that was filed in the calendar year of the date of the enactment that would have been required to be submitted to the appropriate congressional officials under subsection (d) if this section were in effect from the start of the calendar year.\n##### (g) Applicability\nThis section shall apply with respect to a return of tax under the Internal Revenue Code of 1986 for a tax year that begins in 2025 or each succeeding year.",
      "versionDate": "2026-04-30",
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
        "name": "Congress",
        "updateDate": "2026-05-20T20:01:33Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8637ih.xml"
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
      "title": "Release Your Taxes Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Release Your Taxes Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require incumbent and aspiring Members of Congress to disclose their income tax returns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:36Z"
    }
  ]
}
```
