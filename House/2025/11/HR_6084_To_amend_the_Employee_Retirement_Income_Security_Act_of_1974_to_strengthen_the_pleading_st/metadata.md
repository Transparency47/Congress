# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6084
- Title: ERISA Litigation Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 6084
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-03-30T18:22:00Z
- Update date including text: 2026-03-30T18:22:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-18 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6084",
    "number": "6084",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "ERISA Litigation Reform Act",
    "type": "HR",
    "updateDate": "2026-03-30T18:22:00Z",
    "updateDateIncludingText": "2026-03-30T18:22:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
        "item": [
          {
            "date": "2026-03-17T19:37:37Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-18T15:03:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-18T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6084ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6084\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Fine introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to strengthen the pleading standards for certain claims, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ERISA Litigation Reform Act .\n#### 2. Pleading standard\nSection 502 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1132 ) is amended by adding at the end the following:\n(n) For the purpose of any civil action under this section alleging that a fiduciary caused a plan to engage in a transaction that violates subparagraph (C) or (D) of section 406(a)(1), a plaintiff has the burden of plausibly alleging and proving that the transaction is not exempt under section 408(b)(2). (o) For the purpose of any civil action under this section alleging that a fiduciary caused a plan to engage in a transaction that violates section 406 with respect to the purchase or sale of qualified employer securities, a plaintiff has the burden of plausibly alleging and proving that the transaction is not exempt under section 408(e). (p) (1) For the purpose of any civil action under this section against a plan or its fiduciaries, all discovery and other proceedings shall be stayed during the pendency of a motion brought under Rule 12 of the Federal Rules of Civil Procedure or pending any reply to an answer under Rule 7(a)(7) of the Federal Rules of Civil Procedure, unless the court finds, upon the motion of any party, that particularized discovery is necessary to preserve evidence or to prevent undue prejudice to that party. (2) During the pendency of any stay of discovery pursuant to this subsection, unless otherwise ordered by the court or if doing so is contrary to the party\u2019s document preservation obligations under the Federal Rules of Civil Procedure, any party to the action with actual knowledge of the allegations contained in the complaint shall treat all documents, data compilations (including electronically recorded or stored data), and tangible objects that are in the possession, custody, or control of such person and that the person would reasonably believe are relevant to the allegations, as if they were the subject of a continuing request for production of documents from an opposing party under the Federal Rules of Civil Procedure. A party\u2019s document preservation obligations under this paragraph extend to all documents held by custodians (such as recordkeepers) that are in the possession, custody, or control of the plan or the party. (3) A party aggrieved by the willful failure of an opposing party to comply with paragraph (2) may apply to the court for an order awarding appropriate sanctions. (4) Upon a proper showing, a court may stay discovery proceedings in any civil action in a State court as necessary in aid of its jurisdiction, or to protect or effectuate its judgments, in an action subject to a stay of discovery pursuant to this subsection. .",
      "versionDate": "2025-11-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-03-30T18:21:44Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-03-30T18:21:55Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2026-03-30T18:22:00Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-03-30T18:21:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-12-01T16:56:28Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6084ih.xml"
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
      "title": "ERISA Litigation Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ERISA Litigation Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 to strengthen the pleading standards for certain claims, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:18Z"
    }
  ]
}
```
