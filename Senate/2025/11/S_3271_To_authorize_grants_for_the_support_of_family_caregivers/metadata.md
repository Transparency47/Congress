# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3271?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3271
- Title: In-Home CARE Act
- Congress: 119
- Bill type: S
- Bill number: 3271
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-06T19:36:58Z
- Update date including text: 2026-01-06T19:36:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3271",
    "number": "3271",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "In-Home CARE Act",
    "type": "S",
    "updateDate": "2026-01-06T19:36:58Z",
    "updateDateIncludingText": "2026-01-06T19:36:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:41:58Z",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3271is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3271\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Booker (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize grants for the support of family caregivers.\n#### 1. Short title\nThis Act may be cited as the In-Home Caregiver Assessment Resources and Education Act or the In-Home CARE Act .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto improve the ability of family caregivers to care for individuals in the home; and\n**(2)**\nto increase opportunities for individuals who are in need of care to remain at home and reduce or postpone the need for such individuals to receive care at an institution or hospital.\n#### 3. Family caregiver grants\nSubpart IV of part D of title III of the Public Health Service Act ( 42 U.S.C. 255 et seq. ) is amended by adding at the end the following:\n339A. Family caregiver grants (a) In General The Secretary, acting through the Administrator of the Administration for Community Living, shall award 3-year grants, on a competitive basis, to eligible organizations to carry out home visiting programs for family caregivers. (b) Definitions In this section: (1) Caregiver assessment The term caregiver assessment means a defined process of gathering information from a family caregiver, through direct contact, which may include contact through a home visit, the internet, telephone or teleconference, or in-person interaction, to identify the specific needs, barriers to carrying out caregiving responsibilities, and existing supports of the family caregiver, to appropriately target recommendations for support services for the family caregiver. (2) Eligible organization The term eligible organization means any of the following that has experience providing the services described in subsection (f): (A) A local government agency. (B) A health care entity. (C) Any other nonprofit or community organization. (3) Family caregiver The term family caregiver means an adult family member or other individual who has a significant relationship with, and who provides in-home assistance with monitoring, management, supervision, or treatment of an individual with a chronic or other health condition, disability, or functional limitation. (c) Coordination In carrying out this section, the Secretary shall coordinate with\u2014 (1) the heads of the National Family Caregiver Support Program of the Administration on Aging and other programs within the Department of Health and Human Services (such as the Lifespan Respite Care Program) and the Secretary of Veterans Affairs, to ensure coordination of caregiver services for family caregivers; and (2) the Administrator of the Centers for Medicare & Medicaid Services, to avoid duplicative services and payments. (d) Application An eligible organization that desires a grant under this section shall submit an application at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum\u2014 (1) an outreach plan that identifies how the eligible organization will ascertain which family caregivers in the community\u2014 (A) are most in need of support and education, particularly caregivers who have had no training and provide complex chronic care activities or perform medical or nursing tasks in addition to assisting with activities of daily living; (B) are caring for individuals who are at the greatest risk of needing institutional care; and (C) desire to participate in the family caregiver home visiting program; (2) a description of the services that the eligible organization will provide directly using grant funds, and a description of the services that the eligible organization will use grant funds to provide through contracts or referrals; (3) a description of how the eligible organization will identify gaps in the services that family caregivers and individuals with a chronic or other health condition, disability, or functional limitation who receive care from a family caregiver in the community are receiving; (4) a description of how the eligible organization can provide\u2014 (A) an initial visit to family caregivers in order to complete a caregiver assessment, including a description of the eligible organization\u2019s expertise in conducting caregiver assessments; (B) education and training, based on evidence-based models, to help the family caregiver learn how to best care for an individual with a chronic or other health condition, disability, or functional limitation, by an individual with expertise in the tasks for which the caregiver requires education and training, including education and training regarding, as applicable\u2014 (i) medication management; (ii) wound care; (iii) nutrition and food preparation for special diets; (iv) fall prevention; (v) management of depression, anxiety, stress, trauma, and other behavioral health conditions, including ways to minimize negative mental health effects; (vi) assistance with activities of daily living; (vii) ways to engage other family members in providing care; (viii) ways to identify and utilize available community resources; and (ix) self-care; and (C) recommendations for home modifications or physical environmental changes that could improve the health or quality of life of an individual with a chronic or other health condition, disability, or functional limitation who is receiving care from a family caregiver; (5) a description of the eligible organization\u2019s ability to provide, or refer family caregivers to local resources or appropriate programs of the Department of Health and Human Services or the Department of Veterans Affairs that will provide\u2014 (A) physical and mental health care, including home health care and long-term support services; (B) transportation; (C) home modification services; (D) respite care; (E) adult day services; (F) support groups; and (G) legal assistance; (6) a description of the eligible organization\u2019s ability to coordinate with other State and community-based agencies; (7) a description of the eligible organization\u2019s understanding of family caregiver issues\u2014 (A) across demographic groups, including age, gender, race and ethnicity, socioeconomic status, sexual orientation, military status, and geographical region; and (B) including disabilities and chronic conditions that affect the populations that the eligible organization will serve; (8) a description of the capacity of the eligible organization to engage family caregivers, family members, and individuals with a chronic or other health condition, disability, or functional limitation who receive care from a family caregiver; and (9) with respect to the population of family caregivers to whom caregiver visits or services will be provided, or for whom workers and volunteers will be recruited and trained, a description of\u2014 (A) the population of family caregivers; (B) the extent and nature of the needs of that population; and (C) existing caregiver services for that population, including the number of caregivers served and the extent of unmet need. (e) Priority In awarding grants under this section, the Secretary shall give priority to eligible organizations that\u2014 (1) the Secretary determines show the greatest likelihood of implementing or enhancing family caregiver home visiting services that best meet the needs of the community; (2) will allow family caregivers to contact the eligible organization by phone, email, or 2-way interactive video for up to 6 months after home visits have ended, or to otherwise contact the organization at any time if a caregiver has questions or concerns; (3) have a proven record of family caregiver support; (4) will use evidence-based programs; or (5) will provide matching funds or can demonstrate that the program funded by a grant under this section will be sustainable after grant funds are no longer provided. (f) Authorized activities An eligible organization receiving a grant under this section shall use grant funds to\u2014 (1) conduct an initial home visit for each family caregiver participating in the program, during which a representative from the eligible organization who has expertise in care management in the home and caregiving will perform a caregiver assessment and determine what follow-up services may benefit the caregiver and the individual with a chronic or other health condition, disability, or functional limitation who receives care from the family caregiver; (2) conduct home visits for the purpose of family caregiver education and training; (3) provide, or provide referrals for, the services described in subsection (d)(5); (4) provide an assessment and referral for physical and mental health services for the family caregiver and for the individual with a chronic or other health condition, disability, or functional limitation who receives care from the family caregiver, as needed; and (5) carry out any other activities that are described in the grant application submitted under subsection (d). (g) Technical assistance center The Secretary shall establish, or contract to establish, a technical assistance center, to be carried out by the National Caregiver Support Collaborative Technical Assistance and Coordinating Center, through which the Secretary shall\u2014 (1) provide evidence-based models for programs funded by grants under this section; (2) provide training for grantees; (3) answer questions from grantees; and (4) facilitate an exchange of information among grantees, and between grantees and other programs within the Department of Health and Human Services, in order to maximize the use of existing resources and services for family caregivers and to avoid the duplication of such services. (h) Evaluation (1) In general Not later than 2 years after the date of enactment of this section, and annually thereafter, the Secretary shall evaluate the success of the grant program carried out under this section, based on criteria that the Secretary may develop for such evaluation. (2) Optional contents of evaluation The evaluation described in paragraph (1) may include an evaluation of\u2014 (A) the extent to which individuals with a chronic or other health condition, disability, or functional limitation who are cared for by a participating family caregiver have\u2014 (i) a reduction in the potential number of hospitalizations; (ii) a reduction in the potential number of institutionalizations; (iii) cost reductions across the health care system; (iv) improved connection to community resources; (v) improved care; and (vi) improved quality of life (including a reduction of stress and anxiety and improved relationships and mood); and (B) the extent to which participating family caregivers have improved quality of life (including a reduction of stress and anxiety and improved health, relationships, mood, and connection to community resources). (i) Reports and recommendations Not later than 1 year before the expiration of the grants awarded under this section, the Secretary shall prepare and submit a report to Congress that includes recommendations, based on the evaluation described in subsection (h), about\u2014 (1) changes to the grant program under this section; (2) the potential for expanding the number and scope of family caregiver home visiting program grants distributed by the Secretary; and (3) extending the length of the grant program. (j) Authorization of appropriations There are authorized to be appropriated to carry out this section such sums as may be necessary. .",
      "versionDate": "2025-11-20",
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
        "name": "Health",
        "updateDate": "2026-01-06T19:36:58Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3271is.xml"
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
      "title": "In-Home CARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "In-Home CARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "In-Home Caregiver Assessment Resources and Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize grants for the support of family caregivers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:31Z"
    }
  ]
}
```
