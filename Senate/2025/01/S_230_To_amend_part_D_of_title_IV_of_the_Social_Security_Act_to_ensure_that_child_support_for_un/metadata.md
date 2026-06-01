# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/230
- Title: Unborn Child Support Act
- Congress: 119
- Bill type: S
- Bill number: 230
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-05T21:46:24Z
- Update date including text: 2025-12-05T21:46:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/230",
    "number": "230",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Unborn Child Support Act",
    "type": "S",
    "updateDate": "2025-12-05T21:46:24Z",
    "updateDateIncludingText": "2025-12-05T21:46:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T20:32:41Z",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s230is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 230\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cramer (for himself, Mr. Banks , Mrs. Blackburn , Mrs. Britt , Mr. Daines , Mr. Hoeven , Mrs. Hyde-Smith , Mr. Lankford , Mr. Marshall , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend part D of title IV of the Social Security Act to ensure that child support for unborn children is collected and distributed under the child support enforcement program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unborn Child Support Act .\n#### 2. Child support enforcement on behalf of unborn children\n##### (a) State plan amendment\nSection 454 of the Social Security Act ( 42 U.S.C. 654 ) is amended\u2014\n**(1)**\nin paragraph (4)(A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nby inserting , including an unborn child, after child ; and\n**(ii)**\nby inserting and after the semicolon; and\n**(B)**\nin clause (ii), by inserting , including an unborn child after other child ;\n**(2)**\nin paragraph (33), by striking and after the semicolon;\n**(3)**\nin paragraph (34), by striking the period and inserting ; and ;\n**(4)**\nby inserting after paragraph (34), the following:\n(35) provide that the State will establish and enforce child support obligations of the biological father of an unborn child (and subsequent to the birth of the child) to the mother of such child provided that\u2014 (A) the mother has requested payment of such child support obligations; (B) the start date for such obligations may begin with the first month in which the child was conceived, as determined by a physician (and shall begin with that month if the mother so requests); (C) payments for such obligations may be retroactively collected or awarded, including in the case where paternity is established subsequent to the birth of the child; (D) the payment amount for such obligations shall be determined by a court, in consultation with the mother, taking into account the best interests of the mother and child; (E) any measure to establish the paternity of a child (born or unborn) shall not be required without the consent of the mother; and (F) any measure to establish the paternity of an unborn child shall not be taken if the measure poses any risk of harm to the child if unborn. ; and\n**(5)**\nby adding at the end the following: For purposes of paragraphs (4) and (35), the term unborn child means a member of the species homo sapiens, at any stage of development, who is carried in the womb.\n##### (b) Limitation of waiver authority\nSection 1115 of the Social Security Act ( 42 U.S.C. 1315 ) is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by striking In the case of and inserting Except as provided in subsection (c), in the case of ;\n**(2)**\nin subsection (b)(1), in the matter preceding subparagraph (A), by striking In the case of and inserting Except as provided in subsection (c), in the case of ; and\n**(3)**\nby striking subsection (c) and inserting the following:\n(c) No experimental, pilot, or demonstration project undertaken under subsection (a) to assist in promoting the objectives of part D of title IV, may permit modifications of paragraphs (4)(A)(ii) and (35) of section 454 to establish and enforce child support obligations of the biological father of an unborn child. For purposes of the preceding sentence, the term unborn child means a member of the species homo sapiens, at any stage of development, who is carried in the womb. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 2 years after the date of enactment of this Act and shall apply to payments under part D of title IV of the Social Security Act ( 42 U.S.C. 651 et seq. ) for calendar quarters beginning on or after such date.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1630",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MOMS Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-07",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3235",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MOMS Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Unborn Child Support Act",
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
            "name": "Separation, divorce, custody, support",
            "updateDate": "2025-03-21T19:52:31Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-21T19:52:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-03-01T17:21:24Z"
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
          "measure-id": "id119s230",
          "measure-number": "230",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s230v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Unborn Child Support Act</b><br/> <br/> This bill requires states to apply child support obligations to the time period during pregnancy. This requirement is applicable retroactively based on a court order at the request of the pregnant parent and a determination by a physician of the month during which the child was conceived. Existing state requirements are applicable to these obligations, such as proof of parenthood.</p>"
        },
        "title": "Unborn Child Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s230.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Unborn Child Support Act</b><br/> <br/> This bill requires states to apply child support obligations to the time period during pregnancy. This requirement is applicable retroactively based on a court order at the request of the pregnant parent and a determination by a physician of the month during which the child was conceived. Existing state requirements are applicable to these obligations, such as proof of parenthood.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s230"
    },
    "title": "Unborn Child Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Unborn Child Support Act</b><br/> <br/> This bill requires states to apply child support obligations to the time period during pregnancy. This requirement is applicable retroactively based on a court order at the request of the pregnant parent and a determination by a physician of the month during which the child was conceived. Existing state requirements are applicable to these obligations, such as proof of parenthood.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s230"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s230is.xml"
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
      "title": "Unborn Child Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unborn Child Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend part D of title IV of the Social Security Act to ensure that child support for unborn children is collected and distributed under the child support enforcement program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:41Z"
    }
  ]
}
```
