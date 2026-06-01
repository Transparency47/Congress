# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1671?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1671
- Title: Justice for Vaccine Injured Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1671
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-02T17:48:58Z
- Update date including text: 2025-09-02T17:48:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1671",
    "number": "1671",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Justice for Vaccine Injured Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-02T17:48:58Z",
    "updateDateIncludingText": "2025-09-02T17:48:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:00:23Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:02:45Z",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KY"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AZ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1671ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1671\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Davidson (for himself, Mr. Nehls , Mr. Massie , Mrs. Miller of Illinois , Mr. Gosar , Mr. Weber of Texas , and Mr. Fallon ) introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 38, United States Code, to provide for a presumption of service-connection under the laws administered by the Secretary of Veterans Affairs for certain diseases associated with the COVID\u201319 vaccine that become manifest during the one-year period following the receipt of the vaccine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Vaccine Injured Veterans Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOn August 24, 2021, Secretary of Defense Lloyd Austin issued a memorandum titled, Mandatory Coronavirus Disease 2019 Vaccination of Department of Defense Service Members .\n**(2)**\nThis memorandum stated, I therefore direct the Secretaries of the Military Departments to immediately begin full vaccination of all members of the Armed Forces under DoD authority on active duty or in the Ready Reserve, including the National Guard, who are not fully vaccinated against COVID\u201319 .\n**(3)**\nIn December 2022, the Department of Defense reported that 98 percent of active duty service members and 96 percent of the total force have been vaccinated from COVID\u201319.\n**(4)**\nAs a result of this memorandum, more than 8,400 members of the Armed Forces were forced out of the military for refusing to get the COVID\u201319 vaccine.\n**(5)**\nOn January 10, 2023, Secretary Austin was forced to rescind this memorandum as a requirement of section 525 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ).\n##### (b) Sense of Congress\nIt is the sense of Congress that the actions referred to in subsection (a) that were taken by the Department of Defense under the Biden administration caused irreparable harm to the health and readiness of the United States Armed Forces.\n#### 3. Department of Veterans Affairs presumption of service-connection for certain diseases associated with COVID\u201319 vaccine\n##### (a) In general\nSubchapter II of chapter 11 of title 38, United States Code, is amended by adding at the end the following new section:\n1120A. Presumption of service-connection for certain diseases associated with COVID\u201319 vaccine (a) In general For the purposes of section 1110 of this title, and subject to section 1113 of this title, a disease specified in subsection (b) becoming manifest in a member of the Armed Forces who, during the period beginning on August 24, 2021, and ending on January 10, 2023, received a COVID\u201319 vaccine under orders shall be considered to have been incurred in or aggravated during active military, naval, air, or space service, notwithstanding that there is no record of evidence of such disease during the period of such service. (b) Covered diseases The diseases specified in this subsection are the following: (1) Myocarditis. (2) Pericarditis. (3) Thrombosis with thrombocytopenia syndrome. (4) Guillian-Barre Syndrome. (5) Any other disease for which the Secretary determines that a presumption of service connection is warranted based on a positive association with the COVID\u201319 vaccine. (c) Congressional notice requirement If the Secretary determines that an additional disease should be specified pursuant to subsection (b)(4), the Secretary shall submit to the Committees on Veterans Affairs\u2019 of the Senate and the House of Representatives notice of such determination. (d) Report Not later than 60 days after the date of enactment of the Justice for Vaccine Injured Veterans Act of 2025 , and every 60 days thereafter for the subsequent four year-period, the Secretary shall submit to the Committees of Veterans\u2019 Affairs of the Senate and the House of Representatives a report that contains each of the following: (1) The total number of claims for compensation under this chapter related to a disease associated with the COVID\u201319 vaccine. (2) The status of each such claim, disaggregated by\u2014 (A) the number of claims that were approved; (B) the number of claims that were denied and for which the claimant took no further action; (C) the number of claims that were denied and for which the claimant filed a supplemental claim; (D) the number of claims that were denied and for which the claimant requested a higher level review; and (E) the number of claims that were denied and for which the claimant filed an appeal to the Board of Veterans\u2019 Appeals. (3) The total number of such claims that, as of the date of the submission of the report, had been submitted but were pending a decision. (e) Public access to reports The Secretary shall make each report required by subsection (d) publicly available, including by making publicly available on an appropriate website of the Department each such report together with such additional information or comments as the Secretary considers appropriate to provide context for the report. (f) COVID\u201319 vaccine defined In this section, the term COVID\u201319 vaccine means vaccine licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) or authorized for emergency use under section 564 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20133 ) for immunization against the virus responsible for COVID\u201319. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1120 the following new item:\n1120A. Presumption of service-connection for certain diseases associated with COVID\u201319 vaccine. .",
      "versionDate": "2025-02-27",
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-09-02T17:48:31Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T17:48:41Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-02T17:48:46Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-09-02T17:48:20Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-09-02T17:48:35Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-09-02T17:48:58Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-09-02T17:48:53Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-09-02T17:48:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T18:07:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1671",
          "measure-number": "1671",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-07-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1671v00",
            "update-date": "2025-07-15"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Justice for Vaccine Injured Veterans Act of 2025</strong></p><p>This bill establishes a presumption of service-connection for certain conditions that become manifest in a member of the Armed Forces who received a COVID-19 vaccine under orders any time from August 24, 2021, through January 10, 2023. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Specifically, the bill establishes a presumption of service-connection, regardless of whether there is a record of evidence of the condition during a servicemember's\u00a0period of service, for myocarditis, pericarditis, thrombosis with thrombocytopenia syndrome, Guillain-Barre Syndrome, and any other condition the Department of Veterans Affairs (VA) determines is warranted based on a positive association with the COVID-19 vaccine. Under the bill, if the VA determines an additional condition should be specified, it must submit a notice of such determination to Congress.</p><p>The VA must also report to Congress every 60 days for four\u00a0years regarding claims for compensation related to a condition associated with the COVID-19 vaccine. Such reports must be made publicly available.</p>"
        },
        "title": "Justice for Vaccine Injured Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1671.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for Vaccine Injured Veterans Act of 2025</strong></p><p>This bill establishes a presumption of service-connection for certain conditions that become manifest in a member of the Armed Forces who received a COVID-19 vaccine under orders any time from August 24, 2021, through January 10, 2023. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Specifically, the bill establishes a presumption of service-connection, regardless of whether there is a record of evidence of the condition during a servicemember's\u00a0period of service, for myocarditis, pericarditis, thrombosis with thrombocytopenia syndrome, Guillain-Barre Syndrome, and any other condition the Department of Veterans Affairs (VA) determines is warranted based on a positive association with the COVID-19 vaccine. Under the bill, if the VA determines an additional condition should be specified, it must submit a notice of such determination to Congress.</p><p>The VA must also report to Congress every 60 days for four\u00a0years regarding claims for compensation related to a condition associated with the COVID-19 vaccine. Such reports must be made publicly available.</p>",
      "updateDate": "2025-07-15",
      "versionCode": "id119hr1671"
    },
    "title": "Justice for Vaccine Injured Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for Vaccine Injured Veterans Act of 2025</strong></p><p>This bill establishes a presumption of service-connection for certain conditions that become manifest in a member of the Armed Forces who received a COVID-19 vaccine under orders any time from August 24, 2021, through January 10, 2023. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Specifically, the bill establishes a presumption of service-connection, regardless of whether there is a record of evidence of the condition during a servicemember's\u00a0period of service, for myocarditis, pericarditis, thrombosis with thrombocytopenia syndrome, Guillain-Barre Syndrome, and any other condition the Department of Veterans Affairs (VA) determines is warranted based on a positive association with the COVID-19 vaccine. Under the bill, if the VA determines an additional condition should be specified, it must submit a notice of such determination to Congress.</p><p>The VA must also report to Congress every 60 days for four\u00a0years regarding claims for compensation related to a condition associated with the COVID-19 vaccine. Such reports must be made publicly available.</p>",
      "updateDate": "2025-07-15",
      "versionCode": "id119hr1671"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1671ih.xml"
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
      "title": "Justice for Vaccine Injured Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for Vaccine Injured Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for a presumption of service-connection under the laws administered by the Secretary of Veterans Affairs for certain diseases associated with the COVID-19 vaccine that become manifest during the one-year period following the receipt of the vaccine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:19:18Z"
    }
  ]
}
```
