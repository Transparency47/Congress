# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7875
- Title: POINTS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7875
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-03-30T19:27:52Z
- Update date including text: 2026-03-30T19:27:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7875",
    "number": "7875",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "POINTS Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-30T19:27:52Z",
    "updateDateIncludingText": "2026-03-30T19:27:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "OR"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "IA"
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
      "sponsorshipDate": "2026-03-09",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7875ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7875\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mrs. Houchin (for herself, Ms. Salinas , Mrs. Miller-Meeks , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to establish a grant program for providing services to individuals experiencing gambling addiction.\n#### 1. Short title\nThis Act may be cited as the Providing Opportunities for Individuals in Need of Treatment and Support Act of 2026 or the POINTS Act of 2026 .\n#### 2. Grants for providing services to individuals experiencing gambling addiction\nPart D of title V of the Public Health Service Act ( 42 U.S.C. 290dd et seq. ) is amended by adding at the end the following:\n554. Grants for providing services to individuals experiencing gambling addiction (a) In general The Assistant Secretary shall make grants to States, Indian Tribes, and Tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )) on a competitive basis to establish, improve, or expand programs providing prevention, screening, assessment, intervention, and treatment services, including culturally and linguistically appropriate services, to individuals at risk of or experiencing clinical gambling addiction. (b) Use of funds A State, Indian Tribe, or Tribal organization that receives a grant under this section shall use funds received through such grant to, with respect to gambling addiction\u2014 (1) provide training on screening, brief intervention, referral for treatment, and treatment to health care providers and health paraprofessionals who practice in primary care, behavioral health, or other relevant health care settings; (2) implement a prevention strategy, including public outreach and awareness, in the State or Indian Tribe that receives such funds; (3) provide a specialized treatment service, including\u2014 (A) in-person or telehealth outpatient treatment; or (B) a peer support group, including a program operated by Gamblers Anonymous; (4) establish or expand help lines or such other real-time service for prevention or intervention, including coordinating with the National Problem Gambling Helpline operated by the National Council on Problem Gambling, for individuals in the State or Indian Tribe that receives such funds; or (5) implement such other innovative prevention, intervention, or treatment services determined appropriate by the Assistant Secretary. (c) Priority In making grants under this section, the Assistant Secretary shall give priority to a State, Indian Tribe, or Tribal organization that\u2014 (1) proposes to establish, improve, or expand a program described under subsection (a) that serves individuals who are disproportionally impacted by gambling addiction, including men, youth, Native Americans (as defined in section 103 of the Native American Languages Act ( 25 U.S.C. 2902 )), members of the Armed Forces, and veterans; (2) proposes to establish, improve, or expand a program described under subsection (a) in a primary care setting; (3) partners with, or proposes to partner with, at least one community-based organization to address gambling addiction; or (4) operates in a health professional shortage area (as defined in section 332), including a rural target area. (d) Application (1) In general A State, Indian Tribe, or Tribal organization seeking to receive a grant under this section shall submit an application to the Assistant Secretary at such time, in such manner, and containing such information as the Assistant Secretary may require. (2) Required content At a minimum, an application submitted under this subsection shall explain how the applicant establishing, improving upon, or expanding a program described under subsection (a) would increase\u2014 (A) access to services for gambling addiction in the communities served by such applicant; and (B) the percentage of individuals served by such program in at least one such community. (e) Technical assistance The Assistant Secretary shall provide technical assistance related to the services described under subsection (b) to each State, Indian Tribe, or Tribal organization that receives a grant under this section. (f) Report (1) In general Not later than December 29, 2027, and annually thereafter, the Assistant Secretary shall submit to the appropriate congressional committees a report on the effectiveness of grants made under this section for establishing, improving, or expanding programs. (2) Appropriate congressional committee defined In this subsection, the term appropriate congressional committee means\u2014 (A) the Committee on Energy and Commerce of the House of Representatives; (B) the Committee on Appropriations of the House of Representatives; (C) the Committee on Health, Education, Labor, and Pensions of the Senate; and (D) the Committee on Appropriations of the Senate. (g) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section for fiscal year 2027 an amount that is equal to 33 percent of the amounts received by the Secretary of the Treasury under section 4401(a) of the Internal Revenue Code of 1986 ( 26 U.S.C. 4401(a) ), with respect to the 2025 calendar year. (2) Adjustment for inflation For fiscal years 2028 through 2032, the amount authorized by this subsection shall be adjusted by the percentage increase, if any, in the Consumer Price Index for All Urban Consumers (CPI\u2013U) published by the Bureau of Labor Statistics of the Department of Labor for the most recent 12-month period for which data is available. .",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-03-30T19:27:52Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7875ih.xml"
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
      "title": "POINTS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POINTS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Opportunities for Individuals in Need of Treatment and Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to establish a grant program for providing services to individuals experiencing gambling addiction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:20Z"
    }
  ]
}
```
