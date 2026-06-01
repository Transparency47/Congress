# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4011?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4011
- Title: Community Paramedicine Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4011
- Origin chamber: House
- Introduced date: 2025-06-13
- Update date: 2026-05-21T08:08:30Z
- Update date including text: 2026-05-21T08:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-13: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-13: Introduced in House

## Actions

- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-13",
    "latestAction": {
      "actionDate": "2025-06-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4011",
    "number": "4011",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Community Paramedicine Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:30Z",
    "updateDateIncludingText": "2026-05-21T08:08:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-13",
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
      "actionDate": "2025-06-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-13",
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
          "date": "2025-06-13T13:30:30Z",
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
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-13",
      "state": "TN"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IA"
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
      "sponsorshipDate": "2025-10-17",
      "state": "DC"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "CO"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MI"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
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
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NH"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "KS"
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
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "ME"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4011ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4011\nIN THE HOUSE OF REPRESENTATIVES\nJune 13, 2025 Mr. Cleaver (for himself and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to award grants to eligible entities to support community paramedicine programs carried out in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Paramedicine Act of 2025 .\n#### 2. Community paramedicine grant program\n##### (a) In general\nSection 330A of the Public Health Service Act ( 42 U.S.C. 254c ) is amended\u2014\n**(1)**\nby redesignating subsections (h), (i), and (j) as subsections (i), (j), and (k), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Community paramedicine grants (1) In general The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall award grants to eligible entities to support community paramedicine programs carried out in rural areas. (2) Use of funds A grant received under this subsection may be used for any of the following: (A) Hiring community paramedicine personnel. (B) Recruiting and retaining community paramedicine personnel. (C) Reimbursing costs associated with a medical director providing medical oversight (as the terms medical director and medical oversight are defined in section 303(k)(13) of the Controlled Substances Act). (D) Purchasing necessary equipment, including personal protective equipment, uniforms, medical supplies, and vehicles. (E) Reimbursing costs associated with certification and recertification courses. (F) Conducting public outreach and education on the patient-centered outcomes that can be achieved through community paramedicine. (G) Any other activity the Secretary determines appropriate related to paramedicine services. (3) Eligibility (A) In general To be eligible to receive a grant under this subsection, an entity shall be one of the following: (i) An emergency medical services agency (as defined in section 303(k)(13) of the Controlled Substances Act). (ii) A State, Indian Tribe, Tribal organization, county, or municipality. (iii) An organization representing the interests of one or more emergency medical services organizations. (B) Limitation A for-profit entity is ineligible to apply for a grant under this subsection. (C) Subgrants A recipient of a grant under the subsection may make a subgrant, or enter into a contract with, one or more persons (including governmental entities) to provide items or services in connection with the grant. (4) Applications (A) In general To be eligible to receive a grant under this subsection, an eligible entity shall prepare and submit an application at such time, in such manner, and containing such information and assurances as the Secretary may require. (B) Contents Any such application shall, at a minimum, include the following: (i) A description of the financial need of the eligible entity. (ii) The costs and benefits of the community paramedicine program to be supported through the grant. (C) Joint applications An eligible entity may submit an application for a grant under this subsection jointly with one or more other eligible entities. (5) Advisory board The Secretary, after consultation with national community paramedicine, national fire service, national emergency medical service, and Tribal health organizations, shall appoint an advisory board\u2014 (A) to advise the Secretary on carrying out the grant program under this subsection; and (B) to conduct peer review of applications for grants under this subsection. (6) Selection considerations In selecting the recipients of grants under this subsection, the Secretary shall consider each of the following: (A) The recommendations of the advisory board appointed under paragraph (5) with respect to the applications for such grants. (B) The need in the rural area involved for the community paramedicine program proposed to be funded. (7) Notice to Tribal communities The Secretary shall give notice of the grant program under this subsection to the heads of community emergency management for Tribal communities. (8) Maximum amount of awards The maximum amount of an award under this subsection shall be\u2014 (A) in the case of an eligible entity applying individually, $750,000; and (B) in the case of two or more eligible entities applying jointly, $1,500,000. (9) Period of a grant The period of a grant under this subsection shall not exceed 5 years. (10) Administrative costs Of the amount received through a grant under this subsection for a fiscal year, a grantee may use not more than\u2014 (A) 10 percent for administrative costs for the first year of grant funding; and (B) 5 percent for administrative costs for any subsequent year of grant funding. (11) Reporting by grantees As a condition on receipt of a grant under this subsection, an eligible entity shall agree to submit to the Secretary such information as the Secretary may require regarding the activities funded through the grant and the results of such activities. (12) Definition In this subsection, the term community paramedicine means mobile-integrated health care through which communities utilize specially trained paramedics, often teamed with other health care practitioners or social workers, to\u2014 (A) address health problems; (B) minimize the use of emergency care resources in circumstances when non-emergency resources such as community paramedic or mobile integrated healthcare programs might be used, thereby making emergency resources more available; and (C) enhance access to primary care for medically underserved populations and those with acute and chronic health issues. (13) Reservation Of the amount allocated to award grants under this subsection for a fiscal year, the Secretary\u2014 (A) shall reserve 15 percent for applicants proposing to use a grant to serve one or more Tribal communities; and (B) if the full amount of such reservation is not obligated, may reallocate the unobligated portion for grants to other eligible entities. .\n##### (b) Conforming amendments\nSection 330A of the Public Health Service Act ( 42 U.S.C. 254c ) is amended\u2014\n**(1)**\nin the section heading, by striking AND SMALL HEALTH CARE PROVIDER QUALITY IMPROVEMENT and inserting SMALL HEALTH CARE PROVIDER QUALITY IMPROVEMENT, AND COMMUNITY PARAMEDICINE SERVICES SUPPORT ;\n**(2)**\nin subsection (a), by striking and for the planning and implementation of small health care provider quality improvement activities and inserting for the planning and implementation of small health care provider quality improvement activities, and for providing support for community paramedicine services ; and\n**(3)**\nin subsection (j) (as redesignated by subsection (a)(1) of this section) by striking subsections (e), (f), and (g) and inserting subsections (e), (f), (g), and (h) .",
      "versionDate": "2025-06-13",
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
        "updateDate": "2025-07-08T13:42:36Z"
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
      "date": "2025-06-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4011ih.xml"
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
      "title": "Community Paramedicine Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Paramedicine Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to award grants to eligible entities to support community paramedicine programs carried out in rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T04:48:30Z"
    }
  ]
}
```
