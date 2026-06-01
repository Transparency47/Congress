# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1969?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1969
- Title: AFIDA Improvements Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1969
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-01-06T12:04:06Z
- Update date including text: 2026-01-06T12:04:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1969",
    "number": "1969",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "AFIDA Improvements Act of 2025",
    "type": "S",
    "updateDate": "2026-01-06T12:04:06Z",
    "updateDateIncludingText": "2026-01-06T12:04:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
            "date": "2025-06-05T17:02:27Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-05T17:02:27Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MS"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-05",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1969is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1969\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Ricketts (for himself, Mr. Tuberville , Mr. Fetterman , Mr. Wicker , Mr. Cornyn , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Foreign Investment Disclosure Act of 1978 to establish an additional reporting requirement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AFIDA Improvements Act of 2025 .\n#### 2. Reporting; enforcement\n##### (a) Reporting requirement\nSection 2 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 ) is amended by adding at the end the following:\n(g) Minimum ownership In the case of agricultural land in which more than 1 foreign person acquires or transfers any interest, other than a security interest, the reporting requirements under this section shall apply to each foreign person who holds at least a 1 percent interest in that land\u2014 (1) directly through the first tier of ownership; or (2) in the aggregate through an interest in other entities at various tiers. .\n##### (b) Enforcement\nSection 4 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3503 ) is amended\u2014\n**(1)**\nby striking the section designation and all that follows through The Secretary and inserting the following:\n4. Investigative actions (a) In general The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Actions by FPAC\u2013BC As part of the actions taken under subsection (a), the Farm Production and Conservation Business Center shall\u2014 (1) take such actions as are necessary to validate the data collected under section 2, including revising and validating information throughout the data collection process; (2) take such actions as are necessary to ensure compliance with section 2(g); and (3) in coordination with the Farm Service Agency, to the maximum extent practicable, identify persons that have carried out an activity subject to a civil penalty described in paragraph (1) or (2) of section 3(a). .\n#### 3. Agricultural foreign investment disclosure improvements\n##### (a) Definitions\nIn this section:\n**(1) AFIDA**\nThe term AFIDA means the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 et seq. ).\n**(2) FPAC\u2013BC**\nThe term FPAC\u2013BC means the Farm Production and Conservation Business Center.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) MOU with CFIUS\nNot later than 1 year after the date of enactment of this Act, the Secretary shall enter into 1 or more memoranda of understanding with the Committee on Foreign Investment in the United States under which the Secretary shall provide the Committee with all relevant information relating to reports on foreign ownership of United States agricultural land submitted to the Secretary under section 2 of AFIDA ( 7 U.S.C. 3501 ), including information on\u2014\n**(1)**\neach report submitted to the Secretary; and\n**(2)**\nwith respect to each such report, the identity of the person submitting the report and the date of submission.\n##### (c) AFIDA handbook updates\n**(1) First update**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall update the most recent version of the Farm Service Agency handbook entitled Foreign Investment Disclosure as determined necessary by the Secretary for the effective implementation of AFIDA, which update shall incorporate recommendations made by the report of the Government Accountability Office entitled Foreign Investments in U.S. Agricultural Land: Enhancing Efforts to Collect, Track, and Share Key Information Could Better Identify National Security Risks and dated January 18, 2024.\n**(2) Subsequent updates**\nAfter updating the handbook described in paragraph (1) under that paragraph, the Secretary shall carry out an update of that handbook every 10 years thereafter, including by incorporating any recommendations of the Government Accountability Office.\n##### (d) Analysis of streamlined process for electronic submission and retention of reports under AFIDA\n**(1) Definition of covered process**\nIn this subsection, the term covered process means the streamlined process for electronic submission and retention of disclosures made under AFIDA required under section 773 of division A of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 3501 note; 136 Stat. 4509).\n**(2) Analysis**\nUnless the covered process is established by not later than 1 year after the date of enactment of this Act, the FPAC\u2013BC, in coordination with the Farm Service Agency, shall, by that date\u2014\n**(A)**\ncarry out an analysis of the specific steps required to establish that process and the elements of that process; and\n**(B)**\ndevelop a timeline for specific implementation benchmarks to be met.\n**(3) Report**\nThe Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report describing the analysis and implementation timeline under paragraph (2), if applicable.",
      "versionDate": "2025-06-05",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-14",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4362",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AFIDA Improvements Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-07-11T17:30:31Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1969is.xml"
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
      "title": "AFIDA Improvements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T12:04:06Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AFIDA Improvements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Foreign Investment Disclosure Act of 1978 to establish an additional reporting requirement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T04:48:18Z"
    }
  ]
}
```
