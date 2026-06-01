# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3073?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3073
- Title: Pay Our Capitol Police Act
- Congress: 119
- Bill type: S
- Bill number: 3073
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-12-05T22:02:09Z
- Update date including text: 2025-12-05T22:02:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3073",
    "number": "3073",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Pay Our Capitol Police Act",
    "type": "S",
    "updateDate": "2025-12-05T22:02:09Z",
    "updateDateIncludingText": "2025-12-05T22:02:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T18:19:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "OK"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "AK"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "SC"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "AK"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "OK"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "ND"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "KS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "FL"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3073is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3073\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Mr. Scott of South Carolina (for himself, Mr. Mullin , Ms. Murkowski , Mr. Graham , Mr. Sullivan , Mrs. Hyde-Smith , Mr. Lankford , Mr. Cramer , Mr. Moran , Mr. Scott of Florida , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for the United States Capitol Police with respect to a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Pay Our Capitol Police Act .\n#### 2. Continuing appropriations for the United States Capitol Police\n##### (a) In general\nThere are hereby appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 are not in effect\u2014\n**(1)**\nsuch sums as are necessary to provide salaries, including overtime, hazardous duty pay, and Government contributions for health, retirement, social security, professional liability insurance, tuition reimbursement, recruitment and retention bonuses, and other applicable employee benefits, to\u2014\n**(A)**\nmembers of the Capitol Police whom the Chief of the Capitol Police determines are excepted employees or employees performing emergency work, as those terms are defined by the Office of Personnel Management, during such period; and\n**(B)**\ncivilian employees of the Capitol Police whom the Chief of the Capitol Police determines are providing support to the members of the Capitol Police described in subparagraph (A); and\n**(2)**\nsuch sums as are necessary to provide payment to contractors of the Capitol Police whom the Chief of the Capitol Police determines are providing support to members of the Capitol Police described in paragraph (1)(A).\n##### (b) Interim continuing appropriations\nAppropriations made available under subsection (a) may not be obligated or expended for the Capitol Police during any period during which continuing appropriations for the purposes for which amounts are made available under subsection (a) are in effect for the Capitol Police.\n##### (c) Charge to future appropriations\nExpenditures made pursuant to subsection (a) shall be charged to the applicable appropriation, fund, or authorization whenever an Act in which such applicable appropriation, fund, or authorization is included is enacted into law.\n#### 3. Termination\nAppropriations and funds made available and authority granted pursuant to this Act shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of appropriations for the Capitol Police through September 30, 2026 (including a continuing appropriation) for any purpose for which amounts are made available in section 2.\n**(2)**\nThe enactment into law of appropriations for the legislative branch through September 30, 2026 (including a continuing appropriation) without any appropriation for such purpose.\n**(3)**\nSeptember 30, 2026.\n#### 4. Effective date; special rule\n##### (a) Effective date\nThis Act shall take effect as if enacted on October 1, 2025.\n##### (b) Special rule\nPayments of pay and allowances from amounts appropriated under section 2 for any portion of the period beginning on October 1, 2025, and ending on the day before the date of enactment of this Act shall be provided as soon as practicable after such date of enactment.",
      "versionDate": "2025-10-29",
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
        "actionDate": "2025-11-04",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5924",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Pay Our Capitol Police Act",
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
        "name": "Congress",
        "updateDate": "2025-11-06T16:47:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-29",
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
          "measure-id": "id119s3073",
          "measure-number": "3073",
          "measure-type": "s",
          "orig-publish-date": "2025-10-29",
          "originChamber": "SENATE",
          "update-date": "2025-11-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3073v00",
            "update-date": "2025-11-06"
          },
          "action-date": "2025-10-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Pay Our Capitol Police Act</strong></p><p>This bill provides FY2026 continuing appropriations for the U.S. Capitol Police (USCP) to pay and provide benefits for employees who are working during a government shutdown.</p><p>The bill provides the appropriations for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown). Specifically, the bill provides the appropriations to the USCP for salaries, overtime pay, hazardous duty pay, recruitment and retention bonuses, and employee benefits for (1) members of the\u00a0USCP who are excepted employees (i.e., required to work) or are performing emergency work during the shutdown, and (2) civilian employees who are providing support to the members.</p><p>The bill also provides appropriations for payments to USCP contractors who are providing support to the members of the\u00a0USCP who are working during the shutdown.\u00a0</p><p>The appropriations provided by this bill may not be used during any period in which continuing appropriations are in effect for these purposes.\u00a0</p><p>The appropriations are available until the earlier of (1) the enactment into law of legislation to provide FY2026 appropriations for the USCP or the legislative branch (including continuing appropriations), or (2) September 30, 2026.</p><p>The bill must take effect as if it had been enacted on October 1, 2025.</p>"
        },
        "title": "Pay Our Capitol Police Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3073.xml",
    "summary": {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Capitol Police Act</strong></p><p>This bill provides FY2026 continuing appropriations for the U.S. Capitol Police (USCP) to pay and provide benefits for employees who are working during a government shutdown.</p><p>The bill provides the appropriations for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown). Specifically, the bill provides the appropriations to the USCP for salaries, overtime pay, hazardous duty pay, recruitment and retention bonuses, and employee benefits for (1) members of the\u00a0USCP who are excepted employees (i.e., required to work) or are performing emergency work during the shutdown, and (2) civilian employees who are providing support to the members.</p><p>The bill also provides appropriations for payments to USCP contractors who are providing support to the members of the\u00a0USCP who are working during the shutdown.\u00a0</p><p>The appropriations provided by this bill may not be used during any period in which continuing appropriations are in effect for these purposes.\u00a0</p><p>The appropriations are available until the earlier of (1) the enactment into law of legislation to provide FY2026 appropriations for the USCP or the legislative branch (including continuing appropriations), or (2) September 30, 2026.</p><p>The bill must take effect as if it had been enacted on October 1, 2025.</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3073"
    },
    "title": "Pay Our Capitol Police Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Pay Our Capitol Police Act</strong></p><p>This bill provides FY2026 continuing appropriations for the U.S. Capitol Police (USCP) to pay and provide benefits for employees who are working during a government shutdown.</p><p>The bill provides the appropriations for any period during which interim or full-year appropriations for FY2026 are not in effect (i.e., a government shutdown). Specifically, the bill provides the appropriations to the USCP for salaries, overtime pay, hazardous duty pay, recruitment and retention bonuses, and employee benefits for (1) members of the\u00a0USCP who are excepted employees (i.e., required to work) or are performing emergency work during the shutdown, and (2) civilian employees who are providing support to the members.</p><p>The bill also provides appropriations for payments to USCP contractors who are providing support to the members of the\u00a0USCP who are working during the shutdown.\u00a0</p><p>The appropriations provided by this bill may not be used during any period in which continuing appropriations are in effect for these purposes.\u00a0</p><p>The appropriations are available until the earlier of (1) the enactment into law of legislation to provide FY2026 appropriations for the USCP or the legislative branch (including continuing appropriations), or (2) September 30, 2026.</p><p>The bill must take effect as if it had been enacted on October 1, 2025.</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119s3073"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3073is.xml"
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
      "title": "Pay Our Capitol Police Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay Our Capitol Police Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill making continuing appropriations for the United States Capitol Police with respect to a Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-31T04:18:14Z"
    }
  ]
}
```
