# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7305
- Title: Energy Threat Analysis Center Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7305
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-05-27T18:41:27Z
- Update date including text: 2026-05-27T18:41:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-02 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-12 - Calendars: Placed on the Union Calendar, Calendar No. 563.
- 2026-05-12 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.
- 2026-05-12 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-02 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-12 - Calendars: Placed on the Union Calendar, Calendar No. 563.
- 2026-05-12 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.
- 2026-05-12 - Committee: Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7305",
    "number": "7305",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Energy Threat Analysis Center Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-27T18:41:27Z",
    "updateDateIncludingText": "2026-05-27T18:41:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-12",
      "calendarNumber": {
        "calendar": "U00563"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 563.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Energy and Commerce. H. Rept. 119-646.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
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
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
            "date": "2026-05-12T23:35:51Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-02T14:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T22:33:36Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-04T22:33:22Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-02T22:32:16Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7305ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7305\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Ms. Castor of Florida (for herself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the Department of Energy\u2019s Energy Sector Operational Support for Cyberresilience Program to provide operational support for energy sector cybersecurity and resilience.\n#### 1. Short title\nThis Act may be cited as the Energy Threat Analysis Center Act of 2026 .\n#### 2. Energy Sector Operational Support for Cyberresilience Program\nSection 40125(c) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18724(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (E) as subparagraphs (B) through (F), respectively;\n**(B)**\nby inserting before subparagraph (B), as so redesignated, the following:\n(A) to strengthen the collective defense, response, and resilience of the United States energy sector\u2014 (i) by enhancing collaboration between the government and the energy sector to analyze threats to the energy sector and to deny, disrupt, and mitigate operational impacts to energy systems\u2014 (I) by exchanging information at the classified and unclassified level, collectively analyzing potential and realized threats, and providing recommendations to mitigate these threats that benefit the broader energy sector; and (II) by increasing operational collaboration through establishing the technical infrastructure necessary to house, access, and perform advanced analytics and experimentation to enable analysis, discovery, alerts, and collaboration activities of intelligence-driven and intelligence-informed technical data and knowledge, threat information and to share actionable insights and threat mitigation; (ii) by advancing the collective understanding of national security risks and vulnerabilities associated with the energy sector that may be exploited by adversaries; and (iii) by increasing the energy sector\u2019s understanding of threat actor tactics, techniques, procedures, indicators of compromise, capabilities, and activities that present risks to the energy sector. ;\n**(C)**\nin subparagraph (D), as so redesignated, by striking sector; and inserting sector; and ;\n**(D)**\nin subparagraph (E), as so redesignated, by striking ; and and inserting . ; and\n**(E)**\nby striking subparagraph (F), as so redesignated;\n**(2)**\nby redesignating paragraph (2) as paragraph (6);\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Energy Threat Analysis Center The Secretary may carry out any activity of the program developed and carried out under paragraph (1) through an Energy Threat Analysis Center, which may be established at one or more physical locations. (3) No right or benefit (A) Secretarial authority The provision of assistance or information under the program developed and carried out under paragraph (1) to a governmental or private entity shall be at the sole and unreviewable discretion of the Secretary. (B) Provision of assistance or information The provision of assistance or information under the program developed and carried out under paragraph (1) to a governmental or private entity shall not create a right or benefit, substantive or procedural, for any other governmental or private entity to similar assistance or information. (4) Nonapplicability of FACA The program developed and carried out under paragraph (1) shall not be considered an advisory committee under chapter 10 of title 5, United States Code. (5) Exemption from disclosure Information shared by or with the Federal Government or a State, Tribal, or local government under the program developed and carried out under paragraph (1) shall be\u2014 (A) deemed voluntarily shared information and exempt from disclosure under section 552 of title 5, United States Code, and any State, Tribal, or local provision of law requiring disclosure of information or records; and (B) withheld, without discretion, from the public under section 552(b)(3)(B) of title 5, United States Code, and any State, Tribal, or local provision of law requiring disclosure of information or records. ; and\n**(4)**\nin paragraph (6), as so redesignated, by striking 2022 through 2026 and inserting 2027 through 2031 .",
      "versionDate": "2026-02-02",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7305rh.xml",
      "text": "IB\nUnion Calendar No. 563\n119th CONGRESS\n2d Session\nH. R. 7305\n[Report No. 119\u2013646]\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Ms. Castor of Florida (for herself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nMay 12, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on February 2, 2026\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to reauthorize the Department of Energy\u2019s Energy Sector Operational Support for Cyberresilience Program to provide operational support for energy sector cybersecurity and resilience.\n#### 1. Short title\nThis Act may be cited as the Energy Threat Analysis Center Act of 2026 .\n#### 2. Energy Sector Operational Support for Cyberresilience Program\nSection 40125(c) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18724(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (A) through (E) as subparagraphs (B) through (F), respectively;\n**(B)**\nby inserting before subparagraph (B), as so redesignated, the following:\n(A) to strengthen the collective defense, response, and resilience of the United States energy sector\u2014 (i) by enhancing collaboration between the government and the energy sector to analyze threats to the energy sector and to deny, disrupt, and mitigate operational impacts to energy systems\u2014 (I) by exchanging information at the classified and unclassified level, collectively analyzing potential and realized threats, and providing recommendations to mitigate these threats that benefit the broader energy sector; and (II) by increasing operational collaboration through establishing the technical infrastructure necessary to house, access, and perform advanced analytics and experimentation to enable analysis, discovery, alerts, and collaboration activities of intelligence-driven and intelligence-informed technical data and knowledge, threat information and to share actionable insights and threat mitigation; (ii) by advancing the collective understanding of national security risks and vulnerabilities associated with the energy sector that may be exploited by adversaries; and (iii) by increasing the energy sector\u2019s understanding of threat actor tactics, techniques, procedures, indicators of compromise, capabilities, and activities that present risks to the energy sector; ;\n**(C)**\nin subparagraph (D), as so redesignated, by striking sector; and inserting sector; and ;\n**(D)**\nin subparagraph (E), as so redesignated, by striking ; and and inserting . ; and\n**(E)**\nby striking subparagraph (F), as so redesignated;\n**(2)**\nby redesignating paragraph (2) as paragraph (7);\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Energy Threat Analysis Center The Secretary may carry out any activity of the program developed and carried out under paragraph (1) through an Energy Threat Analysis Center, which may be established at one or more physical locations. (3) No right or benefit (A) Secretarial authority The provision of assistance or information under the program developed and carried out under paragraph (1) to a governmental or private entity shall be at the sole and unreviewable discretion of the Secretary. (B) Provision of assistance or information The provision of assistance or information under the program developed and carried out under paragraph (1) to a governmental or private entity shall not create a right or benefit, substantive or procedural, for any other governmental or private entity to similar assistance or information. (4) Nonapplicability of FACA The program developed and carried out under paragraph (1) shall not be considered an advisory committee under chapter 10 of title 5, United States Code. (5) Exemption from disclosure Information shared by or with the Federal Government or a State, Tribal, or local government under the program developed and carried out under paragraph (1) shall be\u2014 (A) deemed voluntarily shared information and exempt from disclosure under section 552 of title 5, United States Code, and any State, Tribal, or local provision of law requiring disclosure of information or records; and (B) withheld, without discretion, from the public under section 552(b)(3)(B) of title 5, United States Code, and any State, Tribal, or local provision of law requiring disclosure of information or records. (6) Transaction authority (A) In general In addition to any other authority granted to the Secretary under any other provision of law, the Secretary is authorized to enter into and perform contracts, cooperative agreements, grants, and other transactions with public agencies, private organizations, and persons to carry out the program developed and carried out under paragraph (1). (B) Minimizing delays The Secretary may establish and utilize pre-approved national security contracting mechanisms, model partnership agreements, and expedited review procedures for purposes of entering into transactions under subparagraph (A). ; and\n**(4)**\nin paragraph (7), as so redesignated, by striking 2022 through 2026 and inserting 2027 through 2031 .",
      "versionDate": "2026-05-12",
      "versionType": "Reported in House"
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-25T15:39:08Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-02-25T15:39:02Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-02-25T15:38:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-05-15T19:14:42Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7305ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7305rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Energy Threat Analysis Center Act of 2026",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-13T09:23:25Z"
    },
    {
      "title": "Energy Threat Analysis Center Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Energy Threat Analysis Center Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to reauthorize the Department of Energy's Energy Sector Operational Support for Cyberresilience Program to provide operational support for energy sector cybersecurity and resilience.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:40Z"
    }
  ]
}
```
