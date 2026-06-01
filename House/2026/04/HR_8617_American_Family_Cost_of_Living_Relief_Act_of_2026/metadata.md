# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8617?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8617
- Title: American Family Cost-of-Living Relief Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8617
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T19:42:41Z
- Update date including text: 2026-05-20T19:42:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8617",
    "number": "8617",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "American Family Cost-of-Living Relief Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T19:42:41Z",
    "updateDateIncludingText": "2026-05-20T19:42:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:04:00Z",
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
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8617ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8617\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Mace (for herself and Mr. Massie ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require an agency to prepare a household cost impact analysis before publishing a proposed and final rule, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Family Cost-of-Living Relief Act of 2026 .\n#### 2. Evaluation of impacts of proposed rules on household costs\n##### (a) Rule making impact on household costs\nChapter 5 of title 5, United States Code, is amended by inserting after section 553 the following:\n553a. Impact of rule making on household costs (a) Whenever an agency is required by section 553 of this title, or any other law, to publish general notice of proposed rule making for any proposed rule, the agency shall\u2014 (1) prepare an initial household cost impact analysis for such rule that contains\u2014 (A) a statement about whether a proposed rule would substantially increase household costs; (B) a description of how such increase would affect a household based on the income level of such household; (C) a list of any categories of goods or services that may be affected by such increase; and (D) any recommendations for an alternative rule that would not substantially increase household costs; and (2) make such analysis available for public comment by publishing such analysis in the Federal Register at the time of the publication of such general notice. (b) After notice and receipt of public comments, or a hearing pursuant to section 553, an agency shall prepare a final household cost impact analysis that contains\u2014 (1) the information required under subsection (a)(1); (2) a statement of any significant issues raised by public comments or a hearing in response to the initial household cost impact analysis prepared under subsection (a); and (3) a description of how any such public comments or hearing impacted the analysis of whether the proposed rule would substantially increase household costs. (c) An agency may not promulgate a final rule, if the agency determines, after preparing a final household cost analysis required under subsection (b), that such rule would substantially increase household costs unless\u2014 (1) the rule is required by law; or (2) such agency\u2014 (A) determines the rule is necessary to address\u2014 (i) an imminent threat to national security; (ii) a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ); or (iii) an emergency declared by the President under section 502 of such Act ( 42 U.S.C. 5191 ); and (B) submits a certification to the House of Representatives and the Senate of such imminent threat. (d) Any final household cost impact analysis prepared pursuant to subsection (b) shall be published in the Federal Register when an agency promulgates a final rule under section 553. (e) Any rules finalized pursuant to subsection (c)(2) may remain in effect for not more than 1 year, unless such rule is subsequently authorized by law. (f) Not later than 1 year after the date of enactment of this section, and annually thereafter, the Director of the Office of Management and Budget shall review and publish a report in the Federal Register on any major rules in effect including\u2014 (1) identifying any such major rules that have substantially increased household costs; (2) making any recommendations to amend or repeal such major rules for the purpose of addressing such increase to household costs; and (3) making any recommendations for legislative action for the purpose of addressing such increase to household costs. (g) In this section: (1) The term agency has the meaning given such term in section 551. (2) The term household cost means the average annual out-of-pocket expenditures incurred by a household for basic goods and services necessary for living, including direct and indirect costs related to\u2014 (A) housing, including rent, mortgage payments, homeowner\u2019s insurance, renter\u2019s insurance, maintenance, and homebuilding; (B) utilities, including electric, natural gas, water, sewer, and trash collection; (C) transportation, including vehicle purchase or lease, fuel, insurance, maintenance, and public transportation; (D) food, including raw, cooked, processed, or prepared food, infant formula, or any substance to provide nutrients through human consumption; (E) health care, including insurance premiums, deductibles, copayments, prescription drugs, medical devices, over-the-counter medicine, and medical services; (F) child care, elder care, and dependent care required to maintain employment or household activities; (G) expenses related to education and workforce, including tuition, fees, supplies, and required training or credentialing; (H) household products, including furniture, appliances, cleaning supplies, paper goods, hygiene products, kitchen items, and tools from home upkeep; (I) taxes, fees, and mandatory charges imposed directly or indirectly on households under Federal law; and (J) any other essential goods or services that the Director of the Office of Management and Budget determines materially affects the cost of living for households. (3) The term household means any individual or group of individuals who are living together as one economic unit. (4) The term major rule has the meaning given such term in section 804. (5) The term rule has the meaning given such term in section 551. (6) The term substantially increase with respect to household costs, means an increase of $50 or more a year. 553b. Judicial review (a) For any rule subject to section 553a, any household that is adversely affected or aggrieved by final agency action is entitled to judicial review of agency compliance with the requirements of such section in accordance with chapter 7. (b) Each court having jurisdiction to review such rule for compliance with section 553, or under any other provision of law, shall have jurisdiction to review any claims of noncompliance with section 553a in accordance with chapter 7. (c) The term household has the meaning given such term in section 553a. .\n##### (b) Guidance\nNot later than 180 days after the date of enactment of this Act, the Director of the Office of Management and Budget shall issue guidance to the head of each agency on complying with the amendments made by this Act.\n##### (c) Application\nThis Act, and the amendments made by this Act, shall apply to rules proposed on or after the date of enactment of this Act.",
      "versionDate": "2026-04-30",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-20T19:42:41Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8617ih.xml"
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
      "title": "American Family Cost-of-Living Relief Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Family Cost-of-Living Relief Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require an agency to prepare a household cost impact analysis before publishing a proposed and final rule, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:43Z"
    }
  ]
}
```
