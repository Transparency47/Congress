# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1707
- Title: Helping Young Americans Save for Retirement Act
- Congress: 119
- Bill type: S
- Bill number: 1707
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-02-11T12:03:24Z
- Update date including text: 2026-02-11T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1707",
    "number": "1707",
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
    "title": "Helping Young Americans Save for Retirement Act",
    "type": "S",
    "updateDate": "2026-02-11T12:03:24Z",
    "updateDateIncludingText": "2026-02-11T12:03:24Z"
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
        "item": [
          {
            "date": "2025-05-12T19:28:05Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-12T19:28:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "VA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NH"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "OH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "ME"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1707is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1707\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Cassidy (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 with respect to minimum participation standards for pension plans and qualified trusts.\n#### 1. Short title\nThis Act may be cited as the Helping Young Americans Save for Retirement Act .\n#### 2. Eligibility at age 18 under certain conditions\n##### (a) ERISA\n**(1) Age 18**\nSubparagraphs (A) and (B) of section 202(c)(1) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1052(c)(1) ) are amended to read as follows:\n(A) the period permitted under subsection (a)(1), determined\u2014 (i) without regard to subparagraph (B)(i) thereof; and (ii) by substituting 18 for 21 in subparagraph (A)(i) thereof; or (B) the first 24-month period\u2014 (i) consisting of 2 consecutive 12-month periods during each of which the employee has at least 500 hours of service; and (ii) by the close of which the employee has met the requirement of subsection (a)(1)(A)(i) (without regard to subparagraph (A)(ii) of this paragraph). .\n**(2) Conforming amendments**\nSection 202(c) of such Act ( 29 U.S.C. 1052(c) ) is amended\u2014\n**(A)**\nin the subsection heading\u2014\n**(i)**\nby striking Special rule and inserting Special rules ; and\n**(ii)**\nby adding and certain younger employees after employees ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking paragraph (1)(B) and inserting paragraph (1) ; and\n**(ii)**\nby striking section 401(k)(2)(D)(ii) and inserting section 401(k)(2)(D) .\n**(3) Opinion of independent qualified public accountant**\nSection 104(a)(2) of such Act ( 29 U.S.C. 1024(a)(2) ) is amended by adding at the end the following:\n(C) For purposes of subparagraph (A) and the last sentence of section 103(a)(3)(A), with respect to a pension plan in which at least one employee participates solely by reason of section 202(c)(1)(A), no employee participating in such plan solely by reason of section 202(c)(1)(A) shall be counted as a participant until the date that is 5 years after the date on which the first such employee first becomes a participant in such plan. .\n##### (b) Internal Revenue Code of 1986\n**(1) Age 18**\nClauses (i) and (ii) of section 401(k)(2)(D) of the Internal Revenue Code of 1986 are amended to read as follows:\n(i) the period permitted under section 410(a)(1), determined\u2014 (I) without regard to subparagraph (B)(i) thereof, and (II) by substituting 18 for 21 in subparagraph (A)(i) thereof, or (ii) subject to the provisions of paragraph (15), the first of 2 consecutive 12-month periods during each of which the employee has at least 500 hours of service, provided that the employee has satisfied the requirements of section 410(a)(1)(A)(i) (without regard to clause (i)(II) of this subparagraph). .\n**(2) Conforming amendments**\nThe Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin section 401(k)(15)\u2014\n**(i)**\nin the paragraph heading, by adding and certain younger workers after workers ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clauses (i) and (ii), by striking (2)(D)(ii) each place it appears and inserting (2)(D) ;\n**(II)**\nin clause (i), by striking 202(c)(1)(B) and inserting 202(c)(1) ; and\n**(III)**\nin clause (iv), striking paragraph (2)(D)(ii) and inserting clauses (i)(II) and (ii) of paragraph (2)(D) ; and\n**(B)**\nin section 403(b)(12)\u2014\n**(i)**\nin subparagraph (A), by striking section 202(c) and inserting section 202(c)(1)(B) ; and\n**(ii)**\nin subparagraph (D)\u2014\n**(I)**\nin the subparagraph heading, by inserting and certain younger employees after employees ; and\n**(II)**\nin clause (i), by striking 202(c)(1)(B) and adding 202(c)(1) .\n##### (c) Application\nThe amendments made by this section shall apply to plan years beginning on or after the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-05-12",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4718",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping Young Americans Save for Retirement Act",
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
        "updateDate": "2025-06-06T18:30:20Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1707is.xml"
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
      "title": "Helping Young Americans Save for Retirement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Young Americans Save for Retirement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 with respect to minimum participation standards for pension plans and qualified trusts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:32Z"
    }
  ]
}
```
