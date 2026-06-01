# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/680
- Title: Caring for Survivors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 680
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-12-05T21:42:47Z
- Update date including text: 2025-12-05T21:42:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H538)
- 2025-02-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H538)
- 2025-02-26 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/680",
    "number": "680",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Caring for Survivors Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:47Z",
    "updateDateIncludingText": "2025-12-05T21:42:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H538)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-26T22:39:49Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr680ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 680\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mrs. Hayes (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve and to expand eligibility for dependency and indemnity compensation paid to certain survivors of certain veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Caring for Survivors Act of 2025 .\n#### 2. Increase in amount of dependency and indemnity compensation for surviving spouses\n##### (a) Increase\nSection 1311(a) of title 38, United States Code, is amended in paragraph (1), by striking of $1,154 and inserting equal to 55 percent of the rate of monthly compensation in effect under section 1114(j) of this title .\n##### (b) Effective date\n**(1) In general**\nExcept as provided by paragraph (2), the amendments made by subsection (a) shall apply with respect to compensation paid under chapter 13 of title 38, United States Code, for months beginning after the date that is six months after the date of the enactment of this Act.\n**(2) Special rule for certain individuals**\n**(A) In general**\nFor months beginning after the date that is six months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall pay to an individual described in subparagraph (B) dependents and survivors income security benefit under section 1311 of title 38, United States Code, in the monthly amount that is the greater of the following:\n**(i)**\nThe amount determined under subsection (a)(3) of such section 1311, as in effect on the day before the date of the enactment of this Act.\n**(ii)**\nThe amount determined under subsection (a)(1) of such section 1311, as amended by subsection (a).\n**(B) Individuals described**\nAn individual described in this subparagraph is an individual eligible for dependents and survivors income security benefit under section 1311 of title 38, United States Code, that is predicated on the death of a veteran before January 1, 1993.\n#### 3. Modification of requirements for dependency and indemnity compensation for survivors of certain veterans rated totally disabled at time of death\nSection 1318 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking The Secretary and inserting (1) Except as provided in paragraph (2), the Secretary ; and\n**(B)**\nby adding at the end the following new paragraph:\n(2) In any case in which the Secretary makes a payment under paragraph (1) of this subsection by reason of subsection (b)(1) and the period of continuous rating immediately preceding death is less than 10 years, the amount payable under paragraph (1) of this subsection shall be an amount that bears the same relationship to the amount otherwise payable under such paragraph as the duration of such period bears to 10 years. ; and\n**(2)**\nin subsection (b)(1), by striking 10 or more years and inserting five or more years .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-11",
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "611",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Caring for Survivors Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-24",
        "text": "Subcommittee Hearings Held"
      },
      "number": "2055",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Caring for Survivors Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability assistance",
            "updateDate": "2025-03-17T17:53:50Z"
          },
          {
            "name": "Marriage and family status",
            "updateDate": "2025-03-17T17:53:50Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-17T17:53:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:55:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr680",
          "measure-number": "680",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr680v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>"
        },
        "title": "Caring for Survivors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr680.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr680"
    },
    "title": "Caring for Survivors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr680"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr680ih.xml"
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
      "title": "Caring for Survivors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T11:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Caring for Survivors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T11:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve and to expand eligibility for dependency and indemnity compensation paid to certain survivors of certain veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T11:48:31Z"
    }
  ]
}
```
