# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7201?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7201
- Title: Rural Service and Workforce Corps Act
- Congress: 119
- Bill type: HR
- Bill number: 7201
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-19T16:12:06Z
- Update date including text: 2026-02-19T16:12:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7201",
    "number": "7201",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Rural Service and Workforce Corps Act",
    "type": "HR",
    "updateDate": "2026-02-19T16:12:06Z",
    "updateDateIncludingText": "2026-02-19T16:12:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:07:30Z",
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
          "date": "2026-01-22T14:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7201ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7201\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Bynum introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a program to fill critical rural workforce shortages through an education assistance and loan repayment in exchange for service in designated rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Service and Workforce Corps Act .\n#### 2. Rural Service and Workforce Corps Program\n##### (a) Design\n**(1) In general**\nThe Secretary of Agriculture shall design a program to be known as the Rural Service and Workforce Corps Program , modeled after the service-for-benefits framework of the National Health Service Corps, to fill critical workforce shortages in targeted rural areas, through the provision of scholarships, tuition assistance, student loan repayment, stipends or wage support during service, and relocation and retention incentives in exchange for 3 years of service in a rural area designated by the Secretary.\n**(2) Priority employment sectors**\n**(A) In general**\nThe program shall be designed to prioritize filling workforce shortages in the following employment sectors, subject to subparagraph (B):\n**(i)**\nHealth care, including primary care, behavioral health, dental, and emergency services.\n**(ii)**\nSkilled trades, such as electricians, plumbers, heating, ventilation, and air conditioning, welding, and construction.\n**(iii)**\nEnergy infrastructure, such as lineworkers, renewable energy technicians, grid operators.\n**(iv)**\nUtilities and public works, such as water and wastewater operators and broadband technicians.\n**(v)**\nOther sectors with aging workforces, as determined by the Secretary of Labor.\n**(B) Updating**\nThe Secretary of Agriculture, in consultation with the Secretary of Labor, shall, from time to time, update the employment sectors to be prioritized under subparagraph (A), as necessary to ensure that the program prioritizes any sector facing an aging workforce and a limited recruitment pipeline.\n**(3) Targeted rural areas**\nThe program shall be designed to target any rural area\u2014\n**(A)**\ncategorized by the Economic Research Service of the Department of Agriculture as a persistent poverty county;\n**(B)**\ndesignated by the Health Resources and Services Administration of the Department of Health and Human Services as a health professional shortage area; or\n**(C)**\nin which an Indian tribal, an Alaska Native, or a Native Hawaiian community resides.\n**(4) Employer participation**\nThe program shall be designed to allow public, nonprofit, cooperative, tribal, and private employers that meet such wage and training standards as the Secretary of Agriculture shall establish, in consultation with the Secretary of Labor, to participate in the program.\n##### (b) Administration\nThe Secretary of Agriculture shall carry out the program in consultation with\u2014\n**(1)**\nthe Secretary of Education, with respect to the provision of scholarships, tuition assistance, and student loan repayment;\n**(2)**\nthe Secretary of Labor, with respect to the provision of stipends or wage support during service, and relocation and retention incentives;\n**(3)**\nthe Secretary of Health and Human Services, with respect to the health care employment sector;\n**(4)**\nthe Secretary of Energy, with respect to the energy infrastructure and utilities employment sectors; and\n**(5)**\nthe heads of other Federal departments and agencies, with respect to any matter calling for the expertise of the relevant department or agency.\n##### (c) Reports\nWithin 4 years after the date of the enactment of this Act, the Secretary of Agriculture shall prepare and submit to the Congress a written report on the implementation and effectiveness of the program provided for in this Act, which shall\u2014\n**(1)**\ninclude information, with respect to the 1st cohort subject to the 3-year service requirement under the program, on\u2014\n**(A)**\nthe number of persons in the cohort;\n**(B)**\nthe employment sectors in which a member of the cohort has been placed;\n**(C)**\nthe geographical spread of the placements;\n**(D)**\nthe types of employers referred to in subsection (a)(4) with whom a member of the cohort has been placed;\n**(E)**\nthe number of the placements; and\n**(F)**\nthe percentage of the cohort who remain in the geographic area in which placed;\n**(2)**\naddress any challenges arising from interagency coordination; and\n**(3)**\ninclude recommendations for improvements in the program.\n##### (d) Definition of rural area\nIn this section, the term rural area has the meaning given the term in subparagraph (A) of section 343(a)(13) of the Consolidated Farm and Rural Development Act, subject to subparagraphs (D) and (F) of such section.\n#### 3. Effective date\nThis Act shall take effect on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2026-01-22",
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
        "name": "Labor and Employment",
        "updateDate": "2026-02-19T16:12:06Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7201ih.xml"
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
      "title": "Rural Service and Workforce Corps Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Service and Workforce Corps Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a program to fill critical rural workforce shortages through an education assistance and loan repayment in exchange for service in designated rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:33Z"
    }
  ]
}
```
