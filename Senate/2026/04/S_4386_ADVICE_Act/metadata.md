# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4386?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4386
- Title: ADVICE Act
- Congress: 119
- Bill type: S
- Bill number: 4386
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-18T18:25:43Z
- Update date including text: 2026-05-18T18:25:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4386",
    "number": "4386",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "ADVICE Act",
    "type": "S",
    "updateDate": "2026-05-18T18:25:43Z",
    "updateDateIncludingText": "2026-05-18T18:25:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T20:41:37Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4386is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4386\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Cassidy (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish an advisory committee regarding data standardization and integration for apprenticeships, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apprenticeship Data Value Improvements to Create Employment Act or the ADVICE Act .\n#### 2. Establishment of an advisory committee regarding apprenticeships\n##### (a) Establishment\nThere is established an apprenticeship advisory committee within the Department of Labor (in this section referred to as the Committee ).\n##### (b) Membership\nThe Secretary of Labor shall appoint to the Committee\u2014\n**(1)**\n4 members representing State workforce agencies, of which 2 members shall be from States with a State apprenticeship agency;\n**(2)**\n2 members representing statewide longitudinal data systems that specialized in privacy, security, and interoperability;\n**(3)**\n2 members who are sponsors of a registered apprenticeship program, of which 1 member shall be from a sponsor that is an intermediary;\n**(4)**\n2 members that are sponsors of a registered apprenticeship program who represent industries with a historically low proportion of registered apprenticeship programs that experienced a high growth of such programs in the 5 years before the date of enactment of this Act;\n**(5)**\n2 members representing labor organizations and labor-management organizations;\n**(6)**\n2 members representing industry, of which 1 member shall be from an industry with a historically low proportion of registered apprenticeship programs that experienced a high growth of such programs in the 5 years before the date of enactment of this Act; and\n**(7)**\n2 members representing institutions of higher education institutions that work with sponsors of registered apprenticeship programs.\n##### (c) Period of appointment; vacancies\n**(1) In general**\nA member of the Committee shall be appointed for the life of the Committee.\n**(2) Vacancies**\nA vacancy in the Committee\u2014\n**(A)**\nshall not affect the powers of the Committee; and\n**(B)**\nshall be filled in the same manner as the original appointment.\n##### (d) Duties\nNot later than 2 years after the date of enactment of this Act, the Committee shall submit a report with recommendations to the Secretary of Labor and Congress that includes the following:\n**(1)**\nRecommendations to incentivize and permit States to increase the standardization, integration, and interoperability of registered apprenticeship program data with\u2014\n**(A)**\nthe Workforce Integrated Performance System of the Department of Labor;\n**(B)**\nthe State wage interchange system of the Department;\n**(C)**\ndata collection for the Consolidated Annual Report of the Office of Career, Technical, and Adult Education of the Department of Education;\n**(D)**\nunemployment insurance claims data;\n**(E)**\nlocal career and technical education management systems;\n**(F)**\nhigher education attainment data;\n**(G)**\nthe data collected for purposes of the temporary assistance for needy families program under section 611 of the Social Security Act ( 42 U.S.C. 411 );\n**(H)**\nthe data collected for the quality control database of the supplemental nutrition assistance program under section 16 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025 );\n**(I)**\nthe data collected for the transformed Medicaid Statistical Information System (T\u2013MSIS) (or a successor system);\n**(J)**\nthe data collected for the National Housing Preservation Database (or a successor database);\n**(K)**\nsocial services data not otherwise described in this paragraph; and\n**(L)**\nother systems determined by the Secretary of Labor to be appropriate for workforce data standardization.\n**(2)**\nRecommendations to increase such standardization and integration by\u2014\n**(A)**\nimproving user interface and user friendliness;\n**(B)**\nlowering the burden on sponsors to meet reporting requirements, including by\u2014\n**(i)**\nlowering the amount of software a State is required to use to collect, input, and transfer data to Federal offices; and\n**(ii)**\nlowering the human hours needed to conduct data collection and aggregation;\n**(C)**\nimproving the timeliness and accuracy at which data is collected; and\n**(D)**\npreparing States to report data to the Department of Labor in a standardized format that reduces the need for duplicative input.\n**(3)**\nRecommendations to incentivize and establish a mechanism for registered apprenticeship programs to collect outcomes-based data, including for\u2014\n**(A)**\nstatistics on retention when an apprentice completes an apprenticeship and within 5 years of the apprentice completing the apprenticeship; and\n**(B)**\nstatistics on pay during and after the apprenticeship program.\n**(4)**\nRecommendations to\u2014\n**(A)**\nbetter track the outcomes-based data of paid training programs that are not otherwise a registered apprenticeship program, incorporate related technical instruction into the program, and pay participants in the program; and\n**(B)**\nencourage incorporation of such outcomes-based data into State longitudinal data systems.\n**(5)**\nRecommendations to incorporate registered apprenticeship program data into the individual data for students in elementary and secondary education and postsecondary education and individual analysis of such data.\n**(6)**\nRecommendations to encourage the inclusion and analysis of registered apprenticeship program data within statewide longitudinal systems (as described in section 208(a) of the Educational Technical Assistance Act of 2002 ( 20 U.S.C. 9607 )), to ensure that data is accurately and efficiently managed, analyzed, disaggregated.\n**(7)**\nRecommendations to increase the access of an individual to their own learning and employment records.\n##### (e) Personnel matters\n**(1) Detail of government employees**\nUpon determination of need by the Committee, in coordination with the Secretary of Labor, a Federal Government employee may be detailed to the Committee without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n**(2) Travel expenses**\nA member of the Committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Committee.\n##### (f) Definitions\nFor purposes of this section:\n**(1) Registered apprenticeship program**\nThe term registered apprenticeship program means an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n**(2) Sponsor**\nThe term sponsor means any person, association, committee, or organization operating an apprenticeship program and in whose name the program is (or is to be) registered or approved as a registered apprenticeship program.\n**(3) State apprenticeship agency**\nThe term State apprenticeship agency means an entity of the government of a State that is recognized, under criteria established by the Secretary of Labor, for purposes of approving program standards that conform with the standards set by the Secretary for registering an apprenticeship program as a registered apprenticeship program.\n##### (g) Termination\nThe Committee shall terminate on the day after the date described in subsection (d).\n#### 3. Recommendations from the Secretary of Labor\nNot later than 30 days after receipt of the report submitted under section 2(d), the Secretary of Labor, in consultation with the Secretary of Education, shall\u2014\n**(1)**\nissue a policy plan based on the recommendations in such report; and\n**(2)**\nsubmit to Congress a request with targeted appropriations to empower and incentivize States to carry out the recommendations in the policy plan.\n#### 4. Implementation of the data standardization and integration policy plan\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 4 as section 5; and\n**(2)**\nby inserting after section 3 the following:\n4. Recommendations from the apprenticeship advisory committee data standardization and integration policy plan In administering a system to carry out the activities authorized and directed to be carried out under section 1, the Secretary of Labor, in collaboration with the Secretary of Education, shall consider the recommendations in the policy plan issued under section 3 of the ADVICE Act . .",
      "versionDate": "2026-04-27",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-18T18:25:42Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4386is.xml"
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
      "title": "ADVICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ADVICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Apprenticeship Data Value Improvements to Create Employment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an advisory committee regarding data standardization and integration for apprenticeships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:32Z"
    }
  ]
}
```
