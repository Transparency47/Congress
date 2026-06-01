# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2678
- Title: Global Fragility Reauthorization Act
- Congress: 119
- Bill type: S
- Bill number: 2678
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-11T18:59:50Z
- Update date including text: 2025-09-11T18:59:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2678",
    "number": "2678",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Global Fragility Reauthorization Act",
    "type": "S",
    "updateDate": "2025-09-11T18:59:50Z",
    "updateDateIncludingText": "2025-09-11T18:59:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-02T01:00:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2678is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2678\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Coons (for himself and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo reauthorize the Global Fragility Act of 2019, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Global Fragility Reauthorization Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Sense of Congress.\nSec. 3. Statement of policy.\nSec. 4. Selection of new priority countries.\nSec. 5. Annual Global Fragility Act Steering Committee meeting on policy alignment.\nSec. 6. Implementation of the Global Fragility Strategy.\nSec. 7. Global fragility report and strategy.\nSec. 8. Reauthorization of the Prevention and Stabilization Fund.\nSec. 9. Reauthorization of the Complex Crises Fund.\nSec. 10. Use of Economic Support Fund to support monitoring, evaluation, and learning activities.\n#### 2. Sense of Congress\nIt is the sense of Congress that integrating all development, diplomatic, and defense tools into the Global Fragility Strategy, including all forms of diplomatic engagement and security cooperation, is crucial to achieving the national security interests of the United States.\n#### 3. Statement of policy\nIt is the policy of the United States to seek to stabilize conflict-affected areas and prevent violence and fragility globally in order to increase the security, stability, and prosperity of the United States, including by\u2014\n**(1)**\nensuring that all relevant Federal departments and agencies coordinate to achieve coherent, long-term goals for programs designed to carry out such policy;\n**(2)**\nseeking to improve global, regional, and local coordination of relevant international and multilateral development and donor organizations regarding efforts to carry out such policy; and\n**(3)**\nenhancing the effectiveness of United States foreign assistance programs and activities to carry out such policy, including by improving assessment, monitoring, and evaluation conducted by the relevant Federal departments and agencies.\n#### 4. Selection of new priority countries\nSection 505 of the Global Fragility Act of 2019 ( 22 U.S.C. 9804 ) is amended by adding at the end the following:\n(c) Selection of new priority countries (1) Authorization During the 1-year period beginning on the date of the enactment of the Global Fragility Reauthorization Act , the President may select additional countries as priority countries in accordance with subsections (a) and (b). (2) Report Not later than 30 days before designating a country as a priority country pursuant to paragraph (1), the President shall submit a report to the appropriate congressional committees that describes the criteria used to select such country as a priority country. (d) Discontinuance of programming in countries The Department of State is not obligated to continue programming to implement a country or regional plan described in section 506 if the Secretary of State, after consultation with relevant departments or agencies, certifies to Congress that\u2014 (1) such country or region is no longer fragile due to no longer meeting the indicators required for designation as a priority country or region set forth in subsection (a)(1)(B); or (2) the government of such country or the governments in such region are no longer committed to effectively working with the United States to implement reforms or other programs required to implement the relevant country or regional plan. .\n#### 5. Annual Global Fragility Act Steering Committee meeting on policy alignment\n##### (a) In general\nSection 506 of the Global Fragility Act of 2019 ( 22 U.S.C. 9805 ; title V of division J of Public Law 116\u201394 ) is amended\u2014\n**(1)**\nby striking Not later than and inserting the following:\n(a) In general Not later than ; and\n**(2)**\nby adding at the end the following:\n(b) Annual meetings (1) In general The senior Federal officials referred to in paragraph (2) shall convene an annual meeting\u2014 (A) to evaluate the extent to which the strategic approach and objectives of priority country and regional plans described in subsection (a) align to current United States policy priorities in the relevant countries and regions; (B) to assess the elements described in paragraphs (1) through (11) of subsection (a) and consider steps to address any deficiencies in such elements; (C) to determine any beneficial updates or amendments to the priority country and region plans or United States policy priorities to ensure effective short- and long-term alignment; and (D) to consider any beneficial steps to increase alignment of relevant diplomatic, development, and security assistance and cooperation activities with the objectives of such plans and priorities. (2) Participants Each meeting convened pursuant to paragraph (1) shall be chaired by a position not lower than the Deputy Secretary of State or the Deputy National Security Advisor and include the participation of\u2014 (A) the Counselor of the Department of State; (B) the Under Secretary of State for Civilian Security, Democracy, and Human Rights; (C) the Under Secretary of State for Political Affairs; (D) the Under Secretary of Defense for Policy; (E) the Under Secretary of the Treasury for International Affairs; (F) the Joint Staff Director for Strategy, Plans, and Policy; (G) each relevant Assistant Secretary, Assistant Administrator, National Security Counsel Senior Director, and relevant equivalent level official with regional or functional responsibility for planning, coordination, or implementation of diplomatic, development, or security cooperation or assistance activities in a priority country; and (H) equivalent level participation from all other relevant Federal departments and agencies with activities relevant to conflict prevention or stabilization in a priority county or region. .\n##### (b) Conforming amendments\nThe Global Fragility Act of 2019 ( 22 U.S.C. 9801 et seq. ) is amended\u2014\n**(1)**\nin section 507(1) ( 22 U.S.C. 9806(1) ), by striking section 506 and inserting section 506(a) ; and\n**(2)**\nin section 508(a) ( 22 U.S.C. 9807(a) ) in the matter preceding paragraph (1), by striking section 506 and inserting section 506(a) .\n#### 6. Implementation of the Global Fragility Strategy\n##### (a) Required interagency coordination\nSection 507 of the Global Fragility Act of 2019 ( 22 U.S.C. 9806 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by inserting the Chief Executive Officer of the United States Development Finance Corporation, the Chief Executive Officer of the Millennium Challenge Corporation, after Secretary of Defense, ;\n**(2)**\nin paragraph (1), by striking and at the end;\n**(3)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(4)**\nby adding at the end the following:\n(3) the Secretary of Defense fully meets the Department\u2019s responsibilities under the Global Fragility Strategy, including to fully implement the defense and security-related goals outlined under the 10-year country plans by utilizing funding appropriated for Global Fragility Strategy implementation and additional funding mechanisms, as appropriate; and (4) private sector investment to support conflict prevention and stabilization is mobilized by setting United States Development Finance Corporation investment targets in fragile countries. .\n##### (b) In general\nSection 507 of the Global Fragility Act of 2019, as amended by subsection (a), is further amended\u2014\n**(1)**\nby striking The President and inserting the following:\n(a) In general The President ; and\n**(2)**\nby adding at the end the following:\n(b) Staffing (1) Counselor The Counselor of the Department of State shall lead the implementation of the Global Fragility Strategy required under section 504. (2) Additional staffing Each relevant regional affairs bureau of the Department of State shall delegate employees with expertise in conflict prevention to assist the Counselor in the implementation of the Global Fragility Strategy. .\n##### (c) Continued implementation of the Global Fragility Strategy\nThe President, in carrying out section 507 of the Global Fragility Act of 2019, as amended by subsections (a) and (b), including implementing the 10-year plans developed pursuant to section 506 of such Act ( 22 U.S.C. 9805 )\u2014\n**(1)**\nshall discontinue the implementation of the Global Fragility Strategy in Haiti and Libya, which no longer meet the criteria required for priority country status under section 505(a) of such Act ( 22 U.S.C. 9804(a) );\n**(2)**\nshall continue implementing the Global Fragility Strategy in Coastal West Africa, Mozambique, and Papua New Guinea; and\n**(3)**\nmay add a new country or region to the list of countries and regions designated as priority countries and priority regions under section 505 of such Act ( 22 U.S.C. 9804 ) at least 30 days after notifying Congress of such proposed addition.\n#### 7. Global fragility report and strategy\n##### (a) In general\nSection 508 of the Global Fragility Act of 2019 ( 22 U.S.C. 9807 ) is amended by adding at the end the following:\n(c) Study; strategy; report The Secretary of State, using the principles identified in the Global Fragility Strategy established pursuant to section 504, shall\u2014 (1) study the feasibility of applying such principles to support cost-efficient and effective United States foreign policy goals and foreign assistance objectives in other geographic areas; (2) develop a strategy for applying such principles across Department of State regional bureaus, foreign assistance operations, and overseas diplomatic missions, which shall include exporting the successes of regional collaboration between posts in priority regions; and (3) not later than 180 days after the date of the enactment of the Global Fragility Reauthorization Act , submit a report to the appropriate congressional committees that\u2014 (A) summarizes the findings of the study under paragraph (1) and the strategy developed under paragraph (2); and (B) includes a detailed description of the staffing and resources identified pursuant to subsection (d) are necessary to implement such global fragility principles. .\n##### (b) Identification of necessary reforms To remove impediments to conflict prevention\nSection 508 of the Global Fragility Act of 2019, as amended by subsection (a), is further amended by adding at the end the following:\n(d) Reforms The President, in collaboration with the heads of relevant Federal departments and agencies, shall determine what staffing, resources, and reforms are necessary to remove persistent impediments to conflict prevention and stabilization, including\u2014 (1) addressing overly restrictive diplomatic security posture and staffing constraints; (2) strengthening mandatory professional development around conflict prevention; and (3) regularizing the process for providing surge staffing support to fragile countries, including sustaining global fragility coordinator posts in such countries and in Washington, DC. .\n##### (c) Maintenance of staffing levels\nSection 508 of the Global Fragility Act of 2019, as amended by subsections (a) and (b), is further amended by adding at the end the following:\n(e) Staffing levels Subject to appropriations, the relevant Federal departments and agencies shall maintain sufficient staffing levels to fully implement the Global Fragility Strategy established pursuant to section 504. .\n#### 8. Reauthorization of the Prevention and Stabilization Fund\nSection 509(a) of the Global Fragility Act of 2019 ( 22 U.S.C. 9808(a) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking 2024 and inserting 2030 ; and\n**(2)**\nin paragraph (3)(A)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) for administrative and other expenses related to the operation, management, and monitoring, evaluation, and learning for programs and activities related to the implementation of the Global Fragility Strategy established pursuant to section 504, including diplomatic and other operational activities carried out to implement such strategy in countries and regions selected by the President, pursuant to section 505(a). .\n#### 9. Reauthorization of the Complex Crises Fund\nSection 509(b) of the Global Fragility Act of 2019 ( 22 U.S.C. 9808(b) ) is amended\u2014\n**(1)**\nin the subsection header, by striking Crisis and inserting Crises ; and\n**(2)**\nin paragraph (2), by striking 2024 and inserting 2030 .\n#### 10. Use of Economic Support Fund to support monitoring, evaluation, and learning activities\n##### (a) Use of funds\nAmounts appropriated or otherwise made available to carry out chapter 4 of part II of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2346 et seq. ; relating to the Economic Support Fund) may be expended for monitoring, evaluation, and learning activities in countries and regions selected by the President, pursuant to section 505(a) of the Global Fragility Act of 2019 ( 22 U.S.C. 9804 ), notwithstanding any other provision of law for any program funded from amounts available for the Prevention and Stabilization Fund established under section 509(a) of such Act ( 22 U.S.C. 9808(a) ) in any fiscal year and related programs funded by other agencies to implement the Global Fragility Strategy established pursuant to section 504 of such Act ( 22 U.S.C. 9803 ).\n##### (b) Appointment of personnel To implement monitoring, evaluation, and learning activities\nThe Secretary of Defense, in consultation with the Under Secretary of Defense for Policy, shall\u2014\n**(1)**\nappoint a senior Department of Defense official to lead the efforts described in subsection (a); and\n**(2)**\nmake available sufficient staffing and other resources to carry out such efforts in accordance with section 507 of the Global Fragility Act of 2019, as amended by section 6.",
      "versionDate": "2025-08-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-11T18:59:50Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2678is.xml"
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
      "title": "Global Fragility Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Global Fragility Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Global Fragility Act of 2019, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-14T03:18:21Z"
    }
  ]
}
```
