# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1917?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1917
- Title: Investing in All of America Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1917
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-02-05T12:03:16Z
- Update date including text: 2026-02-05T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1917",
    "number": "1917",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Investing in All of America Act of 2025",
    "type": "S",
    "updateDate": "2026-02-05T12:03:16Z",
    "updateDateIncludingText": "2026-02-05T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T19:56:57Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T19:56:57Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "KS"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1917is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1917\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Hickenlooper (for himself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Investment Act of 1958 to exclude from the limit on leverage certain amounts invested in smaller enterprises located in rural or low-income areas and small businesses in critical technology areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Investing in All of America Act of 2025 .\n#### 2. Small business investment company maximum leverage exclusion\n##### (a) Definitions\nSection 103(9) of the Small Business Investment Act of 1958 ( 15 U.S.C. 662(9) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by striking and at the end;\n**(2)**\nin subparagraph (B)(iii)\u2014\n**(A)**\nin subclause (I), by striking established prior to October 1, 1987 ;\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby striking or and inserting , ; and\n**(ii)**\nby inserting , or a foundation, endowment, or trust of a college or university after pension plan ; and\n**(C)**\nin subclause (III), by striking the semicolon at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) does not include any funds obtained directly or indirectly from any Federal, State or local government or any government agency or instrumentality, except for funds described in subclauses (I) through (III) of subparagraph (B)(iii), for the purpose of approval by the Administrator of any request for leverage. .\n##### (b) Maximum leverage exclusion\nSection 303(b)(2) of the Small Business Investment Act of 1958 ( 15 U.S.C. 683(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking 300 and inserting 200 ; and\n**(B)**\nby striking clause (ii) and inserting the following:\n(ii) (I) with respect to such a company that makes quarterly or semiannual interest payments, $175,000,000, as adjusted in accordance with subparagraph (E); or (II) $175,000,000 with respect to any other such company. ;\n**(2)**\nin subparagraph (B), by striking may not exceed $350,000,000. and inserting the following: \u201cmay not exceed\u2014\n(i) with respect to such companies that are commonly controlled and that make quarterly or semiannual interest payments, $350,000,000, as adjusted in accordance with subparagraph (E); or (ii) $350,000,000 with respect to other such companies that are commonly controlled. ;\n**(3)**\nin subparagraph (C)\u2014\n**(A)**\nin the heading\u2014\n**(i)**\nby inserting or rural after low-income ; and\n**(ii)**\nby inserting , critical technology areas, or small manufacturers after geographic areas ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nby striking (i) In calculating and inserting the following:\n(i) In general Except as provided in clause (iii), in calculating ;\n**(ii)**\nby inserting or companies after of a company ;\n**(iii)**\nby striking subparagraph (A) and inserting subparagraphs (A) and (B) ;\n**(iv)**\nby striking equity ; and\n**(v)**\nby striking the company in a smaller enterprise and all that follows and inserting the following:\nthe company or companies in\u2014 (I) a small business concern located in a low-income geographic area (as defined in section 351 of this title) or in a rural area (as defined in section 343(a) of the Agricultural Act of 1961 ( 7 U.S.C. 1991(a) )); (II) a small business concern operating primarily in a covered technology category (as defined in section 149 of title 10, United States Code); or (III) a small manufacturer (as defined in section 501(e) of this Act). ; and\n**(C)**\nby amending clause (ii) to read as follows:\n(ii) Limitation While maintaining the limitation of subparagraph (A)(i) and consistent with a leverage determination ratio issued pursuant to section 301(c), the aggregate amount excluded for a company or companies under clause (i) from the calculation of the outstanding leverage such company or companies for the purposes of subparagraphs (A) and (B) may not exceed the lesser of 50 percent of the private capital of such company or companies or $125,000,000 ; and\n**(D)**\nby amending clause (iii) to read as follows:\n(iii) Prospective applicability An investment by a licensee is eligible for exclusion from the calculation of outstanding leverage under clause (i) only if such investment is made by such licensee after the date of enactment of this clause. ; and\n**(4)**\nby adding at the end the following:\n(E) Annual adjustment Except as provided in subparagraph (F), the Administrator shall adjust the dollar amounts described in subparagraphs (A) and (B)\u2014 (i) on the date of the enactment of this subparagraph, by a percentage equal to the percentage (if any) by which the Consumer Price Index (all items; United States city average), as published by the Bureau of Labor Statistics, increased during the period\u2014 (I) beginning on December 18, 2015, and ending on the date of enactment of the Investing in All of America Act of 2025 , with respect to a dollar amount under subparagraph (B); and (II) beginning on June 21, 2018, and ending on the date of enactment of the Investing in All of America Act of 2025 , with respect to a dollar amount under subparagraph (A); and (ii) on the date that is 1 year after the date of enactment of the Investing in All of America Act of 2025 , and annually thereafter, by a percentage equal to the percentage (if any) by which the Consumer Price Index (all items; United States city average), as published by the Bureau of Labor Statistics, increased during the 1-year period preceding the date of the adjustment under this clause. (F) Exclusion Subparagraph (E) shall not apply with respect to a small business investment company authorized to issue accrual debentures (as defined in section 107.50 of title 13, Code of Federal Regulations). .",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-12-02",
        "text": "Received in the Senate and Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "2066",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Investing in All of America Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-03",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "3341",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Investing in All of America Act of 2025",
      "type": "S"
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
            "name": "Business investment and capital",
            "updateDate": "2025-08-27T17:30:34Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-27T17:30:34Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-08-27T17:30:34Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-08-27T17:30:34Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-08-27T17:30:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-06-13T13:33:55Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1917is.xml"
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
      "title": "Investing in All of America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investing in All of America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Investment Act of 1958 to exclude from the limit on leverage certain amounts invested in smaller enterprises located in rural or low-income areas and small businesses in critical technology areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:26Z"
    }
  ]
}
```
