# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/76?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/76
- Title: SMART Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 76
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2025-04-03T19:28:32Z
- Update date including text: 2025-04-03T19:28:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/76",
    "number": "76",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "SMART Act of 2025",
    "type": "S",
    "updateDate": "2025-04-03T19:28:32Z",
    "updateDateIncludingText": "2025-04-03T19:28:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T23:28:54Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s76is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 76\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Lankford (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to improve the effectiveness of major rules in accomplishing their regulatory objectives by promoting retrospective review, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Setting Manageable Analysis Requirements in Text Act of 2025 or the SMART Act of 2025 .\n#### 2. Incorporating retrospective review into new major rules\n##### (a) In general\nSubchapter II of chapter 5 of title 5, United States Code, is amended\u2014\n**(1)**\nin section 551\u2014\n**(A)**\nin paragraph (13), by striking and at the end;\n**(B)**\nin paragraph (14), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(15) Administrator means the Administrator of the Office of Information and Regulatory Affairs of the Office of Management and Budget established under section 3503 of title 44 and any successor to that office; and (16) major rule means any rule that the Administrator finds has resulted in or is likely to result in\u2014 (A) an annual effect on the economy of $100,000,000 or more; (B) a major increase in costs or prices for consumers, individual industries, Federal, State, or local government agencies, or geographic regions; or (C) significant adverse effects on competition, employment, investment, productivity, innovation, health, safety, the environment, or the ability of United States-based enterprises to compete with foreign-based enterprises in domestic and export markets. ; and\n**(2)**\nin section 553, by adding at the end the following:\n(f) Major rule frameworks (1) In general On and after the date that is 1 year after the date of enactment of this subsection\u2014 (A) with respect to a proposed rule published by an agency in the Federal Register that the agency reasonably expects would meet the definition of a major rule, the agency shall include a potential framework for assessing the implemented rule, which shall include a general statement of how the agency intends to measure the effectiveness of the rule; and (B) with respect to a final major rule published by an agency in the Federal Register, including a major rule that the agency did not initially reasonably expect would meet the definition of a major rule under subparagraph (A), the agency shall include a framework for assessing the major rule under paragraph (2), which shall include\u2014 (i) a statement of the regulatory objectives of the major rule, including a summary of the societal benefit and cost of the major rule; (ii) the methodology by which the agency plans to analyze the qualitative and quantitative outcomes of the major rule so that the agency can assess\u2014 (I) the effectiveness and benefits of the major rule in producing the regulatory objectives of the major rule; and (II) the effects and costs of the major rule on regulated and other affected entities; (iii) a plan for gathering data, including public input, regarding the methodology described in clause (ii) on an ongoing basis or at periodic times; and (iv) a time frame, as appropriate to the major rule and not more than 10 years after the effective date of the major rule, under which the agency shall conduct the assessment of the major rule in accordance with paragraph (2)(A). (2) Assessment (A) In general Each agency shall assess the data gathered under paragraph (1)(B)(iii), using the methodology set forth in paragraph (1)(B)(ii) or any other appropriate methodology developed after the issuance of a final major rule\u2014 (i) to analyze how the actual benefits and costs of the major rule may have varied from those anticipated at the time the major rule was issued; and (ii) to determine whether\u2014 (I) the major rule is accomplishing the regulatory objective of the major rule; (II) the major rule has been rendered unnecessary, taking into consideration\u2014 (aa) changes in the subject area affected by the major rule; and (bb) whether the major rule overlaps with, duplicates, or conflicts with other rules or, to the extent feasible, State and local government regulations; (III) the major rule needs to be expanded, streamlined, or otherwise modified in order to accomplish the regulatory objective of the major rule; and (IV) other alternatives to the major rule or a modification of the major rule could better achieve the regulatory objective of the major rule by increasing the benefits of the major rule or imposing a smaller burden on society, or both, taking into consideration any changes in the regulatory environment that may have made the major rule more or less necessary or effective, and any cost already incurred. (B) Different methodology If an agency uses a methodology other than the methodology set forth in paragraph (1)(B)(ii) to assess data under subparagraph (A), the agency shall include notification of the revised methodology and an explanation of the changes in circumstances that necessitated the use of that other methodology as part of the notice required under subparagraph (D). (C) Subsequent assessments If, after an assessment of a major rule under subparagraph (A), an agency determines that the major rule will remain in effect with or without modification, the agency shall, in consultation with the Administrator, include with the assessment produced under subparagraph (A) a list of circumstances or events that would necessitate a subsequent review in accordance with subparagraph (A) to ensure that the major rule continues to meet the regulatory objective of the major rule. (D) Publication Not later than 180 days after the date on which an agency completes an assessment of a major rule under subparagraph (A), the agency shall publish prominently on the website of the agency the results of the assessment, including the circumstances or events that would necessitate a subsequent assessment of the major rule under subparagraph (C). (3) Agency head responsibilities The head of each agency shall\u2014 (A) oversee the timely compliance of the agency with this subsection; and (B) ensure that the results of each assessment conducted under paragraph (2) are published promptly in accordance with paragraph (2)(D). (4) OMB oversight The Administrator shall\u2014 (A) issue guidance for agencies regarding the development of the framework under paragraph (1) and the conduct of the assessments under paragraph (2)(A); (B) encourage and assist agencies to streamline and coordinate the assessment of major rules with similar or related regulatory objectives; (C) exempt an agency from including the framework required under paragraph (1)(B) when publishing a final major rule, if\u2014 (i) the agency did not issue a notice of proposed rule making for the major rule in order to provide a timely response to an emergency or comply with a statutorily imposed deadline, in accordance with paragraph (6)(B); or (ii) the Administrator determines that\u2014 (I) the major final rule falls within a category of major rules that are routine or periodic in nature, including those issued on an annual basis in order to put in place annual spending programs; or (II) for any other reason, the conduct of an assessment would be impracticable, unnecessary, or contrary to the public interest; and (D) extend the deadline specified by an agency for an assessment of a major rule under paragraph (1)(B)(iv) or paragraph (2)(C) for a period of not more than 90 days if the agency justifies why the agency is unable to complete the assessment by that deadline. (5) Rule of construction Nothing in this subsection may be construed to affect\u2014 (A) the authority of an agency to assess or modify a major rule of the agency earlier than the end of the time frame specified for the major rule under paragraph (1)(B)(iv); or (B) any other provision of law that requires an agency to conduct retrospective reviews of rules issued by the agency. (6) Applicability (A) In general This subsection shall not apply to\u2014 (i) a major rule of an agency\u2014 (I) that the Administrator reviewed before the date of enactment of this subsection; (II) for which the agency is required to conduct a retrospective review under\u2014 (aa) section 2222 of the Economic Growth and Regulatory Paperwork Reduction Act of 1996 ( 12 U.S.C. 3311 ); (bb) section 170(d) of the Financial Stability Act of 2010 ( 12 U.S.C. 5370(d) ); or (cc) any other provision of law with requirements that the Administrator determines\u2014 (AA) include robust public participation; (BB) include significant agency consideration and analysis of whether the rule is achieving the regulatory objective of the rule; and (CC) meet, are substantially similar to, or exceed the requirements of this subsection; (III) for which the authorizing statute of the rule is subject to periodic authorization by Congress not less frequently than once every 10 years; or (IV) for which the authorizing statute of the rule requires the promulgation of a new or revised rule not less frequently than once every 10 years; or (ii) interpretative rules, general statements of policy, or rules of agency organization, procedure, or practice. (B) Good cause exemption In the case of a major rule for which an agency has not issued a notice of proposed rule making, the agency shall publish the framework required under paragraph (1)(B) in the Federal Register not later than 6 months after the date on which the agency publishes the final major rule. (7) Judicial review (A) In general Judicial review of agency compliance with this subsection\u2014 (i) shall be strictly limited to\u2014 (I) whether an agency published the framework for assessment of a major rule described in paragraph (1); or (II) whether an agency published the assessment or subsequent assessment of a major rule described in subparagraphs (A), (C), and (D) of paragraph (2); and (ii) shall not include a substantive review of the framework, assessment, or action of an agency under this subsection. (B) Remedy available In granting relief in an action brought under subparagraph (A), a court may only issue an order remanding the major rule to the agency to comply with paragraph (1) or subparagraph (A), (C), or (D) of paragraph (2), as applicable. (C) Effective date of major rule If, in an action brought under subparagraph (A)(i), a court determines that the agency did not comply, the major rule shall take effect notwithstanding any order issued by the court. (D) Administrator Any determination, action, or inaction of the Administrator shall not be subject to judicial review. .\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out the amendments made by subsection (a).",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2025-03-05T16:11:52Z"
          },
          {
            "name": "Competition and antitrust",
            "updateDate": "2025-03-05T16:11:52Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-03-05T16:11:52Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2025-03-05T16:11:52Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-03-05T16:11:52Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-03-05T16:11:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:25:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119s76",
          "measure-number": "76",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s76v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Setting Manageable Analysis Requirements in Text Act of 2025 or the SMART Act of 2025</strong></p><p>This bill requires agencies, when publishing a proposed or final major rule, to include a framework for assessing whether the rule achieves its regulatory objective. An agency must assess a rule in the time frame included in the framework. The assessment must compare the rule's anticipated and actual benefits and costs.</p><p>Additionally, the assessment must determine whether\u00a0(1) the rule has been rendered unnecessary because of changes to the subject area affected by the rule or it overlaps with, duplicates, or conflicts with other rules, or\u00a0state and local government regulations; (2)\u00a0the rule should be expanded, streamlined, or otherwise modified to accomplish the rule's objective; and (3) other alternatives or modifications to the rule could better achieve the rule's\u00a0objective.\u00a0</p><p>The bill defines a\u00a0major rule\u00a0as a rule likely to cause (1)\u00a0an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices; or (3) significant adverse effects on competition, employment, investment, productivity, innovation, health, safety, the environment, or the ability of U.S.-based enterprises to compete with foreign-based enterprises.\u00a0</p>"
        },
        "title": "SMART Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s76.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Setting Manageable Analysis Requirements in Text Act of 2025 or the SMART Act of 2025</strong></p><p>This bill requires agencies, when publishing a proposed or final major rule, to include a framework for assessing whether the rule achieves its regulatory objective. An agency must assess a rule in the time frame included in the framework. The assessment must compare the rule's anticipated and actual benefits and costs.</p><p>Additionally, the assessment must determine whether\u00a0(1) the rule has been rendered unnecessary because of changes to the subject area affected by the rule or it overlaps with, duplicates, or conflicts with other rules, or\u00a0state and local government regulations; (2)\u00a0the rule should be expanded, streamlined, or otherwise modified to accomplish the rule's objective; and (3) other alternatives or modifications to the rule could better achieve the rule's\u00a0objective.\u00a0</p><p>The bill defines a\u00a0major rule\u00a0as a rule likely to cause (1)\u00a0an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices; or (3) significant adverse effects on competition, employment, investment, productivity, innovation, health, safety, the environment, or the ability of U.S.-based enterprises to compete with foreign-based enterprises.\u00a0</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119s76"
    },
    "title": "SMART Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Setting Manageable Analysis Requirements in Text Act of 2025 or the SMART Act of 2025</strong></p><p>This bill requires agencies, when publishing a proposed or final major rule, to include a framework for assessing whether the rule achieves its regulatory objective. An agency must assess a rule in the time frame included in the framework. The assessment must compare the rule's anticipated and actual benefits and costs.</p><p>Additionally, the assessment must determine whether\u00a0(1) the rule has been rendered unnecessary because of changes to the subject area affected by the rule or it overlaps with, duplicates, or conflicts with other rules, or\u00a0state and local government regulations; (2)\u00a0the rule should be expanded, streamlined, or otherwise modified to accomplish the rule's objective; and (3) other alternatives or modifications to the rule could better achieve the rule's\u00a0objective.\u00a0</p><p>The bill defines a\u00a0major rule\u00a0as a rule likely to cause (1)\u00a0an annual effect on the economy of $100 million or more; (2) a major increase in costs or prices; or (3) significant adverse effects on competition, employment, investment, productivity, innovation, health, safety, the environment, or the ability of U.S.-based enterprises to compete with foreign-based enterprises.\u00a0</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119s76"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s76is.xml"
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
      "title": "SMART Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SMART Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Setting Manageable Analysis Requirements in Text Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to improve the effectiveness of major rules in accomplishing their regulatory objectives by promoting retrospective review, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T03:03:29Z"
    }
  ]
}
```
