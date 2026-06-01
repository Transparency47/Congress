# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4310?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4310
- Title: No Tax on Overtime for All Workers Act
- Congress: 119
- Bill type: S
- Bill number: 4310
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-12T11:03:32Z
- Update date including text: 2026-05-12T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4310",
    "number": "4310",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "No Tax on Overtime for All Workers Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:32Z",
    "updateDateIncludingText": "2026-05-12T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T23:31:38Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4310is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4310\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Justice introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a deduction for certain overtime compensation.\n#### 1. Short title\nThis Act may be cited as the No Tax on Overtime for All Workers Act .\n#### 2. Deduction for certain overtime compensation\n##### (a) In general\nSection 225(c)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general For purposes of this section, the term qualified overtime compensation means\u2014 (A) any overtime compensation paid to an individual required under section 7 of the Fair Labor Standards Act of 1938 that is in excess of the regular rate (as used in such section) at which such individual is employed, or (B) any compensation paid to an individual that is in excess of the regular rate at which such individual is employed if\u2014 (i) such compensation is paid for work for a single employer pursuant to an agreement between the employee (or labor organization representing such employee) and employer entered into before the performance of the work, and (ii) either\u2014 (I) such work is in excess of a standard number of hours of such work for a specified period of time, and such agreement specifies that such standard number of hours for a specified period of time is not less than 40 hours for a 7-day work period, or (II) if the employee (including any crewmember or flight crewmember, or rail operating craft employee) and employer referred to in clause (i) are both covered by the Railway Labor Act, such work is beyond scheduled or anticipated hours on duty or for hours on duty that exceed a maximum number of hours with respect to a specified period of time (as determined pursuant to such agreement). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2026-04-15",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5475",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Tax on Overtime for All Workers Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2026-05-07T02:48:31Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4310is.xml"
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
      "title": "No Tax on Overtime for All Workers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax on Overtime for All Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow a deduction for certain overtime compensation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:39Z"
    }
  ]
}
```
