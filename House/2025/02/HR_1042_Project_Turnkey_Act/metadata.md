# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1042?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1042
- Title: Project Turnkey Act
- Congress: 119
- Bill type: HR
- Bill number: 1042
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-06-05T08:06:52Z
- Update date including text: 2025-06-05T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1042",
    "number": "1042",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Project Turnkey Act",
    "type": "HR",
    "updateDate": "2025-06-05T08:06:52Z",
    "updateDateIncludingText": "2025-06-05T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:08:20Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "RI"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "VT"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "OR"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1042ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1042\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Bonamici (for herself, Ms. Norton , Ms. Tlaib , Ms. Salinas , Mr. Garcia of California , Mrs. Ramirez , Mrs. Watson Coleman , Mr. Amo , Ms. Jacobs , Mrs. Cherfilus-McCormick , Ms. Ansari , and Ms. Hoyle of Oregon ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the HOME Investment Partnerships Act to establish a Project Turnkey Program to leverage vacant hotels and motels for housing and enhance shelter capacity nationally, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Project Turnkey Act .\n#### 2. Project Turnkey Program\nSubtitle E of the HOME Investment Partnerships Act ( 42 U.S.C. 12821 ) is amended by adding at the end the following:\n272. Project Turnkey Program (a) In general There is established a Project Turnkey Program through which the Secretary shall award amounts to eligible entities to use for eligible activities. (b) Use of amounts by eligible entities (1) Administrative and planning costs An eligible entity that receives amounts under this section may use not more than 15 percent of such amounts for administrative and planning costs. (2) Operating expenses of other organizations (A) In general An eligible entity that receives amounts under this section may use not more than 5 percent of such amounts to cover the operating expenses of community housing development organizations and nonprofit organizations carrying out activities authorized under this section. (B) An eligible entity may only use amounts in the manner described in subparagraph (A) if\u2014 (i) such funds are used to develop the capacity of the community housing development organization or nonprofit organization in the jurisdiction or insular area to carry out activities authorized under this section; and (ii) the community housing development organization or nonprofit organization complies with the limitation on assistance in section 234(b). (3) Contracting A grantee, when contracting with service providers engaged directly in the provision of supportive services as defined by section 578.53 of title 24, Code of Federal Regulations shall, to the extent practicable, enter into contracts in amounts that cover the actual total program costs and administrative overhead to provide the services contracted. (c) Subgrants Any eligible entity that is a public entity may subgrant any amounts received under this section. (d) Supplement not supplant As a condition of receiving amounts under this section, an eligible entity shall use such funds received under this section only to supplement the level of State or local funds that would, in the absence of the receipt of funds under this section, be made available for activities described in this section. (e) Authorization of appropriations In addition to amounts otherwise available under this Act, there is authorized to be appropriated to carry out this section $1,000,000,000 annually. (f) Availability of amounts Amounts appropriated pursuant to this section shall remain available until 2035. (g) Allocation of amounts (1) Formula assistance Except as provided in paragraphs (2) and (3), the Secretary shall allocate amounts appropriated under this section to grantees that received allocations under section 217 in fiscal year 2025. (2) Technical assistance $25,000,000 of any amounts appropriated under this section may be provided by the Secretary to be used to increase capacity building and technical assistance available to grantees receiving amounts under this section. (3) Administration Not more than $50,000,000 of any amounts appropriated under this section may be used by the Secretary to cover costs related to the administration and implementation of this section. (4) Waivers and alternative requirements The Secretary may waive or specify alternative requirements for any provision of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12701 et seq. ) and titles I and IV of the McKinney-Vento Homelessness Act ( 42 U.S.C. 11301 et seq. , 11360 et seq.) or regulation for the administration of the amounts made available under this section other than requirements related to fair housing, nondiscrimination, labor standards, and the environment, upon a finding that the waiver or alternative requirement is necessary to expedite or facilitate the use of amounts made available under this section. (h) Special rules The cost limits described in section 212(e), the commitment requirements described in section 218(g), the matching requirements described in section 220, and the set-aside for housing developed, sponsored, or owned by community housing development organizations required in section 231 shall not apply for any amounts appropriated under this section. (i) Definitions In this section: (1) Qualifying individual or family defined The term qualifying individual or family means an individual or family that is\u2014 (A) homeless, as such term defined in section 103(a) of the McKinney-Vento Homeless Assistance Act; (B) at-risk of homelessness, as defined in section 401(1) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360(1) ; (C) fleeing, or attempting to flee, domestic violence, dating violence, sexual assault, stalking, or human trafficking, as such terms are defined by the Secretary; (D) a homeless children or youth, as that term is defined in section 725 of McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11434a ); or (E) a youth experiencing homelessness as that term is defined in section 38723 of the Runaway and Homeless Youth Act ( 34 U.S.C. 11279 ). (2) Eligible entity The term eligible entity means\u2014 (A) a State, city, county, regional government, or territory government; (B) a public housing agency; (C) a project sponsor receiving amounts under the Continuum of Care program under title IV of this Act, or any combination of such entities; (D) a nonprofit that provides housing; (E) a Community Development Corporation; or (F) a Community Development Financial Institution. (3) Eligible activity The term eligible activity means\u2014 (A) rental assistance, including\u2014 (i) providing rent payment assistance; (ii) providing security deposit assistance; and (iii) providing utility deposits and utility payments; (B) any eligible use of investments described under section 212(a); (C) supportive services as defined in section 578.53 of title 24, Code of Federal Regulations including\u2014 (i) activities listed in section 401(29) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360(29) ); (ii) housing counseling; and (iii) homeless prevention services; (D) the acquisition, development, and operation of non-congregate shelter units or affordable rental housing; (E) the rehabilitation, retrofitting, and conversion of newly acquired or vacant properties, including motels, hotels, schools, hospitals, and office buildings, for the purposes of providing affordable housing or shelter; (F) the repair and expansion of shelters and preservation of bed capacity; and (G) any other purpose as determined appropriate by the Secretary. (4) Hotel The term hotel has the meaning given the term in section 301(7)(A) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12181(7)(A) ), that are no longer affecting commerce (as such term is defined in such section 301). (5) Motel The term motel has the meaning given the term in section 301(7)(A) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12181(7)(A) ), that are no longer affecting commerce (as such term is defined in such section 301). .",
      "versionDate": "2025-02-06",
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
            "name": "Homelessness and emergency shelter",
            "updateDate": "2025-04-23T17:09:27Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-04-23T17:09:33Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2025-04-23T17:09:21Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-04-23T17:09:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-10T15:09:38Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1042ih.xml"
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
      "title": "Project Turnkey Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Project Turnkey Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the HOME Investment Partnerships Act to establish a Project Turnkey Program to leverage vacant hotels and motels for housing and enhance shelter capacity nationally, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:34Z"
    }
  ]
}
```
