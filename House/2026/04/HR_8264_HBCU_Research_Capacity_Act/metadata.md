# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8264
- Title: HBCU Research Capacity Act
- Congress: 119
- Bill type: HR
- Bill number: 8264
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-05-21T08:08:29Z
- Update date including text: 2026-05-21T08:08:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8264",
    "number": "8264",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "HBCU Research Capacity Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:29Z",
    "updateDateIncludingText": "2026-05-21T08:08:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:02:45Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "GA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "AL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "UT"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MS"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8264ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8264\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Hill of Arkansas (for himself, Ms. Adams , Mr. McCormick , and Mr. Figures ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish the Federal Clearinghouse on Grant Opportunities for Historically Black Colleges and Universities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HBCU Research Capacity Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHistorically Black Colleges and Universities (HBCUs) are a vital source to the Nation\u2019s research and workforce communities. While enrolling 8.5 percent of Black undergraduate students, HBCUs produce almost 18 percent of Black STEM bachelor\u2019s degree recipients, as of 2024.\n**(2)**\nDespite these major contributions, only one HBCU, Howard University, has achieved very high research activity status. Furthermore, HBCUs received less than 1 percent of the approximately $60,000,000,000 in Federal research and development expenditures at colleges and universities in fiscal year 2023.\n**(3)**\nDue to historical underfunding, HBCUs face cyclical barriers in building research capacity, further limiting grant access, resources, and exasperating issues related to smaller endowments. This makes it even more difficult for scholars to secure Federal research funding.\n**(4)**\nIn finding solutions to research and development barriers, a May 2024 report by the National Science and Technology Council recommends strategies such as expanding flexibility in funding, encouraging interagency collaboration to share best practices, and reforming merit-review to reduce bias and improve transparency.\n**(5)**\nExpanding research diversity is strategically important for national security, economic growth, and innovation. Underrepresentation of HBCUs in Federal research funding represents a missed opportunity.\n**(6)**\nA Federal clearinghouse providing information on grant opportunities and sharing best practices would help address barriers such as knowledge gaps, transparency, and capacity limitations.\n**(7)**\nCoordinated agency review, gap identification, and reporting to Congress should improve accountability and help ensure equitable access to Federal research funding for HBCUs.\n**(8)**\nEstablishing, maintaining, and creating accountability measures for the Clearinghouse is therefore appropriate and necessary to notify eligible HBCUs and guide Federal agencies in supporting HBCU research capacity.\n#### 3. Federal Clearinghouse on Grant Opportunities for Historically Black Colleges and Universities\nPart B of title III of the Higher Education Act of 1965 ( 20 U.S.C. 1060 et seq. ) is amended by adding at the end the following:\n328. Federal Clearinghouse on Grant Opportunities for Historically Black Colleges and Universities (a) Establishment (1) In general The Secretary, in coordination with the Secretary of Commerce, the Secretary of Energy, the Secretary of Defense, the Secretary of Agriculture, the Director of the National Science Foundation, the Administrator of the Environmental Protection Agency, and the Administrator of the National Aeronautics and Space Administration shall establish a Federal Clearinghouse on Research Capacity and Grant Opportunities for Historically Black Colleges and Universities (in this section referred to as the Clearinghouse ) within the Department. (2) Purpose The Clearinghouse shall be the primary resource of the Federal Government to identify and provide comprehensive information on Federal grant opportunities for which part B institutions are eligible or are exclusively eligible, delineating between the two categories, that support\u2014 (A) research and development; and (B) building institutional research capacity. (3) Personnel (A) Assignments The Clearinghouse shall be assigned such personnel and resources as the Secretary considers appropriate to carry out this section. (B) Detailees The Secretary of Education, the Secretary of Commerce, the Secretary of Energy, the Secretary of Defense, the Secretary of Agriculture, the Director of the National Science Foundation, the Administrator of the Environmental Protection Agency, and the Administrator of the National Aeronautics and Space Administration may detail personnel to the Clearinghouse. (4) Exemptions (A) Paperwork reduction act Subchapter I of chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ) shall not apply to any rulemaking or information collection required under this section. (B) Federal advisory committee act Chapter 10 of title 5, United States Code, shall not apply for the purposes of carrying out this section. (b) Clearinghouse contents The Clearinghouse shall include best practices and recommendations for part B institutions to build institutional research capacity and access Federal research funding, including best practices and recommendations from appropriate Federal, State, and local organizations, including from annual Agency Plan submissions described under section 4 of the HBCU PARTNERS Act ( 20 U.S.C. 1063d ). .\n#### 4. Notification of Clearinghouse\n##### (a) Notification of publication\nThe Secretary of Education shall provide written notification of the publication of the Federal Clearinghouse on Grant Opportunities for Historically Black Colleges and Universities (referred to in this section and section 5 as the Clearinghouse ), as required to be established under section 328 of the Higher Education Act of 1965, as added by section 3 of this Act, to each part B institution (as such term is defined in section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 )) and to Congress.\n##### (b) Annual notification to Congress\nThe Secretary of Education shall provide an annual report to Congress on the contents of the Clearinghouse.\n##### (c) Updates\nThe Secretary of Education shall\u2014\n**(1)**\nprovide each part B institution described in subsection (a) with the option to receive quarterly updates of Clearinghouse contents; and\n**(2)**\nsend quarterly updates of Clearinghouse contents to each part B institution that chooses to receive the updates.\n#### 5. Grant program review\nThe Secretary of Education, the Secretary of Commerce, the Secretary of Energy, the Secretary of Defense, the Secretary of Agriculture, the Director of the National Science Foundation, the Administrator of the Environmental Protection Agency, and the Administrator of the National Aeronautics and Space Administration shall each\u2014\n**(1)**\nreview grant programs administered by their respective agency and identify any grant program that may be used to implement best practices and recommendations of the Clearinghouse;\n**(2)**\nidentify any best practices and recommendations of the Clearinghouse for which there is not a Federal grant program that may be used for the purposes of implementing the best practice or recommendation as applicable to the agency; and\n**(3)**\non an annual basis, report any findings under paragraph (2) to the appropriate committees of Congress.",
      "versionDate": "2026-04-14",
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
        "actionDate": "2026-03-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4167",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HBCU Research Capacity Act",
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
        "name": "Education",
        "updateDate": "2026-04-21T16:27:48Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8264ih.xml"
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
      "title": "HBCU Research Capacity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HBCU Research Capacity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Federal Clearinghouse on Grant Opportunities for Historically Black Colleges and Universities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:44Z"
    }
  ]
}
```
