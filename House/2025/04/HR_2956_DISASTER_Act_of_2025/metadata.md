# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2956?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2956
- Title: DISASTER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2956
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-06-12T08:07:03Z
- Update date including text: 2025-06-12T08:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-17 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2956",
    "number": "2956",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "DISASTER Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:03Z",
    "updateDateIncludingText": "2025-06-12T08:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:37:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-17T21:13:44Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2956ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2956\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Peters (for himself, Mr. Obernolte , Ms. Scholten , Mr. Valadao , Mr. Moskowitz , and Mr. Womack ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend chapter 11 of title 31, United States Code, to require the Director of the Office of Management and Budget to annually submit to Congress a report on all disaster-related assistance provided by the Federal Government.\n#### 1. Short title\nThis Act may be cited as the Disclosing Aid Spent to Ensure Relief Act of 2025 or the DISASTER Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAt a time of constrained budgets, it is fiscally prudent to understand the amount and the scope of the Federal Government\u2019s involvement in providing disaster-related assistance to communities in need.\n**(2)**\nThe Federal Government does not provide a single, publicly available estimate of the amount it is spending on disaster-related assistance.\n**(3)**\nBecause recovery is a long-term process, providing disaster-related assistance requires significant Federal resources to support a multi-agency, multi-year restoration of infrastructure and commerce in affected communities.\n**(4)**\nUnderstanding the expenditures of individual Federal agencies for disaster-related assistance will help better inform the congressional appropriations process, as well as presidential budget requests.\n**(5)**\nKnowledge about disaster-related expenses will illustrate opportunities for reducing these expenses through efforts to reduce vulnerabilities to future natural disasters.\n#### 3. Purpose\nThe purpose of this Act is to require the Director of the Office of Management and Budget to annually submit to Congress a report on all disaster-related assistance provided by the Federal Government.\n#### 4. Reporting of disaster-related assistance\n##### (a) In general\nChapter 11 of title 31, United States Code, is amended by adding at the end the following new section:\n1127. Reporting of disaster-related assistance (a) In general On the same day that the President makes the annual budget submission to the Congress under section 1105(a) for a fiscal year, the Director of the Office of Management and Budget shall submit to Congress a report on Federal disaster-related assistance for the fiscal year ending in the calendar year immediately preceding the calendar year in which the annual budget submission is made. Disaster-related assistance encompasses Federal obligations related to disaster response, recovery, and mitigation efforts, as well as administrative costs associated with these activities, including spending by the following agencies and programs: (1) Department of Agriculture: (A) Agriculture Research Service. (B) Farm Service Agency. (C) Food and Nutrition Service. (D) Natural Resource Conservation Service. (E) Forest Service. (F) Rural Housing Service. (G) Rural Utilities Service. (2) Department of Commerce: (A) National Marine Fisheries Service of the National Oceanic and Atmospheric Administration. (B) Economic Development Administration Economic Adjustment Assistance. (3) Army Corps of Engineers of the Department of Defense (Civil). (4) Department of Defense (Military): (A) Military Personnel. (B) Operations and Maintenance. (C) Procurement. (D) Research, Development, Test, and Evaluation. (E) Military Construction (MILCON) and Family Housing. (F) Management Funds. (G) Other Department of Defense Programs. (5) Department of Education: (A) Elementary and Secondary Education. (B) Higher Education. (6) Department of Health and Human Services: (A) Administration for Children and Families. (B) Public Health and Medical Assistance. (C) Public Health Emergency Fund. (7) Department of Homeland Security: (A) Federal Emergency Management Agency: (i) Emergency Declarations. (ii) Fire Management Assistance Grants. (iii) Major Disaster Declarations. (iv) Administrative Assistance. (B) FEMA Missions Assignments by Federal Agency. (C) Community Disaster Loan Program. (8) Department of Housing and Urban Development (HUD): (A) Community Development Block Grants. (B) Rental Assistance/Section 8 Vouchers. (C) Supportive Housing. (D) Public Housing Repair. (E) Inspector General. (9) Department of the Interior: (A) Bureau of Indian Affairs. (B) United States Fish and Wildlife Service. (C) National Park Service. (D) Wildland Fire Management. (10) Department of Justice: (A) Legal Activities. (B) United States Marshals Service. (C) Federal Bureau of Investigation. (D) Drug Enforcement Administration. (E) Bureau of Tobacco, Firearms, and Explosives. (F) Federal Prison System (Bureau of Prisons). (G) Office of Justice Programs. (11) Department of Labor: (A) National Emergency Grants for Dislocation Events. (B) Workforce Investment Act (WIA) Dislocated Worker Program. (12) Department of Transportation: (A) Federal Highway Administration: Emergency Relief Program (ER). (B) Federal Aviation Administration (FAA). (C) Federal Transit Administration (FTA). (13) Department of the Treasury: Internal Revenue Service. (14) Department of Veterans Affairs. (15) Corporation for National and Community Service. (16) Environmental Protection Agency: (A) Hurricane Emergency Response Authorities. (B) EPA Hurricane Response. (C) EPA Regular Appropriations. (17) The Federal Judiciary. (18) Disaster Assistance Program of the Small Business Administration. (19) Department of Energy: (A) Office of Cybersecurity, Energy Security, and Emergency Response. (B) Office of Petroleum Services. (20) General Services Administration. (21) Other authorities as appropriate. (b) Content The report shall detail the following: (1) Overall amount of disaster-related assistance obligations during the fiscal year. (2) Disaster-related assistance obligations by agency and account. (3) Disaster for which the spending was obligated. (4) Obligations by disaster. (5) Disaster-related assistance by disaster type. (6) Response and recovery spending. (7) Mitigation spending. (8) Spending in the form of loans. (9) Spending in the form of grants. (c) Availability of report The report shall be made publicly available on the website of the Office of Management and Budget and should be searchable, sortable and downloadable. .\n##### (b) Conforming amendment\nThe table of chapters for chapter 11 of title 31, United States Code, is amended by adding at the end the following new item:\n1127. Reporting of disaster-related assistance. .\n#### 5. Effective date\nThe reporting requirement under the amendment made by section 3(a) shall take effect with the budget submission of the President under section 1105(a) of title 31, United States Code, for fiscal year 2027.",
      "versionDate": "2025-04-17",
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
        "updateDate": "2025-05-29T12:26:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-17",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2956",
          "measure-number": "2956",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-17",
          "originChamber": "HOUSE",
          "update-date": "2025-05-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2956v00",
            "update-date": "2025-05-29"
          },
          "action-date": "2025-04-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disclosing Aid Spent to Ensure Relief Act of 2025 or the DISASTER Act of 2025</strong></p><p>This bill requires the Office of Management and Budget to submit an annual report to Congress on all disaster-related assistance provided by the federal government. The report must include all federal obligations related to disaster response, recovery, mitigation efforts, and administrative costs associated with these activities for specified agencies and programs.</p>"
        },
        "title": "DISASTER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2956.xml",
    "summary": {
      "actionDate": "2025-04-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disclosing Aid Spent to Ensure Relief Act of 2025 or the DISASTER Act of 2025</strong></p><p>This bill requires the Office of Management and Budget to submit an annual report to Congress on all disaster-related assistance provided by the federal government. The report must include all federal obligations related to disaster response, recovery, mitigation efforts, and administrative costs associated with these activities for specified agencies and programs.</p>",
      "updateDate": "2025-05-29",
      "versionCode": "id119hr2956"
    },
    "title": "DISASTER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disclosing Aid Spent to Ensure Relief Act of 2025 or the DISASTER Act of 2025</strong></p><p>This bill requires the Office of Management and Budget to submit an annual report to Congress on all disaster-related assistance provided by the federal government. The report must include all federal obligations related to disaster response, recovery, mitigation efforts, and administrative costs associated with these activities for specified agencies and programs.</p>",
      "updateDate": "2025-05-29",
      "versionCode": "id119hr2956"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2956ih.xml"
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
      "title": "DISASTER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DISASTER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disclosing Aid Spent to Ensure Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 11 of title 31, United States Code, to require the Director of the Office of Management and Budget to annually submit to Congress a report on all disaster-related assistance provided by the Federal Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:43Z"
    }
  ]
}
```
