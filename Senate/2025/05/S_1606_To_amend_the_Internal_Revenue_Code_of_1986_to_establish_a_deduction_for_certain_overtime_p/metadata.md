# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1606
- Title: Overtime Wages Tax Relief Act
- Congress: 119
- Bill type: S
- Bill number: 1606
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-06-06T12:45:47Z
- Update date including text: 2025-06-06T12:45:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1606",
    "number": "1606",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Overtime Wages Tax Relief Act",
    "type": "S",
    "updateDate": "2025-06-06T12:45:47Z",
    "updateDateIncludingText": "2025-06-06T12:45:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:46:13Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "AL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NE"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1606is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1606\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Marshall (for himself, Mr. Tuberville , Mr. Ricketts , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a deduction for certain overtime payments.\n#### 1. Short title\nThis Act may be cited as the Overtime Wages Tax Relief Act .\n#### 2. Deduction for overtime compensation\n##### (a) In general\n**(1) Deduction allowed**\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Overtime compensation (a) In general There shall be allowed as a deduction an amount equal to so much of any overtime compensation received by an individual as does not exceed $10,000 ($20,000 in the case of a joint return) for the taxable year. (b) Limitation The amount of the deduction allowable under subsection (a) shall be reduced (but not below zero) by $50 for each $1,000 (or fraction thereof) by which the taxpayer's modified adjusted gross income exceeds $100,000 ($200,000 in the case of a joint return). For purposes of the preceding sentence, the term modified adjusted gross income means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (c) Overtime compensation For purposes of this section, the term overtime compensation means compensation that is paid to a taxpayer\u2014 (1) at a rate of not less than one and one-half times the regular rate at which the taxpayer is employed, and (2) for work for a single employer that is in excess of a maximum number of hours of such work for a specified period of time as required pursuant to\u2014 (A) section 7 of the Fair Labor Standards Act of 1938, or (B) an agreement that\u2014 (i) is a collective bargaining agreement or an agreement or understanding arrived at between the employer and the employee before performance of the work, and (ii) provides that such maximum number of hours for a specified period of time is not less than 40 hours for a 7-day work period. (d) Regulations The Secretary shall provide such regulations or other guidance as may be necessary to carry out this section. .\n**(2) Conforming amendment**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Overtime payments. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (3), by striking the period at the end of paragraph (4) and inserting and , and by adding at the end the following new paragraph:\n(5) the deduction provided in section 224. .\n##### (c) Non-Application of certain limitations for itemizers\n**(1) Deduction not treated as a miscellaneous itemized deduction**\nSection 67(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (11), by striking the period at the end of paragraph (12) and inserting , and , and by adding at the end the following new paragraph:\n(13) the deduction under section 224 (relating to overtime compensation). .\n**(2) Deduction not taken into account under overall limitation**\nSection 68(c) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (2), by striking the period at the end of paragraph (3) and inserting , and , and by adding at the end the following new paragraph:\n(4) the deduction under section 224 (relating to overtime compensation). .\n##### (d) Reporting\nSection 6051(a) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) the total amount of overtime compensation as defined in section 224(b). .\n##### (e) Withholding\nThe Secretary of the Treasury (or the Secretary's delegate) shall modify the tables and procedures prescribed under section 3402(a) of the Internal Revenue Code of 1986 to take into account the deduction allowed under section 224 of such Code (as added by this Act).\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-06-06T12:45:47Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1606is.xml"
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
      "title": "Overtime Wages Tax Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Overtime Wages Tax Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a deduction for certain overtime payments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:29Z"
    }
  ]
}
```
