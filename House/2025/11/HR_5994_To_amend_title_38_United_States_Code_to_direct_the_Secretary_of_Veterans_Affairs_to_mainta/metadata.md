# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5994
- Title: Every Veteran Counts Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5994
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2025-11-18T16:12:42Z
- Update date including text: 2025-11-18T16:12:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5994",
    "number": "5994",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Every Veteran Counts Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-18T16:12:42Z",
    "updateDateIncludingText": "2025-11-18T16:12:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5994ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5994\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Ms. Brownley (for herself and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to maintain demographic information regarding veterans and publish such information on a website of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Every Veteran Counts Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Department of Veterans Affairs is responsible for providing a variety of benefits and services to more than 19,000,000 living veterans.\n**(2)**\nPursuant to section 527 of title 38, United States Code, the Secretary of Veterans Affairs has conducted the National Survey of Veterans to assess the needs and sentiments of a statistically valid sample of all veterans.\n**(3)**\nThe Secretary has conducted this National Survey of Veterans in the late 1970s, 1987, 1993, 2001, and 2010.\n**(4)**\nThe last survey conducted in 2010 included veterans and other beneficiary groups, such as members of the Armed Forces serving on active duty, members of the reserve components of the Armed Forces, military spouses, and surviving spouses of such veterans and members.\n**(5)**\nThe 2010 survey included information on demographics, awareness and utilization of benefits, health status, military service, and employment.\n**(6)**\nThese surveys provide valuable information on the veteran population to the Secretary, Congress, Federal, State, and local governments, academic institutions, and various non-governmental organizations that serve veterans.\n**(7)**\nThis information is used to inform policymaking efforts and to ensure the needs of the ever-changing veteran population are met.\n**(8)**\nHowever, since 2010, the statutory framework for data collection has substantially evolved, notably with the Foundations for Evidence-Based Policymaking Act ( Public Law 115\u2013435 ), the Data Act ( Public Law 113\u2013139 ), and the Geospatial Data Act (subtitle F of title VII of Public Law 115\u2013254 ), known collectively as the Evidence Act , building on previously enacted laws.\n**(9)**\nFurther, the Department, through the National Center for Veterans Analysis and Statistics, has leveraged the vast amount of data generated within the Department and collected by other Federal partners to improve population-based descriptive, statistical, and predictive analytic products to support the Secretary and in evidence-based policymaking, facilitate innovative and collaborative research, and empower modern business intelligence applications.\n**(10)**\nThe Department has been a consistent leader in the Federal Open Data program and offers a platform for scaling access to useful data and insight to external stakeholders.\n**(11)**\nNotwithstanding these recent advances, opportunities exist to strengthen the capability of the Department to develop and disseminate actionable insights into the veteran population through\u2014\n**(A)**\ndeveloping enterprise-focused management and improvements in the quality of administrative data collected by the Department through its delivery of benefits and services;\n**(B)**\nincreased access to data collected by other Federal entities through more flexible and efficient information sharing policies;\n**(C)**\nincreased use of publicly available and commercially generated data; and\n**(D)**\nmaturing data management of the Department.\n**(12)**\nIn line with the Evidence Act, it is incumbent upon the Secretary to regularly engage with key stakeholders, including Congress, veterans service organizations, advocacy groups, and open government groups to\u2014\n**(A)**\nenhance the open data program of the Department; and\n**(B)**\nimprove development and dissemination of relevant data assets and analytic products to provide more current, accurate, and useful insights on veterans and their families.\n**(13)**\nIt is necessary for the Department to collect, collate, and analyze all available data on veteran demographics, and to share this data with Congress and other stakeholders on an ongoing basis, in an easily digestible format, to direct outreach and align policy with the needs of the changing veteran population.\n#### 3. Demographic data of veterans: collection; retention; publication\n##### (a) In general\nSubchapter II of chapter 5 of title 38, United States Code, is amended by inserting after section 527, the following new section:\n528. Demographic data of veterans: collection; retention; publication. (a) Database (1) The Secretary shall collect demographic data of veterans (from any source of such data available to the Secretary, including the National Center for Veterans Analysis and Statistics of the Department, the Bureau of the Census, and the Social Security Administration) and maintain a database of such data. (2) Data collected and maintained under paragraph (1) shall include the following: (A) Sex. (B) Gender identity, disaggregated by\u2014 (i) male; (ii) female; (iii) cisgender; (iv) transgender; (v) gender diverse; (vi) nonbinary; and (vii) combinations of clauses (i) through (vi). (C) Age. (D) Educational level. (E) Race and ethnicity, disaggregated by\u2014 (i) membership in an Indian tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); and (ii) the same major race groups as the decennial censuses. (F) Sexual orientation, disaggregated by\u2014 (i) heterosexual; (ii) lesbian; (iii) gay; (iv) bisexual; and (v) queer. (G) Household makeup, including marital status and number of dependents. (H) Gross income and sources of income. (I) Housing status, disaggregated by\u2014 (i) renter; (ii) homeowner; or (iii) residing in a home owned or rented by another person. (J) Employment status, disaggregated by\u2014 (i) employed; (ii) seeking employment; and (iii) self-employed. (K) History of service in the Armed Forces, disaggregated by\u2014 (i) Armed Force; (ii) regular or reserve component; (iii) service in a combat theater of operations or war zone; (iv) service during a period of war; (v) whether a veteran is a former prisoner of war; (vi) whether the veteran was exposed to dead, dying, or wounded people during active military, naval, air, or space service; (vii) whether the veteran was exposed to environmental hazards during active military, naval, air, or space service; and (viii) whether the veteran experienced military sexual trauma (as that term is defined in section 1166 of this title). (L) Whether the veteran is enrolled in the patient enrollment system under section 1705 of this title. (M) Whether the veteran has received a disability rating from under section 1155 of this title. (N) Location of the veteran\u2019s residence, disaggregated by\u2014 (i) rural or urban setting; (ii) distance to a facility of the Department; and (iii) whether the veteran has access to broadband service. (O) Any other information the Secretary determines appropriate. (b) Data retention standards Demographic data in the database under subsection (a) shall be\u2014 (1) anonymized to prevent the release of sensitive personal information (as that term is defined in section 5727 of this title); and (2) machine readable. (c) Website The Secretary shall maintain a publicly accessible website of the Department that provides access to the database under subsection (a). The Secretary shall update such website not less frequently than once each year. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting, after the item relating to section 527, the following new item:\n528. Demographic data of veterans: collection; retention; publication. .\n##### (c) Implementation date\nThe Secretary of Veterans Affairs shall carry out section 528 of such title, as added by this section, not later than 180 days after the date of the enactment of this Act.\n#### 4. Report on data strategy of the Department of Veterans Affairs\n##### (a) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report describing the progress, challenges, performance, and opportunities of implementing the data strategy of the Department of Veterans Affairs.\n##### (b) Elements\nThe report under this section shall include the following:\n**(1)**\nQualitative and quantitative progress towards strengthening data management of the Department, including business and mission impact enabled by management of data as a strategic asset.\n**(2)**\nRecommendations of the Secretary regarding legislation that may accelerate data management maturity of the Department.\n**(3)**\nProgress and results in cataloging and inventorying data assets of the Department and using such assets to support\u2014\n**(A)**\ninternal evidence-based policymaking; and\n**(B)**\nethical and appropriate dissemination of statistical aggregates, data-driven analysis, and open data.\n**(4)**\nProgress in implementing requirements under chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ), and related data quality efforts to support strategic management of data collected by the Department.\n**(5)**\nEfforts to move towards a rules-based, transparent, Department-wide approach to management, integration, and sharing of, and access to, data.\n**(6)**\nRecommendations of the Secretary regarding adjustments to data requirements of the Department.\n**(7)**\nInformation sharing agreements and outstanding requirements with other Federal entities, including gaps best addressed by the addition of survey questions to an existing Federal survey instrument.\n**(8)**\nProgress on recently enacted public laws, Executive orders, Presidential memoranda, and outstanding recommendations of the Comptroller General of the United States or an inspector general as it pertains to veteran population-based data collection, quality, integration, sharing, interoperability, and analytics within the scope of improving and ensuring equity in services to veterans, their families, and other beneficiaries.\n**(9)**\nA discussion of current risk assessments regarding data breaches and information security (as those terms are defined in section 5727 of title 38, United States Code) of the Department.\n**(10)**\nPriority data requirements of the Department, identified through consultation with the following entities:\n**(A)**\nThe Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives.\n**(B)**\nThe Congressional Budget Office.\n**(C)**\nVeterans service organizations.\n**(D)**\nThe Advisory Committee on Minority Veterans of the Department.\n**(E)**\nThe Advisory Committee on Women Veterans of the Department.\n**(F)**\nThe Advisory Committee on Homeless Veterans of the Department.\n##### (c) Publication\nNot later than 30 days after submitting the report under this section, the Secretary shall publish such report on the open data website of the Department, with all metrics and data included in a machine readable format.",
      "versionDate": "2025-11-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:12:42Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5994ih.xml"
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
      "title": "Every Veteran Counts Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Every Veteran Counts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to maintain demographic information regarding veterans and publish such information on a website of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:19Z"
    }
  ]
}
```
