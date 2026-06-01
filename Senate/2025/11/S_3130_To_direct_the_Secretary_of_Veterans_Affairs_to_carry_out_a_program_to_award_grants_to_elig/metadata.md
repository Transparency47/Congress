# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3130
- Title: Veterans TBI Adaptive Care Opportunities Nationwide Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3130
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-02-25T12:03:23Z
- Update date including text: 2026-02-25T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3130",
    "number": "3130",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Veterans TBI Adaptive Care Opportunities Nationwide Act of 2025",
    "type": "S",
    "updateDate": "2026-02-25T12:03:23Z",
    "updateDateIncludingText": "2026-02-25T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
        "item": [
          {
            "date": "2025-11-06T18:27:51Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T18:27:51Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NV"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "OH"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3130is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3130\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. McCormick (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a program to award grants to eligible entities to develop, implement, and evaluate approaches and methodologies for prospective randomized control trials for neurorehabilitation treatments for the treatment of chronic mild traumatic brain injury in veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans TBI Adaptive Care Opportunities Nationwide Act of 2025 .\n#### 2. Department of Veterans Affairs grant program for supplemental neurorehabilitation approaches to chronic mild TBI treatment\n##### (a) In general\nThe Secretary of Veterans Affairs shall establish a grant program (to be known as the TBI Innovation Grant Program ) to award grants to eligible entities for the development, implementation, and evaluation of approaches and methodologies for prospective randomized control trials for neurorehabilitation treatments for the treatment of chronic mild TBI (in this section referred to mTBI ) in veterans.\n##### (b) Duration\nThe authority of the Secretary to carry out the grant program under this section shall terminate at the end of the three-year period beginning on the date of the enactment of this Act.\n##### (c) Use of funds\nAn eligible entity in receipt of a grant under this section shall use amounts awarded under such grant to support activities that include\u2014\n**(1)**\ndesigning and testing novel or integrative treatments for mTBI that prioritize patient-centered care, including non-pharmacological therapies;\n**(2)**\nconducting clinical studies and assessments to measure the effectiveness of funded approaches\u2014\n**(A)**\nto improve mental health outcomes among veterans;\n**(B)**\nto reduce suicidality and common risk factors for completing suicide, including depression and substance use disorders among veterans; and\n**(C)**\nto mitigate long-term effects of mTBI;\n**(3)**\nproviding training for clinicians and outreach to veterans and their families to improve awareness and accessibility of innovative mTBI treatments; and\n**(4)**\nestablishing partnerships with community organizations, academic institutions, and health care facilities of the Department of Veterans Affairs to implement and evaluate best practices.\n##### (d) Limitation on grant amount\nThe Secretary may not award an eligible entity a grant under this section in an amount that exceeds $5,000,000 per fiscal year.\n##### (e) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that the Secretary determines have demonstrated experience in delivering or researching effective treatments for mTBI.\n##### (f) Program administration\n**(1) Applications**\nAn eligible entity desiring a grant under this section shall submit to the Secretary an application in such form, at such time, and containing such information and assurances as the Secretary determines appropriate, including a detailed description of\u2014\n**(A)**\nproposed activities;\n**(B)**\nexpected outcomes; and\n**(C)**\nplans for evaluating effectiveness.\n**(2) Periodic reports**\nAn eligible entity in receipt of a grant under this section shall, not less frequently than annually, submit to the Secretary a report that includes, with respect to the period covered by the report\u2014\n**(A)**\na description of how the eligible entity used such grant;\n**(B)**\na summary of the progress of activities funded with amounts from such grant; and\n**(C)**\nmeasured outcomes relating to such activities.\n**(3) Oversight; annual evaluations**\nThe Secretary shall\u2014\n**(A)**\nensure rigorous oversight with respect to the grant program under this section; and\n**(B)**\non an annual basis during the period in which the authority to carry out the grant program is effective, evaluate the efficacy of activities funded with a grant awarded under such program.\n##### (g) Coordination with mental health services of Department of Veterans Affairs\nThe Secretary shall ensure that the grant program under this section aligns with the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program of the Department under section 201 of the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 ( Public Law 116\u2013171 ; 38 U.S.C. 1720F note)\u2014\n**(1)**\nto provide for cohesive and comprehensive support for veterans with mTBI and associated mental health conditions; and\n**(2)**\nto increase research and development on integrated mTBI and mental health interventions outside of the scope of traditional pathways, interventions, programs, procedures, and pharmaceuticals of the Department.\n##### (h) Annual review\nNot less frequently than annually during the duration of the grant program under this section, the Secretary shall review the effectiveness of such program to determine the potential of such program for continuation or expansion.\n##### (i) Reports to Congress\nNot later than two years after the date of the enactment of this Act, and not less frequently than annually thereafter, the Secretary shall submit to Congress a report that includes\u2014\n**(1)**\nthe findings of the activities reported under subsection (f)(2); and\n**(2)**\nthe recommendations of the Secretary with respect to policy and programmatic improvements to services of the Department of Veterans Affairs to treat TBI among veterans.\n##### (j) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall prescribe regulations to carry out this section.\n##### (k) Funding\n**(1) Available amounts**\nThe Secretary may carry out the grant program under this section using amounts available to the Secretary for general mental health care programs.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary $30,000,000 for fiscal years 2026 through 2028 to carry out the grant program under this section, which shall remain available until expended.\n##### (l) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means any of the following:\n**(A)**\nA nonprofit organization.\n**(B)**\nAn academic institution engaged in research with respect to TBI.\n**(C)**\nA non-Department of Veterans Affairs health care provider with expertise in neurorehabilitative therapies.\n**(D)**\nAn entity the Secretary determines appropriate for an award of a grant under this section.\n**(2) TBI**\nThe term TBI means traumatic brain injury.\n**(3) Treatment**\nThe term treatment , with respect to TBI, means clinical interventions, therapeutic devices, or rehabilitation care provided directly to a veteran with TBI.\n**(4) Veteran**\nThe term veteran has the meaning given that term in section 101 of title 38, United States Code.",
      "versionDate": "2025-11-06",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:50:48Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3130is.xml"
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
      "title": "Veterans TBI Adaptive Care Opportunities Nationwide Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans TBI Adaptive Care Opportunities Nationwide Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to carry out a program to award grants to eligible entities to develop, implement, and evaluate approaches and methodologies for prospective randomized control trials for neurorehabilitation treatments for the treatment of chronic mild traumatic brain injury in veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:21Z"
    }
  ]
}
```
