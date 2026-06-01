# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4105
- Title: VET Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4105
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-05-21T08:07:31Z
- Update date including text: 2026-05-21T08:07:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-01-21 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-01-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4105",
    "number": "4105",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "VET Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:31Z",
    "updateDateIncludingText": "2026-05-21T08:07:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-21",
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
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-06-24",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:01:00Z",
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
                "date": "2026-01-21T14:11:01Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-19T19:00:39Z",
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
          "date": "2025-06-24T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "PA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "TX"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NM"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NV"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4105ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4105\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mrs. Kiggans of Virginia (for herself, Ms. Houlahan , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans\u2019 Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to direct the Secretary of Labor to carry out a grant program to help certain members of the Armed Forces, veterans, and their spouses, obtain employment in the energy industry.\n#### 1. Short title\nThis Act may be cited as the Veterans Energy Transition Act of 2025 or the VET Act of 2025 .\n#### 2. Establishment of grant program to help certain members of the Armed Forces, veterans, and their spouses obtain employment in the energy industry\n##### (a) Repeal of expired authorities\nSections 1152 and 1153 of title 10, United States Code, are repealed.\n##### (b) Establishment\nChapter 58 of such title is amended by inserting, after section 1151, the following new section 1152:\n1152. Assistance to separating members, veterans, and spouses to obtain employment in the energy industry (a) Establishment The Secretary of Labor, in consultation with the Transition Executive Committee, shall carry out a program to provide grants to eligible entities that hire covered individuals. (b) Covered individuals (1) An covered individual under this section is\u2014 (A) a member of the Armed Forces eligible for preseparation counseling under section 1142 of this title; (B) a veteran; or (C) a spouse of such a member or veteran. (2) In the selection of covered individuals for assistance under a grant agreement under this section, preference shall be given to a covered individual (or the spouse of a covered individual) who\u2014 (A) is involuntarily separated, approved for separation under section 1174a or 1175 of this title, or retires pursuant to the authority provided in section 4403 of the Defense Conversion, Reinvestment, and Transition Assistance Act of 1992 (division D of Public Law 102\u2013484 ; 10 U.S.C. 1293 note); (B) has a military occupational specialty, training, or experience related to energy production, construction, or manufacturing, or meets other criteria prescribed by the Secretary; (C) resides in a qualified opportunity zone; or (D) has a service-connected disability, is a homeless veteran, or faces another significant barrier to employment. (c) Eligible entities (1) An entity is eligible for a grant under this section if the primary function of such entity is any of the following: (A) The generation, transmission, storage, or distribution of energy. (B) The manufacture or distribution of equipment and components critical to the energy industry. (2) In the selection of eligible entities for a grant under this section, preference shall be given to an eligible entity that\u2014 (A) operates in a qualified opportunity zone; or (B) is a small business concern. (d) Grant funds: authorized uses; maximum amounts (1) Grant funds awarded under this section shall be used to reimburse a grantee for costs incurred by such grantee in the course of hiring a covered individual. Such costs may include the following: (A) Costs for the relevant licensure, certification, training, or education of the eligible employee. (B) Recruitment costs. (C) Orientation, administrative, and relocation costs. (2) In any fiscal year, a grantee may not be awarded\u2014 (A) more than $10,000 per covered individual hired by such grantee; and (B) more than $500,000 under this section. (e) Terms As a condition of receiving a grant under this section, an eligible entity shall agree to\u2014 (1) submit to the Secretary a report for each fiscal year in which the grantee receives funds under such grant that includes information regarding\u2014 (A) use of grant funds; (B) whether a covered individual is still employed by such eligible entity; (C) the rates of retention and employee satisfaction of covered individuals employed by such eligible entity; and (D) the salaries and benefits paid by such eligible entity to covered individuals; (2) comply with an audit by the Inspector General of the Department of Labor or the Comptroller General of the United States; and (3) repay the Federal Government any grant funds used by the eligible entity for any purpose not described in subsection (d)(1). (f) Coordination with existing programs (1) The Secretary of Labor shall coordinate with the Secretaries of Defense and Veterans Affairs regarding the grant program under this section and other programs for members separating from active duty, including\u2014 (A) the Transition Assistance Program under sections 1142 and 144 of this title; (B) Skillbridge under section 1143(e) of this title; and (C) the Solid Start program under section 6320 of title 38. (2) In the course of such coordination, the Secretaries shall\u2014 (A) seek to avoid the duplication of services to covered individuals under such programs; (B) promote the grant program under this section to covered individuals; and (C) submit to the appropriate congressional committees, not less than once each fiscal year in which the Secretary of Labor carries out such grant program, a report regarding such coordination. (g) Report Not later than September 30, 2030, the Secretary of Labor shall submit to Congress a report containing the evaluation of the Secretary of the grant program under this section. Such report shall include the recommendation of the Secretary whether to expand, extend, or otherwise amend the grant program. (h) Authorization of appropriations; administrative costs (1) There is authorized to be appropriated to the Department of Labor, to carry out this section, $60,000,000 for each of fiscal years 2026 through 2031. (2) In a fiscal year, the Secretary may not spend more than 15 percent of the funds appropriated to carry out this section on administrative costs. (i) Definitions In this section: (1) The term appropriate congressional committee means the following: (A) The Committee on Armed Services of the House of Representatives. (B) The Committee on Veterans\u2019 Affairs of the House of Representatives. (C) The Committee on Education and Workforce of the House of Representatives. (D) The Committee on Armed Services of the Senate. (E) The Committee on Veterans\u2019 Affairs of the Senate. (F) The Committee on Health, Education, Labor, and Pensions of the Senate. (2) The term equipment and components critical to the energy industry includes the following: (A) Batteries. (B) Solar energy components. (C) Wind energy components. (D) Nuclear energy components. (E) Electronics. (F) Control systems. (G) Transformers. (H) Fuel cell technologies. (I) Advanced materials. (3) The term homeless veteran has the meaning given such term in section 2002 of title 38. (4) The term qualified opportunity zone has the meaning given such term in section 1400Z\u20131 of the Internal Revenue Code of 1986 ( 26 U.S.C. 1400Z\u20131 ). (5) The terms service-connected and veteran have the meanings given such terms in section 101 of title 38. (6) The term small business concern has the meaning given such term in section 3 of the Small Business Act ( Public Law 85\u2013536 ; 15 U.S.C. 632 ). (7) The term Transition Executive Committee means the subordinate committee, established under section 320(b)(2) of title 38, of the Veterans Affairs-Department of Defense Joint Executive Committee. .\n##### (c) Coordination plans\nThe Secretary of Labor shall submit to the appropriate congressional committees, as such term is defined in section (i) of section 1152 of such title, as added by this section, a report regarding\u2014\n**(1)**\nthe initial plan of the Secretary to coordinate under subsection (f) of such section not later than 180 days after the date of the enactment of this Act; and\n**(2)**\nthe final such plan not later than one year after such date.",
      "versionDate": "2025-06-24",
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
            "name": "Accounting and auditing",
            "updateDate": "2026-03-16T18:16:13Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-16T18:16:20Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-03-16T18:16:27Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-03-16T18:18:35Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-03-16T18:18:40Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-03-16T18:18:17Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-16T18:16:09Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2026-03-16T18:18:30Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-03-16T18:16:04Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-03-16T18:15:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-29T20:30:54Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4105ih.xml"
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
      "title": "VET Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VET Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Energy Transition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to direct the Secretary of Labor to carry out a grant program to help certain members of the Armed Forces, veterans, and their spouses, obtain employment in the energy industry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T13:48:23Z"
    }
  ]
}
```
