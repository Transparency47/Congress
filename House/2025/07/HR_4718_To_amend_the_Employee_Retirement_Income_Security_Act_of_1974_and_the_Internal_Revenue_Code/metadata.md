# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4718?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4718
- Title: Helping Young Americans Save for Retirement Act
- Congress: 119
- Bill type: HR
- Bill number: 4718
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-22T08:08:24Z
- Update date including text: 2026-05-22T08:08:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4718",
    "number": "4718",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Helping Young Americans Save for Retirement Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:24Z",
    "updateDateIncludingText": "2026-05-22T08:08:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:10:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:10:10Z",
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
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4718ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4718\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Pettersen (for herself and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 with respect to minimum participation standards for pension plans and qualified trusts.\n#### 1. Short title\nThis Act may be cited as the Helping Young Americans Save for Retirement Act .\n#### 2. Eligibility at age 18 under certain conditions\n##### (a) ERISA\n**(1) Age 18**\nSubparagraphs (A) and (B) of section 202(c)(1) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1052(c)(1) ) are amended to read as follows:\n(A) the period permitted under subsection (a)(1), determined\u2014 (i) without regard to subparagraph (B)(i) thereof; and (ii) by substituting 18 for 21 in subparagraph (A)(i) thereof; or (B) the first 24-month period\u2014 (i) consisting of 2 consecutive 12-month periods during each of which the employee has at least 500 hours of service; and (ii) by the close of which the employee has met the requirement of subsection (a)(1)(A)(i) (without regard to subparagraph (A)(ii) of this paragraph). .\n**(2) Conforming amendments**\nSection 202(c) of such Act ( 29 U.S.C. 1052(c) ) is amended\u2014\n**(A)**\nin the subsection heading\u2014\n**(i)**\nby striking Special rule and inserting Special rules ; and\n**(ii)**\nby adding and certain younger employees after employees ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking paragraph (1)(B) and inserting paragraph (1) ; and\n**(ii)**\nby striking section 401(k)(2)(D)(ii) and inserting section 401(k)(2)(D) .\n**(3) Opinion of independent qualified public accountant**\nSection 104(a)(2) of such Act ( 29 U.S.C. 1024(a)(2) ) is amended by adding at the end the following:\n(C) For purposes of subparagraph (A) and the last sentence of section 103(a)(3)(A), with respect to a pension plan in which at least one employee participates solely by reason of section 202(c)(1)(A), no employee participating in such plan solely by reason of section 202(c)(1)(A) shall be counted as a participant until the date that is 5 years after the date on which the first such employee first becomes a participant in such plan. .\n##### (b) Internal Revenue Code of 1986\n**(1) Age 18**\nClauses (i) and (ii) of section 401(k)(2)(D) of the Internal Revenue Code of 1986 are amended to read as follows:\n(i) the period permitted under section 410(a)(1), determined\u2014 (I) without regard to subparagraph (B)(i) thereof, and (II) by substituting 18 for 21 in subparagraph (A)(i) thereof, or (ii) subject to the provisions of paragraph (15), the first of 2 consecutive 12-month periods during each of which the employee has at least 500 hours of service, provided that the employee has satisfied the requirements of section 410(a)(1)(A)(i) (without regard to clause (i)(II) of this subparagraph). .\n**(2) Conforming amendments**\nThe Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin section 401(k)(15)\u2014\n**(i)**\nin the paragraph heading, by adding and certain younger workers after workers ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clauses (i) and (ii), by striking (2)(D)(ii) each place it appears and inserting (2)(D) ;\n**(II)**\nin clause (i), by striking 202(c)(1)(B) and inserting 202(c)(1) ; and\n**(III)**\nin clause (iv), striking paragraph (2)(D)(ii) and inserting clauses (i)(II) and (ii) of paragraph (2)(D) ; and\n**(B)**\nin section 403(b)(12)\u2014\n**(i)**\nin subparagraph (A), by striking section 202(c) and inserting section 202(c)(1)(B) ; and\n**(ii)**\nin subparagraph (D)\u2014\n**(I)**\nin the subparagraph heading, by inserting and certain younger employees after employees ; and\n**(II)**\nin clause (i), by striking 202(c)(1)(B) and adding 202(c)(1) .\n##### (c) Application\nThe amendments made by this section shall apply to plan years beginning on or after the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-05-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1707",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Helping Young Americans Save for Retirement Act",
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
        "name": "Taxation",
        "updateDate": "2025-09-16T21:57:16Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4718ih.xml"
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
      "title": "Helping Young Americans Save for Retirement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Young Americans Save for Retirement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 and the Internal Revenue Code of 1986 with respect to minimum participation standards for pension plans and qualified trusts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:32Z"
    }
  ]
}
```
