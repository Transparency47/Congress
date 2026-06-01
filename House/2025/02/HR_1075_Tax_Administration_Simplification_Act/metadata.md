# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1075?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1075
- Title: Tax Administration Simplification Act
- Congress: 119
- Bill type: HR
- Bill number: 1075
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-09-10T08:06:18Z
- Update date including text: 2025-09-10T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1075",
    "number": "1075",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Tax Administration Simplification Act",
    "type": "HR",
    "updateDate": "2025-09-10T08:06:18Z",
    "updateDateIncludingText": "2025-09-10T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1075ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1075\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. LaHood (for himself, Ms. DelBene , Mr. Feenstra , Mr. Schneider , Mr. Fitzpatrick , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to make improvements related to tax administration.\n#### 1. Short title\nThis Act may be cited as the Tax Administration Simplification Act .\n#### 2. Application of mailbox rule to documents and payments electronically submitted to the Internal Revenue Service\n##### (a) In general\nSection 7502(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by inserting and payment after filing ,\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the heading, by striking ; electronic filing , and\n**(B)**\nby striking and electronic filing , and\n**(3)**\nby adding at the end the following:\n(3) Electronic filing and payment (A) In general If any return, claim, statement, or other document required to be filed, or any payment required to be made, within a prescribed period or on or before a prescribed date under authority of any provision of the internal revenue laws is sent electronically by any person to the agency, officer, or office with which such return, claim, statement, or other document is required to be filed, or to which such payment is required to be made, the date on which such return, claim, statement, or other document, or payment, is sent electronically by such person shall be deemed to be the date of delivery or the date of payment, as the case may be, regardless of the date on which the applicable agency, officer, or office receives or reviews such return, claim, statement, document, or payment. (B) Regulations Not later than December 31, 2025, the Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this paragraph. .\n##### (b) Effective date\nThe amendments made by this section shall apply to any document or payment sent after December 31, 2025.\n#### 3. Extension of time for making S corporation elections\n##### (a) In general\nSection 1362(b) of the Internal Revenue Code of 1986 is amended to read as follows:\n(b) When made (1) In general An election under subsection (a) may be made by a small business corporation for any taxable year not later than the due date for filing the return of the S corporation for such taxable year (including extensions). (2) Certain elections treated as made for next taxable year If\u2014 (A) an election under subsection (a) is made for any taxable year within the period described in paragraph (1), but (B) either\u2014 (i) on 1 or more days in such taxable year and before the day on which the election was made the corporation did not meet the requirements of subsection (b) of section 1361, or (ii) 1 or more of the persons who held stock in the corporation during such taxable year and before the election was made did not consent to the election, then such election shall be treated as made for the following taxable year. (3) Authority to treat late elections, etc., as timely If\u2014 (A) an election under subsection (a) is made for any taxable year after the date prescribed by this subsection for making such election for such taxable year or no such election is made for any taxable year, and (B) the Secretary determines that there was reasonable cause for the failure to timely make such election, the Secretary may treat such an election as timely made for such taxable year. (4) Election on timely filed returns Except as otherwise provided by the Secretary, an election under subsection (a) for any taxable year may be made on a timely filed return of the S corporation for such taxable year. (5) Secretarial authority The Secretary may prescribe such regulations, rules, or other guidance as may be necessary or appropriate for purposes of applying this subsection. .\n##### (b) Coordination with certain other provisions\n**(1) Qualified subchapter S subsidiaries**\nSection 1361(b)(3)(B) of such Code is amended by adding at the end the following flush sentence:\nRules similar to the rules of section 1362(b) shall apply with respect to any election under clause (ii). .\n**(2) Qualified subchapter S trusts**\nSection 1361(d)(2) of such Code is amended by striking subparagraph (D).\n##### (c) Revocations\nSection 1362(d)(1) of such Code is amended\u2014\n**(1)**\nby striking subparagraph (D) in subparagraph (C) and inserting subparagraphs (D) and (E) , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Authority to treat late revocations as timely If\u2014 (i) a revocation under subparagraph (A) is made for any taxable year after the date prescribed by this paragraph for making such revocation for such taxable year or no such revocation is made for any taxable year, and (ii) the Secretary determines that there was reasonable cause for the failure to timely make such revocation, the Secretary may treat such a revocation as timely made for such taxable year. .\n##### (d) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to elections for taxable years beginning after December 31, 2025.\n**(2) Revocations**\nThe amendments made by subsection (c) shall apply to revocations made after the date of the enactment of this Act.\n#### 4. Quarterly installments for estimated income tax payments by individual\n##### (a) In general\nThe table contained in section 6654(c)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking June 15 and inserting July 15 , and\n**(2)**\nby striking September 15 and inserting October 15 .\n##### (b) Effective date\nThe amendments made by this section shall apply to installments due in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-04-01",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "1152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Electronic Filing and Payment Fairness Act",
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
        "updateDate": "2025-05-05T15:33:45Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1075ih.xml"
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
      "title": "Tax Administration Simplification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Administration Simplification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to make improvements related to tax administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T05:18:29Z"
    }
  ]
}
```
