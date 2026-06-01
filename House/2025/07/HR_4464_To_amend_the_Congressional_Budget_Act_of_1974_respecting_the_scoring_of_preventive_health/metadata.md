# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4464
- Title: Preventive Health Savings Act
- Congress: 119
- Bill type: HR
- Bill number: 4464
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-05-14T08:08:36Z
- Update date including text: 2026-05-14T08:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4464",
    "number": "4464",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Preventive Health Savings Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:36Z",
    "updateDateIncludingText": "2026-05-14T08:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CO"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "WV"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "UT"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "FL"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IL"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4464ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4464\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Obernolte (for himself, Ms. DeGette , Mr. Peters , and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget Act of 1974 respecting the scoring of preventive health savings.\n#### 1. Short title\nThis Act may be cited as the Preventive Health Savings Act .\n#### 2. Scoring of preventive health savings\nSection 202 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 602 ) is amended by adding at the end the following:\n(h) Scoring of preventive health savings (1) Determination by the director Upon a request by the chairman and ranking minority member of the Committee on the Budget of the Senate and chairman and ranking minority member of the committee of primary jurisdiction of the Senate or by the chairman and ranking minority member of the Committee on the Budget of the House of Representatives and the chairman and ranking minority member of the committee of primary jurisdiction of the House of Representatives, the Director shall determine if proposed legislation would result in net reductions in budget outlays in budgetary outyears through the use of preventive health care. (2) Projections If the Director determines that proposed legislation would result in net reductions in budget outlays as described in paragraph (1), the Director\u2014 (A) shall include, in any projection prepared by the Director on such proposed legislation, a description and estimate of the reductions in budget outlays in the budgetary outyears and a description of the basis for such conclusions; and (B) may prepare a budget projection that includes some or all of the budgetary outyears, notwithstanding the time periods for projections described in subsection (e) and sections 308, 402, and 424. (3) Limitation Any estimate provided by the Director pursuant to paragraph (1) shall be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls. (4) Definitions As used in this subsection\u2014 (A) the term budgetary outyears means the 2 consecutive 10-year periods beginning with the first fiscal year that is 10 years after the current fiscal year; and (B) the term preventive health care means an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death, including through the promotion and use of effective, innovative health care interventions that are demonstrated by credible and publicly available evidence from epidemiological projection models, clinical trials, observational studies in humans, longitudinal studies, and meta-analysis. .",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on the Budget."
      },
      "number": "3204",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventive Health Savings Act",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-09-15T17:38:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-16",
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
          "measure-id": "id119hr4464",
          "measure-number": "4464",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-16",
          "originChamber": "HOUSE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4464v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-07-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>"
        },
        "title": "Preventive Health Savings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4464.xml",
    "summary": {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr4464"
    },
    "title": "Preventive Health Savings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventive Health Savings Act</strong></p><p>This bill requires the Congressional Budget Office (CBO), upon receiving a request from Congress, to determine if proposed legislation would reduce spending outside of the 10-year budget window through the use of preventive health care.</p><p>Under the bill, the term <em>preventive health care</em> generally refers to an action that focuses on the health of the public, individuals, and defined populations in order to protect, promote, and maintain health and wellness and prevent disease, disability, and premature death.</p><p>If CBO determines that the proposed legislation would result in net reductions in budget outlays from the use of preventive health care, any CBO projection regarding the legislation must include (1) a description and estimate of the reductions in outlays, and (2) a description of the basis for these conclusions.\u00a0</p><p>Any estimate provided by CBO pursuant to this bill must be used as a supplementary estimate and may not be used to determine compliance with the Congressional Budget Act of 1974 or any other budgetary enforcement controls.</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr4464"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4464ih.xml"
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
      "title": "Preventive Health Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventive Health Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-26T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget Act of 1974 respecting the scoring of preventive health savings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:18Z"
    }
  ]
}
```
