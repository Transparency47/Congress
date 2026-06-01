# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4426
- Title: SMART Act
- Congress: 119
- Bill type: HR
- Bill number: 4426
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-11-01T08:05:35Z
- Update date including text: 2025-11-01T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4426",
    "number": "4426",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "SMART Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:35Z",
    "updateDateIncludingText": "2025-11-01T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-17T17:03:19Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "AZ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4426ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4426\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Bresnahan (for himself and Mr. Garamendi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Emergency Management Agency to conduct a study to evaluate the effectiveness, long-term cost savings, and strategic impact of Federal Emergency Management Agency-funded hazard mitigation activities across the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Studying Mitigation And Reporting Transparently Act or the SMART Act .\n#### 2. Study and report on mitigation benefits\n##### (a) In general\nThe Administrator of the Federal Emergency Management Agency shall conduct a comprehensive study to evaluate the effectiveness, long-term cost savings, and strategic impact of Federal Emergency Management Agency-funded hazard mitigation activities across the United States.\n##### (b) Objectives\nIn conducting the study required under subsection (a), the Administrator shall assess how the mitigation programs of the Federal Emergency Management Agency\u2014\n**(1)**\nreduce Federal and non-Federal expenditures for disaster response and recovery;\n**(2)**\nenhance community preparedness for natural hazards;\n**(3)**\nimprove the availability and affordability of hazard-related insurance;\n**(4)**\nsupport continuity of operations for critical services and infrastructure; and\n**(5)**\ngenerate long-term cost savings and measurable returns on investment.\n##### (c) Methodology\nThe study under subsection (a) shall include\u2014\n**(1)**\nquantitative and qualitative analysis of avoided losses;\n**(2)**\nevaluations of the effect of hazard mitigation on community-level risk ratings, actuarial assessments, and insurance penetration;\n**(3)**\ncase studies from diverse geographic regions and hazard types; and\n**(4)**\nexaminations of the role of mitigation activities in reducing Federal disaster response and recovery costs.\n##### (d) Data sources\nIn carrying out the study under subsection (a), the Administrator shall use data from\u2014\n**(1)**\nFederal, State, local, and Tribal agencies;\n**(2)**\nindependent third-party assessments and academic studies; and\n**(3)**\ninternal program evaluations and disaster recovery records.\n##### (e) Consultation\nIn conducting the study under subsection (a), the Administrator may consult with\u2014\n**(1)**\nthe Government Accountability Office;\n**(2)**\nthe National Institute of Standards and Technology;\n**(3)**\nState, local, Tribal, and territorial governments; and\n**(4)**\nrelevant academic and research institutions.\n##### (f) Report to Congress\nNot later than 18 months after the date of enactment of this Act and annually thereafter, the Administrator shall submit to the Committee on Transportation and Infrastructure and the Committee on Appropriations of the House of Representatives and the Committee on Homeland Security and Governmental Affairs and the Committee on Appropriations of the Senate a report detailing\u2014\n**(1)**\nthe findings of the study;\n**(2)**\nrecommendations for improving program design, targeting, and oversight; and\n**(3)**\nrecommendations for legislative and administrative actions.\n#### 3. Public availability and ongoing review\n##### (a) Public access\nNot later than 2 years after the date of enactment of this Act, the Administrator shall make the results of the initial study required under section 2 publicly available in a searchable, user-friendly format on the website of the Federal Emergency Management Agency.\n##### (b) Contents\nThe published data under subsection (a) shall include\u2014\n**(1)**\nsummarized findings and datasets, excluding any information that would compromise national security or privacy;\n**(2)**\nvisualizations and geographic mappings of mitigation outcomes; and\n**(3)**\nclear explanations of methodology, data sources, and limitations.\n##### (c) Annual updates\nThe Administrator shall conduct the study described in section 2 on an annual basis, incorporating the most recent available data, updates to methodology, and stakeholder feedback.\n##### (d) Availability\nEach annual report under section 2(e) shall be made publicly available on the website of the Federal Emergency Management Agency not later than 60 days after the submission of such report to Congress.",
      "versionDate": "2025-07-16",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-30T21:59:59Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4426ih.xml"
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
      "title": "SMART Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SMART Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Studying Mitigation And Reporting Transparently Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Emergency Management Agency to conduct a study to evaluate the effectiveness, long-term cost savings, and strategic impact of Federal Emergency Management Agency-funded hazard mitigation activities across the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:33:23Z"
    }
  ]
}
```
