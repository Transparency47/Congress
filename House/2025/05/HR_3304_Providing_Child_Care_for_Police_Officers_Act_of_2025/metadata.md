# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3304?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3304
- Title: Providing Child Care for Police Officers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3304
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-21T08:07:48Z
- Update date including text: 2026-05-21T08:07:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3304",
    "number": "3304",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Providing Child Care for Police Officers Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:48Z",
    "updateDateIncludingText": "2026-05-21T08:07:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-08T13:06:30Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "WA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "FL"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NH"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AZ"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "WA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CO"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MO"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NJ"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "GU"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
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
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "VA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "OH"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3304ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3304\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Peters (for himself, Mr. Valadao , Mr. Harder of California , and Mr. Issa ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant pilot program to provide child care services for the minor children of law enforcement officers to accommodate the shift work and nontraditional work hours of such officers, and to enhance recruitment and retention of such officers.\n#### 1. Short title\nThis Act may be cited as the Providing Child Care for Police Officers Act of 2025 .\n#### 2. Child care grant program to support law enforcement\n##### (a) Establishment\nThe Secretary of Health and Human Services, acting through the Assistant Secretary of the Administration for Children and Families, shall establish a program to award grants to lead agencies, on a competitive basis, to assist lead agencies in providing funds to encourage the establishment and operation of child care programs to provide child care services for the minor children of law enforcement officers during the shift work and nontraditional work hours of such officers.\n##### (b) Application\nTo be eligible to receive a grant under this section, a lead agency shall prepare and submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including an assurance that the funds required under subsection (f) will be provided.\n##### (c) Period of grant\nThe Secretary shall award a grant under this section for a period of 3 years.\n##### (d) Set-Aside\nOf the amount appropriated to carry out this section for a fiscal year, not less than 20 percent shall be used to award grants under this section to lead agencies to provide funds to\u2014\n**(1)**\na law enforcement agency that employs fewer than 200 full-time law enforcement officers; or\n**(2)**\na consortium comprised of law enforcement agencies, one of which employs fewer than 200 such officers.\n##### (e) Use of funds\n**(1) In general**\nA lead agency shall use a grant awarded under this section to provide funds to covered entities located in the State, territory, or Tribal land of the lead agency to enable the covered entities to establish and operate child care programs (directly or by contract with child care providers). Such funds may be used by the covered entity or (through such a contract) child care provider to provide assistance that may include\u2014\n**(A)**\nassistance for the startup costs related to a child care program;\n**(B)**\nassistance for the training of child care providers;\n**(C)**\nassistance for law enforcement agencies to provide financial assistance for child care costs for families;\n**(D)**\nassistance for the provision of services to care for sick children or to provide care to children;\n**(E)**\nassistance through contracts entered into by law enforcement agencies with local child care resource and referral organizations or local health departments;\n**(F)**\nassistance for care for children with disabilities;\n**(G)**\nassistance to maintain nonstandard hours for expanded hours of child care;\n**(H)**\nassistance for payment of expenses for operation, construction, or renovation of a child care facility; or\n**(I)**\nassistance for any other relevant activity determined appropriate by the lead agency.\n**(2) Application**\nIn order for a covered entity to be eligible to receive funds from a lead agency under this section, the covered entity or, if the entity is a consortium including a unit of local government, the unit of local government involved, shall prepare and submit to the lead agency an application at such time, in such manner, and containing such information as the lead agency may require.\n**(3) Limitations**\nWith respect to grant funds received under this section, a lead agency may not provide in excess of $3,000,000 from such funds to any single applicant.\n##### (f) Matching requirement\nTo be eligible to receive a grant under this section, a lead agency shall provide assurances to the Secretary that, with respect to the costs to be incurred by a covered entity receiving funds in carrying out activities under this section, the covered entity will make available (directly or through donations from public or private entities) non-Federal contributions for such costs in an amount equal to\u2014\n**(1)**\nfor the first fiscal year for which the covered entity receives such funds, not less than 10 percent of such costs;\n**(2)**\nfor the second fiscal year for which the covered entity receives such funds, not less than 25 percent of such costs; and\n**(3)**\nfor the third fiscal year for which the covered entity receives such funds, not less than 33 2/3 percent of such costs.\n##### (g) Requirements of providers\nTo be eligible to receive assistance under a grant awarded under this section, a child care provider shall meet the definitions of, and requirements specified in, each of the following:\n**(1)**\nSection 658P(6) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n(6) ).\n**(2)**\nSection 98.41 of title 45, Code of Federal Regulations (or successor regulations).\n**(3)**\nSection 98.43 of title 45, Code of Federal Regulations (or successor regulations).\n##### (h) Administration\n**(1) Lead agency**\nA lead agency shall, with respect to administering a grant awarded under this section, have the duties described in section 658D(b) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858b(b) ). A lead agency shall have the responsibility for administering a grant awarded under this section and for monitoring use of funds and adherence to health and safety requirements by covered entities and child care providers that receive funds under such grant.\n**(2) Technical assistance**\nA lead agency administering a grant awarded under this section shall, for the duration of the period of such grant, provide to covered entities technical assistance regarding such grant.\n**(3) Audits**\nA lead agency shall require each covered entity receiving funds under a grant awarded under this section, and any child care provider receiving funds through the covered entity, to conduct an annual audit with respect to the activities of the covered entity and the child care provider. Such audits shall be submitted to the lead agency.\n**(4) Misuse of funds**\n**(A) Repayment**\nIf the lead agency determines, through an audit or otherwise, that a covered entity or child care provider receiving funds under a grant awarded under this section has misused the funds, the lead agency shall notify the Secretary of the misuse. The Secretary, upon such a notification, may seek from such covered entity or child care provider the repayment of an amount equal to the amount of any such misused funds plus interest.\n**(B) Appeals process**\nThe Secretary shall by regulation provide for an appeals process with respect to repayments under this paragraph.\n**(5) 2-year study**\n**(A) In general**\nNot later than 2 years after the date on which the Secretary first awards grants under this section, the Secretary shall conduct a study to determine\u2014\n**(i)**\nthe capacity of covered entities, and child care providers receiving funds through such a grant, to meet the child care needs of communities within States;\n**(ii)**\nthe kinds of consortia that are being formed with respect to child care at the local level to carry out programs funded under this section; and\n**(iii)**\nwho is using the programs funded under this section and the income levels of such individuals.\n**(B) Report**\nNot later than 28 months after the date on which the Secretary first awards grants under this section, the Secretary shall prepare and submit to the appropriate committees of Congress a report on the results of the study conducted in accordance with subparagraph (A).\n**(6) Four-year study**\n**(A) In general**\nNot later than 4 years after the date on which the Secretary first awards grants under this section, the Secretary shall conduct a study to determine\u2014\n**(i)**\nthe number of child care facilities that\u2014\n**(I)**\nreceive funds for construction or renovation through covered entities that received funds through a grant awarded under this section; and\n**(II)**\nremain in operation;\n**(ii)**\nthe extent to which such facilities are meeting the child care needs of the individuals served by such facilities; and\n**(iii)**\nthe extent to which other sectors of first responders, as defined in section 3025 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10705 ), have unmet child care needs.\n**(B) Report**\nNot later than 52 months after the date on which the Secretary first awards grants under this section, the Secretary shall prepare and submit to the appropriate committees of Congress a report on the results of the study conducted in accordance with subparagraph (A).\n##### (i) Definitions\nIn this section:\n**(1) Consortium**\nThe term consortium means a partnership that includes one or more law enforcement agencies and may also include a unit of local government, a child care provider, or a foundation.\n**(2) Covered entity**\nThe term covered entity means a law enforcement agency or a consortium.\n**(3) Eligible child care provider**\nThe term eligible child care provider has the meaning given the term in section 658P(6) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n(6) ).\n**(4) Law enforcement agency**\nThe term law enforcement agency means a government agency with criminal or civil law enforcement powers.\n**(5) Law enforcement officer**\nThe term law enforcement officer has the meaning given the term in section 2503 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10533 ).\n**(6) Lead agency**\nThe term lead agency means an agency or office designated or established under section 658D(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858b ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Health and Human Services, acting through the Assistant Secretary of the Administration for Children and Families.\n**(8) State**\nThe term State means\u2014\n**(A)**\neach of the several States of the United States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe territories of the United States; and\n**(D)**\nan Indian Tribe or Tribal organization (as such terms are defined in section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n )).\n##### (j) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section, $24,000,000 for each of fiscal years 2026 through 2030.\n**(2) Studies and administration**\nWith respect to the total amount appropriated for the period of fiscal years 2026 through 2030 in accordance with this subsection, not more than $2,500,000 of that amount may be used for expenditures related to conducting studies required under, and the administration of, this section.\n##### (k) Termination of program\nThe program established under this section shall terminate on September 30, 2030.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-07-17",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2337",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Providing Child Care for Police Officers Act of 2025",
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
        "name": "Families",
        "updateDate": "2025-05-22T17:26:34Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3304ih.xml"
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
      "title": "Providing Child Care for Police Officers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Child Care for Police Officers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant pilot program to provide child care services for the minor children of law enforcement officers to accommodate the shift work and nontraditional work hours of such officers, and to enhance recruitment and retention of such officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:18:21Z"
    }
  ]
}
```
