# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/822?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/822
- Title: Scientific EXPERT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 822
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2025-12-05T22:49:32Z
- Update date including text: 2025-12-05T22:49:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/822",
    "number": "822",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Scientific EXPERT Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:49:32Z",
    "updateDateIncludingText": "2025-12-05T22:49:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T23:48:07Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s822is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 822\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Ms. Klobuchar (for herself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to establish a process for science-focused drug development meetings led by the Reagan-Udall Foundation for the Food and Drug Administration with respect to drugs for rare diseases and conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scientific External Process for Educated Review of Therapeutics Act of 2025 or the Scientific EXPERT Act of 2025 .\n#### 2. Science-focused drug development meetings\nThe Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) is amended by inserting after section 770 ( 21 U.S.C. 379dd ) the following:\n770A. Science-focused drug development meetings (a) In general The Secretary shall develop and implement a process for Foundation led, science-focused drug development meetings to provide an opportunity for academic researchers and medical experts, drug sponsors, scientific organizations, and patient organizations to\u2014 (1) discuss science-related challenges impacting the development of drugs for rare diseases and conditions; (2) identify scientific approaches and opportunities to facilitate the development, review, and approval of such drugs; and (3) align on novel approaches for the development of drugs for particular diseases, including appropriate clinical trial designs and metrics, manufacturing standards, patient populations, clinical endpoints, the use of biomarkers as surrogate endpoints, and natural history as a control, to advance treatment options to address unmet medical needs. (b) Arrangement (1) Qualified third party convenor The Secretary shall enter into an arrangement with the Foundation under which the Foundation agrees to convene EL\u2013SFDD meetings regarding drugs for rare diseases or conditions in accordance with this section. (2) Minimum number of meetings The Foundation shall convene no fewer than 4 EL\u2013SFDD meetings each year, with each such meeting focused on addressing a different rare disease or condition or a different group of rare diseases and conditions. (3) Steering committee (A) In general The Foundation shall establish and maintain a permanent steering committee, to be known as the Science-Focused Drug Development Multistakeholder Steering Committee, to advise the Foundation on implementation of this section, including by\u2014 (i) establishing a process by which licensed and board-certified medical clinicians and academics with expertise in a rare disease or condition, sponsors of drugs for a rare disease or condition, scientific organizations, rare disease or condition patient organizations, and other entities can provide suggested meeting topics to the Foundation; (ii) reviewing such suggested meeting topics for EL\u2013SFDD meetings; and (iii) based on the criteria under subparagraph (B), recommending to the Foundation topics for EL\u2013SFDD meetings. (B) Criteria for meetings In formulating recommendations under subparagraph (A), the Foundation shall consider\u2014 (i) unmet therapeutic needs; (ii) the size of the patient population of the rare disease or condition; (iii) whether there were or are multiple products in development to prevent or treat the rare disease or condition involved; (iv) whether there is a need for increased regulatory flexibility to facilitate the development of products; (v) whether the rare disease or condition involved would benefit from clarity and alignment on drug development questions (such as clinical trial design, natural history as a control, appropriate clinical endpoints, biomarkers that may serve as surrogate endpoints, and other approaches) to expedite drug development for such disease or condition; and (vi) whether the discussions about such rare disease or condition may have broader impact on other rare diseases and conditions. (C) Membership The members of the Steering Committee shall be subject to all relevant conflict of interest policies of the Foundation, and shall include\u2014 (i) representatives of the Center for Drug Evaluation and Research, the Center for Biologics Evaluation and Research, and the Center for Devices and Radiological Health; (ii) academic and licensed and board-certified medical clinicians; (iii) patient representatives; and (iv) industry representatives engaged in the development of drugs for rare diseases and conditions. (4) Planning process In planning an EL\u2013SFDD meeting under this section, the Foundation, in consultation with the stakeholders listed in paragraph (5), shall develop\u2014 (A) a list of the specific objectives of the meeting related to key drug development issues for the rare disease or condition, or group of rare diseases and conditions, with a goal of expediting drug development; (B) a proposed agenda for the meeting; and (C) a list of medical experts, drug sponsors, scientific organizations, patient organizations, and other entities to be invited to participate in the meeting. (5) Agency and stakeholder engagement Throughout the process of planning an EL\u2013SFDD meeting, the Foundation shall consult with\u2014 (A) appropriate staff of the Food and Drug Administration; (B) the Steering Committee; (C) industry representatives engaged in the development of products for rare diseases and conditions to be discussed at such EL\u2013SFDD meeting; (D) patient representatives of rare diseases and conditions under discussion in such EL\u2013SFDD meeting; (E) academics or board-certified and licensed medical clinicians with expertise in treating a rare disease or condition; and (F) other appropriate stakeholders. (6) Post-meeting reports (A) In general Not later than 180 days after an EL\u2013SFDD meeting, the Foundation shall make publicly available on the website of the Food and Drug Administration\u2014 (i) a transcript and recording of the meeting; and (ii) in consultation with the stakeholders listed in paragraph (5), a summary analysis of the input received during the meeting that is relevant to approval or licensing of drugs for the rare disease or condition involved. (B) Contents Each publication under subparagraph (A) shall include a clear identification of\u2014 (i) areas of consensus; (ii) areas where additional clarification or information is needed to reach consensus; and (iii) next steps agreed upon with the Food and Drug Administration. (c) Representatives of FDA review divisions The Secretary shall require appropriate representatives of the review divisions of the Food and Drug Administration to participate in each EL\u2013SFDD meeting under this section. (d) Rules of construction Nothing in this section shall be construed\u2014 (1) to prevent other third-party organizations from organizing similarly structured EL\u2013SFDD-like meetings to discuss challenges in rare disease drug development; (2) to require the Food and Drug Administration to participate in additional meetings described in paragraph (1); (3) to alter the protections offered by laws, regulations, or policies governing disclosure of confidential commercial or trade secret information and any other information exempt from disclosure pursuant to section 552(b) of title 5, United States Code; (4) to limit the ability of the Secretary to consult with individuals and organizations; (5) to create a legal right for consultation on any matter or require the Secretary to meet with any particular expert or stakeholder; (6) to alter agreed-upon goals and procedures identified in the letters described in section 1001(b) of the FDA User Fee Reauthorization Act of 2022; or (7) to increase the number of review cycles for drugs. (e) Definitions In this section: (1) The term EL\u2013SFDD meeting means an externally led, science-focused drug development meeting. (2) The term rare disease or condition has the meaning given such term in section 526. (3) The term Steering Committee means the Science-Focused Drug Development Multistakeholder Steering Committee established under subsection (b)(3). (f) Authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $1,000,000 for each of fiscal years 2025 through 2029. (2) Rule of construction Nothing in this section shall be construed to prohibit the Foundation from soliciting or accepting funds pursuant to section 770(i) for the purposes of planning or operating an EL\u2013SFDD meeting authorized by this section. 770B. Required actions following EL\u2013SFDD meetings (a) Incorporation of input into risk-Benefit assessments In approving or licensing a drug under subsection (c) or (j) of section 505 of this Act or subsection (a) or (k) of section 351 of the Public Health Service Act, the Secretary shall make public\u2014 (1) a statement of whether any EL\u2013SFDD meeting under section 770A was held that was relevant to such approval or licensure; and (2) if a meeting described in paragraph (1) was held, a description of how the Secretary incorporated input from such meeting in the risk-benefit assessment described in section 505(d). (b) Annual report On an annual basis, the Secretary shall submit a report to Congress summarizing\u2014 (1) the number and topics of EL\u2013SFDD meetings held during the reporting period; (2) the extent of participation in such meetings from the review divisions of the Food and Drug Administration; (3) the impact of EL\u2013SFDD meetings on the workload and resources of the Food and Drug Administration; and (4) an assessment of how the input received during such meetings was used in\u2014 (A) deliberations throughout the drug development lifecycle; (B) regulatory decision-making; and (C) formulating recommendations for future meetings. (c) Definition In this section, the term EL\u2013SFDD meeting has the meaning given to that term in section 770A. (d) Authorization of appropriations To carry out this section, there is authorized to be appropriated $1,000,000 for each of fiscal years 2025 through 2029. .",
      "versionDate": "",
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
        "actionDate": "2025-02-24",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1532",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Scientific EXPERT Act of 2025",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-17T19:23:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T19:23:57Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-07-17T19:23:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T19:23:57Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-07-17T19:23:57Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-07-17T19:23:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-28T11:25:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119s822",
          "measure-number": "822",
          "measure-type": "s",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2025-08-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s822v00",
            "update-date": "2025-08-25"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Scientific External Process for Educated Review of Therapeutics Act of 2025 or the Scientific EXPERT Act of 2025</strong></p><p>This bill requires the Food and Drug Administration (FDA) to facilitate and participate in externally led, science-focused drug development meetings to discuss the development of treatments for rare diseases and conditions.\u00a0</p><p>The FDA must enter into an arrangement with the Reagan-Udall Foundation for the FDA under which the foundation agrees to convene such meetings. Meetings must be held at least four times a year, and each meeting must focus on a different rare disease or condition.\u00a0</p><p>The foundation must establish a permanent steering committee to review and recommend topics for each meeting. In evaluating potential topics, the committee must consider unmet therapeutic needs, patient population sizes for different diseases and conditions, and whether a disease or condition would benefit from clarity and alignment on drug development questions, among other factors.\u00a0</p><p>In planning each meeting, the foundation must develop a list of medical experts, drug sponsors, scientific organizations, patient organizations, and other entities to be invited to participate. Representatives of the FDA\u2019s review divisions must attend each meeting.\u00a0</p><p>After each meeting, the foundation must make available a summary of the meeting noting areas of consensus, areas where additional clarification or information is needed, and next steps agreed upon with the FDA.</p><p>The bill also requires the FDA to indicate whether it incorporated any input from these meetings when approving a new drug or biologic.\u00a0</p>"
        },
        "title": "Scientific EXPERT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s822.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Scientific External Process for Educated Review of Therapeutics Act of 2025 or the Scientific EXPERT Act of 2025</strong></p><p>This bill requires the Food and Drug Administration (FDA) to facilitate and participate in externally led, science-focused drug development meetings to discuss the development of treatments for rare diseases and conditions.\u00a0</p><p>The FDA must enter into an arrangement with the Reagan-Udall Foundation for the FDA under which the foundation agrees to convene such meetings. Meetings must be held at least four times a year, and each meeting must focus on a different rare disease or condition.\u00a0</p><p>The foundation must establish a permanent steering committee to review and recommend topics for each meeting. In evaluating potential topics, the committee must consider unmet therapeutic needs, patient population sizes for different diseases and conditions, and whether a disease or condition would benefit from clarity and alignment on drug development questions, among other factors.\u00a0</p><p>In planning each meeting, the foundation must develop a list of medical experts, drug sponsors, scientific organizations, patient organizations, and other entities to be invited to participate. Representatives of the FDA\u2019s review divisions must attend each meeting.\u00a0</p><p>After each meeting, the foundation must make available a summary of the meeting noting areas of consensus, areas where additional clarification or information is needed, and next steps agreed upon with the FDA.</p><p>The bill also requires the FDA to indicate whether it incorporated any input from these meetings when approving a new drug or biologic.\u00a0</p>",
      "updateDate": "2025-08-25",
      "versionCode": "id119s822"
    },
    "title": "Scientific EXPERT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Scientific External Process for Educated Review of Therapeutics Act of 2025 or the Scientific EXPERT Act of 2025</strong></p><p>This bill requires the Food and Drug Administration (FDA) to facilitate and participate in externally led, science-focused drug development meetings to discuss the development of treatments for rare diseases and conditions.\u00a0</p><p>The FDA must enter into an arrangement with the Reagan-Udall Foundation for the FDA under which the foundation agrees to convene such meetings. Meetings must be held at least four times a year, and each meeting must focus on a different rare disease or condition.\u00a0</p><p>The foundation must establish a permanent steering committee to review and recommend topics for each meeting. In evaluating potential topics, the committee must consider unmet therapeutic needs, patient population sizes for different diseases and conditions, and whether a disease or condition would benefit from clarity and alignment on drug development questions, among other factors.\u00a0</p><p>In planning each meeting, the foundation must develop a list of medical experts, drug sponsors, scientific organizations, patient organizations, and other entities to be invited to participate. Representatives of the FDA\u2019s review divisions must attend each meeting.\u00a0</p><p>After each meeting, the foundation must make available a summary of the meeting noting areas of consensus, areas where additional clarification or information is needed, and next steps agreed upon with the FDA.</p><p>The bill also requires the FDA to indicate whether it incorporated any input from these meetings when approving a new drug or biologic.\u00a0</p>",
      "updateDate": "2025-08-25",
      "versionCode": "id119s822"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s822is.xml"
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
      "title": "Scientific EXPERT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Scientific EXPERT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Scientific External Process for Educated Review of Therapeutics Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to establish a process for science-focused drug development meetings led by the Reagan-Udall Foundation for the Food and Drug Administration with respect to drugs for rare diseases and conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:03:27Z"
    }
  ]
}
```
