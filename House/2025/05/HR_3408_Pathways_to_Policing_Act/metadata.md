# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3408?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3408
- Title: Pathways to Policing Act
- Congress: 119
- Bill type: HR
- Bill number: 3408
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2025-05-27T14:09:21Z
- Update date including text: 2025-05-27T14:09:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3408",
    "number": "3408",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001234",
        "district": "3",
        "firstName": "Kelly",
        "fullName": "Rep. Morrison, Kelly [D-MN-3]",
        "lastName": "Morrison",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Pathways to Policing Act",
    "type": "HR",
    "updateDate": "2025-05-27T14:09:21Z",
    "updateDateIncludingText": "2025-05-27T14:09:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:00:10Z",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3408ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3408\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Ms. Morrison (for herself, Mr. Finstad , Ms. Craig , Mr. Fitzpatrick , Ms. McCollum , Mr. Bacon , Mr. Panetta , Mr. Valadao , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize a grant to encourage recruitment of law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pathways to Policing Act .\n#### 2. Grant program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Law Enforcement Hiring Support Grant 3061. Grant authorization (a) In general Not later than 180 days after the date of enactment of this part, the COPS Director is authorized to make grants, on a competitive basis, to States, units of local government, and law enforcement agencies for the purposes described in subsection (c). (b) Applications To be eligible to receive a grant under this part, a State, unit of local government, or law enforcement agency shall submit an application to the COPS Director at such time, in such manner, and containing such information as the COPS Director may require. (c) Use of funds A recipient of a grant under this part may use the grant funds for the following: (1) Marketing and Recruitment campaigns Not more than 50 percent of the grant funds awarded to a recipient under this part may be used to develop, implement, or expand marketing and recruitment campaigns for the purpose of encouraging candidates to seek careers in law enforcement. (2) Pathways to policing Not more than 50 percent of the grant funds awarded to a recipient under this part may be used to develop, operate, or expand Pathways to Policing programs. (d) Report For each fiscal year in which a grant is awarded under this part, each recipient of such grant shall submit to the COPS Director a report containing a summary of each activity carried out using such grant and such other information as the COPS Director may require. 3062. Priority (a) Underrepresented and nontraditional groups In awarding a grant under this part, priority shall be given to applicants that seek to recruit candidates who are members of communities traditionally underrepresented in the field of law enforcement or who have nontraditional educational or career backgrounds. (b) Community policing In awarding a grant under this part, priority shall be given to applicants that seek to recruit candidates who reside in or who are willing to relocate to the communities that the candidates will serve, or that are in close proximity to the communities that the candidates will serve. 3063. Definitions In this part: (1) COPS Director The term COPS Director means the Attorney General, acting through the Director of the Office of Community Oriented Policing Services. (2) Pathways to Policing programs The term Pathways to Policing programs refers to any program that\u2014 (A) facilitates the entry into full-time law enforcement positions for candidates that\u2014 (i) face barriers in obtaining the education and training necessary to pursue a law enforcement career; and (ii) have no prior law enforcement experience; (B) provides candidates with financial support, including tuition, compensation, or benefits, while attending a law enforcement officer education and training program, and (C) may include service in part-time, uniformed positions that further a candidate\u2019s training to be a full-time law enforcement officer. 3064. Authorization of appropriations There is authorized to be appropriated $50,000,000 to carry out sections 3061, 3062, and 3063 for each of fiscal years 2026 to 2030. 3065. Nationwide law enforcement marketing and recruitment campaign (a) Marketing and recruitment campaigns Not later than 1 year after the date of enactment of this section, the Attorney General shall develop and implement nationwide marketing and recruitment campaigns for the purpose of encouraging candidates, including candidates who are members of communities traditionally underrepresented in the field of law enforcement or who have nontraditional educational or career backgrounds, to seek careers in law enforcement. (b) Consultation In developing and implementing the marketing and recruitment campaigns under subsection (a), the Attorney General shall consult with State attorneys general, State and local law enforcement entities, professional law enforcement associations, community-based organizations, and academic researchers. (c) States, units of local government, and law enforcement agencies In developing and implementing the marketing and recruitment campaigns under subsection (a), the Attorney General shall create educational materials and related resources for States, units of local government, and law enforcement agencies to operate a marketing and recruitment campaign under section 3061. (d) Authorization of appropriations There is authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2026 to 2030. .",
      "versionDate": "2025-05-14",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-27T14:09:21Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3408ih.xml"
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
      "title": "Pathways to Policing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pathways to Policing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize a grant to encourage recruitment of law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:25Z"
    }
  ]
}
```
