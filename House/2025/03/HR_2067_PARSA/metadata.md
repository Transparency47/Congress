# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2067
- Title: PARSA
- Congress: 119
- Bill type: HR
- Bill number: 2067
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-03-06T20:43:46Z
- Update date including text: 2026-03-06T20:43:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2067",
    "number": "2067",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "PARSA",
    "type": "HR",
    "updateDate": "2026-03-06T20:43:46Z",
    "updateDateIncludingText": "2026-03-06T20:43:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2067ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2067\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Moolenaar introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Employment Retirement Income Security Act of 1974 to prohibit plan investments in foreign adversary and sanctioned entities, require disclosure of existing investments in such entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Americans\u2019 Retirement Savings Act or PARSA .\n#### 2. Prohibition on investment in certain entities\nSection 404(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104(a) ) is amended by adding at the end the following:\n(3) Prohibition on investment in certain entities (A) In general It shall be a violation of paragraph (1) for a fiduciary of a plan to fail to ensure that the plan does not engage in a transaction that the fiduciary knows, or should know, will result in the plan\u2014 (i) acquiring an interest (as defined in section 103(h)) between the plan and a covered entity; (ii) lending money or extending credit to a covered entity; (iii) furnishing goods, services, or facilities to a covered entity; and (iv) transferring, directly or indirectly, to or for use by or for the benefit of a covered entity\u2014 (I) any assets of the plan; or (II) any data with respect to any participant or beneficiary of the plan. (B) Definitions (i) Covered entity For purposes of this paragraph, the term covered entity means a foreign adversary entity or sanctioned entity, as such terms are defined in section 103(h). (ii) Fiduciary For purposes of subparagraph (A)(iv)(II), the term fiduciary includes any person who exercises direct or indirect discretionary authority, responsibility, or control with respect to any participant beneficiary data. (C) Continuation of current investments In the case of a plan holding an investment in a covered entity on the date of enactment of the Protecting Americans\u2019 Retirement Savings Act , such plan may, notwithstanding subparagraph (A), continue to hold such investment without violating paragraph (1) if the fiduciary of such plan complies with the requirements of subparagraphs (I) and (J) of section 103(b)(3). (D) Contractually obligated investments In the case of a plan that has entered into a binding agreement prior to the date of enactment of the Protecting Americans\u2019 Retirement Savings Act obligating such plan to engage in a transaction described in subparagraph (A), if the fiduciary of such plan complies with the requirements of subparagraphs (I), (J), and (K) of section 103(b)(3), such plan may, notwithstanding subparagraph (A), fulfill the terms of such agreement without violating paragraph (1) until such agreement\u2014 (i) expires; or (ii) allows for termination. .\n#### 3. Additional disclosures for employee retirement funds\n##### (a) In general\nSection 103(b)(3) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1023(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (H)(iv), by striking the period at the end and inserting ; and ; and\n**(2)**\nby inserting at the end the following:\n(I) a statement of all assets in the plan that consist, in whole or in part, of an interest in a sanctioned entity, including\u2014 (i) the aggregate value of such assets in the plan; (ii) the identity of each sanctioned entity in which such plan holds an interest; and (iii) information identifying each list under subsection (h)(5) on which such sanctioned entity is listed, and the reasons for which an entity may be placed on such list. (J) a statement of all assets in the plan that consist, in whole or in part, of an interest in a foreign adversary entity, including\u2014 (i) the aggregate value of such assets in the plan; (ii) the specific interest, and value thereof, that such plan holds in each such foreign adversary entity; (iii) the name of any investment vehicle through which the plan holds such interest; (iv) the name of the fiduciary responsible for such investment; and (v) a brief statement of factors considered by the fiduciary in maintaining such investment. (K) a description of any ongoing agreement subject to section 404(a)(3)(D), including\u2014 (i) the assets involved in such agreement; (ii) the date on which such agreement expires; (iii) the date on which such commitment may be terminated; and (iv) such other information as the Secretary may deem appropriate. .\n##### (b) Definitions\nSection 103 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1023 ) is further amended by adding at the end the following:\n(h) Definitions In this section: (1) Control The term control has the meaning given in section 800.208 of title 31, Code of Federal Regulations (as in effect on the date of enactment of the Protecting Americans\u2019 Retirement Savings Act ). (2) Export Administration Regulations The term Export Administration Regulations means the regulations set forth in subchapter C of chapter VII of title 15, Code of Federal Regulations, or successor regulations. (3) Foreign adversary The term foreign adversary \u2014 (A) has the meaning given the term covered nation in section 4872(d) of title 10, United States Code (as in effect on the date of enactment of this Act); and (B) includes any Special Administrative Region of any such covered nation. (4) Foreign adversary entity The term foreign adversary entity means\u2014 (A) any official governmental body at any level in a foreign adversary; (B) the Armed Forces of a foreign adversary; (C) the leading political party of a foreign adversary; (D) a person organized under the laws of, headquartered in, or with its principal place of business in a foreign adversary; or (E) a person subject to the direction or control of an entity listed in subparagraphs (A) through (D). (5) Interest The term interest includes any interest\u2014 (A) held directly or indirectly through any chain of ownership; or (B) held as a derivative financial instrument or other contractual arrangement with respect to a sanctioned entity or foreign adversary entity, including any financial instrument or other contract which seeks to replicate any financial return with respect to such an entity or an interest in such an entity. (6) Sanctioned entity The term sanctioned entity means an entity listed on any of the following lists: (A) The Non-SDN Chinese Military-Industrial Complex Companies List (NS\u2013CMIC List) maintained by the Office of Foreign Assets Control of the Department of the Treasury under Executive Order 14032 (86 Fed. Reg. 30145; relating to Addressing the Threat From Securities Investments That Finance Certain Companies of the People\u2019s Republic of China), or any successor order. (B) The list of Chinese military companies identified by the Secretary of Defense pursuant to section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note). (C) The Entity List maintained by the Department of Commerce and set forth in Supplement No. 4 to part 744 of the Export Administration Regulations. (D) The Denied Persons List maintained by the Department of Commerce and described in section 764.3(a)(2) of the Export Administration Regulations. (E) The Unverified List set forth in Supplement No. 6 to part 744 of the Export Administration Regulations. (F) The Military End User List set forth in Supplement No. 7 to part 744 of the Export Administration Regulations. (G) The list of companies whose equipment or services are maintained by the Federal Communications Commission under section 2(a) of the Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1601(a) ), commonly referred to as the FCC Covered list. (H) The Uyghur Forced Labor Prevention Act Entity List maintained pursuant to section 2(d)(2)(B) of the Act entitled \u2018An Act to ensure that goods made with forced labor in the Xinjiang Uyghur Autonomous Region of the People's Republic of China do not enter the United States market, and for other purposes\u2019, approved December 23, 2021 ( Public Law 117\u201378 ). (I) The Withhold Release Orders and Findings List maintained by the Commissioner of U.S. Customs and Border Protection pursuant to the Act entitled \u2018An Act to ensure that goods made with forced labor in the Xinjiang Uyghur Autonomous Region of the People's Republic of China do not enter the United States market, and for other purposes\u2019, approved December 23, 2021 ( Public Law 117\u201378 ). .\n##### (c) Effective date\n**(1) Regulations required**\nNot more than 180 days after the enactment of this Act, the Secretary shall issue regulations implementing this Act.\n**(2) Effective date of regulations**\nThe regulations issued under paragraph (1) shall take effect not later than 1 year after the date of enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "928",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PARSA",
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
            "updateDate": "2026-03-06T20:43:42Z"
          },
          {
            "name": "Asia",
            "updateDate": "2026-03-06T20:43:20Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-03-06T20:43:32Z"
          },
          {
            "name": "China",
            "updateDate": "2026-03-06T20:43:16Z"
          },
          {
            "name": "Department of Labor",
            "updateDate": "2026-03-06T20:43:46Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-03-06T20:43:00Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-03-06T20:43:07Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-03-06T20:43:11Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2026-03-06T20:43:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-26T16:40:24Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2067ih.xml"
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
      "title": "PARSA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PARSA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Americans\u2019 Retirement Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employment Retirement Income Security Act of 1974 to prohibit plan investments in foreign adversary and sanctioned entities, require disclosure of existing investments in such entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:38Z"
    }
  ]
}
```
