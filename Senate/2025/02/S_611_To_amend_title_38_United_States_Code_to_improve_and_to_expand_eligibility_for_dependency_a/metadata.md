# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/611?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/611
- Title: Caring for Survivors Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 611
- Origin chamber: Senate
- Introduced date: 2025-02-18
- Update date: 2025-12-05T21:42:47Z
- Update date including text: 2025-12-05T21:42:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in Senate
- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-02-18: Introduced in Senate

## Actions

- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/611",
    "number": "611",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Caring for Survivors Act of 2025",
    "type": "S",
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
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
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
            "date": "2025-03-11T14:30:14Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-18T21:16:53Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-21",
      "state": "VT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "WA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "IL"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s611is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 611\nIN THE SENATE OF THE UNITED STATES\nFebruary 18, 2025 Mr. Blumenthal (for himself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve and to expand eligibility for dependency and indemnity compensation paid to certain survivors of certain veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Caring for Survivors Act of 2025 .\n#### 2. Increase in amount of dependency and indemnity compensation for surviving spouses\n##### (a) Increase\nSection 1311(a) of title 38, United States Code, is amended in paragraph (1), by striking of $1,154 and inserting equal to 55 percent of the rate of monthly compensation in effect under section 1114(j) of this title .\n##### (b) Effective date\n**(1) In general**\nExcept as provided by paragraph (2), the amendments made by subsection (a) shall apply with respect to compensation paid under chapter 13 of title 38, United States Code, for months beginning after the date that is six months after the date of the enactment of this Act.\n**(2) Special rule for certain individuals**\n**(A) In general**\nFor months beginning after the date that is six months after the date of the enactment of this Act, the Secretary of Veterans Affairs shall pay to an individual described in subparagraph (B) dependents and survivors income security benefit under section 1311 of title 38, United States Code, in the monthly amount that is the greater of the following:\n**(i)**\nThe amount determined under subsection (a)(3) of such section 1311, as in effect on the day before the date of the enactment of this Act.\n**(ii)**\nThe amount determined under subsection (a)(1) of such section 1311, as amended by subsection (a).\n**(B) Individuals described**\nAn individual described in this subparagraph is an individual eligible for dependents and survivors income security benefit under section 1311 of title 38, United States Code, that is predicated on the death of a veteran before January 1, 1993.\n#### 3. Modification of requirements for dependency and indemnity compensation for survivors of certain veterans rated totally disabled at time of death\nSection 1318 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking The Secretary and inserting (1) Except as provided in paragraph (2), the Secretary ; and\n**(B)**\nby adding at the end the following new paragraph:\n(2) In any case in which the Secretary makes a payment under paragraph (1) of this subsection by reason of subsection (b)(1) and the period of continuous rating immediately preceding death is less than 10 years, the amount payable under paragraph (1) of this subsection shall be an amount that bears the same relationship to the amount otherwise payable under such paragraph as the duration of such period bears to 10 years. ; and\n**(2)**\nin subsection (b)(1), by striking 10 or more years and inserting five or more years .",
      "versionDate": "2025-02-18",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs."
      },
      "number": "680",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Caring for Survivors Act of 2025",
      "type": "HR"
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
            "updateDate": "2025-03-17T17:54:04Z"
          },
          {
            "name": "Marriage and family status",
            "updateDate": "2025-03-17T17:54:04Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-17T17:54:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:24:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119s611",
          "measure-number": "611",
          "measure-type": "s",
          "orig-publish-date": "2025-02-18",
          "originChamber": "SENATE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s611v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>"
        },
        "title": "Caring for Survivors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s611.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s611"
    },
    "title": "Caring for Survivors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Caring for Survivors Act of 2025</strong></p><p>This bill increases the monthly rate of dependency and indemnity compensation payable to surviving spouses through the Department of Veterans Affairs (VA).</p><p>Dependency and indemnity compensation is a monthly payment made to eligible survivors (i.e., spouses, parents, or children) of (1) certain veterans who died as a result of a service-connected condition; (2) service members killed while on active military duty or active or inactive duty for training; or (3) veterans who did not die from a service-connected condition, but were totally disabled by a service-connected disability for a certain period of time.</p><p>The bill also (1) reduces, from 10 years to 5 years, the period of time that certain veterans must have been rated totally disabled due to a service-connected disability in order for a survivor to qualify for benefits; and (2) specifies the amount that is payable to survivors of veterans who were rated totally disabled for a period of less than 10 years before their death.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s611"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s611is.xml"
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
      "title": "Caring for Survivors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Caring for Survivors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to improve and to expand eligibility for dependency and indemnity compensation paid to certain survivors of certain veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:30Z"
    }
  ]
}
```
