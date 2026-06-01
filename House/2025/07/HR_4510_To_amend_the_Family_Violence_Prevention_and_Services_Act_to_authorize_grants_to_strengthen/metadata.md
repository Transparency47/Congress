# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4510
- Title: Healing Partnerships for Survivors Act
- Congress: 119
- Bill type: HR
- Bill number: 4510
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-03-17T16:00:57Z
- Update date including text: 2026-03-17T16:00:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4510",
    "number": "4510",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Healing Partnerships for Survivors Act",
    "type": "HR",
    "updateDate": "2026-03-17T16:00:57Z",
    "updateDateIncludingText": "2026-03-17T16:00:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:06:45Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "OH"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NM"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
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
      "sponsorshipDate": "2025-08-12",
      "state": "HI"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4510ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4510\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Leger Fernandez (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Family Violence Prevention and Services Act to authorize grants to strengthen relationships between health and wellness providers or systems (including for behavioral health) and community-based sexual assault programs to support survivors of sexual assault across the lifespan of the survivor, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healing Partnerships for Survivors Act .\n#### 2. Grants for strengthening relationships between health and wellness providers or systems, behavioral health programs, disability programs, and other service provider or community-based sexual assault programs to support survivors of sexual assault\n##### (a) In general\nThe Family Violence Prevention and Services Act ( 42 U.S.C. 10401 et seq. ) is amended by adding at the end the following:\n315. Grants for strengthening public health systems of support for survivors of sexual assault (a) In general (1) Grants authorized From amounts appropriated under section 303(d) to carry out this section, the Secretary, acting through the Office of Family Violence Prevention and Services, may award grants to eligible entities to develop, implement, and improve systems of support and service provision through partnerships with health and wellness providers or systems, behavioral health programs, disability programs, or other service provider or community-based sexual assault programs. (2) Eligible entities (A) In general To be eligible to receive a grant under paragraph (1), an entity shall be\u2014 (i) a State sexual assault coalition, a territorial sexual assault coalition, or a tribal coalition; (ii) a nonprofit community-based sexual assault program, including such a program that is a rape crisis center, culturally specific organization, or community-based organization, with a history of demonstrated work with survivors of sexual assault; or (iii) an Indian tribe or tribal organization. (B) Definitions In this paragraph: (i) Sexual assault; State sexual assault coalition; tribal coalition The terms sexual assault , State sexual assault coalition , and tribal coalition have the meanings given such terms in section 40002 of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291 ). (ii) Territorial sexual assault coalition The term territorial sexual assault coalition means a program addressing sexual violence that is\u2014 (I) an established nonprofit, nongovernmental territorial coalition addressing sexual assault within the territory; or (II) a nongovernmental organization with a demonstrated history of addressing sexual assault within the territory that proposes to incorporate as a nonprofit, nongovernmental territorial coalition. (3) Application To be eligible to receive a grant under paragraph (1), an eligible entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary determines appropriate. (4) Use of funds (A) In general An eligible entity that receives a grant under paragraph (1) shall, directly or through subgrants or contracts, develop and implement a program for developing partnerships with health and wellness providers or systems, behavioral health programs, disability programs, or other service providers or community-based sexual assault programs to develop trauma-informed, culturally relevant partnerships, training, responses, services, and policies to address and improve the comprehensive response to the health and well-being of survivors of sexual assault across the lifespan of the survivor, including adult survivors of childhood sexual abuse, regardless of age. (B) Authorized activities The program developed and implemented under subparagraph (A) may engage in the following: (i) The provision of services, including prevention, screening, linkages to care, and treatment, including therapy, support groups, holistic healing services, somatic approaches, substance-use services and supports, temporary housing assistance, and personal advocacy through case management, and information and referral services. (ii) Support for an adult survivor of childhood sexual abuse or sexual assault while the survivor receives health care or substance-use treatment services, including recovery and harm reduction support. (iii) The provision of training for staff and partners associated with delivering services described in clause (i). (iv) The provision of a trauma-informed and culturally relevant or specific health and wellness modality for a survivor of sexual assault. (v) Such other activities as the Secretary determines appropriate. (5) Reports and evaluations An eligible entity that receives a grant under paragraph (1) shall submit to the Secretary, at such time as shall be reasonably required by the Secretary, a report that\u2014 (A) describes the activities that have been carried out with such grant funds; (B) includes an evaluation of the impact and effectiveness of such activities; and (C) provides such additional information as the Secretary determines appropriate. (6) Privacy Each eligible entity receiving a grant under paragraph (1) shall ensure that each program developed or implemented with such grant protects victim privacy, confidentiality, and safety in compliance with applicable confidentiality, privacy, and nondisclosure requirements. (b) Technical assistance and training (1) In general From amounts appropriated under section 303(d) for any fiscal year to carry out this section, the Secretary shall award not more than 10 percent of the funds available for the fiscal year to 2 or more eligible entities for the provision of training and technical assistance to grantees and potential grantees under subsection (a)(1). (2) Eligible entities (A) In general To be eligible to receive a grant under paragraph (1), an eligible entity shall\u2014 (i) be a private, nonprofit organization that focuses primarily on issues related to sexual assault; (ii) in an application for a grant under paragraph (1), provide documentation to the Secretary demonstrating experience working directly on issues related to sexual assault; (iii) demonstrate to the Secretary in such application, the strong support of sexual assault service programs, including through letters of support, from around the United States for the entity\u2019s demonstrated history in providing training and technical assistance on issues related to sexual assault. (B) Demonstrated expertise To be eligible to receive a grant under paragraph (1), at least one of the eligible entities applying for the grant shall have\u2014 (i) a demonstrated expertise primarily working with culturally specific communities; or (ii) a demonstrated expertise in addressing, and a primary purpose to address, the development and provision of culturally specific services. (3) Required uses of funds An eligible entity awarded a grant under paragraph (1) shall use the grant\u2014 (A) to provide training and technical assistance to entities receiving grants under subsection (a)(1) for the implementation of programs funded under such subsection; (B) to conduct evaluations of the programs; (C) to identify and disseminate best practices that emerge from the programs; and (D) to carry out any other activity determined appropriate by the Secretary. (c) Federal administration From amounts appropriated under section 303(e) for any fiscal year, not more than $5,000,000 for such fiscal year may be used by the Secretary for evaluation, monitoring, and other administrative expenses. (d) Definition of sexual assault For purposes of this section, the term sexual assault has the meaning given the term in section 40002 of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291 ). .\n##### (b) Authority of the Secretary\nSection 304 of the Family Violence Prevention and Services Act ( 42 U.S.C. 10404(a)(5) ) is amended\u2014\n**(1)**\nby striking and dating violence each place it appears and inserting dating violence, and sexual assault ; and\n**(2)**\nby striking or dating violence each place it appears and inserting dating violence, or sexual assault .\n##### (c) Authorization of appropriations\nSection 303 of the Family Violence Prevention and Services Act ( 42 U.S.C. 10403 ) is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (e); and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Grants for strengthening public health systems of support for survivors of sexual assault There is authorized to be appropriated to carry out section 315 $30,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-07-17",
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
      "number": "2348",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Healing Partnerships for Survivors Act",
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
        "name": "Health",
        "updateDate": "2026-03-17T16:00:56Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4510ih.xml"
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
      "title": "Healing Partnerships for Survivors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:43:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healing Partnerships for Survivors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:43:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Family Violence Prevention and Services Act to authorize grants to strengthen relationships between health and wellness providers or systems (including for behavioral health) and community-based sexual assault programs to support survivors of sexual assault across the lifespan of the survivor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:33:30Z"
    }
  ]
}
```
