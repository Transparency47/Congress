# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2326
- Title: Dietary Guidelines Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2326
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-04-14T14:43:43Z
- Update date including text: 2026-04-14T14:43:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2326",
    "number": "2326",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Dietary Guidelines Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T14:43:43Z",
    "updateDateIncludingText": "2026-04-14T14:43:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:09:00Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "KS"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NE"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2326ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2326\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Jackson of Texas (for himself, Mr. Mann , Mr. Baird , Mr. Harris of Maryland , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the National Nutrition Monitoring and Related Research Act of 1990 to improve the dietary guidelines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dietary Guidelines Reform Act of 2025 .\n#### 2. Establishment of dietary guidelines\n##### (a) In general\nSection 301(a) of the National Nutrition Monitoring and Related Research Act of 1990 ( 7 U.S.C. 5341(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking the paragraph designation and heading and all that follows through five years in the first sentence and inserting the following:\n(1) In general At least every 10 years, ; and\n**(B)**\nby adding at the end the following: Rulemaking requirements under section 553 of title 5, United States Code, shall apply to the development of each report under this paragraph. ;\n**(2)**\nby indenting paragraphs (2) and (3) appropriately;\n**(3)**\nin paragraph (2), by striking shall and all that follows through the period at the end and inserting the following:\nshall\u2014 (A) be based on significant scientific agreement that is determined by evidence-based review (as defined in paragraph (9)(A)); (B) be current at the time that the report is prepared; (C) be derived from the questions generated under paragraph (5)(E); (D) address high-priority areas of concern to advance health outcomes; (E) be designed to achieve nutritional adequacy and promote health, as specified by the Food and Nutrition Board of the National Academies of Sciences, Engineering, and Medicine, through the consumption of food, including nutrients and bioactive food components occurring naturally and in fortified foods; (F) include nutritional and dietary information relevant to individuals with common nutrition-related chronic diseases, as defined by the Centers for Disease Control and Prevention; and (G) include recommendations that are affordable, available, and accessible for the general population. ;\n**(4)**\nby redesignating paragraph (3) as paragraph (8);\n**(5)**\nby inserting after paragraph (2) the following:\n(3) Frequency The Secretaries may publish the report required under paragraph (1) more frequently than required under that paragraph if the Secretaries determine that more frequent publication is necessary to promote health based on updated dietary reference intake values specified by\u2014 (A) the Food and Nutrition Board of the National Academies of Sciences, Engineering, and Medicine; and (B) other relevant scientific advancements based on continuous review of the totality of publicly available scientific evidence. (4) Notification of update (A) In general Not later than 90 days before the Secretaries plan to update a report under paragraph (1), the Secretaries shall submit notification of that plan, in writing, to the Committees on Agriculture, Nutrition, and Forestry and Health, Education, Labor, and Pensions of the Senate and the Committees on Agriculture and Energy and Commerce of the House of Representatives. (B) Justification The notification under subparagraph (A) shall include a justification for updating the report. (5) Independent Advisory Board (A) In general Not later than 90 days after the Secretaries submit a notification under paragraph (4)(A), the Secretaries shall establish an Independent Advisory Board (referred to in this paragraph as the Board ). (B) Members The Board shall comprise not more than 8 members, of which\u2014 (i) 4 shall be appointed by the Secretaries, 2 of whom shall not be Federal employees; and (ii) 1 shall be appointed by each of the highest-ranking Member on each Committee described in paragraph (4)(A) of the opposite political party of the President of the United States. (C) Expertise Each member appointed to the Board shall have expertise in nutrition science or food science, including academic and applied experience. (D) Meetings (i) In general The first meeting of the Board shall take place on or after the date that is 90 days after the Secretaries submit a notification under paragraph (4)(A). (ii) Quorum A 6/8 majority of the members shall constitute a quorum for the transaction of the business of the Board. (E) Duties Not later than 1 year after the establishment of the Board, the Board shall submit to the Secretaries and the Committees described in paragraph (4)(A) a list of scientific questions based on the proposed report under paragraph (1), which questions shall be used to inform the work of the Secretaries on that report and any relevant work of the Committees described in paragraph (4)(A). (F) Termination The authority of the Board shall terminate, and the Board shall disband, immediately after carrying out subparagraph (E). (6) Dietary reference intake updates (A) In general The Secretaries shall coordinate with the Joint United States-Canada Dietary Reference Intake Working Group to ensure that the Food and Nutrition Board of the National Academies of Sciences, Engineering, and Medicine update the dietary reference intake values to represent the most up-to-date understanding of nutritional science. (B) Updates The Joint United States-Canada Dietary Reference Intake Working Group is encouraged\u2014 (i) to initiate at least 1 dietary reference intake update per year; and (ii) to identify updates that are of highest priority and necessitate review. (7) Exclusion The information and guidelines contained in each report required under paragraph (1) shall not be based on or include topics that are not relevant to dietary guidance, as determined by the Secretaries, in consultation with the Independent Advisory Board established under paragraph (5), including taxation, social welfare policies, purchases under Federal feeding programs, food and agricultural production practices, food labeling, socioeconomic status, race, religion, ethnicity, culture, or regulations relating to nutrition. ; and\n**(6)**\nby adding at the end the following:\n(9) Evidence-based review (A) Definition of evidence-based review In this paragraph, the term evidence-based review means a process under which\u2014 (i) the totality of the scientific evidence relevant to a question of interest is collected, analyzed, and evaluated; (ii) scientific studies, conclusions, and recommendations are rated, adhering strictly to standardized, generally accepted evidence-based review methods; and (iii) external peer review is conducted by nongovernment experts with recognized expertise in quality-of-evidence evaluation. (B) Strength of evidence Each guideline contained in a report published under paragraph (1) shall be assigned a rating by the Secretaries for the strength of evidence used, including the extent to which the guideline will improve the Healthy Eating Index. (10) Transparency (A) Disclosure Any individual appointed to the Dietary Guidelines Advisory Committee or an Independent Advisory Board established under paragraph (5) shall provide full disclosure of all financial and nonfinancial conflicts of interest relevant to their membership using the Office of Government Ethics Form 450 (or successor form). (B) Publication Notwithstanding any other provision of law, not later than 30 days after the date on which a Dietary Guidelines Advisory Committee is established, the Secretaries shall make publicly available\u2014 (i) the disclosures required under subparagraph (A), categorized by the name of the individual; and (ii) a detailed plan for managing any disclosed conflicts of interest, including financial or ethical conflicts of interest, preferences, values, and beliefs. (11) Funding Of the funds made available by section 32 of the Act of August 24, 1935 ( 7 U.S.C. 612c ), the Secretary of Agriculture shall make available to carry out this subsection $5,000,000 for each of fiscal years 2025 through 2029, to remain available until expended. .\n##### (b) Controlling report\nThe 2020 Dietary Guidelines for Americans published by the Secretaries under section 301(a)(1) of the National Nutrition Monitoring and Related Research Act of 1990 ( 7 U.S.C. 5341(a)(1) ) (as in effect before the date of enactment of this Act) shall be considered the most recent Dietary Guidelines for Americans until the publication of the first report under that section (as amended by subsection (a)).",
      "versionDate": "2025-03-25",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1129",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dietary Guidelines Reform Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T19:55:07Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2326ih.xml"
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
      "title": "Dietary Guidelines Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dietary Guidelines Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Nutrition Monitoring and Related Research Act of 1990 to improve the dietary guidelines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:46Z"
    }
  ]
}
```
