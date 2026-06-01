# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8110
- Title: Cyber Ready Workforce Act
- Congress: 119
- Bill type: HR
- Bill number: 8110
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-12T08:06:11Z
- Update date including text: 2026-05-12T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8110",
    "number": "8110",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Cyber Ready Workforce Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:11Z",
    "updateDateIncludingText": "2026-05-12T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:00:40Z",
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
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8110ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8110\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Lee of Nevada (for herself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish a grant program within the Department of Labor to support the creation, implementation, and expansion of registered apprenticeship programs in cybersecurity.\n#### 1. Short title\nThis Act may be cited as the Cyber Ready Workforce Act .\n#### 2. Definitions\nIn this Act:\n**(1) Registered apprenticeship program**\nThe term registered apprenticeship program means a program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 29 U.S.C. 50 et seq. ).\n**(2) Workforce intermediary**\nThe term workforce intermediary means an entity that facilitates the establishment of registered apprenticeship programs, and may be a partnership that includes one or more of the following as partners:\n**(A)**\nA business or industry organization.\n**(B)**\nA community-based organization, as defined in section 3201(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801(5) ).\n**(C)**\nA State board or local board, as such terms are defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(D)**\nA postsecondary education institution with experience in developing and administering registered apprenticeship programs.\n**(E)**\nA joint labor-management partnership.\n**(F)**\nAn institution of higher education, as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(G)**\nA nonprofit organization.\n#### 3. Cybersecurity apprenticeship grant program\n##### (a) In general\nThe Secretary of Labor shall award grants, on a competitive basis, to workforce intermediaries, to support the establishment, implementation, and expansion of registered apprenticeship programs in cybersecurity.\n##### (b) Description of programs eligible\nFor purposes of subsection (a), registered apprenticeship programs in cybersecurity shall include technical instruction, workplace training, and industry-recognized certification in cybersecurity. Programs shall\u2014\n**(1)**\ninclude certifications in CompTIA Network+, CompTIA A+, CompTIA Security+, Microsoft Windows 10 Technician, Microsoft Certified System Administrator, Certified Network Defender, Certified Ethical Hacker, ISACA Cybersecurity Nexus (CSX), (ISC) 2 's Certified Information Systems Security Professional (CISSP), or other industry-recognized certification in cybersecurity;\n**(2)**\nencourage stackable and portable credentials; and\n**(3)**\nlead to occupations such as computer support specialists, cybersecurity support technicians, cloud computing architects, computer programmers, computer systems analysts, or security specialists.\n#### 4. Use of funds\n##### (a) Required activities\nA workforce intermediary shall use at least 85 percent of the amount of grant funds received under this Act for the following:\n**(1) Development and technical support**\nComplete the apprenticeship registration process with the Department of Labor, and assist employers with other logistical and technical issues.\n**(2) Employer partnership**\n**(A) In general**\nDevelop curricula and technical instruction for the registered apprenticeship program in cooperation with local businesses, organizations, and employer-partners, referencing the work roles and tasks outlined in the National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework Special Publication 800\u2013181 to develop skills and standards for the program.\n**(B) Offsite training**\nAssist employers in paying for the cost of offsite training and acquiring course materials provided to apprentices.\n**(C) Connecting employers**\nConnect employers with education and training providers to complement on-the-job learning.\n**(3) Support services for apprentices**\nProvide support services to apprentices to assist with their success in the registered apprenticeship program, which may include the following:\n**(A)**\nCareer counseling.\n**(B)**\nMentorship.\n**(C)**\nAssisting with costs of transportation, housing, and child care services.\n##### (b) Allowable activities\nA workforce intermediary may use up to 15 percent of the amount of grant funds received under this Act for the following outreach and marketing activities:\n**(1)**\nMarket apprenticeships and the apprenticeship model to employers, secondary school administrators, and counselors.\n**(2)**\nRecruit and conduct outreach to potential apprentices, including secondary school students, underrepresented populations (such as women and minorities), youth, and veterans.\n**(3)**\nConnect and collaborate with other workforce intermediaries, and coordinate resources with Federal investments in the registered apprenticeship program, to\u2014\n**(A)**\nminimize the duplication of efforts;\n**(B)**\nshare best practices; and\n**(C)**\nwidely disseminate training resources and materials developed with grant funds provided under this Act.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated, such sums as may be necessary to carry out this Act.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4263",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Cyber Ready Workforce Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-04-01T21:11:47Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8110ih.xml"
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
      "title": "Cyber Ready Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cyber Ready Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program within the Department of Labor to support the creation, implementation, and expansion of registered apprenticeship programs in cybersecurity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T08:18:21Z"
    }
  ]
}
```
