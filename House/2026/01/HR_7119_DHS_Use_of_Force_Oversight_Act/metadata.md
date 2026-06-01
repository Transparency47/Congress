# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7119
- Title: DHS Use of Force Oversight Act
- Congress: 119
- Bill type: HR
- Bill number: 7119
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-16T08:07:03Z
- Update date including text: 2026-05-16T08:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-01-16 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-01-16 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7119",
    "number": "7119",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "DHS Use of Force Oversight Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:03Z",
    "updateDateIncludingText": "2026-05-16T08:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Homeland Security, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-01-16T21:03:49Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2026-01-16T21:03:49Z",
                "name": "Referred to"
              }
            },
            "name": "Oversight, Investigations, and Accountability Subcommittee",
            "systemCode": "hshm09"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-15T14:02:35Z",
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
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "RI"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MS"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "LA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MD"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "AL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NC"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "OH"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CT"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WI"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "GA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7119ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7119\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mrs. Ramirez (for herself, Mr. Magaziner , Mr. Thompson of Mississippi , Ms. Norton , Mr. Thanedar , Mr. Carter of Louisiana , Ms. Elfreth , Ms. Crockett , Mr. Green of Texas , Mr. Krishnamoorthi , Mr. Goldman of New York , Ms. Sewell , Ms. Garcia of Texas , Mrs. Foushee , Ms. Schakowsky , Mr. Jackson of Illinois , Mr. Neguse , Mrs. Beatty , and Mr. Larson of Connecticut ) introduced the following bill; which was referred to the Committee on Homeland Security , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Homeland Security Act of 2002 to require a policy on use of force and deescalation by law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DHS Use of Force Oversight Act .\n#### 2. DHS policy on use of force\n##### (a) In general\nSubtitle H of Title VII of the Homeland Security Act of 2002 ( 6 U.S.C. 341 et seq. ) is amended by adding at the end the following new section:\n890E. Use of force policy (a) In general The Secretary shall implement a Department-wide policy on the use of force by law enforcement officers and agents of the Department to ensure such officers and agents\u2014 (1) use only the amount of force that is objectively reasonable in light of the totality of the circumstances; (2) when feasible, prior to the application of force, attempt to identify themselves and issue a verbal warning to comply with such officer or agent\u2019s instructions; (3) seek to employ tactics and techniques that\u2014 (A) effectively bring an incident under control, while promoting the safety of such officers or agents and the public; and (B) minimize the risk of unintended injury or serious property damage; and (4) are prohibited from using chokeholds and carotid restraints as a means to control non-compliant persons resisting arrest. (b) Requirements The Department-wide policy under subsection (a) shall\u2014 (1) specify in a clear and consistent manner that deescalation is preferred; (2) require law enforcement officers or agents of the Department to complete initial and recurrent training in the full range of use of force tactics and techniques, including deescalation; (3) require the head of each component of the Department with such officers or agents to\u2014 (A) designate an individual, having subject matter expertise relating to the use of force, training, and the application of use of force tactics and techniques, including deescalation, to be responsible for ensuring compliance with such policy; and (B) maintain a use of force review council or committee, the members of which shall have subject matter expertise described in subparagraph (A) to perform internal analysis of use of force incidents to\u2014 (i) inform training, tactics, and techniques, and develop recommendations for improvements to such policy; and (ii) identify trends and lessons learned to be shared within each such component and across the Department. (c) Reporting (1) In general The Secretary shall carry out the following: (A) Issue requirements for the head of each component of the Department to collect and maintain consistent data relating to the use of force within each such component necessary to publish the reports required under subparagraph (B). (B) Publish, every six months, a report on the website of the Department that includes data relating to each incident during the previous six-month period in which force was used by a law enforcement officer or agent of the Department in any of the following circumstances: (i) Such use of force caused any injury or death to\u2014 (I) such an officer or agent; or (II) a person. (ii) Such use of force included deadly force against a person, including when a firearm is discharged at a person. (iii) Such use of force included a less-than-lethal device or canine that was intentionally deployed against a person. (iv) Such use of force involved a vehicle, weapon, or physical tactic or technique that delivers a kinetic impact to a person. (v) Such use of force included disabling fire against a maritime vessel or aircraft. (2) Additional elements Each report required under paragraph (1)(B) shall also include\u2014 (A) data that\u2014 (i) is disaggregated by Department component; and (ii) describes\u2014 (I) specific information on the region or jurisdiction in which each use of force incident included in such report occurred; and (II) the circumstances surrounding each such incident; and (B) a specification of whether a law enforcement officer or agent of the Department or other person was injured or killed in each such incident. (3) Summaries In conjunction with each report required under paragraph (1)(B), the Secretary shall publish a summary of any analyses under subsection (b)(3)(B) with respect to which, during the previous six-month period, final action was taken, including a summary of any findings resulting from any such analyses, including any findings relating to whether the uses of force contemplated by any such analyses complied with Federal law and Department-wide policy under subsection (a). (4) Public availability Not later than 24 hours after any use of force incident by a law enforcement officer or agent of the Department that results in the hospitalization or death of such an officer or agent or a person, the Secretary shall brief the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate and inform the public with respect to the facts ascertained relating to such incident. (5) Privacy protection Any information published or made available pursuant to this subsection shall be published or made available in a manner that protects individual privacy. (d) Office of Inspector General The Inspector General of the Department shall, on an ongoing basis, review compliance with subsections (a) and (b). .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 890D the following new item:\nSec. 890E. Use of force policy. .",
      "versionDate": "2026-01-15",
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
        "name": "Immigration",
        "updateDate": "2026-02-06T16:48:57Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7119ih.xml"
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
      "title": "DHS Use of Force Oversight Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DHS Use of Force Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to require a policy on use of force and deescalation by law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:27Z"
    }
  ]
}
```
