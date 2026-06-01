# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2013?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2013
- Title: Higher Wages for American Workers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2013
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-06-30T13:21:01Z
- Update date including text: 2025-06-30T13:21:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2013",
    "number": "2013",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Higher Wages for American Workers Act of 2025",
    "type": "S",
    "updateDate": "2025-06-30T13:21:01Z",
    "updateDateIncludingText": "2025-06-30T13:21:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T18:39:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "VT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2013is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2013\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Hawley (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to provide for increases in the minimum wage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Higher Wages for American Workers Act of 2025 .\n#### 2. Minimum wage increase\n##### (a) In general\nSection 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ) is amended to read as follows:\n(1) except as otherwise provided in this section, not less than\u2014 (A) $15, beginning on January 1 of the first year that begins after the date of enactment of the Higher Wages for American Workers Act of 2025 ; and (B) beginning on January 1 of the second year that begins after such date of enactment, and each January 1 thereafter, the amount determined by the Secretary under subsection (h); .\n##### (b) Annual change based on inflation\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ) is amended by adding at the end the following:\n(h) (1) On September 30 of the first year that begins after the date of enactment of the Higher Wages for American Workers Act of 2025 and on September 30 of each year thereafter, the Secretary shall determine, in accordance with paragraph (2), the amount of the minimum wage to be in effect under subsection (a)(1)(B) for each period described in such subsection. (2) The wage determined under this subsection for a year shall be\u2014 (A) the amount in effect under subsection (a)(1) on the date of such determination increased by the percentage increase, if any, in the Consumer Price Index for Urban Wage Earners and Clerical Workers (or a successor index), as published by the Bureau of Labor Statistics, for the 12-month period ending with July of the year in which the determination occurs; and (B) rounded to the nearest multiple of $0.05, if the amount after applying subparagraph (A) is not a multiple of $0.05. .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect on January 1 of the first year that begins after the date of enactment of this Act.",
      "versionDate": "2025-06-10",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-06-30T13:21:01Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2013is.xml"
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
      "title": "Higher Wages for American Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Higher Wages for American Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Labor Standards Act of 1938 to provide for increases in the minimum wage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:33:23Z"
    }
  ]
}
```
