# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/572
- Title: RED TAPE Act
- Congress: 119
- Bill type: HR
- Bill number: 572
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2026-03-10T23:41:16Z
- Update date including text: 2026-03-10T23:41:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/572",
    "number": "572",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "RED TAPE Act",
    "type": "HR",
    "updateDate": "2026-03-10T23:41:16Z",
    "updateDateIncludingText": "2026-03-10T23:41:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-21T17:03:30Z",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr572ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 572\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Sessions (for himself and Ms. Hageman ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Small Business , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of non-monetized or unqualified factors for regulatory analyses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulations Evaluated to Determine The Anticipated Price and Effect Act or the RED TAPE Act .\n#### 2. Findings\nCongress finds that agencies must prioritize tangible, immediately quantifiable monetary benefits in their decision making processes, ensuring regulatory actions yield clear and measurable financial benefits to the public and private sectors while minimizing unnecessary regulatory costs or burdens.\n#### 3. Prohibition on net benefit discounts; consideration of regulatory impact analyses\n##### (a) In general\nChapter 6 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 601\u2014\n**(A)**\nin paragraph (6), by striking and at the end;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting a semicolon;\n**(C)**\nin paragraph (8)\u2014\n**(i)**\nby striking Recordkeeping requirement.\u2014 T and inserting the ; and\n**(ii)**\nby striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(9) the term benefit-cost analysis has the meaning given the term in Office of Management and Budget Circular A\u201394, as revised on November 9, 2023, or any successor revision; and (10) the term regulatory impact analysis means a regulatory analysis described in\u2014 (A) Executive Order 12866 ( 5 U.S.C. 601 note; relating to regulatory planning and review); (B) Executive Order 13563 ( 5 U.S.C. 601 note; relating to improving regulation and regulatory review); (C) Executive Order 14094 (88 Fed. Reg. 21879; relating to modernizing regulatory review); (D) Office of Management and Budget Circular No. A\u20134, as revised on November 9, 2023, or any successor revision; or (E) Office of Management and Budget Circular No. A\u201394, as revised on November 9, 2023, or any successor revision. ; and\n**(2)**\nby adding at the end the following:\n613. Prohibition on use of non-monetized or unqualified factors for regulatory analyses (a) Agency prohibition An agency may not consider any non-monetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule. (b) OMB prohibition The Office of Management and Budget may not\u2014 (1) authorize in any manner, such as in issuing guidance, a memorandum, a directive, or a rule that permit or endorse the analysis or use of any non-monetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule; or (2) consider any non-monetized or unquantified factor presented in a regulatory impact analysis or benefit-cost analysis of another agency. (c) Public transparency Each agency shall publish in the Federal Register, with respect to and along with each proposed rule, final rule, or interim final rule\u2014 (1) a summary of each regulatory impact analysis and benefit-cost analysis conducted by the agency; (2) the text of each regulatory impact analysis and benefit-cost analysis conducted by the agency, including a disclosure of the methodology and specific analyses used by the agency in estimating economic impacts, and the determination and rationale of such economic impact analyses; and (3) any additional information of the agency relevant to the regulatory impact and benefit-cost analyses conducted by the agency, such as the decision-making processes of the agency. (d) Regulatory guidance Not later than 90 days after the date of enactment of this section, the Director of the Office of Management and Budget shall issue revised guidance to agencies to ensure compliance with the provisions of this section. (e) Judicial review (1) In general Any party affected by a rule issued by an agency that considered a non-monetized or unquantified factor when conducting a regulatory impact or benefit-cost analysis in violation of this section may bring a civil action against the agency to challenge the rule in a district court of the United States. (2) Invalidation of regulation If the court finds that an agency relied upon non-monetized or unquantified factors to evaluate a final rule or interim final rule in contravention of this section, the court shall declare the rule invalid. (3) Application This subsection shall apply with respect to any rule issued by an agency on or after November 9, 2023. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 6 of title 5, United States Code, is amended by adding at the end the following:\n613. Prohibition on use of non-monetized or unquantified factors for regulatory analyses. .\n#### 4. Effective date\nThe amendments made by section 3 shall take effect on the date that is 30 days after the date of enactment of this Act.",
      "versionDate": "2025-01-21",
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
        "text": "Committee on Small Business and Entrepreneurship. Hearings held."
      },
      "number": "148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RED TAPE Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-13T15:44:03Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-13T15:44:03Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T15:44:03Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-03-13T15:44:03Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2025-03-13T15:44:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-27T16:44:59Z"
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
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr572ih.xml"
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
      "title": "RED TAPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RED TAPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Regulations Evaluated to Determine The Anticipated Price and Effect Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of non-monetized or unqualified factors for regulatory analyses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T05:18:28Z"
    }
  ]
}
```
