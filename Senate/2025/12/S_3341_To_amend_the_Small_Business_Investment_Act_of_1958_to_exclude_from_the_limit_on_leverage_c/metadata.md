# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3341
- Title: Investing in All of America Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3341
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-04-27T18:55:44Z
- Update date including text: 2026-04-27T18:55:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3341",
    "number": "3341",
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
    "updateDate": "2026-04-27T18:55:44Z",
    "updateDateIncludingText": "2026-04-27T18:55:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
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
            "date": "2025-12-03T22:59:56Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-03T22:59:56Z",
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
      "sponsorshipDate": "2025-12-03",
      "state": "KS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "IN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "DE"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "OH"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3341is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3341\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Mr. Hickenlooper (for himself, Mr. Marshall , Mr. Young , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Investment Act of 1958 to exclude from the limit on leverage certain amounts invested in smaller enterprises located in rural or low-income areas and small businesses in critical technology areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Investing in All of America Act of 2025 .\n#### 2. Small business investment company maximum leverage exclusion\n##### (a) Definitions\nSection 103(9) of the Small Business Investment Act of 1958 ( 15 U.S.C. 662(9) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by striking and at the end;\n**(2)**\nin subparagraph (B)(iii)\u2014\n**(A)**\nin subclause (I), by striking established prior to October 1, 1987 ;\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby striking or and inserting a comma; and\n**(ii)**\nby inserting , or a foundation, endowment, or trust of a college or university after pension plan ; and\n**(C)**\nin subclause (III), by striking the semicolon at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) does not include any funds obtained directly or indirectly from any Federal, State or local government or any government agency or instrumentality, except for funds described in subclauses (I) through (III) of subparagraph (B)(iii), for the purpose of approval by the Administrator of any request for leverage. .\n##### (b) Maximum leverage exclusion\nSection 303(b)(2) of the Small Business Investment Act of 1958 ( 15 U.S.C. 683(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking 300 and inserting 200 ; and\n**(B)**\nby amending clause (ii) to read as follows:\n(ii) (I) with respect to such a company that makes quarterly or semiannual interest payments, $250,000,000; or (II) $175,000,000 with respect to any other such company licensed under section 301(c). ;\n**(2)**\nin subparagraph (B), by striking may not exceed $350,000,000. and inserting the following: \u201cmay not exceed\u2014\n(i) with respect to such companies that are commonly controlled and that make quarterly or semiannual interest payments, $475,000,000; or (ii) $350,000,000 with respect to other companies licensed under section 301(c) that are commonly controlled. ; and\n**(3)**\nin subparagraph (C)\u2014\n**(A)**\nin the heading\u2014\n**(i)**\nby inserting or rural after low-income ; and\n**(ii)**\nby inserting , critical technology areas, or small manufacturers after geographic areas ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nby striking (i) In calculating and inserting the following:\n(i) In general Except as provided in clause (iii), in calculating ;\n**(ii)**\nby inserting or companies after of a company ;\n**(iii)**\nby striking subparagraph (A) and inserting subparagraphs (A) and (B) ;\n**(iv)**\nby striking equity ; and\n**(v)**\nby striking the company in a smaller enterprise and all that follows and inserting the following:\nthe company or companies in\u2014 (I) a small business concern located in a low-income geographic area (as defined in section 351 of this title) or in a rural area (as defined in section 343(a) of the Agricultural Act of 1961 ( 7 U.S.C. 1991(a) )); (II) a small business concern operating primarily in a covered technology category (as defined in section 149(f) of title 10, United States Code); or (III) a small manufacturer (as defined in section 501(e)(6) of this Act). ;\n**(C)**\nby amending clause (ii) to read as follows:\n(ii) Limitation While maintaining the limitation of subparagraph (A)(i) and consistent with a leverage determination ratio issued pursuant to section 301(c), the aggregate amount excluded for a company or companies under clause (i) from the calculation of the outstanding leverage such company or companies for the purposes of subparagraphs (A) and (B) may not exceed the lesser of 50 percent of the private capital of such company or companies or $125,000,000 ; and\n**(D)**\nby amending clause (iii) to read as follows:\n(iii) Prospective applicability An investment by a licensee is eligible for exclusion from the calculation of outstanding leverage under clause (i) only if such investment is made by such licensee after the date of enactment of this clause. .",
      "versionDate": "2025-12-03",
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
        "actionDate": "2026-04-16",
        "text": "Message on Senate action sent to the House."
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "1917",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-01-07T17:32:02Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3341is.xml"
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
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investing in All of America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Investment Act of 1958 to exclude from the limit on leverage certain amounts invested in smaller enterprises located in rural or low-income areas and small businesses in critical technology areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:23Z"
    }
  ]
}
```
