# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1719?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1719
- Title: Primary Care Enhancement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1719
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2025-10-09T03:26:19Z
- Update date including text: 2025-10-09T03:26:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1719",
    "number": "1719",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Primary Care Enhancement Act of 2025",
    "type": "S",
    "updateDate": "2025-10-09T03:26:19Z",
    "updateDateIncludingText": "2025-10-09T03:26:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
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
      "actionDate": "2025-05-12",
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
          "date": "2025-05-13T00:51:28Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "NH"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "AZ"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1719is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1719\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Cassidy (for himself, Mrs. Shaheen , Mr. Scott of South Carolina , Mr. Kelly , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for the treatment of direct primary care service arrangements as medical care, to provide that such arrangements do not disqualify deductible health savings account contributions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Primary Care Enhancement Act of 2025 .\n#### 2. Treatment of direct primary care service arrangements\n##### (a) Amount treated as medical care\n**(1) In general**\nSection 213(d)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by inserting after subparagraph (D) the following new subparagraph:\n(E) for direct primary care service arrangements. .\n**(2) Limitation**\nSection 213(d)(1) of such Code, as amended by paragraph (1), is further amended by adding at the end the following: In the case of a direct care primary service arrangement, only eligible fee amounts (as defined in paragraph (13)) shall be taken into account under subparagraph (E). .\n**(3) Definitions**\nSection 213(d) of such Code is amended by inserting after paragraph (11) the following new paragraphs:\n(12) Direct primary care service arrangement (A) In general The term direct primary care service arrangement means, with respect to any individual, an arrangement under which such individual is provided medical care (as defined in paragraph (1), determined without regard to subparagraph (E) thereof) consisting solely of primary care services provided by primary care practitioners (as defined in section 1833(x)(2)(A) of the Social Security Act, determined without regard to clause (ii) thereof), if the sole compensation for such care is a fixed periodic fee. (B) Certain services specifically excluded from treatment as primary care services For purposes of this paragraph, the term primary care services shall not include\u2014 (i) procedures that require the use of general anesthesia, and (ii) laboratory services not typically administered in an ambulatory primary care setting. The Secretary, after consultation with the Secretary of Health and Human Services, shall issue regulations or other guidance regarding the application of this subparagraph. (13) Eligible fee amount (A) In general The term eligible fee amount means, with respect to any individual for any month, the amount of fixed periodic fees paid for a direct care primary service arrangement, to the extent that the aggregate fees for all direct primary care service arrangements with respect to such individual for such month do not exceed $150 (twice such dollar amount in the case of an individual with any direct primary care service arrangement that covers more than one individual). (B) Indexing In the case of any taxable year beginning in a calendar year after 2026, the $150 amount contained in subparagraph (A) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. If any increase under the preceding sentence is not a multiple of $10, such increase shall be rounded to the nearest multiple of $10. .\n##### (b) Health savings accounts\nSection 223(c) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Treatment of direct primary care service arrangements A direct care primary service arrangement (as defined in section 213(d)(12))\u2014 (A) shall not be treated as a health plan for purposes of paragraph (1)(A)(ii), and (B) shall not be treated as insurance for purposes of subsection (d)(2)(B). .\n##### (c) Reporting of direct primary care service arrangement fees on W\u20132\nSection 6051(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) in the case of a direct primary care service arrangement (as defined in section 213(d)(12)) which is provided in connection with employment, the aggregate fees for such arrangement for such employee. .\n##### (d) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2025-05-12",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:30:52Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1719is.xml"
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
      "title": "Primary Care Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Primary Care Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide for the treatment of direct primary care service arrangements as medical care, to provide that such arrangements do not disqualify deductible health savings account contributions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:39Z"
    }
  ]
}
```
