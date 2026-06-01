# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2818?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2818
- Title: Tax Excessive CEO Pay Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2818
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-12-05T21:51:21Z
- Update date including text: 2025-12-05T21:51:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2818",
    "number": "2818",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "Tax Excessive CEO Pay Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:51:21Z",
    "updateDateIncludingText": "2025-12-05T21:51:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T20:00:50Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2818is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2818\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mr. Sanders (for himself, Ms. Warren , Mr. Van Hollen , Mr. Markey , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a corporate tax rate increase on companies whose ratio of compensation of the CEO or other highest paid employee to median worker compensation is more than 50 to 1, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Excessive CEO Pay Act of 2025 .\n#### 2. Corporate tax increase based on compensation ratio\n##### (a) In general\nSection 11 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(e) Tax increase based on pay ratio (1) In general (A) Increase imposed In the case of any corporation (except as provided in subparagraph (B)(ii)(II)) the pay ratio of which is greater than 50 to 1 for a taxable year, the 21 percent rate under subsection (b) for such taxable year shall be increased by the penalty determined under paragraph (2). (B) Pay ratio For purposes of this subsection\u2014 (i) In general The term pay ratio means the ratio described in section 229.402(u)(1)(iii) of title 17, Code of Federal Regulations (or any successor thereto), except that\u2014 (I) such ratio shall be determined with respect to any taxable year using the annualized average of the compensation amounts described in such section during the 5-year period ending on the last day of the taxable year, and (II) if the highest compensated employee of the corporation is not the principal executive officer, the ratio shall be determined based on the compensation of such highest compensated employee. (ii) Corporations not subject to SEC filing In the case of a corporation which (without regard to this clause) is not subject to the authorities described in section 229.10(a) of title 17, Code of Federal Regulations (or any successor thereto)\u2014 (I) Large corporations If the average annual gross receipts of such corporation for the 3-taxable-year period ending with the taxable year which precedes such taxable year are at least $100,000,000, such corporation shall calculate and report its pay ratio according to the method which the Secretary shall prescribe by regulations consistent with the regulation described in clause (i). (II) Other private corporations exempt Subparagraph (A) shall not apply to any such corporation if the average annual gross receipts of such corporation for the 3-taxable-year period ending with the taxable year which precedes such taxable year are less than $100,000,000. (2) Amount of penalty The penalty determined under this paragraph is an increase, expressed in percentage points, determined in accordance with the following table: If the pay ratio is: The increase is: Greater than 50 to 1, but not greater than 100 to 1 0.5 Greater than 100 to 1, but not greater than 200 to 1 1 Greater than 200 to 1, but not greater than 300 to 1 2 Greater than 300 to 1, but not greater than 400 to 1 3 Greater than 400 to 1, but not greater than 500 to 1 4 Greater than 500 to 1 5. .\n##### (b) Conforming amendments\n**(1)**\nThe following sections of the Internal Revenue Code of 1986 are each amended by inserting applicable to the corporation (after the application of section 11(e)) after section 11(b) :\n**(A)**\nSection 280C(c)(2)(B)(ii)(II).\n**(B)**\nParagraphs (2)(B) and (6)(A)(ii) of section 860E(e).\n**(C)**\nSection 7874(e)(1)(B).\n**(2)**\nSection 852(b)(3)(A) of such Code is amended by inserting (after the application of section 11(e)) after section 11(b) .\n**(3)**\nParagraphs (1) and (2) of section 1445(e) of such Code are each amended by striking in effect for the taxable year under section 11(b) and inserting applicable to such corporation under section 11 for the taxable year .\n**(4)**\nSection 1446(b)(2)(B) of such Code is amended by striking specified in section 11(b) and inserting applicable to such corporation under section 11 for the taxable year .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n##### (d) Regulations\nThe Secretary of the Treasury (or the Secretary's delegate) shall issue regulations as necessary to prevent avoidance of the purposes of the amendments made by subsection (a), including regulations to prevent the manipulation of the compensation ratio under section 11(e) of the Internal Revenue Code of 1986 by changes to the composition of the workforce (including by using the services of contractors rather than employees).",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-09-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5298",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tax Excessive CEO Pay Act of 2025",
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
        "updateDate": "2025-09-29T18:58:44Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2818is.xml"
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
      "title": "Tax Excessive CEO Pay Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T11:03:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Excessive CEO Pay Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to impose a corporate tax rate increase on companies whose ratio of compensation of the CEO or other highest paid employee to median worker compensation is more than 50 to 1, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:22Z"
    }
  ]
}
```
