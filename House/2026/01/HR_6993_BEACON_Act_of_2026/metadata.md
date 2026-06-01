# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6993
- Title: BEACON Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6993
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-05-16T08:07:24Z
- Update date including text: 2026-05-16T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Health.
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by the Yeas and Nays: 7 - 5.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Health.
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by the Yeas and Nays: 7 - 5.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6993",
    "number": "6993",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "BEACON Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:24Z",
    "updateDateIncludingText": "2026-05-16T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by the Yeas and Nays: 7 - 5.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
        "item": [
          {
            "date": "2026-05-14T20:59:57Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-09T14:00:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-16T20:35:42Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-16T13:36:51Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-22T15:18:43Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "MD"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "MP"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "AL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
      "state": "TX"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "IL"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "CO"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MD"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6993ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6993\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Bergman (for himself, Ms. Elfreth , Ms. King-Hinds , Mr. Davis of North Carolina , Mr. Van Orden , and Mr. Luttrell ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out programs to award grants to eligible entities to conduct research with respect to treatments for traumatic brain injury prospective randomized control trials for neurorehabilitation treatments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans TBI Breakthrough Exploration of Adaptive Care Opportunities Nationwide Act of 2026 or the BEACON Act of 2026 .\n#### 2. Department of Veterans Affairs grant program for supplemental neurorehabilitation approaches to chronic mild TBI treatment\n##### (a) In general\nThe Secretary of Veterans Affairs shall establish a grant program (to be known as the TBI Innovation Grant Program ) to award grants to eligible entities described in subsection (b) for the development, implementation, and evaluation of approaches and methodologies for prospective randomized control trials for neurorehabilitation treatments for the treatment of chronic mild TBI (mTBI) in veterans.\n##### (b) Eligible entities described\nAn eligible entity described in this subsection is any of the following:\n**(1)**\nA nonprofit organization.\n**(2)**\nAn academic institution engaged in research with respect to TBI.\n**(3)**\nA non-Department health care provider with expertise in neurorehabilitative therapies.\n**(4)**\nAn entity the Secretary determines appropriate for an award of a grant under this section.\n##### (c) Use of funds\nAn eligible entity in receipt of a grant under this section shall use such grant to support activities that include\u2014\n**(1)**\ndesigning and testing novel or integrative treatments for mTBI that prioritize patient-centered care, including non-pharmacological therapies;\n**(2)**\nconducting clinical studies and assessments to measure the effectiveness of funded approaches to\u2014\n**(A)**\nimprove mental health outcomes among veterans;\n**(B)**\nreduce suicidality, and common risk factors for completing suicide, including depression and substance use disorders among veterans; and\n**(C)**\nmitigate long-term effects of mTBI;\n**(3)**\nproviding training for clinicians and outreach to veterans and their families to improve awareness and accessibility of innovative mTBI treatments; and\n**(4)**\nestablishing partnerships with community organizations, academic institutions, and health care facilities of the Department of Veterans Affairs to implement and evaluate best practices.\n##### (d) Limitation on grant amount\nThe Secretary may not award an eligible entity a grant under this section in an amount that exceeds $5,000,000 per fiscal year.\n##### (e) Priority\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that the Secretary determines have demonstrated experience in delivering or researching effective treatments for mTBI.\n##### (f) Program administration\n**(1) Applications**\nAn eligible entity desiring a grant under this section shall submit to the Secretary an application in such form, at such time, and containing such information and assurances as the Secretary determines appropriate, including a detailed description of\u2014\n**(A)**\nproposed activities;\n**(B)**\nexpected outcomes; and\n**(C)**\nplans for evaluating effectiveness.\n**(2) Periodic reports**\nAn eligible entity in receipt of a grant under this section shall, not less frequently than annually, submit to the Secretary a report that includes, with respect to the period covered by the report\u2014\n**(A)**\na description of how the eligible entity used such grant;\n**(B)**\na summary of the progress of activities funded with amounts from such grant; and\n**(C)**\nmeasured outcomes relating to such activities.\n**(3) Oversight; annual evaluations**\nThe Secretary shall\u2014\n**(A)**\nensure rigorous oversight with respect to the grant program under this section; and\n**(B)**\non an annual basis during the period the authority to carry out the grant program is effective, evaluate the efficacy of activities funded with a grant awarded under such program.\n##### (g) Coordination with VA mental health services\nThe Secretary shall ensure that the grant program under this section aligns with the Staff Sergeant Fox Suicide Prevention Grant Program of the Department to\u2014\n**(1)**\nprovide for cohesive and comprehensive support for veterans with mTBI and associated mental health conditions; and\n**(2)**\nincrease research and development on integrated mTBI and mental health interventions outside of the scope of traditional Department of Veterans Affairs pathways, interventions, programs, procedures, and pharmaceuticals.\n##### (h) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall prescribe regulations to carry out this section.\n##### (i) Available amounts; authorization of appropriations\n**(1) Available amounts**\nThe Secretary may carry out the program under this section using amounts available to the Secretary for general mental health care programs.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary $30,000,000 for fiscal years 2026 through 2028 to carry out the pilot program under this section, which shall remain available until expended.\n##### (j) Duration; annual review\nThe authority of the Secretary to carry out the grant program under this section shall terminate at the end of the 3-year period beginning on the date of the enactment of this Act. During such period, the Secretary shall, on an annual basis, review the effectiveness of such grant program to determine the potential of such grant program for continuation or expansion.\n#### 3. Department of Veterans Affairs grant program for independent third-party research studies and treatment with respect to supplemental neurorehabilitation treatments for mTBI\n##### (a) Establishment\nThe Secretary of Veterans Affairs shall establish and carry out a research grant program to award grants to eligible entities described in subsection (b) for studies and applied programs on approaches and methodologies for the treatment of TBI in veterans.\n##### (b) Eligible entities described\nAn eligible entity described in this subsection is any of the following:\n**(1)**\nAn academic institution that conducts significant research on TBI.\n**(2)**\nA nonprofit organization with\u2014\n**(A)**\nexpertise in TBI research and neurorehabilitation; and\n**(B)**\ndemonstrated capabilities in clinical trials and TBI treatment evaluation and patient care delivery.\n**(3)**\nAn entity, or a partnership among entities, that the Secretary determines appropriate to receive a grant under this section.\n##### (c) Applications\nAn eligible entity desiring a grant under this section shall submit to the Secretary an application in such form, at such time, and containing such information and assurances as the Secretary determines appropriate, including a summary of\u2014\n**(1)**\nproposed research and treatment activities;\n**(2)**\nmethodology; and\n**(3)**\nexpected outcomes.\n##### (d) Grant categories\n**(1) In general**\nPursuant to the research grant program under this section, the Secretary shall, each fiscal year\u2014\n**(A)**\nsubject to the requirement under paragraph (2), award four grants in amounts of not more than $625,000 for exploratory or pilot research and treatment projects; and\n**(B)**\naward five grants in amounts of not more than $1,500,000 for collaborative or multidisciplinary research and treatment initiatives.\n**(2) Priority**\nThe Secretary shall award not fewer than three grants described in paragraph (1)(A) to nonprofit organizations.\n##### (e) Responsibilities of the third-Party organization\n**(1) In general**\nThe Secretary shall enter into an agreement with an independent third-party organization comparable to the National Center for Posttraumatic Stress Disorder of the Department of Veterans Affairs to\u2014\n**(A)**\nadminister the research grant program; and\n**(B)**\ncarry out studies and implement efforts that include\u2014\n**(i)**\nanalyzing data from TBI treatment methodologies developed pursuant to the research grant program to assess the effect, among veterans, of such methodologies on mental health outcomes and long-term recovery;\n**(ii)**\nidentifying evidence-based best practices and providing recommendations for further research or clinical application; and\n**(iii)**\nrandomized, controlled clinical trials to\u2014\n**(I)**\nvalidate and deliver treatments;\n**(II)**\nestablish a standard of care; and\n**(III)**\nimprove access to such treatments for veterans.\n**(2) Report**\nThe independent third-party organization with which the Secretary enters into an agreement under paragraph (1) shall submit to Congress and the Secretary a comprehensive report that includes\u2014\n**(A)**\nthe findings of the studies required under such agreement; and\n**(B)**\nrecommendations with respect to the expansion of successful TBI treatment methodologies and standard of care recommendations, if any, developed pursuant to the research grant program.\n##### (f) Available amounts; authorization of appropriations\n**(1) Available amounts**\nThe Secretary may use amounts available to the Secretary for the operating budget of the National Center for Posttraumatic Stress Disorder to carry out the research grant program under this section.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary $10,000,000 for each of fiscal years 2026 through 2028 to carry out this section.\n##### (g) Reports to Congress\nNot later than two years after the date on which the Secretary commences the research grant program under this section, and on an annual basis thereafter during the period the authority of the Secretary to carry out such research grant program is effective, the Secretary shall submit to Congress a report that includes\u2014\n**(1)**\nthe findings of the studies under\u2014\n**(A)**\nsection 2(f)(2); and\n**(B)**\nthe agreement required by section 3(e); and\n**(2)**\nrecommendations of the Secretary with respect to policy and programmatic improvements to services of the Department to treat TBI among veterans.\n##### (h) Termination date\nThe authority of the Secretary to carry out the research grant program under this section shall terminate on the date that is three years after the date of the enactment of this Act.\n#### 4. Definitions\nIn this Act:\n**(1)**\nThe term TBI means traumatic brain injury.\n**(2)**\nThe term treatment means clinical interventions, therapeutic devices, or rehabilitation care provided directly to a veteran with TBI.\n**(3)**\nThe term veteran has the meaning given such term in section 101 of title 38, United States Code.",
      "versionDate": "2026-01-09",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-22T20:39:03Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6993ih.xml"
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
      "title": "BEACON Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T03:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BEACON Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans TBI Breakthrough Exploration of Adaptive Care Opportunities Nationwide Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to carry out programs to award grants to eligible entities to conduct research with respect to treatments for traumatic brain injury prospective randomized control trials for neurorehabilitation treatments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:25Z"
    }
  ]
}
```
