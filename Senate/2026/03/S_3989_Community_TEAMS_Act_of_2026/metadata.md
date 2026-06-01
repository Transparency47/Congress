# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3989?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3989
- Title: Community TEAMS Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3989
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3989",
    "number": "3989",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Community TEAMS Act of 2026",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-04T19:34:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-04",
      "state": "ME"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3989is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3989\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Curtis (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to provide community-based training opportunities for medical students in rural areas and medically underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Training, Education, and Access for Medical Students Act of 2026 or the Community TEAMS Act of 2026 .\n#### 2. Grants for community-based training for medical students in rural areas and medically underserved communities\n##### (a) In general\nSection 330A of the Public Health Service Act ( 42 U.S.C. 254c ) is amended\u2014\n**(1)**\nby redesignating subsections (h), (i), and (j) as subsections (i), (j), and (k), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Grants for community-Based training for medical students in rural areas and medically underserved communities (1) Grants The Director may award grants to eligible entities to expand the availability of community-based training for medical students in rural areas and medically underserved communities, including by supporting clinical rotations in health care facilities in such areas and communities, including in outpatient settings, to facilitate long-term, sustainable physician practice in high-need communities. (2) Period of grants A grant under this subsection shall be for a period of 1 to 5 years, as determined by the Director. (3) Eligibility To be eligible for a grant under this subsection, an entity shall be a consortium of the following: (A) One or more schools of osteopathic medicine or allopathic medicine. (B) One or more of the following: (i) A rural health clinic. (ii) A Federally qualified health center. (iii) A health care facility located in a medically underserved community. (4) Applications An eligible entity desiring a grant under this subsection shall, in consultation with the appropriate State office of rural health or another appropriate State entity, submit to the Director an application at such time, in such manner, and containing such information as the Director may require, including\u2014 (A) a description of the project that the eligible entity will carry out using the funds provided through the grant; (B) an explanation of the reasons why Federal assistance is required to carry out the project; (C) a description of the manner in which the project funded through the grant will ensure continuous quality improvement in the provision of services by the entity; (D) a description of how the populations in the rural area or medically underserved community to be served through the grant will experience increased access to quality health care services across the continuum of care as a result of the activities carried out by the entity; (E) a plan for sustaining the project after Federal support for the project has ended; (F) a description of how the project will be evaluated; and (G) such other information as the Director determines to be appropriate. .\n##### (b) Conforming changes\nSection 330A of the Public Health Service Act ( 42 U.S.C. 254c ) is amended\u2014\n**(1)**\nin subsection (a), by striking and for the planning and implementation of small health care provider quality improvement activities and inserting for the planning and implementation of small health care provider quality improvement activities, and for expanding the availability of community-based training for medical students in rural areas and medically underserved communities ;\n**(2)**\nin subsection (b), by inserting In this section: after Definitions\u2014 ;\n**(3)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A), by striking subsections (e), (f), and (g) and inserting subsections (e), (f), (g), and (h) ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (ii), by striking and at the end;\n**(ii)**\nin clause (iii), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(iv) expand the availability of community-based training for medical students in rural areas and medically underserved communities under subsection (h). ;\n**(4)**\nin subsection (j), as so redesignated, by striking subsections (e), (f), and (g) and inserting subsections (e), (f), (g), and (h) ; and\n**(5)**\nin subsection (k), as so redesignated, by striking 2021 through 2025 and inserting 2026 through 2030 .",
      "versionDate": "2026-03-04",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-23T20:31:34Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3989is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Community TEAMS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Community TEAMS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Community Training, Education, and Access for Medical Students Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to provide community-based training opportunities for medical students in rural areas and medically underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:47Z"
    }
  ]
}
```
