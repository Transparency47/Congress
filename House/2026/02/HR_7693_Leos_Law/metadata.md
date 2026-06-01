# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7693?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7693
- Title: Leo’s Law
- Congress: 119
- Bill type: HR
- Bill number: 7693
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-06T21:13:11Z
- Update date including text: 2026-04-06T21:13:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7693",
    "number": "7693",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Leo\u2019s Law",
    "type": "HR",
    "updateDate": "2026-04-06T21:13:11Z",
    "updateDateIncludingText": "2026-04-06T21:13:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7693ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7693\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Gottheimer (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo mitigate the effects of the COVID\u201319 pandemic on incentives under the Federal Food, Drug, and Cosmetic Act for the development of orphan drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Leo\u2019s Law .\n#### 2. Mitigation of effects of COVID\u201319 pandemic on orphan-drug development incentives\n##### (a) In general\nIn the case of a covered orphan drug, each of the following exclusivity periods is deemed to be extended by 180 days, so long as such period is not expired:\n**(1)**\nThe 12-year period referred to in subparagraph (A) of section 351(k)(7) of the Public Health Service Act ( 42 U.S.C. 262(k)(7) ).\n**(2)**\nThe 5-year period referred to in subsection (c)(3)(E)(ii) and subsection (j)(5)(F)(ii) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n**(3)**\nThe 3-year period referred to in each of clauses (iii) and (iv) of subsection (c)(3)(E) and clauses (iii) and (iv) of subsection (j)(5)(F) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n**(4)**\nThe 7-year period referred to in section 527(a) of the Federal, Food, Drug, and Cosmetic Act ( 21 U.S.C. 360cc ).\n**(5)**\nIn the case of a covered orphan drug with one or more certifications specified in clauses (ii), (iii), and (iv) of section 505(b)(2)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b)(2)(A) ), or in subclauses (II), (III), and (IV) of section 505(j)(2)(A)(vii) of such Act ( 21 U.S.C. 355(j)(2)(A)(vii) ), each corresponding patent-related approval-delay period (other than a patent for which the information required pursuant to subsection (b) or (c) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) has not been filed).\n##### (b) Conforming extensions\nIn addition to the periods extended under subsection (a) for a covered orphan drug, the following periods are each deemed to be extended by 180 days:\n**(1)**\nThe 4-year period referred to in subparagraph (B) of section 351(k)(7) of the Public Health Service Act ( 42 U.S.C. 262(k)(7) ).\n**(2)**\nThe 4-year, 48-month, and 7 and one-half-year periods referred to in subsection (c)(3)(E)(ii) and subsection (j)(5)(F)(ii) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term covered orphan drug means an orphan drug for which\u2014\n**(A)**\nan application is submitted under section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) during the COVID\u201319 emergency period (without regard to whether the same applicant has submitted such application for the same drug before December 1, 2019, for a different rare disease or condition);\n**(B)**\nan application under section 505(b) of the Federal Food, Drug, and Cosmetic Act or under section 351(a) of the Public Health Service Act (or a supplemental application, as the case may be) is approved pursuant to the investigational new drug application referred to in paragraph (1); and\n**(C)**\nthere is no approved indication that is not for a rare disease or condition.\n**(2)**\nThe term corresponding patent-related approval delay period , with respect to a covered orphan drug, means the period ending with the last applicable date for the approval of an application within the meaning of subparagraph (A), (B), or (C) of section 505(c)(3) of the Federal, Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c)(3) ), or clause (i), (ii), or (iii) of section 505(j)(5)(B) of such Act ( 21 U.S.C. 355(j)(5)(B) ), whichever applies pursuant to the applicable patent certification.\n**(3)**\nThe term orphan drug means a drug that the Secretary has designated as a drug for a rare disease or condition under section 526(a) of the Federal, Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bb(a) ).\n**(4)**\nThe term COVID\u201319 emergency period means the period beginning on December 1, 2019, and ending on the date that is not later than 120 days before the date on which the emergency period (as defined in section 1135(g)(1)(B) of the Social Security Act ( 42 U.S.C. 1320b\u20135(g)(1)(B) )) terminates.\n**(5)**\nThe term rare disease or condition has the meaning given such term in section 526 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bb ).\n##### (d) Effective date\nThis section takes effect upon the date of the enactment of this Act, without regard to whether the Secretary has issued guidance or regulations regarding the implementation of this Act.",
      "versionDate": "2026-02-25",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2026-03-16T16:48:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
    "originChamber": "House",
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
          "measure-id": "id119hr7693",
          "measure-number": "7693",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7693v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Leo's Law</b></p> <p>This bill extends by 180 days the relevant periods of market exclusivity for drugs for rare diseases or conditions (i.e., orphan drugs) for which applications were submitted during the COVID-19 emergency period. </p>"
        },
        "title": "Leo\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7693.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Leo's Law</b></p> <p>This bill extends by 180 days the relevant periods of market exclusivity for drugs for rare diseases or conditions (i.e., orphan drugs) for which applications were submitted during the COVID-19 emergency period. </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr7693"
    },
    "title": "Leo\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Leo's Law</b></p> <p>This bill extends by 180 days the relevant periods of market exclusivity for drugs for rare diseases or conditions (i.e., orphan drugs) for which applications were submitted during the COVID-19 emergency period. </p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr7693"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7693ih.xml"
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
      "title": "Leo\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leo\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T11:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To mitigate the effects of the COVID-19 pandemic on incentives under the Federal Food, Drug, and Cosmetic Act for the development of orphan drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T11:48:18Z"
    }
  ]
}
```
