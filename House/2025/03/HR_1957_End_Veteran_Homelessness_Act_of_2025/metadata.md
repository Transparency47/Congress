# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1957?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1957
- Title: End Veteran Homelessness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1957
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-05-22T08:08:00Z
- Update date including text: 2026-05-22T08:08:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1957",
    "number": "1957",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "End Veteran Homelessness Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:00Z",
    "updateDateIncludingText": "2026-05-22T08:08:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-24T21:55:52Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-24T14:03:49Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T19:17:52Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:17:47Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-06T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "IN"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TN"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "PR"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MI"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "AL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "WA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "ME"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NV"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DE"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1957ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1957\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Takano (for himself, Ms. Waters , and Mr. Levin ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 38, United States Code, and the United States Housing Act of 1937, to make certain improvements to the supported housing program for veterans commonly known as HUD-VASH .\n#### 1. Short title\nThis Act may be cited as the End Veteran Homelessness Act of 2025 .\n#### 2. Clarification of staffing needs for case managers of the Veterans Health Administration with regards to homeless veterans and veterans at risk of homelessness\n##### (a) In general\nSection 2003(b) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting (1) before The Secretary ;\n**(2)**\nby inserting , and who is determined to require case management, before is assigned ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) In assigning case managers and providing services under this subsection, the Secretary shall prioritize vulnerable homeless veterans, including veterans who are homeless and who have disabilities (including chronic mental illness, chronic substance abuse disorders, or chronic physical disabilities). .\n##### (b) Annual report\nThe Secretary of Veterans Affairs, in coordination with the Secretary of Housing and Urban Development, shall submit to Congress an annual report on the program under section 8(o)(19) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(19) ), as amended by section 3 of this Act and commonly known as the HUD-VASH program , which shall include, for the year covered by the report, each of the following, disaggregated by locality and by demographics (if the Secretary of Veterans Affairs determines it appropriate):\n**(1)**\nAn identification of the number and demographic characteristics of veterans served by the HUD-VASH program.\n**(2)**\nThe number, qualifications, and demographics of case managers described in section 2003(b) of title 38, United States Code, as amended by subsection (a).\n**(3)**\nAn assessment of the standard and scope of care provided by such case managers to such veterans, including factors such as\u2014\n**(A)**\nstaffing ratios;\n**(B)**\npractices used in case management;\n**(C)**\nfrequency with which a case manager contacts a veteran;\n**(D)**\nwhether a case manager successfully connects a veteran to a requested resource or support; and\n**(E)**\nprofessional licenses or certifications possessed by case managers.\n**(4)**\nAn assessment of the types of services provided by such case managers to such veterans.\n**(5)**\nWith regard to vouchers made available under the HUD-VASH program\u2014\n**(A)**\nthe number requested;\n**(B)**\nthe number allocated;\n**(C)**\nthe number used;\n**(D)**\nthe number assigned but unused; and\n**(E)**\nthe average time between such assignation and such use.\n**(6)**\nThe percentage of such veterans who used such a voucher and received case management from such a case manager.\n**(7)**\nAn identification of barriers that prevented the use of such vouchers by such veterans.\n#### 3. Amendments to HUD-VASH program\nSection 8(o)(19) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(19) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin the first sentence\u2014\n**(i)**\nby striking subparagraph (C) and inserting subparagraph (B) ; and\n**(ii)**\nby striking the amounts specified in subparagraph (B) and inserting amounts ;\n**(B)**\nby striking the second sentence and inserting In the course of administering such program\u2014 ; and\n**(C)**\nby adding at the end the following new clauses:\n(i) the Secretary shall provide rental assistance on behalf of a veteran who is\u2014 (I) homeless; (II) at risk of homelessness; or (III) receiving assistance under another housing assistance program if the Secretary determines a voucher under this paragraph is a more appropriate form of assistance for such veteran; (ii) subject to subparagraph (D), the Secretary of Veterans Affairs shall furnish case management to a veteran described in clause (i) whom such Secretary (acting through an appropriately licensed or otherwise qualified employee of the Department of Veterans Affairs or an entity that participates in a centralized or coordinated entry system (as defined in section 578.3 of title 24, Code of Federal Regulations, or successor regulation) of the Department of Housing and Urban Development) determines requires case management; (iii) in the case of a veteran described in clause (ii) who refuses case management\u2014 (I) the Secretary of Veterans Affairs shall\u2014 (aa) make recurring attempts to engage and build a relationship with the veteran, in order to provide such case management to the veteran, solicit feedback from the veteran, and promote the veteran\u2019s housing stability and opportunities to access health care and other benefits under laws administered by the Secretary; and (bb) provide case management to such veteran if the veteran subsequently requests case management; (II) the Secretary of Housing and Urban Development may not revoke such rental assistance on behalf of the veteran solely on the basis of such refusal; (III) a public housing authority may not revoke rental assistance provided by such authority on behalf of the veteran solely on the basis of such refusal; and (IV) the owner may not evict or otherwise penalize the veteran solely on the basis of such refusal; and (iv) in the case of a veteran described in clause (ii) whose case management is suspended for the health and safety of the veteran or the case manager, the owner may not evict or otherwise penalize the veteran solely on the basis of such suspension. ;\n**(2)**\nby striking subparagraph (B);\n**(3)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (E), respectively; and\n**(4)**\nby inserting after subparagraph (B), as redesignated the following new subparagraphs:\n(C) Veterans who do not require case management A voucher made available under this paragraph may be used for a homeless veteran, or a veteran at risk of homelessness, whom the Secretary of Veterans Affairs determines does not require case management if such use is included in the notice of operating requirements of such program. (D) Administrative fees There is authorized to be appropriated such sums as may be necessary for administrative fee payments to public housing agencies for costs of administering vouchers under this paragraph and other eligible expenses, as shall be defined by notice issued by the Secretary, to facilitate the leasing of the vouchers, such as security deposit assistance and other costs related to retention and support of participating owners. .\n#### 4. GAO report on homeless veterans\n##### (a) Report required\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees a report containing the following, disaggregated by demographics (if the Comptroller General determines it appropriate)\u2014\n**(1)**\na description of the demographic characteristics of veterans served by the HUD-VASH program, disaggregated by whether the veteran is receiving services from a case manager described in section 2003(b) of title 38, United States Code, as amended by section 2 of this Act;\n**(2)**\nthe number, qualifications, and demographic characteristics of such case managers;\n**(3)**\nan assessment of the types and quality of case management services provided to veterans by case managers described in section 2003(b) of title 38, United States Code, as amended by section 2, disaggregated by locality;\n**(4)**\nan assessment of recruitment and retention of such case managers, disaggregated by locality and demographic characteristics; and\n**(5)**\nmetrics regarding housing stability and retention for veterans participating in Federal housing assistance programs, including veterans who have participated in more than one such program and reasons why veterans ceased to so participate.\n##### (b) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means the following:\n**(1)**\nThe Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(2)**\nThe Committee on Veterans\u2019 Affairs of the Senate.\n**(3)**\nThe Committee on Financial Services of the House of Representatives.\n**(4)**\nThe Committee on Banking, Housing, and Urban Affairs of the Senate.",
      "versionDate": "2025-03-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-04-01T15:31:59Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-04-01T15:31:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:12:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "House",
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
          "measure-id": "id119hr1957",
          "measure-number": "1957",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-08-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1957v00",
            "update-date": "2025-08-08"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>End Veteran Homelessness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish case management to certain veterans who are eligible for the HUD-Veterans Affairs Supportive Housing (HUD-VASH) program administered by the Department of Housing and Urban Development (HUD) and the VA.</p><p>Specifically, the VA must furnish case management to veterans who are eligible for HUD-VASH that the VA determines require case management. The VA must prioritize vulnerable homeless veterans in assigning case managers and providing services.</p><p>The VA must take certain actions if a veteran refuses case management. HUD or a public housing authority may not revoke assistance solely on the basis that a veteran has refused case management. Additionally, a veteran may not be evicted or penalized by the owner of a property solely on the basis that they have refused case management\u00a0or cannot be provided case management for health and safety reasons.</p><p>The Government Accountability Office must report to Congress on veterans who are served by the\u00a0HUD-VASH program, case managers and case management services provided under the program, and metrics about housing stability for veterans participating in federal housing assistance programs.</p><p>The bill also provides statutory authority to expand eligibility for the HUD-VASH program to any veteran who is homeless, at risk of homelessness, or receiving assistance under another housing assistance program if the VA determines a voucher under HUD-VASH is more appropriate. (Currently, assistance is statutorily limited to certain veterans who have chronic mental illness or substance use disorders.)</p>"
        },
        "title": "End Veteran Homelessness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1957.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Veteran Homelessness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish case management to certain veterans who are eligible for the HUD-Veterans Affairs Supportive Housing (HUD-VASH) program administered by the Department of Housing and Urban Development (HUD) and the VA.</p><p>Specifically, the VA must furnish case management to veterans who are eligible for HUD-VASH that the VA determines require case management. The VA must prioritize vulnerable homeless veterans in assigning case managers and providing services.</p><p>The VA must take certain actions if a veteran refuses case management. HUD or a public housing authority may not revoke assistance solely on the basis that a veteran has refused case management. Additionally, a veteran may not be evicted or penalized by the owner of a property solely on the basis that they have refused case management\u00a0or cannot be provided case management for health and safety reasons.</p><p>The Government Accountability Office must report to Congress on veterans who are served by the\u00a0HUD-VASH program, case managers and case management services provided under the program, and metrics about housing stability for veterans participating in federal housing assistance programs.</p><p>The bill also provides statutory authority to expand eligibility for the HUD-VASH program to any veteran who is homeless, at risk of homelessness, or receiving assistance under another housing assistance program if the VA determines a voucher under HUD-VASH is more appropriate. (Currently, assistance is statutorily limited to certain veterans who have chronic mental illness or substance use disorders.)</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119hr1957"
    },
    "title": "End Veteran Homelessness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Veteran Homelessness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish case management to certain veterans who are eligible for the HUD-Veterans Affairs Supportive Housing (HUD-VASH) program administered by the Department of Housing and Urban Development (HUD) and the VA.</p><p>Specifically, the VA must furnish case management to veterans who are eligible for HUD-VASH that the VA determines require case management. The VA must prioritize vulnerable homeless veterans in assigning case managers and providing services.</p><p>The VA must take certain actions if a veteran refuses case management. HUD or a public housing authority may not revoke assistance solely on the basis that a veteran has refused case management. Additionally, a veteran may not be evicted or penalized by the owner of a property solely on the basis that they have refused case management\u00a0or cannot be provided case management for health and safety reasons.</p><p>The Government Accountability Office must report to Congress on veterans who are served by the\u00a0HUD-VASH program, case managers and case management services provided under the program, and metrics about housing stability for veterans participating in federal housing assistance programs.</p><p>The bill also provides statutory authority to expand eligibility for the HUD-VASH program to any veteran who is homeless, at risk of homelessness, or receiving assistance under another housing assistance program if the VA determines a voucher under HUD-VASH is more appropriate. (Currently, assistance is statutorily limited to certain veterans who have chronic mental illness or substance use disorders.)</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119hr1957"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1957ih.xml"
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
      "title": "End Veteran Homelessness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Veteran Homelessness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, and the United States Housing Act of 1937, to make certain improvements to the supported housing program for veterans commonly known as \"HUD-VASH\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:21Z"
    }
  ]
}
```
