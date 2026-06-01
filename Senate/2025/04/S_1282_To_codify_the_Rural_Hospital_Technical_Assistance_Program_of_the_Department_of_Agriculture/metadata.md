# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1282
- Title: Rural Development Hospital Technical Assistance Program Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1282
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-02-10T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1282",
    "number": "1282",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Rural Development Hospital Technical Assistance Program Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-02-10T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
        "item": [
          {
            "date": "2025-04-03T17:30:57Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-03T17:30:57Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "VT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "AL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1282is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1282\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Rounds (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo codify the Rural Hospital Technical Assistance Program of the Department of Agriculture.\n#### 1. Short title\nThis Act may be cited as the Rural Development Hospital Technical Assistance Program Act of 2025 .\n#### 2. Codification of the Rural Hospital Technical Assistance Program of the Department of Agriculture\n##### (a) Definitions\nIn this section:\n**(1) Development needs**\nThe term development needs means\u2014\n**(A)**\nconstructing, expanding, renovating, or otherwise modernizing health care facilities;\n**(B)**\nincreasing telehealth capabilities;\n**(C)**\nacquiring or upgrading health care information systems, such as electronic health records; and\n**(D)**\nsuch other needs as the Secretary determines to be critical to maintaining health care services in the community in which an eligible hospital facility is located.\n**(2) Eligible hospital facility**\nThe term eligible hospital facility means a facility that is\u2014\n**(A)**\n**(i)**\na hospital (as defined in section 1861(e) of the Social Security Act ( 42 U.S.C. 1395x(e) ));\n**(ii)**\na psychiatric hospital (as defined in section 1861(f) of that Act ( 42 U.S.C. 1395x(f) ));\n**(iii)**\na long-term care hospital (as defined in section 1861(ccc) of that Act ( 42 U.S.C. 1395x(ccc) ));\n**(iv)**\na critical access hospital (as defined in section 1861(mm)(1) of that Act ( 42 U.S.C. 1395x(mm)(1) ));\n**(v)**\na religious nonmedical health care institution (as defined in section 1861(ss)(1) of that Act ( 42 U.S.C. 1395x(ss)(1) ));\n**(vi)**\na rural health clinic (as defined in section 1861(aa)(2) of that Act ( 42 U.S.C. 1395x(aa)(2) ));\n**(vii)**\na sole community hospital (as defined in section 1886(d)(5)(D)(iii) of that Act ( 42 U.S.C. 1395ww(d)(5)(D)(iii) ));\n**(viii)**\na rural emergency hospital (as defined in section 1861(kkk)(2) of that Act ( 42 U.S.C. 1395x(kkk)(2) ));\n**(ix)**\na community health center receiving funding under section 330 of the Public Health Service Act ( 42 U.S.C. 254b ); or\n**(x)**\nany other rural hospital, as determined by the Secretary, in consultation with the Secretary of Health and Human Services; and\n**(B)**\nlocated in a rural area.\n**(3) Health professional shortage area**\nThe term health professional shortage area has the meaning given the term in section 332(a)(1)(A) of the Public Health Service Act ( 42 U.S.C. 254e(a)(1)(A) ).\n**(4) Medically underserved area**\nThe term medically underserved area has the meaning given the term in section 330I(a)(4) of the Public Health Service Act ( 42 U.S.C. 254c\u201314(a)(4) ).\n**(5) Medically underserved population**\nThe term medically underserved population has the meaning given the term in section 330(b)(3) of the Public Health Service Act ( 42 U.S.C. 254b(b)(3) ).\n**(6) Program**\nThe term Program means the Rural Hospital Technical Assistance Program established under subsection (b).\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(8) Rural area**\nThe term rural area has the meaning given the term in section 343(a)(13)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a)(13)(A) ).\n##### (b) Establishment\nIn lieu of any other authority under which the Secretary may provide technical assistance to any eligible hospital facility, the Secretary shall establish, and maintain, directly or by grant, contract, or cooperative agreement, a Rural Hospital Technical Assistance Program to provide technical assistance and training, tailored to the capacity and needs of each eligible hospital facility, to help eligible hospital facilities\u2014\n**(1)**\nidentify development needs for maintaining essential health care services, and support action plans for financial, operational, and quality improvement projects to meet the development needs;\n**(2)**\nbetter manage the financial and business strategies of the eligible hospital facilities; and\n**(3)**\nidentify, and apply for assistance from, loan and grant programs of the Department of Agriculture for which the eligible hospital facilities are eligible.\n##### (c) Goals\nThe goals of the Program shall be\u2014\n**(1)**\nto improve the long-term financial position and operational efficiency of eligible hospital facilities;\n**(2)**\nto prevent the closure of eligible hospital facilities;\n**(3)**\nto strengthen the delivery of health care in rural areas; and\n**(4)**\nto help eligible hospital facilities better access and compete for loans and grants from programs administered by the Department of Agriculture.\n##### (d) Program participation\n**(1) In general**\nThe Secretary shall engage in outreach and engagement strategies to encourage eligible hospital facilities to participate in the Program.\n**(2) Hospital selection**\nIn selecting eligible hospital facilities to participate in the Program, the Secretary\u2014\n**(A)**\nshall give priority to borrowers of loans and recipients of grants from the Rural Housing Service, the Rural Business-Cooperative Service, and the Rural Utilities Service; and\n**(B)**\nmay consider\u2014\n**(i)**\nthe age and physical state of the hospital or clinic facilities involved;\n**(ii)**\nthe financial vulnerability of the hospital or clinic facilities, and the ability of the hospital or clinic facilities to meet debt obligations;\n**(iii)**\nthe electronic health record implementation needs of the hospital or clinic facilities;\n**(iv)**\nwhether the hospital or clinic is located in a health professional shortage area or a medically underserved area;\n**(v)**\nwhether the hospital serves a medically underserved population; and\n**(vi)**\nsuch other criteria and priorities as are determined by the Secretary.\n##### (e) Reporting requirements\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a written report describing the progress and results of the Program, including\u2014\n**(1)**\na brief description of each project to provide technical assistance to an eligible hospital facility, including\u2014\n**(A)**\nthe name and location of the facility;\n**(B)**\na description of the assistance provided;\n**(C)**\na description of the outcomes for completed projects;\n**(D)**\nthe cost of the technical assistance; and\n**(E)**\nany other information the Secretary determines to be appropriate;\n**(2)**\na summary of the technical assistance projects completed;\n**(3)**\na summary of the outcomes of the technical assistance projects;\n**(4)**\nan assessment of the effectiveness of the Program; and\n**(5)**\nrecommendations for improving the Program.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section not more than $2,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-04-03",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T20:17:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
    "originChamber": "Senate",
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
          "measure-id": "id119s1282",
          "measure-number": "1282",
          "measure-type": "s",
          "orig-publish-date": "2025-04-03",
          "originChamber": "SENATE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1282v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Development\u00a0Hospital Technical Assistance Program Act\u00a0of 2025</strong></p><p>This bill provides statutory authority for the Rural Hospital Technical Assistance Program within the Department of Agriculture (USDA).</p><p>Under the bill, USDA must establish and maintain (directly or by grant, contract, or cooperative agreement) a program\u00a0to help eligible hospital facilities in rural areas (i.e., an area with a population of 50,000 inhabitants or less).</p><p>The program must provide tailored technical assistance and training to hospital facilities to identify development needs for maintaining essential health care services and support action plans for financial, operational, and quality improvement projects to meet these needs. Development needs include (1) constructing, expanding, and modernizing health care facilities; (2) increasing telehealth capabilities; and (3) acquiring or upgrading health care information systems (e.g., electronic health records).</p><p>The program must also provide technical assistance and training to help hospital facilities to\u00a0better manage their financial and business strategies and identify, and apply for assistance from, USDA loan and grant programs.</p><p>In selecting eligible hospital facilities to participate in the program, USDA must give priority to borrowers of loans and recipients of grants from certain USDA rural assistance programs.</p><p>USDA must also submit an annual report to Congress on the progress and results of the program.</p>"
        },
        "title": "Rural Development Hospital Technical Assistance Program Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1282.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Development\u00a0Hospital Technical Assistance Program Act\u00a0of 2025</strong></p><p>This bill provides statutory authority for the Rural Hospital Technical Assistance Program within the Department of Agriculture (USDA).</p><p>Under the bill, USDA must establish and maintain (directly or by grant, contract, or cooperative agreement) a program\u00a0to help eligible hospital facilities in rural areas (i.e., an area with a population of 50,000 inhabitants or less).</p><p>The program must provide tailored technical assistance and training to hospital facilities to identify development needs for maintaining essential health care services and support action plans for financial, operational, and quality improvement projects to meet these needs. Development needs include (1) constructing, expanding, and modernizing health care facilities; (2) increasing telehealth capabilities; and (3) acquiring or upgrading health care information systems (e.g., electronic health records).</p><p>The program must also provide technical assistance and training to help hospital facilities to\u00a0better manage their financial and business strategies and identify, and apply for assistance from, USDA loan and grant programs.</p><p>In selecting eligible hospital facilities to participate in the program, USDA must give priority to borrowers of loans and recipients of grants from certain USDA rural assistance programs.</p><p>USDA must also submit an annual report to Congress on the progress and results of the program.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s1282"
    },
    "title": "Rural Development Hospital Technical Assistance Program Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Development\u00a0Hospital Technical Assistance Program Act\u00a0of 2025</strong></p><p>This bill provides statutory authority for the Rural Hospital Technical Assistance Program within the Department of Agriculture (USDA).</p><p>Under the bill, USDA must establish and maintain (directly or by grant, contract, or cooperative agreement) a program\u00a0to help eligible hospital facilities in rural areas (i.e., an area with a population of 50,000 inhabitants or less).</p><p>The program must provide tailored technical assistance and training to hospital facilities to identify development needs for maintaining essential health care services and support action plans for financial, operational, and quality improvement projects to meet these needs. Development needs include (1) constructing, expanding, and modernizing health care facilities; (2) increasing telehealth capabilities; and (3) acquiring or upgrading health care information systems (e.g., electronic health records).</p><p>The program must also provide technical assistance and training to help hospital facilities to\u00a0better manage their financial and business strategies and identify, and apply for assistance from, USDA loan and grant programs.</p><p>In selecting eligible hospital facilities to participate in the program, USDA must give priority to borrowers of loans and recipients of grants from certain USDA rural assistance programs.</p><p>USDA must also submit an annual report to Congress on the progress and results of the program.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119s1282"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1282is.xml"
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
      "title": "Rural Development Hospital Technical Assistance Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Development Hospital Technical Assistance Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to codify the Rural Hospital Technical Assistance Program of the Department of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:22Z"
    }
  ]
}
```
