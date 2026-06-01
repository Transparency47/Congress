# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3658
- Title: 911 Community Crisis Responders Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3658
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-03-25T08:05:44Z
- Update date including text: 2026-03-25T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3658",
    "number": "3658",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "911 Community Crisis Responders Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-25T08:05:44Z",
    "updateDateIncludingText": "2026-03-25T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:01:45Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "HI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "GA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "HI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3658ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3658\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Smith of Washington (for himself, Mr. Fitzpatrick , Mr. Khanna , Mr. Case , and Ms. Strickland ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, to award grants to States, territories, political subdivisions of States and territories, Tribal Governments, and consortia of Tribal Governments to establish an unarmed mobile crisis response program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 911 Community Crisis Responders Act of 2025 .\n#### 2. Grants for unarmed mobile crisis response programs\nPart D of title V of the Public Health Service Act is amended by inserting after section 552 ( 42 U.S.C. 290ee\u201310 ) the following new section:\n554. Grants for unarmed mobile crisis response programs (a) In general The Secretary, acting through the Assistant Secretary for Mental Health and Substance Use, may award grants to States, territories, political subdivisions of States and territories (such as counties), Tribal Governments, and consortia of Tribal Governments to establish an unarmed mobile crisis response program under which nonviolent emergency calls are referred to unarmed professional service providers for response, instead of to a law enforcement agency. (b) Program requirements An unarmed mobile crisis response program funded under this section shall\u2014 (1) dispatch unarmed professional service providers in groups of two or more in a timely manner; (2) be capable of providing screening, assessment, de-escalation, trauma-informed culturally competent services, engagement and referrals to community-based treatment providers, and transportation to immediately necessary treatment; (3) when necessary, coordinate with health, housing, or social services; (4) not be subject to oversight of State, Tribal, or local law enforcement agencies; and (5) clearly outline the scope of calls that must or may be referred to the unarmed mobile crisis response program as first responders. (c) Uses of funds A grant under this section may be used for\u2014 (1) hiring unarmed professional service providers and public safety telecommunicators; (2) training unarmed professional service providers to respond to emergency calls by identifying, understanding, and responding to signs of mental illnesses, physical disabilities, developmental or intellectual disabilities, and substance use disorders, including by means of\u2014 (A) de-escalation; (B) crisis intervention; and (C) connecting individuals to local service providers, health care providers, housing providers, community-based organizations, and the full range of other available providers and resources, with a focus on culturally competent service providers; (3) updating 911 response systems to enable triage between nonviolent 911 calls and those that require a response from law enforcement; (4) developing curriculum to train, and conducting training of, public safety telecommunicators on de-escalation and call processing; (5) coordinating with 9\u20138\u20138 call centers to establish a process for dispatching an unarmed mobile crisis response program; (6) building the capacity\u2014 (A) to coordinate with local trauma-informed social service providers, health care providers, and community-based organizations; and (B) to provide multilingual and culturally competent services; and (7) collecting data for reports to the Secretary. (d) Application An applicant seeking a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may reasonably require, including the applicant\u2019s plan to train 911 public safety telecommunicators to determine when a call requires a response from an unarmed mobile crisis response program. (e) Reports to Secretary A recipient of a grant under this section shall submit to the Secretary, on a biannual basis, a report on the following: (1) The number of calls placed to 911 that were diverted to the grantee\u2019s unarmed mobile crisis response program. (2) Demographic information on the individuals served by the grantee\u2019s unarmed mobile crisis response program, disaggregated by race, ethnicity, age, sex, sexual orientation, gender identity, location, mental illness, physical disabilities, developmental or intellectual disabilities, substance use disorders, and housing status. (3) The effects of the grantee\u2019s unarmed mobile crisis response program on emergency room visits, hospitalizations, use of ambulances, and involvement of law enforcement in mental health or substance use disorder crises. (4) An assessment of the types of events and crises to which the grantee\u2019s unarmed mobile crisis response program responded and the services provided, including\u2014 (A) the number of individuals successfully transferred to an alternative destination; (B) the time between notification by a public safety telecommunicator and arrival at the scene by a provider; and (C) the time spent by providers at scene. (5) A cost analysis of the grantee\u2019s unarmed mobile crisis response program. (f) Reports to Congress The Secretary shall submit to the Congress, on a biannual basis, a report on the program under this section, including a summary of the reports submitted by grantees pursuant to subsection (e). (g) Grant amount The Secretary may make grants to applicants that do not meet all of the criteria under subsection (b)(1), but applicants that do not meet all such criteria may not receive the full grant amount. (h) Definitions In this section: (1) The term alternative destination \u2014 (A) means any service- or care-providing site other than a hospital emergency department or jail; and (B) includes an outpatient clinic, primary care provider\u2019s office, crisis apartment, crisis home, respite home, crisis stabilization center, urgent care facility, and community care center. (2) The term nonviolent emergency call means a 911 call that\u2014 (A) relates to mental health, homelessness, addiction problems, social services, truancy, intellectual and developmental disabilities, or public intoxication; and (B) does not involve obvious violent behavior. (3) The term unarmed professional service provider means a professional (which may include a nurse, social worker, emergency medical technician, counselor, community health worker, trauma-informed personnel, social service provider, substance use disorder professional, or peer support specialist) who\u2014 (A) is trained to deal with mental health or substance abuse crises or intellectual and developmental disabilities; and (B) does not carry a firearm. (i) Nondiscrimination No person in the United States shall, on the basis of actual or perceived race, color, religion, national origin, sex (including sexual orientation and gender identity), or disability, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any program or activity funded, in whole or in part, with funds made available under this section. .",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-06-13T13:35:10Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3658ih.xml"
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
      "title": "911 Community Crisis Responders Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "911 Community Crisis Responders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, to award grants to States, territories, political subdivisions of States and territories, Tribal Governments, and consortia of Tribal Governments to establish an unarmed mobile crisis response program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T09:18:20Z"
    }
  ]
}
```
