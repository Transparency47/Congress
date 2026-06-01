# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1826
- Title: Child Care Workforce Act
- Congress: 119
- Bill type: HR
- Bill number: 1826
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-05-01T08:08:50Z
- Update date including text: 2026-05-01T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1826",
    "number": "1826",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Child Care Workforce Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:50Z",
    "updateDateIncludingText": "2026-05-01T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "KS"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
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
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VA"
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
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1826ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1826\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Carbajal (for himself, Mr. Lawler , Ms. Davids of Kansas , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo implement or strengthen programs that increase the supply of quality child care services by enhancing the wages of child care workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Child Care Workforce Act .\n#### 2. Purpose\nThe purpose of this Act is to establish a pilot program to increase the supply of quality child care services by providing funding to States, Indian Tribes, and Tribal organizations to implement or strengthen programs to supplement the wages of eligible child care workers, in order to\u2014\n**(1)**\nattract and retain eligible child care workers;\n**(2)**\nimprove eligible child care worker well-being;\n**(3)**\nimprove the quality of child care services; and\n**(4)**\nincrease the availability of affordable child care services.\n#### 3. Definitions\nIn this Act:\n**(1) Child care worker**\nThe term child care worker means any individual whose primary and daily focus of work is\u2014\n**(A)**\nproviding child care services, including direct care and education services, to children for a family child care provider or other child care provider, or a provider of early childhood education, that is in compliance with any licensing or registration standards, or regulations, of the State, Indian Tribe, or Tribal organization involved; and\n**(B)**\nproviding the child care services in a center-based or home-based setting.\n**(2) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(3) State**\nThe term State means any of the several States, the District of Columbia, the Virgin Islands of the United States, the Commonwealth of Puerto Rico, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n**(4) Tribal organization**\nThe term Tribal organization has the meaning given the term tribal organization in section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ).\n#### 4. Pilot program\n##### (a) Establishment\nThe Secretary of Health and Human Services (referred to in this Act as the Secretary ) shall establish a pilot program to award competitive grants to States, Indian Tribes, and Tribal organizations to supplement the wages of eligible child care workers.\n##### (b) Considerations\nIn selecting States, Indian Tribes, and Tribal organizations to receive grants under this section, the Secretary shall consider\u2014\n**(1)**\nthe number of children under the age of 5 residing in the State or on the Tribal land of the Indian Tribe or Tribal organization;\n**(2)**\nthe number of child care workers working in licensed, regulated, or registered programs in the State or on the Tribal land;\n**(3)**\nthe average wage of child care workers working in the State or on the Tribal land;\n**(4)**\nthe percentage of families in the State or on the Tribal land who are eligible for child care subsidies under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) but do not receive the subsidies; and\n**(5)**\nthe need for additional child care workers in the State or on the Tribal land.\n##### (c) Eligibility\nTo be eligible for a grant under this section, a State, Indian Tribe, or Tribal organization shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including\u2014\n**(1)**\ninformation showing a significant need for increased numbers of child care workers and increased wages among child care workers;\n**(2)**\na commitment to using the grant funds to supplement the wages of low-wage eligible child care workers;\n**(3)**\na plan for using the grant funds to supplement the wages of eligible child care workers, including\u2014\n**(A)**\nthe criteria that will be used to determine which child care workers are eligible to receive the wage supplements;\n**(B)**\na description of how funds will be prioritized for areas with greatest need, including areas with overall staffing challenges, underserved geographic areas, areas with shortages of programs that serve low-income children and families, and areas with shortages of programs that serve infants and toddlers, that serve children with disabilities, or that offer child care services during nontraditional hours; and\n**(C)**\na description of how the wage supplements will be provided to eligible child care workers (directly, through the employer, or through a trusted intermediary) and how the supplements will be provided in a timely manner;\n**(4)**\na plan to engage in a public awareness campaign directed at eligible child care workers;\n**(5)**\na description of the measures that will be used to assess the impact of the wage supplement pilot program on attraction and retention of eligible child care workers, eligible child care worker well-being, child care services quality, and availability of affordable child care services, provided by eligible child care workers;\n**(6)**\na description of how the pilot program will contribute to the State\u2019s or Tribe\u2019s overall plan for increasing eligible child care worker compensation;\n**(7)**\na description of the plan for addressing and minimizing any destabilization that may occur after the grant funds are expended; and\n**(8)**\nsuch other information as the Secretary may require.\n#### 5. Use of funds\n##### (a) In general\nExcept as provided in subsection (c), a State, Indian Tribe, or Tribal organization that receives a grant under section 4 shall use the grant funds solely to supplement the wages of eligible child care workers.\n##### (b) Requirements\nIn carrying out subsection (a), a State, Indian Tribe, or Tribal organization shall\u2014\n**(1)**\ndisburse the wage supplements to eligible child care workers not less frequently than quarterly;\n**(2)**\ntarget grant funding based on the areas described in section 4(c)(3)(B);\n**(3)**\nprovide to eligible child care workers education on any effect the wage supplements may have on taxes or public benefit eligibility; and\n**(4)**\ninform eligible child care workers that acceptance, of the wage supplements, is voluntary.\n##### (c) Administrative costs\nThe State, Indian Tribe, or Tribal organization may use not more than 10 percent of the grant funds to pay for administrative costs associated with the administration of payments to eligible child care workers, financial counseling for eligible child care workers, including as described in subsection (b)(3), and public awareness campaigns to make child care workers aware of the availability of such payments.\n#### 6. Evaluation\nThe Secretary shall conduct an evaluation of the pilot program to assess its effectiveness in\u2014\n**(1)**\nattracting and retaining eligible child care workers;\n**(2)**\nimproving eligible child care worker well-being and the quality of child care services; and\n**(3)**\nincreasing the availability of affordable child care services.\n#### 7. Report\nNot later than 2 years after the date on which the pilot program is implemented, the Secretary shall submit a report to Congress containing the results of the evaluation.\n#### 8. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary for fiscal year 2025 and each subsequent fiscal year.\n#### 9. Effective date\nThis Act shall take effect 75 days after the date of enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "actionDate": "2026-03-19",
        "text": "Committee on Health, Education, Labor, and Pensions. Hearings held."
      },
      "number": "846",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Child Care Workforce Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child care and development",
            "updateDate": "2026-04-06T15:30:07Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T15:30:07Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2026-04-06T15:30:07Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-04-06T15:30:07Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-04-06T15:30:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-03-21T18:27:59Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1826ih.xml"
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
      "title": "Child Care Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To implement or strengthen programs that increase the supply of quality child care services by enhancing the wages of child care workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:06Z"
    }
  ]
}
```
