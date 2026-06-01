# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/148
- Title: RED TAPE Act
- Congress: 119
- Bill type: S
- Bill number: 148
- Origin chamber: Senate
- Introduced date: 2025-01-17
- Update date: 2026-01-20T16:16:16Z
- Update date including text: 2026-01-20T16:16:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-17: Introduced in Senate
- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-11-19 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-01-17: Introduced in Senate

## Actions

- 2025-01-17 - IntroReferral: Introduced in Senate
- 2025-01-17 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-11-19 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-17",
    "latestAction": {
      "actionDate": "2025-01-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/148",
    "number": "148",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "RED TAPE Act",
    "type": "S",
    "updateDate": "2026-01-20T16:16:16Z",
    "updateDateIncludingText": "2026-01-20T16:16:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-17",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-17",
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
          "date": "2025-11-19T20:16:50Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-17T15:57:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-17",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s148is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 148\nIN THE SENATE OF THE UNITED STATES\nJanuary 17, 2025 Ms. Ernst (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the use of non-monetized or unqualified factors for regulatory analyses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Regulations Evaluated to Determine The Anticipated Price and Effect Act or the RED TAPE Act .\n#### 2. Findings\nCongress finds that agencies must prioritize tangible, immediately quantifiable monetary benefits in their decision making processes, ensuring regulatory actions yield clear and measurable financial benefits to the public and private sectors while minimizing unnecessary regulatory costs or burdens.\n#### 3. Prohibition on net benefit discounts; consideration of regulatory impact analyses\n##### (a) In general\nChapter 6 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 601\u2014\n**(A)**\nin paragraph (6), by striking and at the end;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(8) the term benefit-cost analysis has the meaning given the term in Office of Management and Budget Circular A\u201394, as revised on November 9, 2023, or any successor revision; and (9) the term regulatory impact analysis means a regulatory analysis described in\u2014 (A) Executive Order 12866 ( 5 U.S.C. 601 note; relating to regulatory planning and review); (B) Executive Order 13563 ( 5 U.S.C. 601 note; relating to improving regulation and regulatory review); (C) Executive Order 14094 (88 Fed. Reg. 21879; relating to modernizing regulatory review); (D) Office of Management and Budget Circular No. A\u20134, as revised on November 9, 2023, or any successor revision; or (E) Office of Management and Budget Circular No. A\u201394, as revised on November 9, 2023, or any successor revision. ; and\n**(2)**\nby adding at the end the following:\n613. Prohibition on use of non-monetized or unqualified factors for regulatory analyses (a) Agency prohibition An agency may not consider any non-monetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule. (b) OMB prohibition The Office of Management and Budget may not\u2014 (1) authorize in any manner, such as in issuing guidance, a memorandum, a directive, or a rule that permit or endorse the analysis or use of any non-monetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule; or (2) consider any non-monetized or unquantified factor presented in a regulatory impact analysis or benefit-cost analysis of another agency. (c) Public transparency Each agency shall publish in the Federal Register, with respect to and along with each proposed rule, final rule, or interim final rule\u2014 (1) a summary of each regulatory impact analysis and benefit-cost analysis conducted by the agency; (2) the text of each regulatory impact analysis and benefit-cost analysis conducted by the agency, including a disclosure of the methodology and specific analyses used by the agency in estimating economic impacts, and the determination and rationale of such economic impact analyses; and (3) any additional information of the agency relevant to the regulatory impact and benefit-cost analyses conducted by the agency, such as the decision-making processes of the agency. (d) Regulatory guidance Not later than 90 days after the date of enactment of this section, the Director of the Office of Management and Budget shall issue revised guidance to agencies to ensure compliance with the provisions of this section. (e) Judicial review (1) In general Any party affected by a rule issued by an agency that considered a non-monetized or unquantified factor when conducting a regulatory impact or benefit-cost analysis in violation of this section may bring a civil action against the agency to challenge the rule in a district court of the United States. (2) Invalidation of regulation If the court finds that an agency relied upon non-monetized or unquantified factors to evaluate a final rule or interim final rule in contravention of this section, the court shall declare the rule invalid. (3) Statute of limitations This subsection shall apply with respect to any rule issued by an agency on or after November 9, 2023. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 6 of title 5, United States Code, is amended by adding at the end the following:\n613. Prohibition on use of non-monetized or unquantified factors for regulatory analyses. .\n#### 4. Effective date\nThe amendments made by section 3 shall take effect on the date that is 30 days after the date of enactment of this Act.",
      "versionDate": "2025-01-17",
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
        "actionDate": "2025-01-21",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "572",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RED TAPE Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-13T15:43:06Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-13T15:43:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T15:43:19Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-03-13T15:43:30Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2025-03-13T15:43:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-27T16:45:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-17",
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
          "measure-id": "id119s148",
          "measure-number": "148",
          "measure-type": "s",
          "orig-publish-date": "2025-01-17",
          "originChamber": "SENATE",
          "update-date": "2026-01-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s148v00",
            "update-date": "2026-01-20"
          },
          "action-date": "2025-01-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Regulations Evaluated to Determine The Anticipated Price and Effect Act or the RED TAPE Act</strong><br/><br/>This bill prohibits federal agencies from considering any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis for any proposed rule, final rule, or interim final rule.</p><p>Each agency must publish each regulatory impact analysis and benefit-cost analysis conducted by the agency with respect to a proposed rule, final rule, or interim final rule.<br/><br/>Additionally, the Office of Management and Budget may not (1) authorize or endorse an agency's use of any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule; or (2) consider any nonmonetized or unquantified factor presented in a regulatory impact analysis or benefit-cost analysis of another agency.<br/><br/>The bill provides for judicial review of a rule issued by an agency that considered a nonmonetized or unquantified factor when conducting a regulatory impact or benefit-cost analysis. If a court finds that an agency relied upon such a factor to evaluate a final rule or interim final rule, the court must declare the rule invalid.</p><p>The bill takes effect 30 days after enactment.</p>"
        },
        "title": "RED TAPE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s148.xml",
    "summary": {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Regulations Evaluated to Determine The Anticipated Price and Effect Act or the RED TAPE Act</strong><br/><br/>This bill prohibits federal agencies from considering any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis for any proposed rule, final rule, or interim final rule.</p><p>Each agency must publish each regulatory impact analysis and benefit-cost analysis conducted by the agency with respect to a proposed rule, final rule, or interim final rule.<br/><br/>Additionally, the Office of Management and Budget may not (1) authorize or endorse an agency's use of any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule; or (2) consider any nonmonetized or unquantified factor presented in a regulatory impact analysis or benefit-cost analysis of another agency.<br/><br/>The bill provides for judicial review of a rule issued by an agency that considered a nonmonetized or unquantified factor when conducting a regulatory impact or benefit-cost analysis. If a court finds that an agency relied upon such a factor to evaluate a final rule or interim final rule, the court must declare the rule invalid.</p><p>The bill takes effect 30 days after enactment.</p>",
      "updateDate": "2026-01-20",
      "versionCode": "id119s148"
    },
    "title": "RED TAPE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Regulations Evaluated to Determine The Anticipated Price and Effect Act or the RED TAPE Act</strong><br/><br/>This bill prohibits federal agencies from considering any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis for any proposed rule, final rule, or interim final rule.</p><p>Each agency must publish each regulatory impact analysis and benefit-cost analysis conducted by the agency with respect to a proposed rule, final rule, or interim final rule.<br/><br/>Additionally, the Office of Management and Budget may not (1) authorize or endorse an agency's use of any nonmonetized or unquantified factor when conducting a regulatory impact analysis or benefit-cost analysis on any proposed rule, final rule, or interim final rule; or (2) consider any nonmonetized or unquantified factor presented in a regulatory impact analysis or benefit-cost analysis of another agency.<br/><br/>The bill provides for judicial review of a rule issued by an agency that considered a nonmonetized or unquantified factor when conducting a regulatory impact or benefit-cost analysis. If a court finds that an agency relied upon such a factor to evaluate a final rule or interim final rule, the court must declare the rule invalid.</p><p>The bill takes effect 30 days after enactment.</p>",
      "updateDate": "2026-01-20",
      "versionCode": "id119s148"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s148is.xml"
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
      "title": "RED TAPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RED TAPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Regulations Evaluated to Determine The Anticipated Price and Effect Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of non-monetized or unqualified factors for regulatory analyses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:26Z"
    }
  ]
}
```
